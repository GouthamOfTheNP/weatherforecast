import requests
import streamlit as sl

API_KEY = "69783da471cac5b22c854c721bc1a41b"


@sl.cache(ttl=3600)
@sl.experimental_memo
@sl.experimental_memo
def get_data(place, forecast_days=None, kind="Celsius"):
	if kind == "Celsius":
		url = f"https://api.openweathermap.org/data/2.5/forecast?q=" \
	      f"{place}&appid={API_KEY}&units=metric"
	else:
		url = f"https://api.openweathermap.org/data/2.5/forecast?q=" \
		      f"{place}&appid={API_KEY}&units=imperial"
	response = requests.get(url)
	data = response.json()
	filtered_data = data["list"]
	nr_values = 8 * forecast_days
	filtered_data = filtered_data[:nr_values]
	return filtered_data
