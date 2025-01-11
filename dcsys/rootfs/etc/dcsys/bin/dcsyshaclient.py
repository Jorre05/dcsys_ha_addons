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
host = "dcsys.struyve.lan"
port = 8123
verder_doen = True

entities = [
    "sensor.momentaan_vermogen",
    "switch.stroom_balanceren",
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
    "light.dimmer_boiler_output",
    "switch.plug_1_balanceren",
    "switch.plug_2_balanceren",
    "switch.plug_3_balanceren",
    "switch.plug_4_balanceren",
    "switch.plug_5_balanceren",
    "switch.plug_6_balanceren",
    "switch.plug_7_balanceren",
    "switch.plug_8_balanceren",
    "switch.plug_9_balanceren",
    "switch.plug_10_balanceren",
    "switch.plug_11_balanceren",
    "switch.plug_12_balanceren",
    "switch.dimmer_boiler_balanceren",
    "number.plug_1_vermogen",
    "number.plug_2_vermogen",
    "number.plug_3_vermogen",
    "number.plug_4_vermogen",
    "number.plug_5_vermogen",
    "number.plug_6_vermogen",
    "number.plug_7_vermogen",
    "number.plug_8_vermogen",
    "number.plug_9_vermogen",
    "number.plug_10_vermogen",
    "number.plug_11_vermogen",
    "number.plug_12_vermogen",
    "number.dimmer_boiler_vermogen"
]

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    global verder_doen
    verder_doen = False
    sys.exit(0)

async def initSocket():

    try:
        os.mkfifo("/tmp/pipe1")
    except OSError as oe: 
        if oe.errno != errno.EEXIST:
            print("Error occured")

    fifo = open("/tmp/pipe1","w",buffering=1)
    fifo.write("$")
    fifo.flush()

    while verder_doen:
        try:
            async with websockets.connect('ws://{}:{}/api/websocket'.format(host, port)) as websocket:
                await websocket.send(json.dumps({'type': 'auth','access_token': token}))
                await websocket.send(json.dumps({'id': 1, 'type': 'get_states'}))

                while verder_doen:
                    message = await websocket.recv()
                    if message is None:
                        break
                
                    try:   
                        data = json.loads(message)
                        #print(data['result'])
                        for ent in data['result']:
                            #print(ent['entity_id'])
                            if ent['entity_id'] in entities:
                                #print("PYTHON:" + ent['entity_id'] + " -> " + ent['state'])
                                fifo.write(ent['entity_id'] + ":" + ent['state'] + "$")
                                fifo.flush()
                        break
                    except Exception as e:
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
                            #print("PYTHON:" + entity_id + " -> " + data['new_state']['state'])
                            fifo.write(entity_id + ":" + data['new_state']['state'] + "$")
                            fifo.flush()
                    except Exception as e:
                        pass
        except Exception as e:
            #print(e)
            time.sleep(5)
            pass

async def main():
    signal.signal(signal.SIGINT, signal_handler)
    listen = asyncio.create_task(initSocket()) 
    await listen

if __name__ == "__main__":    
    asyncio.run(main())
