import json
from kafka import KafkaConsumer



class Consumer:

    def __init__(self, topic):
        self.topic = topic
        self.consumer= self.get_consumer_events()


    def get_consumer_events(self):

        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers='localhost:9092',
            group_id='my-group',
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        return consumer

    def consumer_with_auto_commit(self):
        events = self.get_consumer_events()
        try:
            self.print_messages(events)
        except Exception as e:
            print(f"Error while consuming messages: {e}")
            return {"Error : ": e}
        finally:
            events.close()
            print("event closed")

    def print_messages(self, events):
        for message in events:
            print(f"{message.topic}:{message.partition}:{message.offset}: key={message.key} value={message.value}")

# c = Consumer("interesting")
# e = c.get_consumer_events()
# c.consumer_with_auto_commit()