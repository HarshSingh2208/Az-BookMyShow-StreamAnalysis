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
payments_pri_conn_str = key_vault_client.get_secret('eh-payments-conn-str').value
eventhub_topic_name = 'payments_topic'

## creadting prodcuer object
producer = EventHubProducerClient.from_connection_string(
    conn_str = payments_pri_conn_str,
    eventhub_name=eventhub_topic_name
)

payment_id_counter = 3000
order_id_counter = 2000

def generate_payments_data():
    global payment_id_counter,order_id_counter
    payment_id=payment_id_counter
    payment_id_counter+=1
    order_id=order_id_counter
    order_id_counter+=1
    return {
        "payment_id" : f"payment_{payment_id}",
        "order_id" : f"{order_id}",
        "payment_time" : time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "amount" : random.randint(100,200),
        "payment_method" : random.choice(["Credit Card", "Debit Card", "PayPal"]),
        "payment_status" : random.choice(['Success','Failed'])
    }
    
while True:
    try:
        mock_data=generate_payments_data()
        event_data=json.dumps(mock_data)
        event=EventData(event_data)
        producer.send_batch([event],partition_key=str(mock_data['order_id']))
        print("Booking Event Published - ", event_data)
        time.sleep(5)
    except Exception as e:
        print(f"error sending the data {e}")

producer.close()