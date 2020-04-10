# content-fetcher 

Flask based microservice to scrap text and images from web pages. Uses Redis for multitasking.

Project in alpha stage.

## Launching

Requires Redis. Easiest way to provide Redis server is to use Docker:

```docker run redis -d -p 6379:6379```
or
```docker run redis -d --network host```

### Running with python

Go to project root. Ensure all dependencies in requirements.txt are met:

```pip install -r requirements.txt```

At least single RQ worker is needed. Run:

```rq worker content-fetcher-tasks```

Then start app:

```python3 app.py```

### Running with docker

#### Build image

```docker build -t fetcher .```

#### Launch

To provide persistence of data set ```STORAGE_DIR``` to some safe location.

At least one Redis worker is needed. To run worker:

```docker run --network host -v "$STORAGE_DIR":/storage -e RUN_REDIS_WORKER=true fetcher```

To prepare database and launch application run:

```docker run --network host -v $STORAGE_DIR:/storage -e UPGRADE_DB=true fetcher```

Running containers with ```--network host``` is not necessary, that's just the easiest way to provide connection to Redis service.

### Running the tests

The tests use RQ in sync mode, so no workers are needed, but Redis service has to be available.

##### Launching tests

```./run-tests.sh```

## Important TODOs for production-readiness

 - Switch to some production-ready HTTP server
 - Improve image scraping mechanism (handle more ways images are embedded)
 - Add security, provide some basic user mechanism
 - Add more API endpoints allowing some content search and some convenience (would be nice to standardize API with Swagger)
 - Improve error handling
 - Add logging
 - Implement some different storage than file system (e.g. HDFS, Amazon S3)
 - Write more tests
 - Reduce Docker image size
 - Write some docker-compose and Helm chart integrating application, Redis, and Redis workers
