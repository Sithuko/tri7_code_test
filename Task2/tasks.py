# from celery import Celery

# # Create a Celery instance and configure both the broker and the result backend
# app = Celery('tasks', 
#              broker='redis://localhost:6379/0',  # Replace with your Redis broker URL
#              backend='rpc://') # Replace with your Redis result backend URL

# @app.task
# def add(x, y):
#     return x + y

from celery import Celery
import requests
import logging
from pymongo import MongoClient

# Configure Celery
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

# MongoDB setup
def get_mongo_client():
    client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
    return client

# Define a task to fetch data from REST API, process it, and store it in MongoDB
@app.task(bind=True, max_retries=3)
def process_user_data(self):
    try:
        # Step 1: Retrieve data from the REST API
        response = requests.get('http://localhost:3000/users')
        response.raise_for_status()
        users = response.json()

        # Step 2: Process the data (categorize users by age)
        processed_users = []
        for user in users:
            category = 'Over 30' if user['age'] > 30 else 'Under 30'
            processed_users.append({
                'name': user['name'],
                'age': user['age'],
                'email': user['email'],
                'contact': user['contact'],
                'address': user['address'],
                'category': category
            })

        # Step 3: Store the processed data in MongoDB
        client = get_mongo_client()
        db = client['user_data']  # Use a database named 'user_data'
        collection = db['processed_users']  # Use a collection named 'processed_users'
        collection.insert_many(processed_users)

        logging.info("Data processed and stored in MongoDB successfully.")
        client.close()

    except requests.exceptions.RequestException as exc:
        logging.error(f"Error fetching data from API: {exc}")
        self.retry(exc=exc, countdown=60)  # Retry after 60 seconds if API request fails
    except Exception as exc:
        logging.error(f"An error occurred: {exc}")
        raise self.retry(exc=exc)

