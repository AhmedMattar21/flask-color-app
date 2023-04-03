from flask import Flask, render_template
import os, subprocess


def whoami():
    myname = subprocess.check_output(['whoami'])
    myname = str(myname)
    filter1 = myname.split("'")
    filter2 = filter1[1].split('\\')
    cleanName = filter2[0]
    return cleanName


userName = whoami()
color = os.environ.get('APP_COLOR')

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html', userName=userName, color=color)



if __name__ == "__main__":
    app.run()