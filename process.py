pip install apache-beam[gcp]

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import os
from apache_beam import window


# Replace 'my-service-account-path' with your service account path
service_account_path = 'C:\pubsub-project-337207-8c1a5f2a5cb7.json'
print("Service account file : ", service_account_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

# Replace 'my-input-subscription' with your input subscription id
input_subscription = 'projects/pubsub-project-337207/subscriptions/subscribe1'

# Replace 'my-output-subscription' with your output subscription id
output_topic = 'projects/pubsub-project-337207/topics/topics2'

options = PipelineOptions()
options.view_as(StandardOptions).streaming = True

p = beam.Pipeline(options=options)


output_file = 'outputs/part'

pubsub_data = (
                p 
                | 'Read from pub sub' >> beam.io.ReadFromPubSub(subscription= input_subscription)
                | 'Write to pus sub' >> beam.io.WriteToPubSub(output_topic)
              )

result = p.run()
result.wait_until_finish()