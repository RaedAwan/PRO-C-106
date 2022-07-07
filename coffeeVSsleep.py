import pandas as pd
import plotly.express as px

import numpy as np

data = pd.read_csv("coffeeVSsleep.csv")

coffee = data["Coffee in ml"].tolist()

sleep = data["sleep in hours"].tolist()

graph = px.scatter(data , x = coffee  , y = sleep)
# graph.show()

coeff = np.corrcoef(coffee , sleep)

print("The correlation coefficient in between Sleep & Coffee is : " , coeff[0,1])



