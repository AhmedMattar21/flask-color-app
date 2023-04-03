## Flask Color App

Simple Falsk app which changes its background color by passing an environment variable.
![Screenshot of the app.](https://github.com/AhmedMattar21/flask-color-app/blob/master/static/images/color_app.png)

### Run it using Docker
```
$ docker run -e APP_COLOR=blue -p 5000:5000 m4tt4r/flask-color-app
```

### Run it using Python
```
$ cd flask-color-app
$ pip3 install -r requirements.txt
$ export APP_COLOR=gold
$ flask run
```

> Python version 3.10.6
