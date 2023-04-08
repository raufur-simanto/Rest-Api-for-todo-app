# Base Image
FROM python:3.10-slim-buster

# set working directory
WORKDIR /usr/app


# copy and install necessary dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# boot configuration for container
CMD ["flask", "run", "--host=0.0.0.0"]