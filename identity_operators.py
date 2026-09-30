idk = 5

if (type(idk) is int):
    print("true")
else:
    print("false")

gordonramsey = 5.5

if(type(gordonramsey) is float):
    print("true")
else:
    print("false")

buggatichiron = 20
koneiseggjesko = 20
 
if(buggatichiron is koneiseggjesko):
    print("buggatichiron & koneiseggjesko same identity")
    
koneiseggjesko = 30

if(buggatichiron is not koneiseggjesko):
    print("buggatichiron & koneiseggjesko different identity")
  