# FROM python:3.10

# WORKDIR /code

# RUN apt-get -y update  && apt-get install -y \
#   python3-dev \
#   apt-utils \
#   python-dev \
#   build-essential 


# RUN pip install --upgrade pip
# COPY ./requirements.txt /code/requirements.txt
# #RUN code/.venv/bin/pip install --no-cache-dir --upgrade -r /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./iris-api /code/iris-api
# #COPY ./data /code/data
# COPY . /code

# #EXPOSE 8080
# #EXPOSE 8080:8080
# #ENV PORT $PORT


# ENV PYTHONPATH "${PYTHONPATH}:/code/iris-api"
# #CMD ["make dev"]
# EXPOSE $PORT
# CMD gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT iris-api.main:app
# #CMD ["uvicorn", "iris-api.main:app", "--reload",  "--workers", "1", "--host", "0.0.0.0", "--port", "$PORT"]

# # If running behind a proxy like Nginx or Traefik add --proxy-headers
# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port number that the FastAPI application should run on
EXPOSE 8080

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "app:application", "--host", "0.0.0.0", "--port", "8080"]
