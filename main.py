import time
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
units = sl.selectbox("Select units", options=("Celsius", "Fahrenheit"))
sl.subheader(f"{view_option} for the next {days} days in {place}")

try:
    if place:
        filtered_data = gd(place, days, units)
        if view_option == "Temperature":
            temperatures = [dictio["main"]["temp"] for dictio in
                            filtered_data]
            dates = [dictio["dt_txt"] for dictio in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature ("
                                                       "Celsius)"})
            with sl.expander("Expand to show chart", False):
                with sl.spinner("Please wait"):
                    time.sleep(3)
                    sl.balloons()
                    sl.success("Forecast found")
                    sl.plotly_chart(figure)
        else:
            images = {"Clear": "images/sun.png", "Clouds": "images/clouds.png",
                      "Rain": "images/rains.png", "Snow": "images/snow.png"}
            sky_conditions = [dictio["weather"][0]["main"] for dictio in
                              filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            with sl.expander("Expand to show chart", False):
                with sl.spinner("Please wait"):
                    time.sleep(3)
                    sl.balloons()
                    time.sleep(1)
                    sl.success("Forecast found")
                    sl.image(image_paths, width=115)

except KeyError:
    sl.info("The place you entered does not exist. Please enter a valid "
            "place")
