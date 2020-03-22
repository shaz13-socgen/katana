import yaml
import os

from flask import Flask
from apis import api

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':

    if not os.path.exists("./core/models"):
        os.makedirs("./core/models", exist_ok=True)
    app.logger.info("Starting the ML Engines")
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])
