from fastapi import FastAPI
import uvicorn
from consumer import Consumer


app = FastAPI()


@app.get('/get_data')
async def data():
    consumer = Consumer("interesting")
    event = consumer.get_consumer_events()
    consumer.consumer_with_auto_commit()
    return consumer.consumer_with_auto_commit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)

