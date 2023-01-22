##3893d31081047efb96f81391ceaf0e6e524935adcba66eaad547db7560d37221
import requests
import json

respuesta = requests.get('https://www.datos.gov.co/resource/6s6g-7wni.json').json()

respuesta