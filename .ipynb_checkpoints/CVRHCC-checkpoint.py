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

# Título y actualización
st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
st.write('*Actualizada a octubre de 2024*')

# Información personal en columnas
col1, col2 = st.columns(2)
with col1:
    st.markdown('<p class="respuesta"> Currículum Vítae </p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="subtitulo">Puesto Actual</p>', unsafe_allow_html=True)
    st.markdown('<p class="respuesta">Jefe de Proyecto A</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitulo">Área de Adscripción</p>', unsafe_allow_html=True)
st.markdown('<p class="respuesta">Dirección para la Evaluación de la Mejora de Políticas Públicas Educativas | Comisión Nacional para la Mejora Continua de la Educación</p>', unsafe_allow_html=True)

st.markdown('---')

# Resumen de Competencias
with st.expander("**Resumen de Competencias**", expanded=True):
    st.markdown("""
    <ul class="texto">
        <li><strong>Experiencia</strong>: Más de 20 años en investigación académica, social, de consumo y educativa, tanto cualitativa como cuantitativa.</li>
        <li><strong>Análisis y manejo de información</strong>: Dominio en psicometría y procesos de evaluación a gran escala.</li>
        <li><strong>Coordinación</strong>: Más de 10 años liderando estudios de investigación social y de consumo.</li>
        <li><strong>Diseño y Moderación</strong>: Experto en técnicas cualitativas, moderación de grupos de enfoque y diseño de dinámicas proyectivas.</li>
        <li><strong>Gestión de Equipos</strong>: Coordinación de equipos de recolección y codificación de información.</li>
        <li><strong>Educación a Distancia</strong>: Más de 8 años en diseño instruccional para sistemas en línea.</li>
        <li><strong>Tecnología Educativa</strong>: Implementación y mantenimiento de sistemas de recolección de información y plataformas de aprendizaje en línea como Moodle y LimeSurvey.</li>
    </ul>
    """, unsafe_allow_html=True)

# Habilidades y Habilidades Técnicas en columnas
st.markdown('<p class="seccion">Habilidades</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="subtitulo">Competencias</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Trabajo en equipo y liderazgo.</li>
        <li>Organización y supervisión de equipos.</li>
        <li>Análisis y síntesis de información.</li>
        <li>Habilidades comunicativas y empatía.</li>
        <li>Moderación de grupos de discusión.</li>
        <li>Inglés avanzado.</li>
    </ul>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="subtitulo">Habilidades Técnicas</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Software estadístico: <strong>SPSS</strong>, <strong>R</strong>.</li>
        <li>Programación en <strong>Python</strong>; desarrollo de aplicaciones con <strong>PySide6</strong>, <strong>Streamlit</strong>, <strong>PyQt5</strong>.</li>
        <li>Análisis cualitativo: <strong>ATLAS.ti</strong>.</li>
        <li>Plataformas de encuestas en línea: <strong>LimeSurvey</strong>.</li>
        <li>Sistemas LMS: <strong>Moodle</strong>.</li>
        <li>Manejo avanzado de <strong>Microsoft Office</strong> (Excel, PowerPoint, Word).</li>
        <li>Integración y codificación de datos: <strong>DME</strong>, <strong>SDS</strong> (PISA), <strong>SICREDIA</strong> (ERCE).</li>
    </ul>
    """, unsafe_allow_html=True)

# Formación Profesional
st.markdown('<p class="seccion">Formación Profesional</p>', unsafe_allow_html=True)
st.markdown("""
<p class="texto">
- <strong>1999-2004</strong>: Licenciatura en Psicología, <strong>Universidad Nacional Autónoma de México (UNAM)</strong>, Facultad de Psicología, CDMX.<br>
&nbsp;&nbsp;&nbsp;&nbsp;• <strong>Cédula profesional</strong>: 5586797
</p>
""", unsafe_allow_html=True)

st.markdown('---')

# Experiencia Laboral
st.markdown('<p class="seccion">Experiencia Laboral</p>', unsafe_allow_html=True)

# MEJOREDU
with st.expander("**Octubre 2019 - Actualidad: Comisión Nacional para la Mejora de la Educación (MEJOREDU)**", expanded=True):
    st.markdown('<p class="subtitulo">Dirección para la Evaluación de la Mejora de Políticas Públicas Educativas (Desde octubre 2023)</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Gestión y validación de bases de datos para evaluar políticas de infraestructura educativa.</li>
        <li>Implementación de instrumentos en línea con <strong>LimeSurvey</strong>.</li>
        <li>Análisis estadístico avanzado y elaboración de reportes de resultados.</li>
        <li>Diseño y desarrollo de indicadores de evaluación de política educativa.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Dirección de Evaluación para la Mejora de Docentes y Directivos (2019-2023)</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Diseño de instrumentos para evaluar la función docente.</li>
        <li>Realización de entrevistas cualitativas y moderación de grupos de enfoque.</li>
        <li>Análisis estadístico y gestión de bases de datos.</li>
        <li>Elaboración de informes cualitativos y cuantitativos.</li>
    </ul>
    """, unsafe_allow_html=True)

# INEE
with st.expander("**Abril 2017 - Octubre 2019: Instituto Nacional para la Evaluación de la Educación (INEE)**"):
    st.markdown('<p class="subtitulo">Cargo: Jefe de Integración de Materiales de Evaluación </p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Adaptación y conformación de materiales para evaluaciones internacionales.</li>
        <li>Integración de traducciones y ajustes basados en resultados psicométricos.</li>
        <li>Capacitación y supervisión de codificadores para respuestas abiertas.</li>
        <li>Aseguramiento de la comparabilidad y consistencia con estándares internacionales.</li>
    </ul>
    """, unsafe_allow_html=True)

# BS Marketing
with st.expander("**Mayo 2014 - Agosto 2016: BS Marketing**"):
    st.markdown('<p class="subtitulo">Cargo: Coordinador de Estudios de Investigación Nacional</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Investigación de hábitos de consumo.</li>
        <li>Coordinación de equipos de campo.</li>
        <li>Implementación y mantenimiento de plataformas de encuestas y bases de datos.</li>
    </ul>
    """, unsafe_allow_html=True)

# UNADM
with st.expander("**Mayo 2013 - Diciembre 2013: Universidad a Distancia de México (UNADM), SEP**"):
    st.markdown('<p class="subtitulo">Cargo: Diseñador Instruccional</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Diseño de contenidos para licenciaturas en línea.</li>
        <li>Asesoría en encuestas para estudios de estilos de aprendizaje.</li>
    </ul>
    """, unsafe_allow_html=True)

# b@unam
with st.expander("**Abril 2011 - Marzo 2013: UNAM, Coordinación de Bachillerato a Distancia b@unam**"):
    st.markdown('<p class="subtitulo">Cargo: Diseñador Instruccional</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Diseño de asignaturas en el área de ciencias.</li>
        <li>Creación de evaluaciones y encuestas.</li>
        <li>Gestión de puntajes y calificaciones en <strong>Moodle</strong>.</li>
        <li>Enlace académico entre asesores y la Coordinación.</li>
    </ul>
    """, unsafe_allow_html=True)

# CAME
with st.expander("**Enero 2011 - Abril 2011: CAME (Consejo de Asistencia al Micro Emprendedor)**"):
    st.markdown('<p class="subtitulo">Cargo: Coordinador de Inteligencia de Mercados</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Diseño de metodologías de investigación cualitativa y cuantitativa.</li>
        <li>Moderación de grupos de enfoque y entrevistas a profundidad.</li>
        <li>Análisis de datos y elaboración de reportes.</li>
    </ul>
    """, unsafe_allow_html=True)

# Esfera Social SC
with st.expander("**Marzo 2008 - Enero 2011: Esfera Social SC**"):
    st.markdown('<p class="subtitulo">Cargo: Jefe de Proyectos de Investigación</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Coordinación de proyectos sociales y de consumo.</li>
        <li>Diseño de metodologías cualitativas.</li>
        <li>Moderación de grupos de enfoque.</li>
        <li>Análisis de información cualitativa.</li>
        <li>Entrevistas y etnografía.</li>
    </ul>
    """, unsafe_allow_html=True)

# Instituto de Investigación en Psicología Clínica y Social AC
with st.expander("**Febrero 2004 - Enero 2006: Instituto de Investigación en Psicología Clínica y Social AC**"):
    st.markdown("""
    <ul class="texto">
        <li>Estandarización y validación de instrumentos psicológicos.</li>
        <li>Investigación estadística y docencia auxiliar.</li>
        <li>Asesoría estadística a estudiantes de licenciatura y maestría.</li>
        <li>Traducción de textos especializados y aplicación de pruebas psicológicas.</li>
    </ul>
    """, unsafe_allow_html=True)

st.markdown('---')

# Descarga de CV en PDF
with open("Raul_Camara_CV.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Descargar CV en PDF",
        data=file,
        file_name="Raul_Camara_CV.pdf",
        mime="application/octet-stream"
    )
