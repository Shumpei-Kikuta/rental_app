# What 
This application is the platform on which everyone can lend or borrow everything under the given procedure, intended on students attending the University of Tokyo.<br>
It is created to solve the problem that students have to buy textbook just for exam and want to utilize books which does not be used for a while.<br?

# Setup 
## Database
It is necessary to prepare the postgreSQL database named "web_eng".<br>
If the database is to be installed, please follow the formal documentation. Here.https://www.postgresql.org/docs/

## Virtual Environment 
It is necessaty to create the virtual environment specialized in this application.<br>
In order to set it, execute the following command.<br>
```python -m venv web_eng```<br>
To activate this environment, execute this.<br>
```source web_eng/bin/activate```<br>

## Install some tools
This application requires some packages.<br>
Using this one, it is necessary to execute the following command.<br>
```pip install -r requirement.txt```

## Run server 
To run this application, two operations are needed.<br>
First, run the database server.<br>
How to run the database server is documented what mentioned before.<br>
Second, run the flask server.<br>
What you have to do is exercute the following commnad.<br>
```flask run```
