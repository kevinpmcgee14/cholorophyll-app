#!bin/bash
docker buildx build --platform linux/amd64 -t chlorophyll-api .
docker tag chlorophyll-api registry.heroku.com/chlorophyll-api/web
docker push registry.heroku.com/chlorophyll-api/web
heroku container:release web -a chlorophyll-api