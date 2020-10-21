
# Gameshop
##Setup
$ python3 -m venv .venv
$ source .venv/bin/activate

$ pip3 install -r requirements.txt

$ cd gameshop
$ touch .env

Inside .env define your secret key like this:

SECRET_KEY=some_random_key
###Run
$ python3 manage.py runserver
;;