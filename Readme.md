For using the project, 

1.)   Check is python3 installed in your system or not than install django by using the command :- ' pip install django '.


2.)   Update the databases section of the project's settings.py file, according to your database. 
      For instructions visit :- https://www.javatpoint.com/how-to-connect-mysql-to-django


3.)   Now, create a superuser for the project using command to create a superuser :- " python manage.py createsuperuser "
      And than fill the informations it asks whatever you want but just remember that information.


4.)   Now, start your server by running the command :- " python manage.py runserver "
      And a link will shown on your terminal just copy it and than open any browser of your system and than paste the link and write "/admin/". Now, click enter.


5.)   A login page as shown below will be displayed on your screen :- 

	



       Enter the username and password you entered while creating the superuser.


7.)   After logging in you will get a page shown below :- 




	Now, as you can see a add option in front of users. Just click on in and add as many users as your want and remember the passwords and username of them.

8.)   Now, after completing above process just go back to your terminal and hit " ctrl + c " to stop your server and than run the following commands :- 
            a.)  " python manage.py makemigrations "
            b.)  " python manage.py migrate "


9.)   Now, again run the server with the command :- " python manage.py runserver "
