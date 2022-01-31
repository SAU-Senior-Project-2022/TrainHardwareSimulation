# Functional Requirements
  1. Simulates multiple train/crossing hardware(s) which each detect when object (train) is present on tracks
  2. Simulation is highly configurable
     1. Time of trains entering and leaving crossing can be configured
     2. Non-train objects detected at random times [very low probability]
     3. Which location/station is being monitored [station ID]
  3. Transmits state to backend every 30 seconds for the station monitored

# Non-functional Requirements
  1. Uses Python programming language
  2. Communicates with backend API over http with no authentication (currently)
     - Transmit(state)
  3. Configuration in JSON at least for options and 
  4. Runs in docker for compatibility with most systems (Windows, Mac, Linux)
  5. Uses docker-compose for orchestration of multiple simulations at the same time

# Extra/Stretch Goals (Functional)
  1. More configuration options
     1. Hardware failure (after x-y range of time) 
     2. Temporary connectivity loss
     3. Configurable update interval
  2. Interactive terminal that can be used while running simulation (manual control/changing configuration)
  3. Command-line parameters allowed with help

# Extra (non-functional)
  1. Uses CSV for schedules instead of embedding in JSON
  2. Uses OS environment variable to override config path
  3. Uses argparse https://docs.python.org/3/library/argparse.html  for config override
     1. Custom configuration JSON location
     2. Individual config overrides
