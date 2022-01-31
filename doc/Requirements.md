# Functional Requirements
  1. Simulates multiple (as much as computer hardware resources allow) train/crossing hardware(s) which each detect when object (train) is present on tracks
  2. Simulation is highly configurable
     1. Time intervals (start time with duration/start time with stop time) of trains entering and leaving crossing can be configured
     2. Non-train objects detected at random times [very low probability]
     3. Which location/station is being monitored [station ID]
  3. Each simulation transmits state to backend every 30 seconds (or configured interval) for the station being monitored independently of each other


# Non-functional Requirements
  1. Uses Python3 programming language
  2. Communicates with backend API over http with python requests library; no authentication (currently)
     1. Transmit(state)
  3. Uses various standard libraries and external libs
     1. dateutil (latest) for date parsing
     2. random (latest) for random number generation
     3. threading (latest) for running tasks in multiple threads
     4. sched (latest) for scheduling events (trains, communications failures, hardware failure)
     5. time (latest) for current time
     6. csv (latest) for csv parsing
     7.  signal (latest) to get SIGINT when container/user stops app
     8.  os (latest) to get environment variables
     9.  json (latest) to read configuration from JSON files
     10. enum (latest) for event types
  4.  Configuration in JSON at (documentation here -> https://github.com/SAU-Senior-Project-2022/TrainHardwareSimulation#json)
  5.  Runs in docker for compatibility with most systems (Windows, Mac, Linux)
  6.  Uses docker-compose for orchestration of multiple simulations at the same time
      1.  Each container can be separately configured with its own JSON file
      2.  In the docker-compose.yml, multiple containers can be specified (each with own config specified with env variables)


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
