import base64 

  

  

file = open('encode.bin', 'rb') 

byte = file.read() 

file.close() 

  

decodeit = open('encode.jpeg', 'wb') 
decodeit.write(base64.b64decode((byte))) 
decodeit.close() 