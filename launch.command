#!/bin/bash
cd "$(dirname "$0")"
(sleep 1 && open "http://localhost:8080/dashboard.html") &
echo "======================================"
echo "  Håkon Dashboard — Local Server"
echo "======================================"
echo "Opening http://localhost:8080/dashboard.html"
echo "Press Ctrl+C to stop the server."
echo ""
python3 server.py
