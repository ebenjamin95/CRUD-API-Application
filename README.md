Architecture Description
The given code represents a REST API application built with Flask, a Python web framework, for event tracking. 
The architecture consists of the following components:

Flask App: The app object is an instance of the Flask class, representing the main application. 
It serves as the central component for handling incoming requests and routing them to the appropriate endpoints.

SQLAlchemy: The SQLAlchemy object (db) is used to interact with the PostgreSQL database. 
SQLAlchemy is an Object-Relational Mapping (ORM) tool that allows Python classes to be mapped to database tables, simplifying database operations.

Marshmallow: The Marshmallow object (ma) is used for data serialization and deserialization. 
It provides a convenient way to define schemas for data objects (in this case, events) and convert them to JSON format.

Database Model (Event): The Event class represents the model for an event. 
It is a SQLAlchemy model with properties that map to database columns (id, title, description, user_id). 
Each instance of this class corresponds to a row in the "events" table in the PostgreSQL database.

Event Schema: The EventSchema class defines the serialization schema for the Event model. 
It specifies which fields to include when serializing events to JSON format.

Routes and Endpoints: The code defines several routes (URL paths) and corresponding endpoint functions to handle different HTTP requests:

/: The home page of the application.
/events: POST request to create a new event.
/events/all: GET request to fetch all events in the database.
/events/user/<int:user_id>: GET request to fetch events for a specific user.
/events/<int:event_id>: GET request to fetch a specific event by ID.
/events/<int:event_id>: DELETE request to delete a specific event by ID.
/events/search: GET request to search events based on a provided search term.
Database URI Configuration: The code sets the SQLALCHEMY_DATABASE_URI configuration parameter to connect to the PostgreSQL database. 
The URI contains the necessary information to establish a connection, including the database name, username, password, and host.

Overall, this architecture follows the typical pattern of a RESTful API application with a database backend. 
It allows users to perform CRUD (Create, Read, Update, Delete) operations on events, as well as search for events based on their titles or descriptions. 
The application uses PostgreSQL as the relational database management system to store event data.



Installation Instructions (Windows)
1. Download Postman to test the app: https://www.postman.com/downloads/
2. After download, make sure to start the app without creating an account. 
3. If postgresql has not been downloaded, please download it here: https://www.postgresql.org/download/windows/
a. During installation, make note of your chosen username, password, and port. Default username should be postgres
4. After download, open Powershell. Right click on the Powershell icon and choose Run as Administrator 
5. In order to ensure postgres is running, type the following command: 
	net start postgresql-x64-15.
6. Navigate to postgres bin directory using the following command:
	cd C:\Program` Files\PostgreSQL\< version >\bin 
	(<version> should be 12, 13, 14, etc..)
7. To start SQL, type the following command: .\psql -U postgres or psql -U postgres
8. Create the database you are going to use by typing the following:
	CREATE DATABASE events OWNER username (username should be postgres unless you created your own);
9. Navigate to the events database by typing: \c events
10. Create the following table using this command:

	CREATE TABLE event (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	description VARCHAR(200),
	user_id INTEGER NOT NULL
	);

11. Change the username and password on line 8 of the source code (app.py) to match what you recorded in step 2a. The port number should default to 5432. If it doesn’t, please change that as well.
12. Open app.py in Pycharm (or any other IDE for Python)
13. Open a terminal within Pycharm
14. Create a virtual environment through the terminal using the following command:
	python3 -m venv vm_name
15. Activate the virtual environment:
	vm_name \Scripts\activate
	a. If running scripts in disabled on your system, run the following command:
		Powershell -ExecutionPolicy Bypass
		Then run the first command again
16. Install dependencies with the following commands:
	pip3 install flask
	pip3 install flask-sqlalchemy
	pip3 install psycopg2
17. Run the application using the command: flask run
18. When running, click the link that the application is running on and the home page should pop on your browser.
	a. Please see figure below. Ignore the warning message. Click the link highlighted in blue to start the application.



Script Examples

Home Page
URL: http://127.0.0.1:5000 
This solution should provide the following response: Welcome to the Event Tracker App!

Create New Event
URL: http://127.0.0.1:5000/events
Input Event: 
{
    "title": "Essien's Event",
    "description": "This is the first event",
    "user_id": 125
}

This solution should provide the following response: 
{
    "description": "This is the first event",
    "id": 4,
    "title": "Essien's Event",
    "user_id": 125
}

See All Events Created
URL: http://127.0.0.1:5000/events/all
This solution should provide the following response: 
{
    "description": "This is the first event",
    "id": 4,
    "title": "Essien's Event",
    "user_id": 125
}

Get a Specific Event
URL: http://127.0.0.1:5000/events/4
This solution should provide the following response:
{
    "description": "This is the first event",
    "id": 4,
    "title": "Essien's Event",
    "user_id": 125
}

Search for Specific Events by Title or Description
URL: http://127.0.0.1:5000/events/search?term=Essien
This solution should provide the following response:
{
    "description": "This is the first event",
    "id": 4,
    "title": "Essien's Event",
    "user_id": 125
}

Delete a Specific Event
(Set method to Delete)
URL: http://127.0.0.1:5000/events/4
This solution should provide the following response:
{
    "description": "This is the first event",
    "id": 4,
    "title": "Essien's Event",
    "user_id": 125
}
