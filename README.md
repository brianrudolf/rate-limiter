# Rate Limiter testing

## Operation
## Running

The three containers are designed to be built and run with Docker Compose to provide a simplified portable experience.

```
docker compose up --build
```

## Development
### Goals

The main goal of this project is demonstrate various rate limiting methods and progressively build and expand on the ability of the code to respond to high traffic levels.

### Components

The application as a whole is intended to run with a single command and demonstrate an example API, a rate limiter in front of said API, and an example load generator that is able to drive a test load with varying degrees of load.

### Design

This project is initially written in Python, which will eventually caused performance issues and bottlenecks as the load is increased. However this project is designed to evolve over time with performance increases driving the changes. 

#### Algoirthms

`./app/window-limiter.py` implements a basic window limiter to limit request rates to within a given time window.

[FUTURE] `./app/token-limiter.py` aims to implement a 'token bucket' limiter algorithm

[FUTURE] `./app/leaky-limiter.py` aims to implement a 'leaky token bucket' limiter algorithm
