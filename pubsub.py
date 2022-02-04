from google.cloud import pubsub_v1
import time 

publisher = pubsub_v1.PublisherClient()

topic_name = 'projects/consummate-yew-336502/topics/data_stream_from_file'
try:
    publisher.create_topic(topic_name)

except:
    print ('Topic already exists')

with open('food_daily.csv') as f_in:
    for line in f_in:
        data = line
        future = publisher.publish(topic_name, data=data)
        print(future.result())
        time.sleep(1)
