import requests, sched, time

class TrainSim:
    def __init__(self, config) -> None:
    

        self._base_url = config['api_base_url']
        self._station_id = config['station_id']
        self._state = 0
        self._scheduler = sched.scheduler()

    def hardware_failure(self, time_0, time_1): # hardware failure after time_0 to time_1 range of time
        pass

    def comm_loss(self): # temporary communication/connection loss
        pass
    
    def run(self):
        while True:
            self._state = 0
            self.send_state()
            time.sleep(2.0)  # sleep parameter is in seconds, not miliseconds

            self._state = 1
            self.send_state()
            time.sleep(2.0)

    def send_state(self):
        url = f"{self._base_url}/state/{self._station_id}"
        data = {"state":self._state}
        print(f"Sending state to backend: {url} => {data}")
        resp = requests.post(url, json=data)
        print(f"Server returned with: {resp.content}")