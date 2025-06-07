import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Raúl Cámara Carreón - CV", layout="wide")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .titulo {
        font-size:28px;
        font-weight:bold;
    }
    .subtitulo {
        font-size:24px;
        font-weight:bold;
    }
    .texto {
        font-size:18px;
    }
    .respuesta {
        font-size:18px;
        font-weight:bold;
    }
    .seccion {
        font-size:22px;
        font-weight:bold;
        color: #2e7bcf;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="position: absolute; top: 0; right: 0; padding: 10px;">
        <img src="https://raw.githubusercontent.com/raulcamaracarreon/mi-cv-streamlit/main/RHCC_BN.png" width="80">
    </div>
""", unsafe_allow_html=True)

# Título y actualización
st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
st.write('*Actualizado a junio de 2025*')

# Información personal en columnas
col1, col2 = st.columns(2)
with col1:
    st.markdown('<p class="respuesta"> Currículum Vítae </p>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Contacto: raul.camara76@gmail.com |  | Tel: +52 55 32874013</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="subtitulo">Objetivo Profesional</p>', unsafe_allow_html=True)
    st.markdown('<p class="respuesta">Contribuir al desarrollo de la investigación de mercados y educativa a través del análisis de datos aprovechando el desarrollo tecnológico e IA, aportando visión estratégica, experiencia analítica y habilidades en análisis, visualización y automatización.</p>', unsafe_allow_html=True)

st.markdown('---')

# Resumen de Competencias
with st.expander("**Resumen de Competencias**", expanded=True):
    st.markdown("""
    <ul class="texto">
        <li><strong>Experiencia multidisciplinaria:</strong> Más de 18 años en investigación académica, social, de consumo y evaluación educativa, con dominio en diseño de instrumentos, recolección de datos y análisis estadístico.</li>
        <li><strong>Capacidad analítica:</strong> Experto en transformar datos en conocimiento estratégico mediante técnicas de segmentación, inferencia y modelado estadístico.</li>
        <li><strong>Comunicación de resultados:</strong> Redacción de informes claros y efectivos, presentaciones ejecutivas, visualización de datos y generación de materiales de divulgación.</li>
        <li><strong>Integración tecnológica:</strong> Incorporación de tecnologías como Python, IA, Streamlit, automatización de reportes y visualización interactiva.</li>
        <li><strong>Perfil formativo y colaborativo:</strong> Experiencia en capacitación, coordinación de equipos y liderazgo metodológico en proyectos nacionales e internacionales.</li>
    </ul>
    """, unsafe_allow_html=True)

# Habilidades
st.markdown('<p class="seccion">Habilidades</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="subtitulo">Competencias Generales</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Pensamiento analítico, estratégico y crítico.</li>
        <li>Diseño de instrumentos para evaluación de diversos aspectos en el ámbito de investigación social, de mercados y educativa.</li>
        <li>Diseño de indicadores estratégicos para evaluar mejora de aspectos, servicios y productos.</li>
        <li>Diseño y evaluación de políticas públicas educativas.</li>
        <li>Comunicación efectiva escrita y oral para públicos técnicos y no técnicos.</li>
        <li>Enfoque ético y sensibilidad social en el uso de los datos.</li>
    </ul>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="subtitulo">Habilidades Técnicas</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Python: pandas, matplotlib, NumPy, Streamlit, PySide6, PyQt5, PyQt6, scikit-learn.</li>
        <li>SPSS, R, Excel avanzado.</li>
        <li>ATLAS.ti para análisis cualitativo.</li>
        <li>LimeSurvey, Moodle, GitHub, PowerPoint.</li>
        <li>Diseño de bases de datos, integración de resultados, dashboards interactivos.</li>
    </ul>
    """, unsafe_allow_html=True)

# Formación Profesional
st.markdown('<p class="seccion">Formación Profesional</p>', unsafe_allow_html=True)
st.markdown("""
<p class="texto">
- <strong>Licenciatura en Psicología</strong>, UNAM, Facultad de Psicología (1999–2004).<br>
</p>
""", unsafe_allow_html=True)

# Experiencia Laboral
st.markdown('<p class="seccion">Experiencia Laboral</p>', unsafe_allow_html=True)

with st.expander("**2023 - 2025: Dirección para la Evaluación de la Mejora de Políticas Públicas Educativas, MEJOREDU**", expanded=False):
    st.markdown("""
    <ul class="texto">
        <li>Desarrollo de indicadores estratégicos de infraestructura educativa.</li>
        <li>Automatización de reportes con Python y pandas.</li>
        <li>Diseño de visualizaciones interactivas.</li>
    </ul>
    """, unsafe_allow_html=True)

with st.expander("**2019 - 2023: Dirección de Evaluación de Docentes y Directivos, MEJOREDU**"):
    st.markdown("""
    <ul class="texto">
        <li>Diseño, validación y aplicación de instrumentos para la evaluación docente.</li>
        <li>Gestión de datos cuantitativos y cualitativos.</li>
        <li>Elaboración de reportes ejecutivos y presentaciones públicas.</li>
    </ul>
    """, unsafe_allow_html=True)

with st.expander("**2017 - 2019: Instituto Nacional para la Evaluación de la Educación (INEE)**"):
    st.markdown("""
    <ul class="texto">
        <li>Jefe de integración de materiales para evaluaciones internacionales.</li>
        <li>Supervisión de codificadores para la prueba PISA.</li>
        <li>Control de calidad psicométrico y estandarización internacional.</li>
    </ul>
    """, unsafe_allow_html=True)

with st.expander("**Experiencia adicional (2004 - 2016)**"):
    st.markdown("""
    <ul class="texto">
        <li>Consultor en investigación de consumo, hábitos y percepción de marca (BS Marketing).</li>
        <li>Diseñador instruccional para educación a distancia (UNADM, UNAM-b@unam).</li>
        <li>Coordinador de estudios cualitativos y mixtos en Esfera Social y CAME.</li>
        <li>Docente auxiliar y asesor estadístico en Instituto de Investigación en Psicología Clínica y Social AC.</li>
    </ul>
    """, unsafe_allow_html=True)

# Portafolio y Enlaces
st.markdown('<p class="seccion">Desarrollos y Proyectos Tecnológicos (2022–2025)</p>', unsafe_allow_html=True)
st.markdown("""
<ul class="texto">
    <li>Desarrollo de aplicaciones en Python (PyQt5, PyQt6, PySide6): interfaces gráficas para análisis de datos y herramientas de visualización.</li>
    <li>Aplicaciones con Streamlit para dashboards interactivos y visualización de datos. <a href="https://share.streamlit.io/user/raulcamaracarreon" target="_blank">Perfil en Streamlit Cloud</a></li>
    <li>Curso de LLM Engineering: especialización en modelos de lenguaje, embeddings y agentes inteligentes.</li>
    <li>Proyectos de IA: chat entre IAs, agente de ventas, resumidor web, chat con FAISS.</li>
    <li><a href="https://pleen.simep.info" target="_blank">Sistema de monitoreo educativo SIMEPP</a>: análisis de datos educativos en VPS.</li>
    <li>Módulo Mejoredu con despliegue VPS y consultas por CCT.</li>
    <li><a href="https://relax-music.onrender.com/" target="_blank">Web app para música de relajación</a>: generador de paisajes sonoros en Flask.</li>
    <li>Desarrollo de videojuegos en Godot: shooter 2D y RPG con caballero y espada.</li>
    <li><a href="https://github.com/raulcamaracarreon" target="_blank">GitHub personal</a>: proyectos de código abierto.</li>
</ul>
""", unsafe_allow_html=True)

# Descarga de CV
try:
    with open("Raul_Camara_CV.pdf", "rb") as file:
        btn = st.download_button(
            label="📄 Descargar CV en PDF",
            data=file,
            file_name="Raul_Camara_CV.pdf",
            mime="application/octet-stream"
        )
except FileNotFoundError:
    st.warning("El archivo PDF aún no ha sido cargado para descarga.")
