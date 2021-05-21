# Python YOLO Object Detection using OpenCV - Flask App

To run this locally:
* Download the [model weights](https://pjreddie.com/media/files/yolov3.weights) and put them in the `app/weights`. Right now the folder is empty - you need to put the output of the model weights download into this folder once you have cloned this repo. 

* The `cos_bucket` branch updates the model weights by looking for them in an IBM S3 Cloud Object Storage (COS) bucket. You will require a `.env` file with the credentials to connect to an IBM COS bucket and retrieve the model weights from there. The benefit here is that we can have a service that ensures the model weights in the COS bucket are always up to date, this webapp can then always pull and use the most up to date model. The structure of the `.env` file should be:

```
apikey=""
endpoints=""
iam_apikey_description=""
iam_apikey_name=""
iam_role_crn=""
iam_serviceid_crn=""
resource_instance_id=""
auth_endpoint="https://iam.bluemix.net/oidc/token"
service_endpoint="https://s3.eu-gb.cloud-object-storage.appdomain.cloud"
bucket_name=""
```

All of the above credentials can be found from the Service Credentials section in IBM Cloud COS page; the storage bucket can be created via the resource page [here](https://cloud.ibm.com/resources). Note: You will need an IBM Cloud account.

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