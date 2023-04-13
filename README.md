# Snap it API (Django Rest Framework)

* [**Project**](<#project>)
* [**Project Management**](<#project-management>)
* [**Wireframes**](<#wireframes>)
* [**User Experience UX**](<#user-experience-ux>)
* [**Features**](<#features>)
* [**Future Features**](<#future-features>)
* [**Testing**](<#testing>)
* [**Technologies Used**](<#technologies-used>)
* [**Bugs**](<#bugs>)
* [**Unfixed Bugs**](<#unfixed-bugs>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Acknowledgement**](<#acknowledgement>)


# Project
Welcome to Snap it's API. This API is the connection between the front-end and the back-end of the Snap it application. The API is created with Django REST Framework. 

[Front-end live link](https://front-end-react.herokuapp.com/)
<br>

[Front-end repository](https://github.com/frirsta/react-front-end)

The front-end application is connected to Snap it's API.

[Back-end API repository](https://github.com/frirsta/drf-api-react)
<br>

[Back-end API deployment](https://drf-api-frirsta.herokuapp.com/)


<br>


<br>

# Project

<br>

# Project Management

<br>

# Database model
<img src="assets/readme/database_model.png" alt="database model" > 

<br>

# Features

<br>

# Future Features

<br>

# Testing
## [Python Validation](https://pep8ci.herokuapp.com/)
The code passed the pep8 validation.
There were 4 small errors found in the settings.py that cannot be fixed and there is no need for them to be fixed.

<img src="assets/readme/test_fail.png" alt="post test fail" style="width: 50%" > 
<img src="assets/readme/test_pass.png" alt="post test pass" style="width: 50%" > 

<br>

# Technologies used
* Python - For functionality of the website
* Django - Model-View-Template framework
Git 
* GitHub - Used to host the website
* GitPod - For deployment of the website
* [Miro](https://miro.com/) - For creating the Wireframes

<img src="assets/readme/technologies.png" alt="post test pass" > 

## Libraries and other resources
[Django](https://www.djangoproject.com/) Python framework for fast development and clean design.
[Django REST Framework](https://www.django-rest-framework.org/) A toolkit for building Web APIs.
[Django AllAuth](https://django-allauth.readthedocs.io/en/latest/) Authentication, registration, account management and 3rd party account authentication.
[Django Cloudinary Storage](https://pypi.org/project/django-cloudinary-storage/) Provides Cloudinary storages for media and static files.
[Django Cors Headers](https://pypi.org/project/django-cors-headers/) Is an application for handling the server headers required for Cross-Origin Resources Sharing
[Django filter](https://django-filter.readthedocs.io/en/stable/) Allows user to filter down a queryset based on a model's fields, displaying the form to let them do this.
[dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) Provides a set of REST API endpoints, to handle user registration and authentication tasks.
[dj-rest-auth with_social](https://dj-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional) Provides classes for creating a social media authentication view.
[djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) JSON Web Token authentication plugin for Django REST Framework.
[Pillow](https://pypi.org/project/Pillow/) Imaging Library.
[Django phonenumber field](https://django-phonenumber-field.readthedocs.io/en/latest/index.html) Validate and convert phone numbers.
[Dj database URL](https://pypi.org/project/dj-database-url/) Use Database URLs in Django Application.
[Psycopg2](https://pypi.org/project/psycopg2/) Python PostgreSQL Database Adapter.
[gunicorn](https://gunicorn.org/) Allows to run Python applications by running multiple Python processes within a single dyno.


<br>

# Database/Hosting
* Heroku - The platform where the application is deployed
Gunicorn
Cloudinary
Pillow
Psycopg2
PostgreSQL
PyJWT

# Bugs

<br>

# Unfixed Bugs

<br>

# Deployment

This website was deployed to [Heroku](https://heroku.com/). To deploy the website follow the steps below:

1. Log in or create an account on heroku.

2. On the heroku Website click 'New' and after click 'Create new app'.

3. Write the app name, choose a region and then click 'Create app'. 

4. In the application website click 'Deploy' on the navigation menu.

5.  In the 'Deploy' page, click the GitHub logo. Search for the GitHub repository that was made for this project.

6. Search for the GitHub repository that was made for this project.

7. When the repository is found click 'Connect'.

8. Scroll down to manual deploy and make sure you have chosen the main branch.

9. Click deploy.

<br>

# Cloning

1. Open the GitHub repository. 

2. Click the green 'Code' button and copy the given URL.

3. Open Git Bash and change directory to where you want the cloned directory.

4. Write: 
<pre>
"git clone"
</pre> 
, and paste the URL that was copied in Github and then click 'enter'.

<br>

5. In Git Bash locate the cloned directory.

6. Type:
<pre> "code ."
</pre>
This will launch the project in VSCode.

<br>

7. Now install the requirements needed to run the project by typing this command: 
<pre>
"pip3 install -r requirements.txt".
</pre>

<br>

8. Create an 'env.py' file in the top level directory. Add the following code and their values:
<pre>
import os

os.environ['CLOUDINARY_URL'] = 'your cloudinary url'
os.environ['DATABASE_URL'] = 'your database url'
os.environ['SECRET_KEY'] = 'your secret key'
</pre>

<br>

9. Add the variables from the env.py file in Herokus Config Vars when it is time for deployment.


10. Now run this command:
<pre>
"python manage.py migrate"
</pre> 

11. Run this command:
<pre>
"python manage.py runserver"
</pre>

If everything is working as expected the project will launch and be ready for development.

# Credits

Sources that have helped build the website:
Default profile image:
<a href="https://www.flaticon.com/free-icons/user" title="user icons">User icons created by Freepik - Flaticon</a>

Default post image:
<a href="https://www.flaticon.com/free-icons/picture" title="picture icons">Picture icons created by Chanut - Flaticon</a>

[Django REST Framework documentation](https://www.django-rest-framework.org/)
[Stack Overflow](https://stackoverflow.com/)

<br>

# Acknowledgement
This website has been made for my 5th Portfolio Project (Advanced Front-end) - Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/).
I would like to thank my mentor PGareth McGirr from Code Institute who helped me develop the website with feedback through the project.