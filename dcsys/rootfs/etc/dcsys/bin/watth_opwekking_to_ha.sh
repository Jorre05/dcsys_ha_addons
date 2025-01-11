#!/bin/bash
curl --header "Content-Type: application/json" --request POST --data '{"productie": '$1'}'  http://localhost:8123/api/webhook/productie_webhook

