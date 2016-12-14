import tornado.ioloop
import tornado.web
import tornado.websocket
import json
from pymongo import MongoClient
import os
# from bson.objectid import ObjectId

client = MongoClient('localhost',27017)
db = client.fdatascience # create db name "fdatascience"
collection = db.visualisation # create collection name "app"

# collection.insert_one({ # insert data
# 	'name' : 'Top'
# 	})

print(collection.find())

# top = db.app.find_one()

# top = collection.find()
# for i in top:
# 	print(i)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET / request from", self.request.remote_ip)
        # self.write("aada")
        self.render("index.html")

handlers = [
            (r"/", MainHandler)
            ]

settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static"),
        )

application = tornado.web.Application(handlers, **settings)

application.listen(8888, '0.0.0.0')

tornado.ioloop.IOLoop.instance().start()