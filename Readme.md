## Document Guide Webserver

# Start webserver

1. Open terminal
2. Run php server -> terminal -> $sudo php -S 0.0.0.0:80
3. Open new terminal
4. $cd smartbuilding/smartbuilding/smartbuilding/test_options
5. $python3 app_login.py

# Start MQTT recevie message
1. Open terminal
2. $cd smartbuilding/smartbuilding/smartbuilding/
3. $python3 mqtt_ok.py

# Start broker MQTT
1. Open new terminal
2. $cd smartbuilding/smartbuilding/smartbuilding/Blue_eyes/hide_on_push
3. $python3  get_name_unit.py

# Utils-web management
1. Open new browser -> process to IP : localip ( 10.10.46.160 ) 
2. Login user : admin@admin (user@password)
3. Login layer 2 : admin@admin
4. Processed web management.
5. Learn New data
6. $cd test_options/
7. $python3 face_recording.py

# Utils-web welcoming

1. Open new browser -> process to IP : localip (10.10.46.160 )
2. Login user : admin@1234 ( user@password )
3. Processed web-welcoming.

## DEBUG - Bug sometimes meeting.
# file-path - smartbuilding/smartbuilding/smartbuilding/
# UI/welcome.php // welcoming app
# test_options/app_login.py //management app
# Blue_eyes/hide_on_push/get_name_unit.py //broker and push data to server
# mqtt_ok.py //On message MQTT


1. Server down. -> restart webserver.
2. Json Decode error -> restart broker MQTT


