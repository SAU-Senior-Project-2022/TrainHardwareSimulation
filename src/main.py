#!/usr/bin/env python3
import os, json, argparse
from trainsim import TrainSim

# sched Event scheduler -> https://docs.python.org/3/library/sched.html
#                          https://schedule.readthedocs.io/en/stable/
# backend documentation -> http://train.jpeckham.com:5000/site/documentation
# locations ->             http://train.jpeckham.com:5000/location
# get state of station     http://train.jpeckham.com:5000/state/1

parser = argparse.ArgumentParser()

config_file_path = os.getenv('TRAIN_CONFIG_PATH') or 'config.json'

print(f"Loading config from {config_file_path}")
config_file = open(config_file_path)
config = json.load(config_file)
config_file.close()

sim = TrainSim(config)
sim.run()