import sys; sys.path.append('/home/asepter/.local/lib/python3.10/site-packages/')
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg', force=True)  

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

