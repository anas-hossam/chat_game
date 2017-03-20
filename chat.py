from tornado import web,ioloop,websocket
import json ,os

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("chat.html")

clients = {}
client_id=""
names=[]
online_ids=[]
offline_ids=[]
class ChatHandler(websocket.WebSocketHandler):
    def open(self):
        client_id=id(self)
        clients[client_id] = self
        self.name="Anonimas"
        self.id=client_id
        if self.id not in online_ids:
            online_ids.append(self.id)
        if self.id in offline_ids:
            offline_ids.remove(self.id)
        print("Connection Opened")

    def on_message(self,JSON_client):
        dic={}
        data_Client=json.loads(JSON_client)
        data_Client['id']=self.id
        data_Client['countClients']=len(clients)
        self.name=data_Client['name']
        if self.name not in names:
            names.append(self.name)
        data_Client['names']=names
        data_Client['online_ids']=online_ids
        data_Client['offline_ids']=offline_ids
        data=json.dumps(data_Client)
        for c in clients.keys():
            clients[c].write_message(data)

    def on_close(self):
        del clients[self.id]
        online_ids.remove(self.id)
        names.remove(self.name)
        offline_ids.append(self.id)

app = web.Application([
		(r"/", MainHandler),
		(r'/chat',ChatHandler)]
    ,static_path=os.path.join(os.path.dirname(__file__),'scripts')
    ,debug=True)

app.listen(8881)
ioloop.IOLoop.current().start()
