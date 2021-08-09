import pandas as pd
import plotly.express as px

df=pd.read_csv('lol.csv')
fit=px.scatter(df,x="date", y="cases", color="country")
fit.show()