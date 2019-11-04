import os
from flask import Flask

## create an instance of flask and assign it to the app variable
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello there"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)