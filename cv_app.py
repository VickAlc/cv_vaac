import streamlit as st
import data_info
from collections import defaultdict

st.set_page_config(
    page_title="Víctor Alcántar",
    layout="centered"
)

# --- CSS personalizado ---
st.markdown("""
<style>
    /* Header de sección */
    .section-header {
        background-color: #1f4e79;
        color: white;
        padding: 8px 18px;
        border-radius: 6px;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 14px;
    }
    /* Badge de periodo/año */
    .periodo-tag {
        background-color: #dbeafe;
        color: #1d4ed8;
        padding: 3px 10px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.88rem;
        display: inline-block;
        white-space: nowrap;
    }
    /* Badge de factor de impacto */
    .impact-badge {
        background-color: #166534;
        color: white;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
    }
    /* Divisor suave entre items */
    .soft-divider {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 10px 0 14px 0;
    }
</style>
""", unsafe_allow_html=True)


# --- Helpers ---
def section_header(title, icon=""):
    st.markdown(f'<div class="section-header">{icon} {title}</div>', unsafe_allow_html=True)


def periodo_tag(text):
    st.markdown(f'<span class="periodo-tag">{text}</span>', unsafe_allow_html=True)


def impact_badge(value):
    return f'<span class="impact-badge">IF&nbsp;{value}</span>'


def soft_divider():
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)


def strip_prefix(text, prefix):
    """Elimina un prefijo si existe."""
    return text.replace(prefix, "", 1).strip()


def clean_link(raw):
    """Extrae solo la URL de un campo que puede tener texto adicional."""
    return raw.strip().split(" ")[0]


# --- Barra lateral de navegación ---
with st.sidebar:
    st.markdown("## Navegación")
    st.markdown("[Inicio](#inicio)")
    st.markdown("[Formación académica](#formacion)")
    st.markdown("[Antecedentes laborales](#laburo)")
    st.markdown("[Distinciones](#distincion)")
    st.markdown("[Reconocimientos académicos](#rec_aca)")
    st.markdown("[Materias impartidas](#materias)")
    st.markdown("[Membresías](#membresias)")
    st.markdown("[Patentes](#patentes)")
    st.markdown("[Revistas indizadas](#indizadas)")
    st.markdown("[Congresos y revistas arbitradas](#congreso)")


# ============================================================
# Sección inicial / Perfil
# ============================================================
st.markdown('<a id="inicio"></a>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("archivos/foto_cv.png", width=140)
with col2:
    st.markdown("### Víctor Alfonso Alcántar Camarena")
    st.markdown("Dr. en Ingeniería Mecánica")
    st.markdown("Profesor Titular A")
    st.markdown("📧 valcantarc@upbicentenario.edu.mx")

st.info(data_info.semblanza)
st.markdown("---")


# ============================================================
# Formación académica
# ============================================================
st.markdown('<a id="formacion"></a>', unsafe_allow_html=True)
section_header("Formación académica", "🎓")
for item in data_info.formacion:
    col1, col2 = st.columns([1, 5])
    with col1:
        periodo_tag(item["periodo"])
    with col2:
        st.markdown(f"**{item['institucion']}** — {item['grado']}")
        st.markdown(f"*Tesis:* {item['tesis']}")
    soft_divider()
st.markdown("---")


# ============================================================
# Antecedentes laborales
# ============================================================
st.markdown('<a id="laburo"></a>', unsafe_allow_html=True)
section_header("Antecedentes laborales", "💼")
for item in data_info.ant_lab:
    col1, col2 = st.columns([1, 5])
    with col1:
        periodo_tag(item["periodo"])
    with col2:
        st.markdown(f"**{item['institucion']}** — {item['actividad']}")
    soft_divider()
st.markdown("---")


# ============================================================
# Distinciones
# ============================================================
st.markdown('<a id="distincion"></a>', unsafe_allow_html=True)
section_header("Distinciones", "🏅")
for item in data_info.distincion:
    col1, col2 = st.columns([1, 5])
    with col1:
        periodo_tag(item["periodo"])
    with col2:
        st.markdown(f"{item['distincion']}")
    soft_divider()
st.markdown("---")


# ============================================================
# Reconocimientos académicos
# ============================================================
st.markdown('<a id="rec_aca"></a>', unsafe_allow_html=True)
section_header("Reconocimientos académicos", "🏆")
for item in data_info.rec_acad:
    col1, col2 = st.columns([1, 5])
    with col1:
        periodo_tag(item["periodo"])
    with col2:
        st.markdown(f"**{item['reconocimiento']}**")
        st.markdown(f"*{item['trabajo']}*")
        st.markdown(f"{item['institucion']}")
    soft_divider()
st.markdown("---")


# ============================================================
# Materias impartidas — 2 columnas
# ============================================================
st.markdown('<a id="materias"></a>', unsafe_allow_html=True)
section_header("Materias impartidas", "📚")
mid = (len(data_info.materias) + 1) // 2
col1, col2 = st.columns(2)
with col1:
    for m in data_info.materias[:mid]:
        st.markdown(f"- {m}")
with col2:
    for m in data_info.materias[mid:]:
        st.markdown(f"- {m}")
st.markdown("---")


# ============================================================
# Membresías
# ============================================================
st.markdown('<a id="membresias"></a>', unsafe_allow_html=True)
section_header("Membresías", "🤝")
for item in data_info.membresia:
    col1, col2 = st.columns([1, 5])
    with col1:
        periodo_tag(item["periodo"])
    with col2:
        st.markdown(f"**{item['comite']}**")
        st.markdown(f"{item['registro']}")
    soft_divider()
st.markdown("---")


# ============================================================
# Patentes — expanders con link clicable
# ============================================================
st.markdown('<a id="patentes"></a>', unsafe_allow_html=True)
section_header("Patentes", "🔒")
for item in data_info.patentes:
    titulo = strip_prefix(item["titulo"], "Título: ").strip('"')
    inventores = strip_prefix(item["inventores"], "Inventores: ")
    num_patente = strip_prefix(item["num_patente"], "Número de patente: ")
    pais = strip_prefix(item["pais"], "País: ")
    enlace = clean_link(item["enlace"])

    with st.expander(f"📄 {num_patente}  ({item['anio']}) — {pais}"):
        st.markdown(f"**{titulo}**")
        st.markdown(f"*Inventores:* {inventores}")
        st.link_button("Ver patente completa", enlace)
st.markdown("---")


# ============================================================
# Publicaciones en revistas indizadas — agrupadas por año
# ============================================================
st.markdown('<a id="indizadas"></a>', unsafe_allow_html=True)
section_header("Publicaciones en revistas indizadas", "📰")

indizadas_por_anio = defaultdict(list)
for item in data_info.indizadas:
    indizadas_por_anio[item["anio"]].append(item)

for anio in sorted(indizadas_por_anio.keys(), reverse=True):
    st.markdown(f"##### {anio}")
    for item in indizadas_por_anio[anio]:
        titulo = strip_prefix(item["titulo"], "Título: ").strip('"')
        autores = strip_prefix(item["autores"], "Autores: ")
        journal = strip_prefix(item["journal"], "Journal: ")
        volumen = strip_prefix(item["volumen"], "Volumen: ")
        paginas = strip_prefix(item["paginas"], "Páginas: ")
        revista = strip_prefix(item["revista"], "Revista: ")
        impacto = strip_prefix(item["impacto"], "Factor de impacto: ")
        doi_url = strip_prefix(item["doi"], "DOI: ")

        vol_str = f"Vol. {volumen} | " if volumen != "--" else ""

        with st.expander(f"📄 {titulo}"):
            st.markdown(f"*{autores}*")
            st.markdown(f"**{journal}** — {revista}")
            st.markdown(f"{vol_str}Págs. {paginas}")
            col_doi, col_if = st.columns([4, 1])
            with col_doi:
                st.markdown(f"[{doi_url}]({doi_url})")
            with col_if:
                st.markdown(impact_badge(impacto), unsafe_allow_html=True)
st.markdown("---")


# ============================================================
# Publicaciones en congresos y revistas arbitradas
# ============================================================
st.markdown('<a id="congreso"></a>', unsafe_allow_html=True)
section_header("Publicaciones en congresos y revistas arbitradas", "🎤")

congreso_por_anio = defaultdict(list)
for item in data_info.congreso:
    congreso_por_anio[item["anio"]].append(item)

for anio in sorted(congreso_por_anio.keys(), reverse=True):
    st.markdown(f"##### {anio}")
    for item in congreso_por_anio[anio]:
        titulo = strip_prefix(item["titulo"], "Título: ").strip("*").strip()
        autores = strip_prefix(item["autores"], "Autores: ")
        congreso_nombre = strip_prefix(item["congreso"], "Congreso: ")
        isbn = item["isbn"].strip()
        enlace = clean_link(item["enlace"])

        with st.expander(f"📋 {titulo}"):
            st.markdown(f"*{autores}*")
            st.markdown(f"**{congreso_nombre}**")
            st.markdown(f"{isbn}")
            st.link_button("Ver publicación", enlace)
st.markdown("---")
