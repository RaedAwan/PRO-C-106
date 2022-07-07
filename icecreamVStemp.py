import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv("icecreamVStemp.csv")

temp = data["Temperature"].tolist()

icecream = data["Ice-cream Sales( ₹ )"].tolist()

graph = px.scatter(data , x = temp, y = icecream)
# graph.show()

# ---------------------------------------------------------------------

coeff = np.corrcoef(temp, icecream)

print("The correlation coeficient in between Temperature & Ice cream is : " , coeff[0,1])












