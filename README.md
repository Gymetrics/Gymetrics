# Django Channels demo 

The following repo contains code on how to build Django Channels into your application 
with endpoints created by Django REST framework. 

# Depedancies 
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

# References 
- https://realpython.com/blog/python/getting-started-with-django-channels/ 
- https://gearheart.io/blog/creating-a-chat-with-django-channels/ 
- https://channels.readthedocs.io/en/stable/ 
- http://www.django-rest-framework.org/
