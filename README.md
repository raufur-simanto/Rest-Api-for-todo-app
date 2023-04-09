# TODO API
## Introduction
- This is a simple crud api for todo app
## Technologies
- Flask
- Flask-restx
- docker
- postgres

## End Points
- ### GET api/todo/get-data
- ### POST api/todo/add
- ### POST api/todo/get-data-name
- ### PUT api/todo/update
- ### DELETE api/todo/delete

## Necessary CMD
### Running app
- docker-compose up --build

### Connecting postgres
- docker exec -it <db_container> sh
- psql -h <db_server> -u <db_username>


