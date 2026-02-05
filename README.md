# Akhil-Nanduri-cmpe-273
cmpe273-week1-lab1-starter

# 1.) How to Run Locally
# Service A
1.) Create a service named service-a
2.) Run the command python3 service-a.py
# output:
krishnasaiakhilnanduri@Krishnas-MacBook-Air desktop % python3 service-a.py
 * Serving Flask app 'service-a'
 * Debug mode: off
2026-02-04 21:46:31,460 INFO WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8080
2026-02-04 21:46:31,460 INFO Press CTRL+C to quit


# Service B
1.) Create a service named service-b
2.) Run the command python3 service-b.py   
# output:
krishnasaiakhilnanduri@Krishnas-MacBook-Air desktop % python3 service-b.py
 * Serving Flask app 'service-b'
 * Debug mode: off
2026-02-04 21:51:27,460 INFO WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8081
2026-02-04 21:51:27,460 INFO Press CTRL+C to quit

_______________________________________________________________
# 2.) Success+Failure Proof
krishnasaiakhilnanduri@Krishnas-MacBook-Air desktop % curl -i "http://127.0.0.1:8081/call-echo?msg=hello"
HTTP/1.1 200 OK
Server: Werkzeug/3.1.5 Python/3.12.7
Date: Thu, 05 Feb 2026 05:53:09 GMT
Content-Type: application/json
Content-Length: 46
Connection: close

krishnasaiakhilnanduri@Krishnas-MacBook-Air desktop % curl -i "http://127.0.0.1:8081/call-echo?msg=hello"
HTTP/1.1 503 SERVICE UNAVAILABLE
Server: Werkzeug/3.1.5 Python/3.12.7
Date: Thu, 05 Feb 2026 05:56:45 GMT
Content-Type: application/json
Content-Length: 34
Connection: close

{"error":"Service A unavailable"}   
_________________________________________________________________
# 3.) What makes this distributed?
This system is distributed because it has two separate services running as independent processes that communicate with each other over HTTP. 
Service B calls Service A over the network and uses a timeout, so Service A can fail while Service B continues running and returns a 503 error. 
This shows independent execution, network communication, and failure handling across services.



