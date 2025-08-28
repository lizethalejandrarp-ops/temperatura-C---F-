# app.py
import streamlit as st

# Configuración inicial
st.set_page_config(
    page_title="Celsius ↔ Fahrenheit Converter",
    page_icon="🌡️",
    layout="centered"
)

# Título principal
st.title("🌡️ Celsius ↔ Fahrenheit Converter")
st.markdown("Convierte fácilmente entre °C y °F en segundos.")

# Opción de conversión
option = st.radio(
    "Selecciona el tipo de conversión:",
    ("Celsius → Fahrenheit", "Fahrenheit → Celsius")
)

# Entrada de usuario
if option == "Celsius → Fahrenheit":
    celsius = st.number_input(
        "Ingresa la temperatura en °C",
        value=25.0,
        step=0.1,
        format="%.2f"
    )
    if st.button("Convertir"):
        fahrenheit = (celsius * 9/5) + 32
        st.success(f"✅ {celsius:.2f} °C = **{fahrenheit:.2f} °F**")

else:
    fahrenheit = st.number_input(
        "Ingresa la temperatura en °F",
        value=77.0,
        step=0.1,
        format="%.2f"
    )
    if st.button("Convertir"):
        celsius = (fahrenheit - 32) * 5/9
        st.success(f"✅ {fahrenheit:.2f} °F = **{celsius:.2f} °C**")

# Divider visual
st.divider()

# Extra: sliders interactivos
st.subheader("Explora rápidamente con sliders")

col1, col2 = st.columns(2)

with col1:
    c_slider = st.slider("Celsius (°C)", -100.0, 100.0, 0.0, 0.5)
    f_result = (c_slider * 9/5) + 32
    st.metric(label="Resultado en °F", value=f"{f_result:.2f}", delta=f"{c_slider:.2f} °C")

with col2:
    f_slider = st.slider("Fahrenheit (°F)", -148.0, 212.0, 32.0, 0.5)
    c_result = (f_slider - 32) * 5/9
    st.metric(label="Resultado en °C", value=f"{c_result:.2f}", delta=f"{f_slider:.2f} °F")

# Footer
st.caption("🌐 Desarrollado con Streamlit | © 2025")
