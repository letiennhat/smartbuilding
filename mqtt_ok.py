import paho.mqtt.client as mqttclient
import os
broker = "localhost"
port = 1883
client = mqttclient.Client()
client.connect(broker,port)
client.subscribe("/ids",0)
def on_message(client, obj, msg):
    #print(1)
    a = msg.payload.decode('utf8')
    #print(a)
    if a :
        #print(1)
        if 1:#"unknown" not in a:
            print(os.getcwd())
            id_ = open(os.getcwd()+'/Blue_eyes/hide_on_push/id.txt','w+')
            id_.write(str(a))
            id_.close()
            #print(111)
            print(a)
        else:
            pass
    else:
        print("ko co gi")
client.on_message = on_message
client.loop_forever()