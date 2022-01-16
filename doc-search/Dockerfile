FROM python:3.10-slim-bullseye
COPY src /app
COPY requirements.txt /app

RUN pip install -r app/requirements.txt

COPY samples /data

WORKDIR /app
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "__init__.py", "/data" ]