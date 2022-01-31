#!/usr/bin/env python3
import os, json, signal
from trainsim import TrainSim

config_file_path = os.getenv('TRAIN_CONFIG_PATH') or 'config.json'

print(f"Loading config from {config_file_path}")
config_file = open(config_file_path)
config = json.load(config_file)
config_file.close()

sim = TrainSim(config)

def signal_handler(sig, frame):
    print("Received signal to stop...")
    sim.stop()
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

sim.run()