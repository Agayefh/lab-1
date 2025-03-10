import numpy as np 
import math 
l1 = np.log2(3.3)-2*(np.power(6, np.sqrt(0.6)))**3.3* np.exp(-2)
l2= math.tan(4)*math.cos(math.sin(5/4) + math.sin(5/3))
if abs(l1*l2) > 5:
  l3 = np.sqrt(abs(2*l1)) + np.exp(2) - 3 * 12 * np.exp(2)
else:
  l3 = np.sqrt(abs(2*l1)) + 3 * l2
print("l1 =", l1)
print("l2 =", l2)
print("l3 =", l3)
