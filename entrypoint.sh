#!/bin/bash

if [ "$UPGRADE_DB" == "true" ]; then
    flask db upgrade
fi

exec "$@"
