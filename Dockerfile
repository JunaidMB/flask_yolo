# Use the Python3.7.4 container image
FROM python:3.7.4-stretch

# Set the working directory to /app
WORKDIR /app/

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip3 -q install pip --upgrade
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

# Expose Port
EXPOSE 5000

# run the command to start app
ENTRYPOINT ["python"]
CMD ["run.py"]