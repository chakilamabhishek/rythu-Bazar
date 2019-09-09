This A transparent and trustworthy portal to connect farmers directly to the consumers

Demo of this site :https://abhishekch.pythonanywhere.com/


download or clone the project https://github.com/chakilamabhishek/rythu-Bazar.git

download requiremets.txt

install git in your computer ,python3.6 and pip

then run command 
pip install requirements.txt

download and install mysqlworkbench

create a database 'NAME': 'rythubazardb',
        'HOST': 'localhost',
        'USER':"username",
        'PASSWORD': "enter password"
==>change the above details in settings.py


go to the working directory run the following commands

1)py manage.py makemigrations
2)py manage.py migrate

all the tables are created in the repective database

3) to get project up and running 

execute the command==> py manage.py runserver


Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 09, 2019 - 10:56:19
Django version 2.2.1, using settings 'rythubazar.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

go to  http://127.0.0.1:8000/ 


