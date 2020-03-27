# content-fetcher 

Flask based microservice to scrap text and images from web pages. Uses Redis for multitasking.

Project in alpha stage.

## Launching

Requires Redis. Easiest way to provide Redis server is to use Docker:

```docker run redis -d -p 6379:6379```

### Running with python

Ensure all dependencies in requirements.txt are met. Then:

```python3 fetcher.py```

### Running with docker

#### Build image

```docker build -t fetcher .```

#### Launch image

To provide persistence of data set ```STORAGE_DIR``` to some safe location.
As Redis is required, the easiest way to run it using Docker is to run it with host network stack:

```docker run -p 5000:5000 --network host -v $STORAGE_DIR:/storage fetcher```

### Running the tests

Requires Redis. Easiest way to provide Redis server is to use Docker:

```docker run redis -d -p 6379:6379```

##### Launching tests

```./run-tests.sh```

## Important TODOs for production-readiness

 - Add security, provide somme basic user mechaism
 - Add more API endpoints allowing some content search and some convenience (would be nice to standarize API with Swagger)
 - Improve error handling
 - Add logging
 - Allow running Redis queue in async mode, switch to sync mode only for tests (already tested, beside tests async mode works fine)
 - Switch to some producion-ready HTTP server
 - Improve image scraping mechanism (handle more image src formats)
 - Implement some different storage than file system (e.g. HDFS, Amazon S3)
 - Write more tests
 - Reduce Docker image size
 - Write some docker-compose and Helm chart integrating application, Redis, and Redis workers