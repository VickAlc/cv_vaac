import streamlit as st
import data_info

st.set_page_config(
    page_title="Víctor Alcántar",
    layout="centered"
)

st.markdown("""
<style>
.badge-impacto {
    background-color: #0068c9;
    color: white;
    padding: 2px 9px;
    border-radius: 10px;
    font-size: 0.80em;
    font-weight: bold;
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

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
    st.image("archivos/foto_cv.png", width=120)
with col2:
    st.markdown("### Víctor Alfonso Alcántar Camarena")
    st.write("Dr. en Ingeniería Mecánica")
    st.write("Profesor Titular A")
    st.write("📧 valcantarc@upbicentenario.edu.mx")

st.info(data_info.semblanza)
st.markdown("---")


# Formación académica
st.markdown('<a id="formacion"></a>', unsafe_allow_html=True)
st.success('#### Formación académica')
for item in data_info.formacion:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"**{item['institucion']}**  \n{item['grado']}  \n*Tesis:* {item['tesis']}")
st.markdown('---')


# Antecedentes laborales
st.markdown('<a id="laburo"></a>', unsafe_allow_html=True)
st.success('#### Antecedentes laborales')
for item in data_info.ant_lab:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"**{item['institucion']}**  \n{item['actividad']}")
st.markdown('---')


# Distinciones
st.markdown('<a id="distincion"></a>', unsafe_allow_html=True)
st.success('#### Distinciones')
for item in data_info.distincion:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"**{item['distincion']}**")
st.markdown('---')


# Reconocimientos académicos
st.markdown('<a id="rec_aca"></a>', unsafe_allow_html=True)
st.success('#### Reconocimientos académicos')
for item in data_info.rec_acad:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"**{item['reconocimiento']}**  \n*{item['trabajo']}*  \n{item['institucion']}")
st.markdown('---')


# Materias impartidas
st.markdown('<a id="materias"></a>', unsafe_allow_html=True)
st.success("#### Materias impartidas")
col1, col2 = st.columns(2)
mid = (len(data_info.materias) + 1) // 2
for i, materia in enumerate(data_info.materias):
    (col1 if i < mid else col2).markdown(f"- {materia}")
st.markdown('---')


# Membresías
st.markdown('<a id="membresias"></a>', unsafe_allow_html=True)
st.success('#### Membresías')
for item in data_info.membresia:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['periodo']}**")
    with col2:
        st.markdown(f"**{item['comite']}**  \n{item['registro']}")
st.markdown('---')


# Patentes
st.markdown('<a id="patentes"></a>', unsafe_allow_html=True)
st.success('#### Patentes')
for item in data_info.patentes:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
    with col2:
        st.markdown(f"**{item['titulo']}**")
        st.markdown(f"*Inventores:* {item['inventores']}")
        st.markdown(f"No. `{item['num_patente']}` | {item['pais']}")
        st.markdown(f"[🔗 Ver patente]({item['enlace']})")
        st.markdown("")
st.markdown('---')


# Publicaciones en revistas indizadas
st.markdown('<a id="indizadas"></a>', unsafe_allow_html=True)
st.success('#### Publicaciones en revistas indizadas')
for item in data_info.indizadas:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
        st.markdown(
            f'<span class="badge-impacto">IF&nbsp;{item["impacto"]}</span>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(f"**{item['titulo']}**")
        st.markdown(f"*{item['autores']}*")
        st.markdown(
            f"📰 {item['journal']} | Vol. {item['volumen']} | pp. {item['paginas']} | {item['revista']}"
        )
        st.markdown(f"[🔗 DOI]({item['doi']})")
        st.markdown("")
st.markdown('---')


# Publicaciones en congresos
st.markdown('<a id="congreso"></a>', unsafe_allow_html=True)
st.success('#### Publicaciones en congresos y revistas arbitradas')
for item in data_info.congreso:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"**{item['anio']}**")
    with col2:
        st.markdown(f"{item['titulo']}")
        st.markdown(f"*{item['autores']}*")
        st.markdown(f"📍 {item['congreso']} | {item['isbn']}")
        st.markdown(f"[🔗 Ver publicación]({item['enlace']})")
        st.markdown("")
st.markdown('---')
