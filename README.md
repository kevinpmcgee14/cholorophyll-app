# Chlorophyll Predictions

This project has two sections - Machine Learning (ml folder) and an API (src) folder. 

Live api can be accessed at https://chlorophyll-api.herokuapp.com/, and api documentaiton can be found here:  https://chlorophyll-api.herokuapp.com/apidocs/

## ML

The ml folder contains two files:
* `eda.ipynb` contains basic data exploration to understand relationships in the data
* `model_train.ipynb` contains a basic sklearn pipeline to train a model. This model was then serialized and used in live application 
## API

### Live Application
API has been deployed to Heroku and can be accessed here:   https://chlorophyll-api.herokuapp.com/. The main api call can be accessed as follows:

```python
import requests

# assuming paylod data is stored in variable 
# "data" to see data format, refer to 
# https://chlorophyll-api.herokuapp.com/apidocs/

requests.post(
    "https://chlorophyll-api.herokuapp.com/predict", 
    json=data
)
```

### Local Testing
You can run this application locally using `docker compose` via the following command.

```bash
docker compose build
docker compose up
```
This will build a container and expose the application at https://localhost:5000
### API Documentation

Swagger API specification can be found here:  https://chlorophyll-api.herokuapp.com/apidocs/