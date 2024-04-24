#!/bin/bash

echo "## GET request to httpbin.org"
echo "### GET endpoint"
# curl -X GET https://httpbin.org/get -s | jq

echo "### GET request to httpbin.org with args"
curl -X GET "https://httpbin.org/get?fname=Grigorii&lname=Matiukhin" -sv \
  2> >(rg ">") > >(jq)

echo "## POST request to httpbin.org"
echo "### POST endpoint"
curl -X POST https://httpbin.org/post -s -d {} | jq

echo "### Post request to httpbin.org with form args"
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "fname=Grigorii&lname=Matiukhin&stdnum=1032211403" -sv \
  2> >(rg ">") > >(jq)

echo "### Post request to httpbin.org as json"
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"fname": "Grigorii", "lname": "Matiukhin", "stdnum": 1032211403}' -s | jq
