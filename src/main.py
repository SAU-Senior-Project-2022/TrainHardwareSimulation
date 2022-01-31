#!/usr/bin/env python3
import os, json, argparse, signal
from trainsim import TrainSim

# sched Event scheduler -> https://docs.python.org/3/library/sched.html
#                          https://schedule.readthedocs.io/en/stable/
# backend documentation -> http://train.jpeckham.com:5000/site/documentation
# locations ->             http://train.jpeckham.com:5000/location
# get state of station     http://train.jpeckham.com:5000/state/1


config_file_path = os.getenv('TRAIN_CONFIG_PATH') or 'config.json'

print(f"Loading config from {config_file_path}")
config_file = open(config_file_path)
config = json.load(config_file)
config_file.close()

sim = TrainSim(config)

def signal_handler(sig, frame):
    sim.stop()
signal.signal(signal.SIGINT, signal_handler)

sim.run()