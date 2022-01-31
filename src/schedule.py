import csv
from operator import delitem, index
from typing import Dict
from simevent import SimEvent

class Schedule():
    def __init__(self, events) -> None:
        self.events = events

    def FromObject(obj: Dict):
        
        events: list[SimEvent] = []
        for event in obj['simevents']:
            events.append(SimEvent(event))

        sched = Schedule(events)
        return sched

    def FromCSV(path):
        events: list[SimEvent] = []

        dictevents: list[dict] = []
        with open(path, newline='', encoding="utf-8-sig") as csvfile:
            eventreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            index_map: dict[str,int] = {
                "description":None,
                "type":None,
                "time_start":None,
                "time_end":None,
                "duration":None
            }
            first_row = True
            for row in eventreader:
                if first_row:
                    for index, token in enumerate(row):
                        index_map[token] = index
                else:
                    event:dict = {}
                    for attrib, index in index_map.items():
                        if index is not None:
                            event[attrib] = row[index]
                    events.append(SimEvent(event))
                first_row = False

        sched = Schedule(events)
        return sched
