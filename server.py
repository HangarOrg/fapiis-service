from bottle import route, run, response, default_app
import os
import json

with open("/code/fapiis.json", "r") as fp:
    data = json.load(fp)

application = default_app()


@route("/")
def home():
    res = {"results": "Welcome to the Hangar FAPIIS Service"}
    response.content_type = "application/json"
    return json.dumps(res)


@route("/duns/<duns>")
def duns(duns):
    res = {"results": [obj for obj in data if obj["duns"] == duns]}
    response.content_type = "application/json"
    return json.dumps(res)


if __name__ == "__main__":
    run(application, server="waitress")
