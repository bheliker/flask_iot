from app import app, db
from app.models import TemperatureReading, MultiSensorReading
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    make_response,
    jsonify,
    abort,
)


@app.route("/")
@app.route("/index")
def index():

    readings = TemperatureReading.query.count() + MultiSensorReading.query.count()
    return "Storing " + str(readings) + " readings."


###############
##### API #####
###############


@app.route("/api/v1.0/temperaturereadings/", methods=["POST"])
def post_temperaturereadings():
    if not request.json or not "particleid" in request.json:
        abort(400)

    reading = {
        "temperature": request.json["temperature"],
        "timestamp": request.json.get("timestamp", ""),
        "particleid": request.json.get("particleid"),
    }

    r = TemperatureReading(
        particleid=reading["particleid"], temperature=reading["temperature"]
    )
    db.session.add(r)
    db.session.commit()

    return "OK", 201


@app.route("/api/v1.0/temperaturereadings/<particleid>", methods=["GET"])
def get_temperaturereading(particleid):

    reading = {}
    reading["readings"] = []

    try:
        readingsdb = (
            TemperatureReading.query.filter_by(particleid=particleid)
            .order_by(TemperatureReading.timestamp.desc())
            .paginate(1, 1000, False)
            .items
        )
    except Exception as e:
        return "type error: " + str(e)

    try:
        for i in readingsdb:
            if (
                i.temperature > -20 and i.temperature < 50
            ):  # My sensor occasionally returns ridiculous values. Throw those out.
                reading["readings"].append(
                    {
                        "particleid": i.particleid,
                        "temperature": i.temperature,
                        "timestamp": i.timestamp.isoformat(),
                    }
                )
    except Exception as e:
        return "type error: " + str(e)

    return jsonify(reading), 201


@app.route("/api/v1.0/multisensor/", methods=["POST"])
def post_MultiSensorReadings():
    if not request.json or not "particleid" in request.json:
        abort(400)
    try:
        reading = {
            "sensor1": request.json["sensor1"],
            "sensor2": request.json["sensor2"],
            "sensor3": request.json["sensor3"],
            "sensor4": request.json["sensor4"],
            "sensor5": request.json["sensor5"],
            "time": request.json.get("time", ""),
            "particleid": request.json.get("particleid"),
        }
    except:
        return jsonify({"error": "there was a formatting error"}), 201
    try:
        r = MultiSensorReading(
            particleid=reading["particleid"],
            sensor1=reading["sensor1"],
            sensor2=reading["sensor2"],
            sensor3=reading["sensor3"],
            sensor4=reading["sensor4"],
            sensor5=reading["sensor5"],
        )
        db.session.add(r)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "there was a db error: " + e}), 201

    return "OK", 201


@app.route("/api/v1.0/multisensor/<particleid>", methods=["GET"])
def get_MultiSensorReadings(particleid):
    reading = {}
    reading["readings"] = []

    try:
        readingsdb = (
            MultiSensorReading.query.filter_by(particleid=particleid)
            .order_by(MultiSensorReading.timestamp.desc())
            .paginate(1, 1000, False)
            .items
        )
    except Exception as e:
        return "type error: " + str(e)
    try:
        for i in readingsdb:
            reading["readings"].append(
                {
                    "particleid": i.particleid,
                    "sensor1": i.sensor1,
                    "sensor2": i.sensor2,
                    "sensor3": i.sensor3,
                    "sensor4": i.sensor4,
                    "sensor5": i.sensor5,
                    "timestamp": i.timestamp.isoformat(),
                }
            )
    except Exception as e:
        return "type error: " + str(e)

    return jsonify(reading), 201
