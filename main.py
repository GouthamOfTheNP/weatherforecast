import streamlit as sl
import plotly.express as px
from backend import get_data as gd

sl.set_page_config(page_title="Weather Forecast", page_icon="download.png")
sl.title("Weather Forecast App")
place = sl.text_input("Place: ", placeholder="Enter the location")
days = sl.slider("Forecast days",
                 min_value=1, max_value=5,
                 help="Select the number of forecasted days ")
view_option = sl.selectbox("Select data to view",
                           options=("Temperature", "Sky"))
sl.subheader(f"{view_option} for the next {days} days in {place}")

if place:
    filtered_data = gd(place, days, view_option)
    if view_option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures,
                         labels={"x": "Date", "y": "Temperature (""Celsius)"})
        sl.plotly_chart(figure)
    else:
        images = {"Clear": "images/sun.jpg", "Clouds": "images/clouds.png",
                  "Rain": "images/rains.png", "Snow": "images/snow.png"}
        sky_conditons = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditons]
        sl.image(image_paths, width=115, )
