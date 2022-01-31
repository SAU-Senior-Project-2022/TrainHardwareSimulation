# TrainHardwareSimulation
Python software for simulating hardware which monitors for trains and communicates with a backend [here](https://github.com/SAU-Senior-Project-2022/train_backend).

  - [Train Hardware Simulation](#trainhardwaresimulation)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
    - [Development](#development)
      - [Docker](#docker)
      - [Without Docker](#without-docker)
## Prerequisites
  * Docker
  * Docker Compose
  * Python (for development outside docker)
## Usage
Basic usage of the train simulation can be done with `docker-compose`. The examples below show how to start, monitor, and end the application (for however many instances are specified in `docker-compose.yaml`)
```bash
# bring up containers and detach
docker-compose -d up
# check logs and follow
docker-compose logs -f
# bring down and destroy containers
docker-compose down
```

## Development

### Docker
When any changes are made to the source code or configs, just destroy the current containers with `docker-compose down`, run `docker-compose build` and then run `docker-compose up -d` again
### Without docker
Also, if just developing, you may run `main.py` directly with proper arguments/environment variables

## Configuration
### Environment Variables
  * `TRAIN_CONFIG_PATH` - the path to a JSON configuration file
### JSON
There is an example `config.json` at [config.json](sampleconfigs/config.json), as well as others in that folder, and a reference below:
  * `api_base_url` - base url of API to communicate with
  * `station_id` - ID of the station
  * `update_time` - interval between updates sent to backend server
  * `schedule` - the schedule of the train, communication failures, and hardware failures
    * `type` - either `json` or `csv` - if csv then include `csv_path`
    * `simevents` - only include if schedule type is `json` - an array of objects with the structure below:
      * `description` - tells about the schedule event
      * `type` - says what type of event it is (`train`, `comm_failure`, `hard_failure`)
      * `start_time` - the start of the event
      * `end_time` - end of the event
      * `duration` - how long the event lasts

Note: if `start_time`, `duration`, and `end_time` are present, the system will pick an interval of length `duration` between `start_time` and `end_time`.
### CSV Schedule
You can find example csv schedules [here](sampleconfigs/train1.csv). They follow the same format as a `simevent` from above.