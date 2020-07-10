# flask_iot
A very simple method for saving IoT data, as from a Particle, to a db with Flask and SQLAlchemy

- Test server using a simple python script, or cURL, or Postman: 
```
import requests
data = {"temperature": "42", "particleid":"1" }
r = requests.post('http://127.0.0.1:5000/api/v1.0/temperaturereadings/', json=data)
print(r.status_code)
```
- setup [a Particle webhook](https://console.particle.io/integrations/webhooks/create)
	- URL: http://www.yoursite.com
  - request format: JSON
  - json data: 
  ```
    {
	  "time": "{{PARTICLE_PUBLISHED_AT}}",
	  "particleid": "{{PARTICLE_DEVICE_ID}}",
	  "temperature": "{{temperature}}"
    }
  ```
- flash your particle with some code: 
	```
	#define SENSOR_PIN	D3

	void setup()
	{
	  pinMode(SENSOR_PIN, INPUT);
	}

	void loop() {
	  analogvalue = analogRead(SENSOR_PIN);
	  tempC = (((analogvalue * 3.3) / 4095) - 0.5) * 100;
	  Particle.publish("temperature", tempC, PRIVATE);
	  delay(300000); // 5 minute delay
	}
	```
