## Flask Color App

Simple Falsk app which changes its background color by passing an environment variable.
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

### Using Docker
```
$ docker run -e APP_COLOR=blue -p 5000:500 m4tt4r/flask-color-app
```