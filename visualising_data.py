import pandas as pd
import plotly.express as px

#line graph
#df = pd.read_csv("line_chart.csv")
#fig = px.line(df, x = 'year', y = 'per capita income', color = 'country', title = 'Per Capita Income')

#bar graph
#df = pd.read_csv("data.csv")
#fig = px.bar(df, x='Country', y='InternetUsers')

#scater plot
df = pd.read_csv("data.csv")
fig = px.scatter(df, x='Population', y='Per capita', size='Percentage', color = 'Country', size_max=60)
fig.show()