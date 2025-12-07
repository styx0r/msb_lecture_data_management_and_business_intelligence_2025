#!/bin/bash

# Start a local development server for the lecture slides
# Press Ctrl+C to stop the server

PORT=${1:-8080}

echo "Starting development server at http://localhost:$PORT"
echo "Press Ctrl+C to stop"
echo ""

cd "$(dirname "$0")"
python3 -m http.server $PORT

