from azure.eventhub import EventHubProducerClient, EventData
import random
import json
import time
from faker import Faker
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Initialize Faker
fake=Faker()

key_vault_url = 'https://bookmyshow-credentials.vault.azure.net/'

##Connecting to AzureKeyVault
credential = DefaultAzureCredential()
key_vault_client = SecretClient(vault_url=key_vault_url,credential=credential) 

#Fetch bookings primary-conn-str from keyVaults
bookings_pri_conn_str = key_vault_client.get_secret('eh-bookings-conn-str').value
eventhub_topic_name = 'bookings_topic'

## creadting prodcuer object
producer = EventHubProducerClient.from_connection_string(
    conn_str = bookings_pri_conn_str,
    eventhub_name=eventhub_topic_name
)

order_id_counter=2000
def generate_bookings_data():
    global order_id_counter
    order_id = order_id_counter
    order_id_counter +=1
    return {
        "order_id" : f"{order_id}",
        "booking_time" : time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "customer" : {
            "customer_id" : f"cust{order_id}",
            "name" : fake.name(),
            "email" : fake.email()
        },
        "event_details" : {
            "event_id" : f"{random.randint(1,100)}",
            "event_name" : random.choice(["Concert", "Play", "Movie"]),
            "event_location" : fake.address(),
            "seats" : [
                {"seat_number": f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 10)}", "price": random.randint(50, 100)},
                {"seat_number": f"{random.choice(['A', 'B', 'C'])}{random.randint(1, 10)}", "price": random.randint(50, 100)}
            ]
        }
    }
    
while True:
    try:
        mock_data=generate_bookings_data()
        event_data=json.dumps(mock_data)
        event=EventData(event_data)
        producer.send_batch([event],partition_key=str(mock_data['order_id']))
        print("Booking Event Published - ", event_data)
        time.sleep(5)
    except Exception as e:
        print(f"error sending the data {e}")

producer.close()

