import streamlit as st
import pywhatkit 

# Diseño personalizado
st.header("Automatización de mensajes para chats de WhatsApp")

telefono = st.text_input("Ingresa el numero de telefono al que quieres enviar el mensaje") 
st.info('¡Recuerda colocar el indicativo junto con el signo + ! y no dejar espacios', icon="ℹ️")
mensaje = st.text_input("Ingresa el Mensaje que quieres enviar")
hora = st.text_input("Ingresa la hora a la que quieres que se envie")
st.info('¡Recuerda utilizar el formato de 24h! y solo coloca la hora, los minutos en la caja siguiente', icon="ℹ️")
minuto = st.text_input("Ingresa el minuto al que quieres que se envie")

if st.button("enviar"):
    if telefono == "" or mensaje == "" or hora == "" or minuto == "":
        st.warning('Debes llenar todo los campos', icon="⚠️")
    else:
        pywhatkit.sendwhatmsg(telefono, mensaje, int(hora), int(minuto))