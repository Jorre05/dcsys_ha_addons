#!/bin/bash
curl -s --header "Content-Type: application/json" --request POST --data '{"opwekking": '$1'}'  http://dcsys.struyve.lan:8123/api/webhook/opwekking_webhook

