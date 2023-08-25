import configparser
from flask import Flask
import requests

def chave():
    config = configparser.ConfigParser()
    config.read('h_twikeys.ini')
    auth = config['twitter']['api_key'], config['twitter']['api_key_secret'], config['twitter']['bearer_token'], config['twitter']['access_token'], config['twitter']['access_token_secret']
    return auth

app = Flask(__name__)
app.config.from_object(chave())
@app.route('/chaves', methods=['GET'])
def root():
    return 


if __name__ == "__main__":
    app.run()
