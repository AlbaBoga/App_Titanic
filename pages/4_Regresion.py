#--------------LIBRERÍAS--------------#
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Predictor de precios', page_icon='🧮', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)

#---------------------------------------------------------------COSAS QUE VAMOS A USAR EN TODA LA APP---------------------------------------------------------------#

st.title('Estimador para precio de billetes')

if st.button('Redirección 👈'):
    link = 'https://titanicmodels.streamlit.app/Regression'
    st.markdown(f'<a href="{link}">Predictor</a>', unsafe_allow_html=True)
else:
    st.write('📝 Estimando ... ')

#--------------------------------------SIDEBAR-------------------------------------#

image1 = Image.open('img/logo.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#