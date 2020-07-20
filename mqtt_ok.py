import paho.mqtt.client as mqttclient
import os
broker = "localhost"
port = 1883
client = mqttclient.Client()
client.connect(broker,port)
client.subscribe("/ids",0)
''' 
    On message while loop never die
    take message on broker/ids/message 

    json formatted : {
        "id":#xx,
        "time":#xx,
        "evidence_path":#xx,
        "emotions":#xx,
        "postprocessing":#xx,
    }
''' 
def on_message(client, obj, msg):
    a = msg.payload.decode('utf8')
    if a :
        if 1:
            print(os.getcwd())
            id_ = open(os.getcwd()+'/Blue_eyes/hide_on_push/id.txt','w+')
            id_.write(str(a))
            id_.close()
            print(a)
        else:
            pass
    else:
        print("ko co gi")
client.on_message = on_message
client.loop_forever()