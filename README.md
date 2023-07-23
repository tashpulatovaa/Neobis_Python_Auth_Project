# Neobis_Python_Auth_Project
## Authorization and authentication functions implemented  
This project implements simple authorization, authentification and email confirmation functions for educational purpose.
## Status
The project is finished. However I might come back to implement password reset function
## Requirements
The project requires most imortant Python and Django installations. Other required libraries and files are shown in requirements.txt file in 

> Neobis_Python_Auth_Project
  >> requirements.txt

![where requirements.txt file is?](https://i.postimg.cc/vZn9WqJ3/Screenshot-from-2023-07-23-13-29-20.png)

# A guide to installation and use
### Clone the repository to your local machine:
```
git clone [https://github.com/your-username/your-repo.git](https://github.com/tashpulatovaa/Neobis_Python_Auth_Project.git)
cd your-repo
```
### Create a virtual environment (optional but recommended) to keep the project dependencies isolated:
```
python -m venv venv
```
### On Windows:
venv\Scripts\activate
### On macOS/Linux:
source venv/bin/activate
### Install the required dependencies:
```
pip install -r requirements.txt
```
### Set up the database:
```
python manage.py migrate
```
### Create a superuser to access the Django admin interface:
```
python manage.py createsuperuser
```

# Usage
### Run the development server:
```
python manage.py runserver
```
Open your web browser and go to http://127.0.0.1:8000/ to access the application.
### On your page this should appear:
![Home page](https://i.postimg.cc/rwmJ42cW/Screenshot-from-2023-07-23-13-48-58.png)

### To access the Django admin interface, go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created during installation.

The application should have basic user authentication features like registration, login, logout, and password reset. Navigate through the provided user interfaces to test these functionalities.

If you want to integrate the authentication system into your own Django project, follow these steps:

Copy the accounts app from this project into your Django project.

Add 'accounts' to the INSTALLED_APPS list in your project's settings file.

Include the app's URLs in your project's urls.py:

```
from django.urls import path, include

urlpatterns = [
    # Your other URL patterns
    path('accounts/', include('accounts.urls')),
]
```
Customize the templates, views, and forms in the accounts app according to your project's requirements.

## Contributing
If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request. We welcome contributions from the community.

## License
-
