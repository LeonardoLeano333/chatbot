create environment variables

in app directory run:

python manage.py migrate 

obs: this creates the database and make the migrations for the admin table

create superuser, and put the credentials for the user:

python manage.py createsuperuser

runing server:
python manage.py runserver

testing UI:
localhost:8000/

put your user credentials

if it is authenticated it will enter in the page to make the the things to chat with the chat bot

run the comands for running the constainers:

docker-compose up 

obs.: it will show some erros because rabbit is not operational after operational it runs okay

# registering a users
docker exec -i -t app sh
python manage.py createsuperuser
