import requests
import streamlit as sl
import os

API_KEY = os.getenv("API_KEY")


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
