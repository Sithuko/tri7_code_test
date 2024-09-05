Task: Given a list of proxy IP addresses, write a Python script that rotates through them to make requests to a mobile app’s server, 
ensuring that no more than 10 requests are made from the same IP.


Run the server code 
=====================================================================================================
node rotver.js

Run the proxy server
=====================================================================================================
node proxy-server 8001
node proxy-server 8002
node proxy-server 8003

Run the requst code rotating the server
=====================================================================================================
python rotateRequester.py