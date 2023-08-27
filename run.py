import configparser
from flask import Flask

def chave():
    config = configparser.ConfigParser(interpolation=None)
    config.read('h_twikeys.ini')
    auth = config['twitter']['api_key'], config['twitter']['api_key_secret'], config['twitter']['bearer_token'], config['twitter']['access_token'], config['twitter']['access_token_secret']
    return auth

app = Flask(__name__)

#app.config.from_object(chave())
@app.get('/chaves')#, methods=['GET'])
def root():
    chave = chave()
    print(chave, type(chave))
    return chave


if __name__ == "__main__":
    #app.run()
    chave = list(chave())
    print(chave)