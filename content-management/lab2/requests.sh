#!/bin/bash

if ! [ -v RANDOMORG_KEY ]; then
  echo "Please specify your API key with RANDOMORG_KEY variable"
  exit 1
fi

echo "## Generating integers"
echo "### Generating 5 integers the normal way"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -D - \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegers",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "min": -10,
      "max": 50
    }
  }
END
) | tee \
  >(tail -n 1 | jq) \
  >(head -n -2) \
  > /dev/null

sleep 0.1
echo "### Generating integers in octal"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegers",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "min": -10,
      "max": 50,
      "base": 8
    }
  }
END
) | jq

echo "## Doing errors"
echo "### Invalid json"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegerSequences",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "min": -10,
      "max": 50,
      "length": 3,
    }
  }
END
) | jq

echo "### Method not found"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegerSequence",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "min": -10,
      "max": 50,
      "length": 3
    }
  }
END
) | jq

echo "## Generating integer sequences"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegerSequences",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "min": -10,
      "max": 50,
      "length": 3
    }
  }
END
) | jq

echo "## Usage"
echo "### 1d6"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegers",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 1,
      "min": 1,
      "max": 6,
    }
  }
END
) | jq

echo "### Coin flip"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegers",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 1,
      "min": 0,
      "max": 1,
    }
  }
END
) | jq

echo "### 5 IPv4 addresses"
(curl -s -X POST https://api.random.org/json-rpc/4/invoke \
  -H "Content-Type: application/json" \
  -d @- <<END
  {
    "jsonrpc": "2.0",
    "id": 69420,
    "method": "generateIntegerSequences",
    "params": {
      "apiKey": "$RANDOMORG_KEY",
      "n": 5,
      "length": 4,
      "min": 0,
      "max": 255 
    }
  }
END
) | tee >(jq '.result.random.data.[] | join(".")') | jq
