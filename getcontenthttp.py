from http.client import HTTPConnection
conn = HTTPConnection("www.mkbhd.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)