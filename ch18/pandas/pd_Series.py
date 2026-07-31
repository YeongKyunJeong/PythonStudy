# pd_Series.py

import pandas as pd
data = [10, 20, 30]
series = pd.Series(data)
print(series)

data = {"a" : 10, "b" : 20, "C" : 30}
series = pd.Series(data)
print(series)