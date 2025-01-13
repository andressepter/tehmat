import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as FF

#Lineaarsete kongruentside s¨usteemi lahendamine

# C === 1 mod 2 järgi

#syt
print (FF.egcd(0,8))

print (FF.crt([1,3],[2,27]))

