import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# load data
df = pd.read_csv('data/inspection-scores.csv')
all_scores = pd.read_csv('data/all_scores.csv')
df.sort_values(by='Restaurant Name', inplace=True)
df.reset_index(drop=True, inplace=True)
df['name & address'] = df['Restaurant Name'] + ' ' + df['Address']
all_scores['name & address'] = all_scores['Restaurant Name'] + ' ' + all_scores['Address']


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

# function for making score over time line graph
def make_line_graph(df):
    fig = px.line(df, x='Inspection Date', y='Score', markers=True, title='Scores Over Time')
    return fig

# create sidebar menu with options
# with st.sidebar:
#     selected = option_menu(
#         menu_title='Main Menu',
#         options=['Inspection Scores', 'Scores Over Time', 'Filtered Scores']
#     )

# inspection scores page
# if selected == 'Inspection Scores':
#     st.header("Austin Restaurant Inspection Scores")
#     col1, col2 = st.columns([2, 3])
#     with col1:
#         selection = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible')
#         latt=df[df['name & address'] == selection]['new_latitude'].values[0]
#         lonn=df[df['name & address'] == selection]['new_longitude'].values[0]
#         button_plot = st.empty()
#     with col2:
#         df_plot = st.empty()   
#     graph_plot = st.empty()
#     fig = make_map(df)
#     with df_plot:
#         st.dataframe(df[df['name & address'] == selection][['Restaurant Name', 'Score', 'Inspection Date']].reset_index(drop=True))
#     with button_plot:
#         if st.button("Go To Restaurant"):
#             fig.update_layout(mapbox_center=dict(lat=latt, lon=lonn), mapbox_zoom=15)
#     with graph_plot:
#         st.plotly_chart(fig, use_container_width=True)

# scores over time page
# if selected == 'Scores Over Time':
#     st.header('Scores Over Time')
#     selection = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible')
#     restaurant = all_scores[all_scores['name & address'] == selection][['Restaurant Name', 'Inspection Date', 'Score']].reset_index(drop=True)
#     st.dataframe(restaurant)
#     if len(restaurant) > 1:
#         fig = make_line_graph(restaurant)
#         st.plotly_chart(fig, use_container_width=True)

# # filtered scores page
# if selected == 'Filtered Scores':
    # st.header('Filtered Scores')
    # col1, col2 = st.columns([3, 5])
    # with col1:
    #     score_range = st.slider('Choose a range of Scores', value=[40, 100], min_value=40, max_value=100, step=5)
    # filtered_df = df[df['Score'].between(score_range[0], score_range[1])]
    # fig = make_map(filtered_df)
    # st.plotly_chart(fig, use_container_width=True)

st.title('Austin Restaurant Inspection Scores')

tab1, tab2, tab3 = st.tabs(['Inspection Scores', 'Scores Over Time', 'Filtered Scores'])

with tab1:
    col1, col2 = st.columns([2, 3])
    with col1:
        selection = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible', key=1)
        latt=df[df['name & address'] == selection]['new_latitude'].values[0]
        lonn=df[df['name & address'] == selection]['new_longitude'].values[0]
        button_plot = st.empty()
    with col2:
        df_plot = st.empty()   
    graph_plot = st.empty()
    fig = make_map(df)
    with df_plot:
        st.dataframe(df[df['name & address'] == selection][['Restaurant Name', 'Score', 'Inspection Date']].reset_index(drop=True))
    with button_plot:
        if st.button("Go To Restaurant"):
            fig.update_layout(mapbox_center=dict(lat=latt, lon=lonn), mapbox_zoom=15)
    with graph_plot:
        st.plotly_chart(fig, use_container_width=True)
with tab2:
    selection2 = st.selectbox('Choose Restaurant', options=df['name & address'], label_visibility='visible', index = df['name & address'].to_list().index(selection))
    restaurant = all_scores[all_scores['name & address'] == selection2][['Restaurant Name', 'Inspection Date', 'Score']].reset_index(drop=True)
    st.dataframe(restaurant)
    if len(restaurant) > 1:
        fig = make_line_graph(restaurant)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    col1, col2 = st.columns([3, 5])
    with col1:
        score_range = st.slider('Choose a range of Scores', value=[40, 100], min_value=40, max_value=100, step=5)
    filtered_df = df[df['Score'].between(score_range[0], score_range[1])]
    fig = make_map(filtered_df)
    st.plotly_chart(fig, use_container_width=True)
