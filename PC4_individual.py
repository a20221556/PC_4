# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_individual.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
#with st.sidebar:
    #opciones = option_menu("Selecciona una sección: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        #icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
opciones = option_menu(
    menu_title="Let's explore: ",
    options=['Presentación', 'Experiencia', 'Gráficos'], 
    icons=['chat-left-heart','ban-fill', 'balloon-heart'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Presentación':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre del blog</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    col1.image("foto blog.jpeg", caption='Antonella', width=300)

    texto = """
    Mi nombre es Antonella y estudio Publicidad en la PUCP. Me gusta mucho todo lo relacionado con la moda, belleza, redes sociales y la creación de contenido.
    Elegí mi carrera porque me gusta que puedo ser creativa y conocer diferentes formas de comunicar ideas para conectar con las personas.
    En un futuro me encantaría poder desarrollar proyectos propios, trabajar con marcas, crear contenido y realizar todo lo que me apasiona.
    En mi tiempo libre suelo pasar tiempo con la gente que quiero, hacer planes divertidos, conocer nuevos lugares, disfrutar de las pequeñas cosas de la vida y siempre tener algo nuevo por hacer.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
    
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    texto_3 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )
       
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí debes poner tus 3 gráficos y tu mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Lenguas aisladas")
        texto_5 = """
        Interpretación del Gráfico 1
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("aisladas_base_datos.png", width=800)

    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Familias lingüísticas")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("lengua_familia_GB.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_7 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    