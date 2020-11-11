**Assignment - User data storage**

Project is on the web server:

https://tranquil-crag-39487.herokuapp.com/

_all commands for this project:_

######install django in virtual environment

`pipenv install django` 

######activate virtual environment 
`pipenv shell `


######create django project
`django-admin startproject store_data_proj`

######create new application for store,retrieve,update and delete data
`python manage.py startapp stores_data`

######to upload the application to a web server in production level
`pipenv install gunicorn`


######to migrate the model
`python manage.py makemigrations`

`python manage.py migrate`

######to create superuser (admin)
`python manage.py createsuperuser`

######For PostgreSQL and pgAdmin4
`pipenv install psycopg2`

######For static file in server (image,css,javascript,bootstrap etc.)
`pipenv install whitenoise`

###### Upload project to Heroku Server
`heroku login`

`heroku create`

`heroku git:remote -a "domain name"`

`git init`

`git status`

`git add -A`

`git commit -m "Upload Project"`

`git push heroku master`

`heroku ps : scale web =1` 


**API create:** 

######In the api apps(folder) in url section we find the following API:

**All API List:**

https://tranquil-crag-39487.herokuapp.com/api/

**For create parent user:** 

https://tranquil-crag-39487.herokuapp.com/user-create/parent/

**For create child user:** 

https://tranquil-crag-39487.herokuapp.com/user-create/new/child/

**For show all user (Retrieve all data) :** 

https://tranquil-crag-39487.herokuapp.com/userlist/

**For show individual user (Retrieve specific data) :**

`https://tranquil-crag-39487.herokuapp.com/users/<int:pk>/`

**Example:
For retrieve id = 1** 

https://tranquil-crag-39487.herokuapp.com/users/1/

**For update user info:**

`https://tranquil-crag-39487.herokuapp.com/user-update/<int:pk>/`

Example:
For update information for id =1

https://tranquil-crag-39487.herokuapp.com/user-update/1/

**For delete user info:**

`https://tranquil-crag-39487.herokuapp.com/user-delete/<int:pk>/`

Example:
For update information for id =1

https://tranquil-crag-39487.herokuapp.com/user-delete/1/
