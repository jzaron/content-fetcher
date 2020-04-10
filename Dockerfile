FROM python:3

ARG USER="app"
ARG APP_DIR="/app"
ENV STORAGE_DIR="/storage"

RUN groupadd -g 1000 app \
 && useradd -g app -u 1000 -d "$APP_DIR" "$USER" \
 && mkdir "$APP_DIR" \
 && chown -R 1000:1000 "$APP_DIR" \
 && mkdir "$STORAGE_DIR" \
 && chown -R 1000:1000 "$STORAGE_DIR"

WORKDIR "$APP_DIR"
ADD --chown=1000:1000 requirements.txt ./
RUN pip install -r requirements.txt && rm -r /root/.cache
ADD --chown=1000:1000 app.py ./
ADD --chown=1000:1000 fetcher/ fetcher/
ADD --chown=1000:1000 migrations/ migrations/

ENV UPGRADE_DB="false"
ENV RUN_REDIS_WORKER="false"
ENV REDIS_QUEUE_NAME="content-fetcher-tasks"
ADD --chown=1000:1000 entrypoint.sh "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "python", "app.py" ]
EXPOSE 5000

USER "$USER"
