# Pinned to the Python version the project targets (see .github/workflows).
FROM python:3.11-alpine

LABEL maintainer="arnarfkr@gmail.com"

WORKDIR /app

# Prevents Python from writing pyc files and
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PATH="/venv/bin:$PATH" \
DJANGO_SETTINGS_MODULE=Bloggity.settings.production

# Runtime libraries: libpq for psycopg2, tzdata for timezone support.
RUN apk add --no-cache libpq tzdata && python3 -m venv /venv

# Copied on its own so the dependency layer is cached across source changes.
COPY requirements.txt ./

# The toolchain needed to build psycopg2 is installed as a virtual package and
# dropped again once the wheels are in place, so it stays out of the image.
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libpq-dev && \
pip install --no-cache-dir gunicorn && \
pip install --no-cache-dir --requirement ./requirements.txt && \
apk del .build-deps

# Copy the source code into the container.
COPY . .

RUN chmod +x /app/docker-runserver.sh && \
addgroup -S appgroup && adduser -S appuser -G appgroup && chown -R appuser:appgroup /app

EXPOSE 8080

USER appuser

ENTRYPOINT ["/app/docker-runserver.sh"]
