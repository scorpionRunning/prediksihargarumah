  import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = """
NO,LB,LT,KT,KM,GRS,HARGA
1,220,220,3,3,0,3800000000
2,180,137,4,3,2,4600000000
3,267,250,4,4,4,3000000000
4,40,25,2,2,0,430000000
5,400,355,6,5,3,9000000000
6,300,154,5,3,3,4970000000
7,120,150,3,2,1,2600000000
8,350,247,4,4,0,10500000000
9,125,90,3,3,0,3250000000
10,250,96,5,4,1,4500000000
11,154,110,3,3,3,3600000000
12,450,240,4,4,1,9500000000
13,218,118,3,3,2,10500000000
14,200,979,4,2,6,12500000000
15,180,137,5,4,2,4600000000
16,126,144,4,2,2,3000000000
17,400,150,5,4,1,6000000000
18,150,253,5,2,2,7500000000
19,200,251,5,3,3,18000000000
20,450,248,5,5,4,9700000000
21,300,700,8,5,2,14000000000
22,315,218,7,3,2,8000000000
23,75,75,2,3,0,700000000
24,350,230,5,5,3,5500000000
25,650,695,9,6,2,11000000000
26,250,199,8,2,2,4000000000
27,210,130,3,4,2,3900000000
28,300,200,5,5,4,6500000000
29,175,200,6,4,2,5800000000
30,140,110,3,3,2,3200000000
