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

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'> Lo que aprendí en el camino 💻</h1>", unsafe_allow_html=True)

    texto_3 = """
   Al principio, sinceramene me sentí bastante perdida. Me ha costado muchísimo aprender programación porque era algo nuevo para mí y muchas veces no entendía lo que estaba haciendo. Me sentía confundida, sobre todo cuando aparecían códigos, errores o ejercicios que no sabía como resolver. Hubo momentos en los que me frustré porque sentía que no avanzaba, pero poco a poco fui tratando de entenderlo y tener mas paciencia en mi proceso.
   La programación me ha enseñado a tener mas opaciencia, a ser perseverante y sobre todo, a no rendirme cuando algo no me sale a la primera. También he aprendido que los problemas se pueden resolver paso a paso y que equivocarse es parte del proceso. Me ha ayudado a desarrollar una forma mas lógica y estructurada de pensar.
   Lo que mas me gusta de programar es que puedes crear cosas desde cero y encontrar muchas maneras de resolver un mismo problema. Aunque todavía me cuesta bastante descubrir cómo unas cuantas líneas de código pueden convertirse en algo que funciona y que puede ser útil.
   En el futuro me gustaría poder aplicar la programación a proyectos relacionados con la publicidad y la comunicación. Me gustaría desarrollar aplicaciones, plataformas digitales o herramientas que ayuden a las personas y que respondan a necesidades reales. El aprender de programación considero que me puede complementar mucho en mi carrera y abrirme muchas oportunidades.
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Mi primer acercamiento a la programación")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Video 1",
                       "https://youtu.be/a1_ip4VrLvM?feature=shared",
                       use_container_width=True
            )

        st.subheader("🎥 Mis aprendizajes en programación")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Video 2",
                       "https://youtu.be/jbqsELWzYXo?feature=shared",
                       use_container_width=True
            )
            
    ## Formato Google Drive
    st.subheader("🎥 Mis aprendizajes en programación")

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
        texto_5 = """ Para realizar el análisis del primer capítulo de Orgullo y Prejuicio, decidí convertir todas las palabras a minúsculas. También eliminé los signos de puntuación, como puntos, comas, guiones y signos de interrogación, ya que no son necesarios para el conteo de palabras.Por otro lado, seleccioné como stopwords los artículos, preposiciones, conjunciones y otras palabras que aparecen frecuentemente, pero que no aportan información importante para identificar los temas principales del capítulo.De esta manera, las palabras con mayor frecuencia destacan visualmente en la nube y ayudan a identificar los temas y conceptos que tienen más presencia en el capitulo. Finalmente, elegí un fondo crema y una paleta de tonos rosados y vino para personalizar la presentación del gráfico por que son colores que me gustan mucho

        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("nube.png", width=800)

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
        En este trabajo logramos analizar la información de los pilotos Nico Rosberg y Lewis Hamilton durante la temporada 2016 de Fórmula 1 
        utilizando Python y la base de datos que se nos proporcionó. Pude calcular los puntajes totales de ambos pilotos y se creó un mapa 
        interactivo con la librería Folium en el que se representó informacion mas especifica como sus ciudades de nacimiento. 
        Además incorporé marcadores personalizados con ventanas emergentes para msotrar sus fotografías, escuderías y puntajes. 
        De esta manera se logró combinar el análisis de datos con la representación geográfica para asi facilitar la visualización de la información detallada y precisa ambos pilotos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    
