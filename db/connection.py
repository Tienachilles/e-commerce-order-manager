import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "use_pure": True
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name=os.getenv("POOL_NAME"),
    pool_size=int(os.getenv("POOL_SIZE", 5)),
    **dbconfig
)

def get_connection():
    return connection_pool.get_connection()
