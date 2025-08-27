import json
from fastapi import FastAPI
import uvicorn
from consumer_interesting import Consumer
from dal_mongo import DAL_Mongo
import os
import datetime

HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD", None)
DB = os.getenv("DATABASE", "news_reports")
COLLECTION = os.getenv("COLLECTION", "not_interesting_news")


app = FastAPI()
dal = DAL_Mongo(HOST, DB, COLLECTION)


@app.get("/")
async def status():
    """ return the status of the connection """
    connection = dal.open_connection()
    dal.close_connection()
    if connection:
        return {"status: ": "ok"}
    else:
        return {"status: ": "fail to connect"}

# @app.get("/")


@app.get('/get_data')
async def data11():
    consumer = Consumer("interesting")
    event = consumer.get_consumer_events()
    consumer.consumer_with_auto_commit()
    return consumer.consumer_with_auto_commit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)

