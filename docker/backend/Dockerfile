FROM python:3.9.13-slim

RUN python3 -m venv /opt/venv

WORKDIR /apps/backend

COPY ./apps/backend/ .

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r /apps/backend/requirements.txt && \
    chmod +x /apps/backend/entrypoint.sh

CMD ["/apps/backend/entrypoint.sh"]