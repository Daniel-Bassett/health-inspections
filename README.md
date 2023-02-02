# Austin Food Establishment Inspections Scores

## Overview
This project provides an analysis of inspection scores for food establishments in the Austin area. The app can be found [here](https://crispybacon233-health-inspections-app-1qnsr3.streamlit.app/) The data was sourced from the Austin data [website](https://data.austintexas.gov/Health-and-Community-Services/Food-Establishment-Inspection-Scores/ecmv-9xxi) and processed using Pandas to clean and organize the information. More accurate latitude and longitude coordinates were scraped from Google Maps using Selenium to complete the data. The results of the analysis are presented through interactive visualizations made with Plotly Express, and are available through a web app created with Streamlit.

## Data Cleaning and Preparation
The original data from the government website was not organized and had missing information. Pandas was used to clean and organize the data to ensure accuracy and consistency. Further, the latitude and longitude coordinates were often times too general or completely missing. Selenium was used to scrape this information off of Google Maps.

## Visualizations
The visualizations for this project include:
- An interactive map of food establishments in the Austin area, with the ability to view inspection scores for each location.
- A line graph showing the fluctuations in inspection scores for individual establishments over time.

## Web App
The web app, built with Streamlit, allows users to easily access and interact with the visualizations. The app is hosted on Streamlit's platform.

## Technology Stack and Libraries
- Pandas for data cleaning and preparation
- Selenium for web scraping
- Plotly Express for data visualization
- Streamlit for creating the web app

## Conclusion
This project showcases the ability to collect, clean, and analyze data to create useful and informative visualizations. The web app provides a convenient tool for individuals to access information on inspection scores for food establishments in the Austin area.
