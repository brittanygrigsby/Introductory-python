from flask import Flask
import json
from.about import me

app = Flask(__name__) #Create an instance of flash class

#Ciculating endpoints
@app.get("/")
def home():
    return "Hello World from Flask server"

@app.get("/test")
def test():
    return "This is a test page"

@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

@app.get("./api.about")
def about():
    return json.dumps.me