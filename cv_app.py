import streamlit as st
import data_info

st.set_page_config(
    page_title="Víctor Alcántar",  # Título de la pestaña del navegador
    layout="centered"  # o "wide" para más espacio
)

# --- Barra lateral de navegación ---
with st.sidebar:
    st.markdown("## Navegación")
    st.markdown("[Inicio](#inicio)")
    st.markdown("[Formación académica](#formacion)")
    st.markdown("[Antecedentes laborales](#laburo)")
    st.markdown("[Distinciones](#distincion)")
    st.markdown('[Reconocimientos académicos](#rec_aca)')
    st.markdown('[Materias impartidas](#materias)')
    st.markdown('[Membresías](#membresias)')
    st.markdown('[Patentes](#patentes)')
    st.markdown('[Publicaciones en revistas indizadas](#indizadas)')
    st.markdown('[Publicaciones en congresos y revistas arbitradas](#congreso)')


# Sección inicial
st.markdown('<a id="inicio"></a>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    # Muestra la imagen (ajusta el width al tamaño deseado)
    st.image("archivos/foto_cv.png", width=120)

with col2:
    st.markdown("### Víctor Alfonso Alcántar Camarena")
    st.write("Dr. en Ingeniería Mecánica")
    st.write("Profesor Titula A")
    st.write("📧 valcantarc@upbicentenario.edu.mx")

st.info(data_info.semblanza)
st.markdown("---")


# Formación académica
st.markdown('<a id="formacion"></a>', unsafe_allow_html=True)
st.success('#### Formación académica')
for item in data_info.formacion:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"{item['periodo']}")  
    with col2:
        st.markdown(f"""
        {item['institucion']}  
        {item['grado']}  
        *Tesis:* {item['tesis']}  
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Antecedentes laborales
st.markdown('<a id="laburo"></a>', unsafe_allow_html=True)
st.success('#### Antecedentes laborales')
for item in data_info.ant_lab:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"{item['periodo']}")
    with col2:
        st.markdown(f"""
        {item['institucion']}
        {item['actividad']}
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Distinciones
st.markdown('<a id="distincion"></a>', unsafe_allow_html=True)
st.success('#### Distinciones')
for item in data_info.distincion:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"{item['periodo']}")
    with col2:
        st.markdown(f"""
        {item['distincion']}
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Reconocimientos académicos
st.markdown('<a id="rec_aca"></a>', unsafe_allow_html=True)
st.success('#### Reconocimientos académicos')
for item in data_info.rec_acad:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"""
        {item['reconocimiento']}  
        {item['trabajo']}  
        {item['institucion']}
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Materias impartidas
st.markdown('<a id="materias"></a>', unsafe_allow_html=True)
st.success("#### Materias impartidas")
for materia in data_info.materias:
    st.markdown(f"- {materia}")
st.markdown('---')


# Membresías
st.markdown('<a id="membresias"></a>', unsafe_allow_html=True)
st.success('#### Membresías')
for item in data_info.membresia:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"""
        {item['comite']}  
        {item['registro']}  
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Patentes
st.markdown('<a id="patentes"></a>', unsafe_allow_html=True)
st.success('#### Patentes')
for item in data_info.patentes:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
    with col2:
        st.markdown(f"""
        {item['titulo']}  
        {item['inventores']}  
        {item['num_patente']}  
        {item['pais']}  
        {item['enlace']}   
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Publicaciones en revistas indizadas
st.markdown('<a id="indizadas"></a>', unsafe_allow_html=True)
st.success('#### Publicaciones en revistas indizadas')
for item in data_info.indizadas:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
    with col2:
        st.markdown(f"""
        {item['titulo']}  
        {item['autores']}  
        {item['journal']}  
        {item['volumen']}  
        {item['paginas']}  
        {item['revista']}  
        {item['doi']}  
        {item['impacto']}  
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')


# Publicaciones en congresos
st.markdown('<a id="congreso"></a>', unsafe_allow_html=True)
st.success('#### Publicaciones en congresos y revistas arbitradas')
for item in data_info.congreso:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
    with col2:
        st.markdown(f"""
        {item['titulo']}  
        {item['autores']}  
        {item['congreso']}  
        {item['isbn']}  
        {item['enlace']}   
        """)
    #st.markdown("<br>", unsafe_allow_html=True)
st.markdown('---')