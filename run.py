from os import environ
from flask import Flask, render_template

from APIGateway.API import service

app = Flask(__name__) # Flask app tanımlandı.
app.register_blueprint(service) #API modülü içinden çağrılacak tanımlandı.


if __name__ == '__main__':


    app.run(host='0.0.0.0', port=9000, debug=True)
  

