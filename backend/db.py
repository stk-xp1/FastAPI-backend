# Import only the settings object.
from .config import settings
from pathlib import Path
import mysql.connector

def get_connection():
    # Create a MySQL connection using values from the settings class.
    return mysql.connector.connect(
        host=settings.db_host,
        port=int(settings.db_port) if settings.db_port else 3306,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name
    )

# read Customer SQL from the file 
def load_sql(file_name: str) -> str:
    sql_path = Path(__file__).resolve().parent / "sql" / file_name
    return sql_path.read_text()


def get_customer_sql() -> str:
    return load_sql("customer.sql")

def get_payment_sql() -> str:
    return load_sql("payment.sql")