from tornado import web,ioloop,websocket

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("chat.html")

clients = {}
class ChatHandler(websocket.WebSocketHandler):
	def open(self):
		clients[id(self)] = self
		print("Connection Opened")

	def on_message(self,msg):
		for c in clients.keys():
			clients[c].write_message(msg)

	def on_close(self):
		del clients[id(self)]

app = web.Application([
		(r"/", MainHandler),
		(r'/chat',ChatHandler)
	],debug=True)

app.listen(8888)
ioloop.IOLoop.current().start()
