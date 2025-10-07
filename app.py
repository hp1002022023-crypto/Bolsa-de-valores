import streamlit as stl
import requests

stl.title("Bolsa de Valores")
accion = stl.text_input("Escriba la Acción a Cotizar")

API_KEY = "de87830a787dbda9f6bcea1939c0429b"

if stl.button("Ver Cotizaciones"):
    if accion:
        url = "https://marketstack.com/search"        
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:                        
            info = {

            }

        else:
            stl.error("NO se encontro la accion")