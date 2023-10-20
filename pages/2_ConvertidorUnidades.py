import streamlit as st
import pint


st.title("Conversor de Unidades de Longitud")


ureg = pint.UnitRegistry()


entrada = st.selectbox("Unidad de entrada:", [str(unit) for unit in ureg])
salida = st.selectbox("Unidad de salida:", [str(unit) for unit in ureg])


valor = st.number_input("Ingrese el valor:", value=0.0)


try:
    canditad_entrada = valor * ureg(entrada)
    cantidad_salida = canditad_entrada.to(salida)
    st.write(f"Resultado: {cantidad_salida.magnitude} {cantidad_salida.units}")
except:
    st.write("Error en la conversión. Asegúrese de que las unidades sean compatibles.")

