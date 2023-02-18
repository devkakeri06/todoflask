# todoflask

## Prerequisites:-

Python 3 or higher installed on your computer.
Flask framework installed in Python. You can install Flask by running the following command in your terminal/command prompt:
```
$ pip install flask
```
## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ ctrl + shift + p
```

3. Then run the command:
```
$ ctrl + shift + `
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Start the web server:
```
$ (env) python -m flask run
```
This will start the Flask development server and your app will be accessible at http://localhost:5000 in your web browser.
Alternatively you can use http://devkakeri.pythonanywhere.com to test the API


## Steps to run on docker

1. First buuild a docker image

```
$ docker build --tag python-docker .

```
2. Run the docker image as a container
```
$ docker run -d -p 5000:5000 python-docker
```

