import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as FF

print (FF.euler_phi(2**23*7**7*13**7*19**5+5))
print (FF.totatives(30))

