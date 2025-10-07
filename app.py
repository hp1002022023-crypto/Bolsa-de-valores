import streamlit as st
import requests

# Estilo
st.markdown("""
    <style>
    .titulo {
        color: #ffffff;
        background-color: #0d6efd;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 32px;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .label {
        font-weight: bold;
        color: #0d6efd;
    }
    </style>
""", unsafe_allow_html=True)

# Imagen decorativa
st.image("https://rentafija.com/wp-content/uploads/2020/04/que-es-la-bolsa-de-valores.jpg", use_container_width=True)

# Título
st.markdown('<div class="titulo">📈 Consulta de Bolsa de Valores</div>', unsafe_allow_html=True)

# Entrada de usuario
accion = st.text_input("Escriba el símbolo de la Acción (por ejemplo: AAPL, TSLA, MSFT)", "")

# Botón
if st.button("🔍 Ver Cotizaciones"):
    if accion:
        url = f"http://api.marketstack.com/v1/eod?access_key=de87830a787dbda9f6bcea1939c0429b&symbols={accion}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                cotizacion = data["data"][0]
                
                # Tarjeta con la información
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown(f'<div class="label">📅 Fecha:</div> {cotizacion["date"]}', unsafe_allow_html=True)
                st.markdown(f'<div class="label">🔓 Apertura:</div> {cotizacion["open"]}', unsafe_allow_html=True)
                st.markdown(f'<div class="label">🔒 Cierre:</div> {cotizacion["close"]}', unsafe_allow_html=True)
                st.markdown(f'<div class="label">📈 Máximo:</div> {cotizacion["high"]}', unsafe_allow_html=True)
                st.markdown(f'<div class="label">📉 Mínimo:</div> {cotizacion["low"]}', unsafe_allow_html=True)
                st.markdown(f'<div class="label">📊 Volumen:</div> {cotizacion["volume"]}', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️ No se encontraron datos para esa acción.")
        else:
            st.error("❌ Error al consultar la API. Verifica tu conexión o clave.")
