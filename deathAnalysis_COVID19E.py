# Covid-19 death analysis program in Europe...
# Benford's Law Tests
#!/usr/bin/env python
# coding: utf-8
# In[22]:
import pandas as pd
import numpy as np
from random import seed
from random import randint
# Case 1: It is verified that if Benford's law is fulfilled
seed(5)
resultados=[];
arr = [0]
for _ in range(10):
	arr.append(0)
for j in range(10):
	resultados=[];
	Datos= pd.read_csv("data.csv");
	y = Datos.iloc[:,4].values;
for i in range(len(y)):
	digito =  y[i];
	while digito > 10:
		digito = int(digito / 10)
	if digito < 0:
		digito = 0
	arr[digito] += 1
for i in range(9):
	print(f"The digit {i+1} has {arr[i+1]} occurrences")

# Case 2: It is verified that Benford's law is NOT satisfied with: random numbers
import pandas as pd
import numpy as np
from random import seed
from random import randint

seed(1)
resultados=[];
arr = [0]
for _ in range(10):
	arr.append(0)    
Datos = pd.read_csv("data.csv");
y = Datos.iloc[:,4].values;
mal = 0
mil  = 9999999999
for i in range(len(y)):
	if y[i] > mal:
		mal = y[i]
	if y[i] < mil:
		mil = y[i]
for i in range(len(y)):
	y[i]= randint(mil, mal) # new dataset between the minimum and maximum variables
for i in range(len(y)):
	digito =  int(y[i]);
	while digito > 10:
		digito = int(digito / 10)
	if digito < 0:
		digito = 0
	arr[digito] += 1
for i in range(9):
	print(f"The digit {i+1} has {arr[i+1]} occurrences")





