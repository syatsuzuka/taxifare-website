import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# url = 'https://taxifare.lewagon.ai/predict'
url = 'https://taxifare-858779445866.europe-west1.run.app/predict?pickup_datetime=2014-07-06&19:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

res = requests.get(url)
if res.status_code == 200:
    prediction = res.json()['fare']
    st.markdown(f'### The predicted fare is: ${prediction:.2f}')
else:
    st.markdown('### An error occurred while fetching the prediction. Please try again later.')
    st.error(f'Error {res.status_code}: {res.text}')

def get_map_data():

    return pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

df = get_map_data()

st.map(df)


def get_plotly_data():

    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    return x, y, z

import plotly.graph_objects as go

x, y, z = get_plotly_data()

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()
