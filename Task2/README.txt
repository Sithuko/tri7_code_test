Task: Implement a Celery task that retrieves data from a REST API, 
processes the data, and stores it in a database. Include error handling and retries.

Database usage : Mongodb

Run the REST API server code 
====================================================================================
C:\Users\Admin\Desktop\jobcodetest\UIautomatorTest\nodeapi> node server.js
Server running at http://localhost:3000

Run the Celery Tasks
====================================================================================
celery -A tasks worker --loglevel=info --pool=solo

Run the test task code
====================================================================================
python callforexe.py