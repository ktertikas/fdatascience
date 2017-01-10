import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from pymongo import MongoClient
import os
from bson import ObjectId
import numpy as np

# Function to encode mongodb data to json
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Connect to Mongo database fdatascience, collection named visualisation
client = MongoClient('localhost',27017)
db = client.fdatascience 
collection = db.visualisation 
websocket_clients = set()


# Handler for rendering main page
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET / request from", self.request.remote_ip)
        self.render("index.html")


# Handler for rendering summary page
class SummaryHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET / request from", self.request.remote_ip)
        self.render("summary.html")


# Handler for websocket of the first page
class VisSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
    	return True
    
    # Print message on server when websocket connection is open
    def open(self):
        print("WebSocket 1 opened") 
        websocket_clients.add(self)

    # Get data from mongo database and send via the websocket to the client when we recieve a message from the client 
    def on_message(self, message):
        response = collection.find({"PopClass": message}, {"_id":0,"VitaminC":1,"Cholesterol":1,"Fat":1,"EnergyCal":1, "Protein":1, "Carbohydrate":1})
        results = []
        for item in response:
            results.append(item)
        final = JSONEncoder().encode(results)
        self.write_message(final)

    # Print message on server when websocket connection closes
    def on_close(self):
        websocket_clients.remove(self)
        print("WebSocket 1 closed")


# Handler for websocket of the summary(second) page
class Vis2SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    
    # Print message on server when websocket connection is open
    def open(self):
        print("WebSocket 2 opened")
        websocket_clients.add(self)

    # Get data from mongo database and send via the websocket to the client when we recieve a message from the client 
    def on_message(self, message):
        print (message)
        results = []
        popclass_keys = ['Infants', 'Toddlers', 'Other children', 'Adolescents', 'Adults', 'Elderly', 'Very elderly']
        for popclass in popclass_keys:
            response = collection.find({"PopClass": popclass}, {"_id":0,"PopClass":1,message:1})
            popclass_value = ""
            nutr_value = []
            for item in response:
                nutr_value.append(item[message])
                popclass_value = item["PopClass"]
            np_nutr_value = np.array(nutr_value)
            nutr_mean = np.mean(np_nutr_value)
            dictionary = {}
            dictionary["label"] = popclass_value
            dictionary["value"] = nutr_mean
            results.append(dictionary)
        final = JSONEncoder().encode(results)
        self.write_message(final)

    # Print message on server when websocket connection closes
    def on_close(self):
        websocket_clients.remove(self)
        print("WebSocket 2 closed")


# Handlers list for assignment of each handler
handlers = [
            (r"/", MainHandler),
            (r"/summary", SummaryHandler),
            (r"/vis", VisSocketHandler),
            (r"/vis2", Vis2SocketHandler)
            ]


# Add directories for use by the tornado server, static for css and js, template for html
settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static")
        )

application = tornado.web.Application(handlers, debug=True, **settings)

# Server listens in port 8888
application.listen(8888, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()