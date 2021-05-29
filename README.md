# Chat Bot

## Running project

run the project:

`docker-compose build `

Obs.: some errors may occor because rabbitmq delays to be operational

after build run the services:

`docker-compose up `

setting up a user 

`docker exec -i -t app sh`

in the container

`python manage.py createsuperuser`

and create a new user passing user name, email, and password

## test the UI

Open the browser in the url: localhost:8000/

put your user and chet it alt the chat and the bot messages
