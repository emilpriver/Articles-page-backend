# Pull Docker Image
FROM python:3.7.4-alpine3.10

# Install Alpine build dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev 

# Install Alpine packages
RUN apk add --no-cache mariadb-connector-c-dev gettext python-dev py-pip jpeg-dev zlib-dev libpq postgresql-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE

# Copy src
COPY /backend /usr/app/backend

# Set work directory
WORKDIR /usr/app/backend

# Install Python packages
RUN pip install -r requirements.txt

# Delete Alpine build dependencies
RUN apk del .build-deps
