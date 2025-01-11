import time
import asyncio
import threading
import json
import os
import sys
import errno
import signal
import websockets

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjMGRiZDE1YzAzM2M0YTJmODQzYmM4NWJmMzg0OTg0OSIsImlhdCI6MTY2MTA2NDQwMSwiZXhwIjoxOTc2NDI0NDAxfQ.8QACIAUEVl7hs8gV0obOz_mwxeElkxa8XVkyfI1Rcvg"
host = "localhost"
port = 8123
verder_doen = True

entities = [
    "sensor.momentaan_vermogen",
    "input_boolean.stroom_balanceren",
    "switch.plug_1_relais",
    "switch.plug_2_relais",
    "switch.plug_3_relais",
    "switch.plug_4_relais",
    "switch.plug_5_relais",
    "switch.plug_6_relais",
    "switch.plug_7_relais",
    "switch.plug_8_relais",
    "switch.plug_9_relais",
    "switch.plug_10_relais",
    "switch.plug_11_relais",
    "switch.plug_12_relais",
    "input_boolean.plug_1_balanceren",
    "input_boolean.plug_2_balanceren",
    "input_boolean.plug_3_balanceren",
    "input_boolean.plug_4_balanceren",
    "input_boolean.plug_5_balanceren",
    "input_boolean.plug_6_balanceren",
    "input_boolean.plug_7_balanceren",
    "input_boolean.plug_8_balanceren",
    "input_boolean.plug_9_balanceren",
    "input_boolean.plug_10_balanceren",
    "input_boolean.plug_11_balanceren",
    "input_boolean.plug_12_balanceren",
    "input_number.plug_1_vermogen",
    "input_number.plug_2_vermogen",
    "input_number.plug_3_vermogen",
    "input_number.plug_4_vermogen",
    "input_number.plug_5_vermogen",
    "input_number.plug_6_vermogen",
    "input_number.plug_7_vermogen",
    "input_number.plug_8_vermogen",
    "input_number.plug_9_vermogen",
    "input_number.plug_10_vermogen",
    "input_number.plug_11_vermogen",
    "input_number.plug_12_vermogen"
]

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    global verder_doen
    verder_doen = False
    sys.exit(0)

async def initSocket():


    print('start loop')
    while verder_doen:
        try:
            print('start hoofd')
            async with websockets.connect('ws://{}:{}/api/websocket'.format(host, port)) as websocket:
                await websocket.send(json.dumps({'type': 'auth','access_token': token}))
                print('send token')
                await websocket.send(json.dumps({'id': 1, 'type': 'get_states'}))
                print('send stats')

                while verder_doen:
                    print('wacht 1')
                    message = await websocket.recv()
                    if message is None:
                        print('bericht is niks')
                        break
                
                    try:   
                        data = json.loads(message)
                        print('DATA:')
                        print(data)
                        for ent in data['result']:
                            print(ent['entity_id'])
                            if ent['entity_id'] in entities:
                                print("PYTHON:" + ent['entity_id'] + " -> " + ent['state'])
                        break
                    except Exception as e:
                        print('wacht 1 error')
                        print(e)
                        pass
            
                await websocket.send(json.dumps({'id': 2, 'type': 'subscribe_events', 'event_type': 'state_changed'}))
                while verder_doen:
                    message = await websocket.recv()
                    if message is None:
                        break
                
                    try:   
                        data = json.loads(message)['event']['data']
                        entity_id = data['entity_id']
                        #print(entity_id)
                        if entity_id in entities:
                            print("PYTHON:" + entity_id + " -> " + data['new_state']['state'])
                    except Exception as e:
                        pass

        except Exception as e:
            print('hoofd error')
            print(e)
            time.sleep(5)
            pass

async def main():
    signal.signal(signal.SIGINT, signal_handler)
    listen = asyncio.create_task(initSocket()) 
    await listen

if __name__ == "__main__":    
    asyncio.run(main())
