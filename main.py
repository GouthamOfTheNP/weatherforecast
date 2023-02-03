import streamlit as sl

sl.set_page_config(page_title="Weather Forecast", page_icon="download.png")
sl.title("Weather Forecast App")
place = sl.text_input("Place: ", placeholder="Enter the location")
days = sl.slider("Forecast days",
                 min_value=1, max_value=5,
                 help="Select the number of forecasted days ")
view_option = sl.selectbox("Select data to view",
                           options=("Temperature", "Sky"))
sl.subheader(f"{view_option} for the next {days} days in {place}")
