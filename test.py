import numpy as np
import galois 
print('Hello, World!')
GF = galois.GF(3**5)
print(GF.properties)
issubclass(GF, galois.FieldArray)
issubclass(GF, np.ndarray)
x = GF([236, 87, 38, 112]); x
isinstance(x, galois.FieldArray)
isinstance(x, np.ndarray)
y = np.array([109, 17, 108, 224]); y
y = y.view(GF); y
GF.repr("poly"); x
print ('polynomial representation',x)
print ('x+y', x + y)
print ('x-y', x - y)
print ('x*y', x * y)
print ('x/y', x / y)
print ('sqrt', np.sqrt(x))

GF.repr("power"); x
print ('astmed',x)
print ('x+y', x + y)
print ('x-y', x - y)
print ('x*y', x * y)
print ('x/y', x / y)
print ('sqrt', np.sqrt(x))

GF.repr("int");
print ('integer representation', x)
print ('x+y', x + y)
print ('x-y', x - y)
print ('x*y', x * y)
print ('x/y', x / y)
print ('sqrt', np.sqrt(x))