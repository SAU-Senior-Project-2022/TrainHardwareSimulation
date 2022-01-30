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
When any changes are made to the source code or configs, just destroy the current containers with `docker-compose down` and run `docker-compose up -d` again
### Without docker
Also, if just developing, you may run `main.py` directly with proper arguments/environment variables

