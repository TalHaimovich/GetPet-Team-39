GetPet

This project was created for the course "Fundamentals of Software Engineering" Sami Shimon Academic College.


------Contributors-------
Tal Haimovich
Mor Merkrebs
Ortal Nosik
Asif Eretz-Kdosha

-------Setup & Installtion-------
Make sure you have the latest version of Python installed.
pip install instructions

------Instructions--------
you should install flask framework(use terminal and install via pip)
you will need to install the further add-ons for flask:
Flask==2.0.2
Flask-Bcrypt==0.7.1
Flask-Login==0.5.0
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.0
email-validator==1.1.3
bcrypt==3.1.4
certifi==2016.2.28
cffi==1.11.5
click==6.7
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
pycparser==2.18
six==1.11.0
SQLAlchemy==1.2.7
Werkzeug==0.14.1
WTForms==2.1
for the unittest:
flask_testing==1.0
blinker==1.4
pytest==1.0

-----Data Base Instructions------
The data base will be created automaticly when running the project for the first time(or if the data base file has been deleted)
-Note: if you change data-baswe related objects and attributs you shuld recreate the data-base file

--------Requirements for development--------
The requirements developed in the system are:
1. Possibility for associations / associations to register on the site
2. As an association / association I want to log in to my user (log in)
3. As an association / association, it is possible to update users with information about events.
4. As an association / association, I would like to have the opportunity to publish ads for adoption
5. As an association / association, I would like to have the opportunity to edit the details of the association / association.
6. As an association / association, it is possible to edit ads on published animals.
7. As an association / association, I have the option of receiving monthly reports
As an association / association, I would like to see all the posts I have published
9. As an association / association in Israel, it is possible to send tips / advice.
10. As an association / association I would like to give Petcoin (GetPet digital currency)
For active users in the community
11. As a business owner, I would like to register on the site as a business manager / store owner.
12. As a business owner I want to connect to a suitable user.
13. As a business owner, I would like the opportunity to upload products on sale.
14. As a business owner I would like the option to upload a product post.
15. As a business owner I want the option to edit the business page.
16. As a business owner, I want to be able to update the users of the site.
17. As a business owner in Israel, it is possible to receive monthly reports.
18. As a business owner, you have the option of editing product ads.
19. As a consumer I want to be able to track the status of my orders.
20. As a business owner I want to be able to see all the posts I have published.
21. As a regular user, I would like the option to register on the site.
22. As a regular user I would like to connect to a suitable user.
23. As a regular user I would like the opportunity to post an animal for foster care.
24. As a regular user I would like the option to post an animal for adoption.
25. As a regular user I would like the option to rate other users.
26. As a regular user I would like the option to know that irrelevant posts will be handled.
27. As a regular user I would like the option to report posts.
28. As a user, I want a filtering option in the search.
29. As a user I would like to view information about animals awaiting adoption.
30. As a user I would like the option to edit ads I post.
31. As a user I would like to give Bitcoin (GetPet digital currency) to users
32. As a regular user I have a high level of safety.
33. As a user, I want to receive reports.

--------Changes in development requirements--------
User story 2,11,12- A requirement has been added to go to the home page in online status
User story  10- Updated transfer field for rules by association.
User Story 20 - A profile profile has been added for a business user.
User story 26- Updated that reporting handling will be done by 3 reports from different users.
User Story 33- Download a regular user's access to user reports.
User story 28 - Its implementation affected the possibility of filtering for other users as well, thus extending to additional requirements that are not specified.
User story 31- A requirement was added that the money be transferred according to the quota that the user has.

------Run Program--------
to run the project please run "run.py" file in the main folder of the project

------Viewing The App------
Go to http://127.0.0.1:5000
