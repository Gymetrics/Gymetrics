# Django Channels demo 

The following repo contains code on how to build Django Channels into your application 
with endpoints created by Django REST framework. 

# Dependancies 
- Install brew from https://brew.sh/ 
- Install python and pip from brew 
- Install redis from brew: ``brew install redis``
- Start the redis service ``brew services start redis``

# Setup 
1. Create a virtual environment by running ``virtualenv env`` in the terminal. 
2. Activate this python environment: ``source env/bin/activate``
3. Install all dependancies found in the requirements.txt. From terminal, run ``pip install -r requirements.txt``
4. Go into the prototype directory: ``cd prototype`` 
4. Migrate: ``python manage.py migrate``
5. Populate the database with some broadcasting channels: ``python manage.py populate_db``
5. Run the server: ``python manage.py runserver``

# Usage 

- Open up your browser and go to localhost:8000/channels. Open up the console and there is a confirmation message
  to assert the connection was successful. 
- With a tool like Postman, you can send PUT requests (as shown below) to update the database. 
<img width="794" alt="screen shot 2017-09-03 at 15 55 40" src="https://user-images.githubusercontent.com/22529514/30004068-5f6e184e-90c0-11e7-9383-d0f30928e9cd.png">


The results will update in real time without the client initially sending off HTTP requests! 

<img width="790" alt="screen shot 2017-09-03 at 15 58 00" src="https://user-images.githubusercontent.com/22529514/30004094-bfc5338a-90c0-11e7-99fa-6373891fef3a.png">

# References 
- https://realpython.com/blog/python/getting-started-with-django-channels/ 
- https://gearheart.io/blog/creating-a-chat-with-django-channels/ 
- https://channels.readthedocs.io/en/stable/ 
- http://www.django-rest-framework.org/
- https://www.getpostman.com/ 
