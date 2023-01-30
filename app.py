import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


df = pd.read_csv('data/inspection-scores.csv')
df.sort_values(by='Restaurant Name', inplace=True)
df.reset_index(drop=True, inplace=True)
df['name & address'] = df['Restaurant Name'] + ' ' + df['Address']
customdata = np.stack((df['Restaurant Name'], df['Score'], df['Address'], df['Inspection Date']),  axis=-1)

# st.dataframe(df)
st.title("Austin Restaurants Inspection Score")

col1, col2 = st.columns([1, 1])
with col1:
    selection = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible')
with col2:
    df_plot = st.empty()
button_plot = st.empty()
graph_plot = st.empty()


fig = px.scatter_mapbox(df,
                        lon=df['new_longitude'],
                        lat=df['new_latitude'],
                        zoom=10,
                        color=df['Score'],
                        text=df['Restaurant Name'],
                        color_continuous_scale='RdYlBu',
                        hover_data=['Restaurant Name'],
                        range_color=[65, 100],
)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(showlegend=False)
fig.update_traces(customdata=customdata, hovertemplate='Name: %{customdata[0]}<br>Score: %{customdata[1]}</br>Address: %{customdata[2]}<br>Inspection Date: %{customdata[3]}</br>')

with df_plot:
    st.dataframe(df[df['name & address'] == selection][['Restaurant Name', 'Score', 'Inspection Date']])
latt=df[df['name & address'] == selection]['new_latitude'].values[0]
lonn=df[df['name & address'] == selection]['new_longitude'].values[0]

with button_plot:
    if st.button("Center Map"):
        fig.update_layout(mapbox_center=dict(lat=latt, lon=lonn), mapbox_zoom=17)

with graph_plot:
    st.plotly_chart(fig)