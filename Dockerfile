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
ADD --chown=1000:1000 fetcher.py requirements.txt ./
ADD --chown=1000:1000 fetcher/ fetcher/
ADD --chown=1000:1000 migrations/ migrations/
RUN pip install -r requirements.txt && rm -r /root/.cache

ENV FLASK_APP="fetcher"
ENV UPGRADE_DB="true"
ADD --chown=1000:1000 entrypoint.sh "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]
CMD [ "python", "fetcher.py" ]
EXPOSE 5000

USER "$USER"
