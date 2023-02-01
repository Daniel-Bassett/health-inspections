import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# load data
df = pd.read_csv('data/inspection-scores.csv')
df.sort_values(by='Restaurant Name', inplace=True)
df.reset_index(drop=True, inplace=True)
df['name & address'] = df['Restaurant Name'] + ' ' + df['Address']


# define function for making map
def make_map(df):
    customdata = np.stack((df['Restaurant Name'], df['Score'], df['Address'], df['Inspection Date']),  axis=-1)
    fig = px.scatter_mapbox(df,
                            lon=df['new_longitude'],
                            lat=df['new_latitude'],
                            zoom=10,
                            color=df['Score'],
                            text=df['Restaurant Name'],
                            color_continuous_scale=['Red', 'Blue'],
                            hover_data=['Restaurant Name'],
                            range_color=[65, 100],
    )
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(coloraxis_showscale=False)
    fig.update_traces(customdata=customdata, hovertemplate='Name: %{customdata[0]}<br>Score: %{customdata[1]}</br>Address: %{customdata[2]}<br>Inspection Date: %{customdata[3]}</br>')
    return fig


with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Inspection Scores', 'Filtered Scores']
    )
if selected == 'Inspection Scores':
    st.title("Austin Restaurant Inspection Scores")

    col1, col2 = st.columns([2, 3])
    with col1:
        selection = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible')
        latt=df[df['name & address'] == selection]['new_latitude'].values[0]
        lonn=df[df['name & address'] == selection]['new_longitude'].values[0]
    with col2:
        df_plot = st.empty()
    button_plot = st.empty()
    graph_plot = st.empty()

    fig = make_map(df)
    

    with df_plot:
        st.dataframe(df[df['name & address'] == selection][['Restaurant Name', 'Score', 'Inspection Date']])
    with button_plot:
        if st.button("Go To Restaurant"):
            fig.update_layout(mapbox_center=dict(lat=latt, lon=lonn), mapbox_zoom=15)
    with graph_plot:
        st.plotly_chart(fig, use_container_width=True)
if selected == 'Filtered Scores':
    st.title('Filtered Scores')
    col1, col2 = st.columns([3, 5])
    with col1:
        score_range = st.slider('Choose a range of Scores', value=[40, 100], min_value=40, max_value=100, step=5)
    filtered_df = df[df['Score'].between(score_range[0], score_range[1])]
    fig = make_map(filtered_df)
    st.plotly_chart(fig, use_container_width=True)

