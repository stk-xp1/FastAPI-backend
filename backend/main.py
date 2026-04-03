from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .db import get_connection, get_customer_sql, get_payment_sql

app = FastAPI()

# @app.get("/")
# async def root():
#     # Simple health route.
#     return {"Message": "Hello from FastAPI"}

@app.get("/Customers")
async def get_customers(customer_id: str | None = None, city: str | None = None):
    # city is optional because its default value is None.

    # Open a new database connection for this request.
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Load the SQL from the external file.
    query = get_customer_sql()

    # Store parameter first.
    params = []

    if customer_id is not None:
        query += " WHERE customer_id = %s"
        params.append(customer_id)
    if city is not None:
        if "WHERE" in query:
            query += " AND city = %s"
        else:
            query += " WHERE city = %s"
        params.append(city)

    # Add the optional parameter only if the client sends it.
    # if city is not None:
    #     query += " AND city = %s"
    #     params.append(city)

    # Execute the query with parameters.
    cursor.execute(query, tuple(params))
    result = cursor.fetchall()

    # Close resources after use.
    cursor.close()
    conn.close()


    # Error handling

    return {"result": result}


@app.get("/Payments")
async def get_payments():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = get_payment_sql()

    param = []

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"result": result}
