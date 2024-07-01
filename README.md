# Solan
- One small step for Solan, a giant leap for Knowledge.
- Check out the [SITE](https://solan.pythonanywhere.com)

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- this [repository](https://github.com/shreyasvinaya/Solan_withdb/).
- python 3.6.7+
- pip
- django

### STEPS TO RUN THE APPLICATION:

1. run activate from the env folder to activate the virtual env
2. create a user called **_db_user_** with password **_dbpass** in mysql and grant all privilege on a new databases called **_solan$cisco_students_**
3. run the code in the next paragraph


4. go to http://127.0.0.1:8080/admin
5. Create 3 groups called **Student**, **Teachers**, **Admin**
6. go to users and and add a user to a group you want
7. go to logins on the admin page and click on the add login button, select the user and save
8. go to points and click on add points, select the login you just created and save
9. now you will be able to access all the featues of the website without any problems

### Code to be run in step 3
**run them one by one following any steps shown if required**
```
python manage.py makemigrations
python manage.py migrations
python manage.py createsuperuser
python manage.py runserver 8080
```

## Authors
* **[Shreyas Vinaya](https://github.com/shreyasvinaya/)**
* **[Kaveesh Khattar](https://github.com/KaveeshKhattar/)**
* **[Suraj Ranganath](https://github.com/suraj-ranganath/)**

