import plotly.express as px
import pandas as pd
from io import BytesIO
obj = BytesIO()

# Create a DataFrame
df = px.data.iris()

# Create a scatter plot
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Iris Dataset Scatter Plot")

# Show the plot
fig.write_image(obj, format="png")
fig.show()

# print(obj.getvalue())
