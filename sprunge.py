import socket
import urllib
import logging
import sys

logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
logger = logging.getLogger("Sprunge POST handler")

logger.info('Init Sprunge POST script')

message = "Hello Sprunge"

data = {

"sprunge": message}


payload = urllib.urlencode(data)
clength = len(payload)

headers = """POST / HTTP/1.1
Host: sprunge.us
Connection: keep-alive
Content-Length: {0}
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: JSON
Accept-Language: en-US,en;q=0.8

{1}""".format(clength,payload)

try:
    s = socket.socket()
    s.connect(("sprunge.us",80))
    logger.info('Connecting to sprunge.us on port 80')
    s.send(headers)
    logger.debug('Sending headers to sprunge.us:80\n:' + headers)
    s.settimeout(30.0)
    response = s.recv(1024)
    logger.info("Receiving server response")
    s.close()

    rfile = response.split("\r\n")[10]
    logger.debug("Server Response: " + response.split("\r\n")[0])
    logger.info("Sprunge file: " + rfile)

except socket.error, m:
    logger.debug("Could not complete the request: " + str(m))
