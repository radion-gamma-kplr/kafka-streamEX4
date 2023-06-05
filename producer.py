from kafka import KafkaProducer
from time import sleep
import requests
import json

# Alpha Vantage API endpoint
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

# Kafka bootstrap servers
bootstrap_servers = ['localhost:9092']

# Kafka topic to produce data to
topic = 'data-stream'

# Creating a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))

while True:
    # Make a request to the Alpha Vantage API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the 'Time Series (5min)' key exists in the response data
        if 'Time Series (5min)' in data:
            time_series = data["Time Series (5min)"]
            
            for timestamp, values in time_series.items():
                # Extract the required values
                open_price = values['1. open']
                high_price = values['2. high']
                low_price = values['3. low']
                close_price = values['4. close']
                volume = values['5. volume']
                
                # Create a dictionary with the extracted values
                price_data = {
                    'timestamp': timestamp,
                    'open': open_price,
                    'high': high_price,
                    'low': low_price,
                    'close': close_price,
                    'volume': volume
                }
                
                # Convert the dictionary to JSON and send it to Kafka
                producer.send(topic, value=price_data)
                
                print("Price data sent to Kafka")
        
    sleep(60)  # Sleep for 60 seconds before making the next API request
