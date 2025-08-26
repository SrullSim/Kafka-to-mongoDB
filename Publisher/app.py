from fastapi import FastAPI
import uvicorn
import data
import random as rd
from producer import Producer

app = FastAPI()
interesting = data.newsgroups_interesting.data
not_interesting= data.newsgroups_not_interesting.data



interesting_random_slice = rd.randint(0,(len(interesting)-10))
not_interesting_random_slice = rd.randint(0,(len(not_interesting)-10))



@app.get('/interesting')
async def get_10_news():
    producer = Producer()
    massage = {"10 news ":interesting[ interesting_random_slice : interesting_random_slice +10] }
    try:
        producer.publish_message("interesting", massage)
        return interesting[ interesting_random_slice : interesting_random_slice +10]
    except Exception as e :
        print("error: ", e)
        return {"error: ": e}

@app.get('/not_interesting')
async def get_10_news():
    producer = Producer()
    massage = {"10 news ": not_interesting[not_interesting_random_slice: not_interesting_random_slice + 10]}
    producer.publish_message("not_interesting", massage)
    return not_interesting[ not_interesting_random_slice : not_interesting_random_slice +10]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

