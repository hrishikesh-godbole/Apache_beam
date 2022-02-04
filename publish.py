import os
import time
from google.cloud import pubsub_v1

if __name__ = "__main__"

    project = 'pubsub-project-337207'
    pubsub_topic = 'projects/pubsub-project-337207/topics/Topic-pubsub'

    path_service_account = 'C:\pubsub-project-337207-8c1a5f2a5cb7.json'

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_service_account

    inpput_file = 'C:\Users\Admin\Downloads\demo+streaming\demo streaming\counts.csv'

    publisher = pubsub_v1.PublisherClient()

with open(input_file, 'rb') as ifp:

    header = ifp.readLine()

    for line in ifp:
        event_data = line
        print('Publishing {0} to {1}'.format(event_data, pubsub_topic))
        publisher.publish(pubsub_topic, event_data)
        time.sleep(1)