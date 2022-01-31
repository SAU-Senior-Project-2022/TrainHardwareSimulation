import requests, sched, time
from dateutil.parser import parse
from threading import Thread
from schedule import Schedule
from simevent import SimEventType
from random import randint

class TrainSim:
    def __init__(self, config: dict) -> None:
    
        self._running = True
        self._base_url = config.get('api_base_url')
        self._station_id = config.get('station_id') or 1
        self._update_time = config.get('update_time') or 30
        self._schedule_type = config.get('schedule').get('type')
        match self._schedule_type:
            case 'csv':
                self._schedule = Schedule.FromCSV(config.get('schedule').get('csv_path'))
            case 'json':
                self._schedule = Schedule.FromObject(config.get('schedule'))
            case _:
                raise Exception("Schedule type must be json or csv")
        self._state = 0
        self._scheduler = sched.scheduler(time.time, time.sleep)
        self._update_thread = Thread(target=self.update_loop)
        self._schedule_thread = Thread(target=self.schedule_loop)
        self._comm_failure = False
        self.populate_schedule()

    def populate_schedule(self):

        now = time.time()
        for event in self._schedule.events:
            start_time = parse(event.start_time).timestamp()
            end_time = None if not event.end_time else parse(event.end_time).timestamp()
            duration = None if not event.duration else event.duration
            random = (end_time is not None) and (duration is not None)
            match event.type:
                case SimEventType.Train:
                    evt_start: int = None
                    evt_end: int = None
                    if random:
                        evt_start = randint(start_time, end_time - duration)
                        evt_end = evt_start + duration
                    else:
                        evt_start = start_time
                        evt_end = end_time or evt_start + duration

                    delay = evt_start - now
                    if (delay > 0):
                        pretty_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(evt_start))
                        print(f"Adding{' randomly' if random else ''} scheduled train enter for {pretty_time} which is in {delay} seconds.")
                        self._scheduler.enter(delay, 1, self.set_state, (1,))
                        delay = evt_end - now
                        pretty_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(evt_end))
                        print(f"Adding{' randomly' if random else ''} scheduled train leave for {pretty_time} which is in {delay} seconds.")
                        self._scheduler.enter(delay, 1, self.set_state, (0,))

                case SimEventType.Comm_Failure:
                    evt_start: int = None
                    evt_end: int = None
                    if random:
                        evt_start = randint(start_time, end_time - duration)
                        evt_end = evt_start + duration
                    else:
                        evt_start = start_time
                        evt_end = end_time or evt_start + duration

                    delay = evt_start - now
                    if (delay > 0):
                        pretty_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(evt_start))
                        print(f"Adding{' randomly' if random else ''} scheduled comm failure start for {pretty_time} which is in {delay} seconds.")
                        self._scheduler.enter(delay, 1, self.comm_failure, (True,))
                        delay = evt_end - now
                        pretty_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(evt_end))
                        print(f"Adding{' randomly' if random else ''} scheduled comm failure end for {pretty_time} which is in {delay} seconds.")
                        self._scheduler.enter(delay, 1, self.comm_failure, (False,))

                case SimEventType.Hard_Failure:
                    evt_start: int = None
                    if random:
                        evt_start = randint(start_time, end_time)
                    else:
                        evt_start = start_time

                    delay = evt_start - now
                    if (delay > 0):
                        pretty_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(evt_start))
                        print(f"Adding{' randomly' if random else ''} scheduled hardware failure for {pretty_time} which is in {delay} seconds.")
                        self._scheduler.enter(delay, 1, self.hard_failure)                    
        
        if (delay > 0):
            pass

    def set_state(self, state):
        print(f"Train is now {'present' if state else 'gone'}")
        self._state = state

    def hard_failure(self): # hardware failure
        print("Simulated hardware has failed!")
        self.stop()

    def comm_failure(self, state): # temporary communication/connection loss
        print(f"Communications are {'now down' if state else 'back up'}")
        self._comm_failure = state
    
    def stop(self):
        self._running = False
        if self._update_thread.is_alive():
            self._update_thread.join(3) # wait 3 s for thread to stop
        if self._schedule_thread.is_alive():
            self._schedule_thread.join(3)

    def run(self):
        self._update_thread.start()
        self._schedule_thread.start()

        while self._running:
            time.sleep(1)

        print("Shutting down...")
        self.stop()

    def update_loop(self):
        # future: replace with custom Thread that allows better cleanup
        while self._running:
            self.send_state()
            time.sleep(self._update_time)

    def schedule_loop(self):
        while self._running:
            self._scheduler.run(blocking=False)
            time.sleep(1.0)

    def send_state(self):
        if not self._comm_failure:
            url = f"{self._base_url}/state/{self._station_id}"
            data = {"state":self._state}
            print(f"Sending state to backend: {url} => {data}")
            try:
                resp = requests.post(url, json=data, timeout=3)
                print(f"Server returned with: {resp.content}")
            except requests.exceptions.ReadTimeout as err:
                print("Server timed out (Read Timeout)")