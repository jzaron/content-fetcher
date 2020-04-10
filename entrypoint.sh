#!/bin/bash

if [ "$RUN_REDIS_WORKER" == "true" ]; then
  exec rq worker "$REDIS_QUEUE_NAME"
fi

if [ "$UPGRADE_DB" == "true" ]; then
    flask db upgrade
fi

exec "$@"
