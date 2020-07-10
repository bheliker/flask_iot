from app import db
from datetime import datetime

class TemperatureReading(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	temperature = db.Column(db.Float)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	particleid = db.Column(db.String(40))
	
	def __repr__(self):
		return '<Temperature {}>'.format(self.weight)


class MultiSensorReading(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sensor1 = db.Column(db.Float)
	sensor2 = db.Column(db.Float)
	sensor3 = db.Column(db.Float)
	sensor4 = db.Column(db.Float)
	sensor5 = db.Column(db.Float)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	particleid = db.Column(db.String(40))
	
	def __repr__(self):
		return '<SensorReading {}>'.format(self.timestamp)
