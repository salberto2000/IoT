import random
import requests
import time
import json
from colorama import Fore

# Paso 1: Simular la recopilación de datos de sensores de temperatura
#def simulate_temperature_data(num_sensors):
#    data = []
#    for sensor_id in range(num_sensors):
#        temperature = round(random.uniform(-10, 40), 2) # Temperatura simulada entre -10 y 40 grados Celsius
#        data.append({'sensor_id': sensor_id, 'temperature': temperature,'timestamp': time.time()})
#    return data

API_KEY = 'Q6RXR4WBU9462KI6'
CHANNEL_ID = '2574333'

# Función para obtener datos de temperatura en tiempo real desde ThinkSpeak
def get_temperature_data():
    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/1.json?api_key={API_KEY}&results=1'
    response = requests.get(url)
    data = response.json()
    feeds = data['feeds']
    if feeds:
        latest_entry = feeds[-1]
        temperature = float(latest_entry['field1'])
        return {'sensor_id': CHANNEL_ID, 'temperature': temperature, 'timestamp':latest_entry['created_at']}
    return None

# Paso 2: Simular la transmisión de datos a un servidor
def transmit_data(data):
    return json.dumps(data)

print(transmit_data(2))

# Paso 3: Procesar los datos recibidos y detectar anomalías
def process_data(data_json):
    data = json.loads(data_json)
    anomalies = []
    for entry in data:
        if entry['temperature'] < 0 or entry['temperature'] > 35:
            anomalies.append(entry)
    return anomalies

# Paso 4: Tomar acciones basadas en las anomalías detectadas
def take_action(anomalies):
    for anomaly in anomalies:
        print(f"{Fore.RED} Alerta: Temperatura anómala detectada en el sensor{anomaly['sensor_id']} con {anomaly['temperature']} °C")
        
# Ejecutar la práctica completa
while True:
    sensor_data = get_temperature_data()
    print(f"{Fore.WHITE} Datos de sensores:", sensor_data)
    transmitted_data = transmit_data(sensor_data)
    print(f"{Fore.WHITE} Datos transmitidos:", transmitted_data)
    anomalies = process_data(transmitted_data)
    print(f"{Fore.WHITE} Anomalías detectadas:", anomalies)
    take_action(anomalies)
    time.sleep(1) # Esperar 1 segundo