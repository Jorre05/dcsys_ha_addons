#!/bin/bash
curl -s --header "Content-Type: application/json" --request POST --data '{"vermogen": '$1'}'  http://dcsys.struyve.lan:8123/api/webhook/vermogen_webhook

