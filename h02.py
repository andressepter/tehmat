import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as FF

#Lineaarsete kongruentside s¨usteemi lahendamine
#n2ide
# C === 6 mod 8 järgi
# C === 4 mod 13 järgi
print (FF.crt([6,4],[8,13]))
# harjutus
print (FF.crt([1,3],[17,19]))
print (FF.crt([5,5],[7,9]))
print (FF.crt([10,30],[19,32]))
print (FF.crt([121,113],[171,119]))
