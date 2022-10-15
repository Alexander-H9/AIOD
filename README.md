# AI-On-Demand (AIOD)

## Description

AI service for application independant image/video processing and analysis.

### Functionality

* Client upload a file and sends parameters to the server
* Server processes the given file using the given parameters
* Server returns information/statistics back to the client

## Built with

* Python 3
* Docker
* MQTT
* Tensorflow

### Executing program

* Builds, (re)creates, starts, and attaches to containers for a service.
```
docker compose up
```
* Stops containers and removes containers, networks, volumes, and images created by up.
```
docker compose down
```

## Authors

Alexander Härle
haerleal@hs-albsig.de

Andreas Fischer
fischea4@hs-albsig.de

## Version History

* 0.1
    * Initial Release
