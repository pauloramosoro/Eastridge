# Project with Flask Eastridge

## Introduction
#### The intention of the application is to create a list of items from any shop to then store the data in MySql database called "flask_invoice" and then proceed to do something with the data. It can be a machine learning model or a visualization dashboard to have some stats about the products sold in the shop.

## Enviroments
Python 3 Installed
Flask library (pip install flask)
Flask-mysqldb (pip install flask-mysqldb)
MySql Database set with the following parameters:
**app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_invoice'**

## Instructions to run the python app in you computer.

**1.-** First step is to intall MySql in your computer. I did it with windows 11 so pleas follow the steps in the following link: https://www.testingdocs.com/download-install-mysql-on-windows-11/.

**2.-** Once that MySql is installed in your computer download raw schema fila named "flask_invoice.sql" and name the new schema EXACTLY the same name as the file without the .sql extention. (e.g "flask_invoice").

**3.-** Download the "Eastridge_Challenge" folder from this github and use an editor to open the full folder (In my case I used VSCode).

**4.-** Run the "app.py" file and open the "http://...." in you browser of preference.

## How the app works?

**Add** : It is adding Data to a table in the database throguh a form in the app. Evrytime the user input a new data it will be added to the original table
![image](https://user-images.githubusercontent.com/41079560/160296227-ccb15b72-6f19-4512-af64-68ad42e1ab1f.png)

**Edit** : If the user clicks on edit data, it will select the expected row and it will take the user to a different windows to alter the data on that especifc row
![image](https://user-images.githubusercontent.com/41079560/160296249-0357abb3-ed65-4e0d-b06a-daa91b789da4.png)

![image](https://user-images.githubusercontent.com/41079560/160296268-7843c875-a5e0-47e2-8a5f-3be74f7aad37.png)

**Delete** : When the user decided that is time to delete some data because a mistake, the user can click on the delete button and the app will ask again to confirm this deletion.
![image](https://user-images.githubusercontent.com/41079560/160296303-991b70b8-f417-4fc4-9f3c-ee032fbb86e5.png)

***All of the 3 actions comes with its confirmation message if everything whent well (e.g "Added Item Successfully" , etc.)***

The project is using bootstrap and css for style layout and some JavaScript for a click function to remove the message.

## Conclusion
This is a simple project  to demonstrate how flask works in the back end to server data from table in a database. This type of project are scalable to create different functions and more coplex systems for users interactions. 


