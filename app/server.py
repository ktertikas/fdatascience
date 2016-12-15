import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from pymongo import MongoClient
import os
from bson import ObjectId
# from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
collection = db.visualisation # create collection name "app"
websocket_clients = set()
# collection.insert_one({ # insert data
# 	'name' : 'Top'
# 	})

# print(collection.find())

# top = db.app.find_one()

# top = collection.find()
# for i in top:
# 	print(i)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET / request from", self.request.remote_ip)
        # self.write("aada")
        self.render("index.html")


class VisSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
    	return True
    def open(self):
        print("WebSocket opened")
        websocket_clients.add(self)
        # response = collection.find()
        # print(response)
        # results = []
        # for item in response:
        #     results.append(item)
        # # print(results)
        # # print(type(results))
        # final = JSONEncoder().encode(results)
        # # final = json.dumps(results)
        # # print final
        # self.write_message(final)

    def on_message(self, message):
        response = collection.find({"PopClass": message}, {"_id":0,"VitaminC":1,"Cholesterol":1,"Fat":1,"EnergyCal":1, "Protein":1, "Carbohydrate":1})
        results = []
        for item in response:
            results.append(item)
        final = JSONEncoder().encode(results)
        self.write_message(final)
        # self.write_message(u"You said: " + message)

    def on_close(self):
        websocket_clients.remove(self)
        print("WebSocket closed")

handlers = [
            (r"/", MainHandler),
            (r"/vis", VisSocketHandler)
            ]

settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static")
        )

application = tornado.web.Application(handlers, debug=True, **settings )

application.listen(8888, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()