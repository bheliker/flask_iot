# flask_iot
A very simple method for saving IoT data, as from a Particle, to a db with Flask and SQLAlchemy

Test using a simple python script, or cURL, or Postman: 
```
import requests
data = {"temperature": "42", "particleid":"1" }
r = requests.post('http://127.0.0.1:5000/api/v1.0/temperaturereadings/', json=data)
print(r.status_code)
```