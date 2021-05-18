# Python YOLO Object Detection using OpenCV - Flask App

To run this locally:
* Download the [model weights](https://pjreddie.com/media/files/yolov3.weights) and put them in the `app/weights`. First create a `weights` directory in the `app` directory, then place the downloaded weights into this folder on your machine - these are the model weights, the app will not run without them.

* In the terminal:
	 1. run the package dependencies `pip install -r requirements.txt`
	 2. We want to run the flask app in development mode so run the following `export FLASK_ENV=development`
	 3. `export FLASK_APP=run.py`
	 4. To run the flask app `flask run`

 * Go to `http://127.0.0.1:5000/uploadfile` to use the flask app
 * Run `Ctrl+ C` in the terminal to kill the flask app

 * To run this via Docker:
	 1. Build the Docker image specified in the Dockerfile: `docker build -t <name of image> .` where `<name of image>` can be whatever you name the image - I suggest `flask_yolo` as an image name. 
	 2. To run the docker image (that doesn't persist): `docker run --rm -p 5000:5000 <name of image>`

* My Docker commands [cheatsheet](https://paper.dropbox.com/doc/Docker-Commands--BK5FqijlQtJSRvllC_T_AG2PAg-IL47J9mwFMg67Lmn0vKaC)
* Warning: The Docker image may crash due to memory issues - to avoid this you can increase the docker memory. The instructions for Mac are [here](https://docs.docker.com/docker-for-mac/#:~:text=Memory%3A%20By%20default%2C%20Docker%20Desktop,swap%20file%20size%20as%20needed.)