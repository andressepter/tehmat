import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import galois as galois

GF = galois.GF(7)

# Ulesanne 1.8 Arvutage 5^2023 (mod 7) ja 14^2023 (mod 7)
result = GF(5)**2023


print(f"5^2023 (mod 7) järgi on {result}.")

#y2 does not compute 14 > 7 
# 14 = 2 x 7 
#result = GF(14)**2023
#print(f"14^2023 (mod 7) järgi on {result}.")
#astendada 2 korda 


# C === 2 mod 7 järgi
# C === 7 mod 7 järgi
#print (galois.crt([2,7],[7,7]))
