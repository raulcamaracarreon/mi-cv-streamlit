import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Raúl Cámara Carreón - CV", layout="wide")

# Selector de idioma
language = st.selectbox("🌐 Select language / Selecciona idioma:", ["Español", "English"])

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

# Logo en la esquina superior derecha
st.markdown("""
    <div style="position: absolute; top: 0; right: 0; padding: 10px;">
        <img src="https://raw.githubusercontent.com/raulcamaracarreon/mi-cv-streamlit/main/RHCC_BN.png" width="80">
    </div>
""", unsafe_allow_html=True)

def contenido_espanol():
    st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
    st.write('*Actualizado a junio de 2025*')
    st.markdown('<p class="subtitulo">Objetivo Profesional</p>', unsafe_allow_html=True)
    st.markdown('<p class="respuesta">Contribuir al desarrollo de la investigación de mercados y educativa a través del análisis de datos, aprovechando el desarrollo tecnológico e IA.</p>', unsafe_allow_html=True)

    with st.expander("**Resumen de Competencias**", expanded=True):
        st.markdown("""
        <ul class="texto">
            <li><strong>Experiencia multidisciplinaria:</strong> Más de 18 años en investigación académica, social, de consumo, de mercados y evaluación educativa.</li>
            <li><strong>Capacidad analítica:</strong> Experto en transformar datos en conocimiento estratégico mediante segmentación, inferencia y modelado.</li>
            <li><strong>Comunicación de resultados:</strong> Redacción de informes claros, presentaciones ejecutivas y visualización de datos.</li>
            <li><strong>Integración tecnológica:</strong> Uso de Python, Streamlit, IA y automatización de reportes.</li>
            <li><strong>Perfil formativo y colaborativo:</strong> Coordinación de equipos y liderazgo metodológico.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Habilidades</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="subtitulo">Competencias Generales</p>', unsafe_allow_html=True)
        st.markdown("""
        <ul class="texto">
            <li>Pensamiento analítico, estratégico y crítico.</li>
            <li>Diseño de instrumentos de evaluación.</li>
            <li>Diseño de indicadores estratégicos.</li>
            <li>Evaluación de políticas educativas.</li>
            <li>Comunicación efectiva escrita y oral.</li>
            <li>Ética y sensibilidad social.</li>
        </ul>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown('<p class="subtitulo">Habilidades Técnicas</p>', unsafe_allow_html=True)
        st.markdown("""
        <ul class="texto">
            <li>Python: pandas, matplotlib, NumPy, Streamlit, PySide6, PyQt5/6, scikit-learn.</li>
            <li>SPSS, R, Excel avanzado.</li>
            <li>ATLAS.ti, LimeSurvey, Moodle, GitHub, PowerPoint.</li>
            <li>Diseño de bases de datos y dashboards interactivos.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Formación Profesional</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Licenciatura en Psicología</strong>, UNAM, Facultad de Psicología (1999–2004).</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Experiencia Laboral</p>', unsafe_allow_html=True)
    with st.expander("**2023 - 2025: MEJOREDU - Dirección para la Evaluación de la Mejora de Políticas Públicas Educativas**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Desarrollo de indicadores de infraestructura educativa.</li>
            <li>Automatización de reportes con Python y pandas.</li>
            <li>Visualizaciones interactivas.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2019 - 2023: MEJOREDU - Dirección de Evaluación de Docentes y Directivos**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Diseño y validación de instrumentos de evaluación docente.</li>
            <li>Gestión de datos cuantitativos y cualitativos.</li>
            <li>Reportes ejecutivos y presentaciones.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2017 - 2019: INEE - Instituto Nacional para la Evaluación de la Educación**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Integración de materiales para evaluaciones internacionales.</li>
            <li>Supervisión de codificadores PISA.</li>
            <li>Control psicométrico y estandarización.</li>
        </ul>
        """, unsafe_allow_html=True)

    # Experiencia adicional
    with st.expander("**2014 - 2016: BS Marketing - Coordinador de Estudios de Investigación Nacional**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Investigación de hábitos de consumo y percepción de marca.</li>
            <li>Coordinación de equipos de campo.</li>
            <li>Mantenimiento de plataformas de encuestas.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2013: UNADM, SEP - Diseñador Instruccional**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Diseño de contenidos para licenciaturas en línea.</li>
            <li>Asesoría en encuestas de estilos de aprendizaje.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2011 - 2013: UNAM b@unam - Diseñador Instruccional**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Diseño de asignaturas de ciencias.</li>
            <li>Evaluaciones y encuestas en Moodle.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2011: CAME - Coordinador de Inteligencia de Mercados**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Investigación cualitativa y cuantitativa.</li>
            <li>Moderación de grupos de enfoque.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2008 - 2011: Esfera Social SC - Jefe de Proyectos de Investigación**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Estudios sociales y de consumo.</li>
            <li>Etnografía y dinámicas proyectivas.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2004 - 2006: Instituto de Investigación en Psicología Clínica y Social AC - Investigador / Docente Auxiliar**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Validación de instrumentos psicológicos.</li>
            <li>Asesoría estadística y docencia auxiliar.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Desarrollos y Proyectos Tecnológicos (2022–2025)</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Apps en Python (PyQt5/6, PySide6).</li>
        <li>Dashboards con Streamlit: <a href="https://share.streamlit.io/user/raulcamaracarreon" target="_blank">Perfil Streamlit</a></li>
        <li>Curso LLM Engineering.</li>
        <li>Proyectos IA: chat IA, agente ventas, FAISS.</li>
        <li>SIMEPP: <a href="https://pleen.simep.info">pleen.simep.info</a></li>
        <li>Relax music: <a href="https://relax-music.onrender.com" target="_blank">relax-music</a></li>
        <li>Videojuegos con Godot (Shooter 2D, RPG).</li>
        <li>GitHub: <a href="https://github.com/raulcamaracarreon" target="_blank">raulcamaracarreon</a></li>
    </ul>
    """, unsafe_allow_html=True)

def contenido_english():
    st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
    st.write('*Updated June 2025*')
    st.markdown('<p class="subtitulo">Professional Objective</p>', unsafe_allow_html=True)
    st.markdown('<p class="respuesta">Contribute to the development of market and educational research through data analysis, leveraging technology and AI.</p>', unsafe_allow_html=True)

    with st.expander("**Summary of Competencies**", expanded=True):
        st.markdown("""
        <ul class="texto">
            <li><strong>Multidisciplinary experience:</strong> Over 18 years in academic, social, consumer, market, and educational research.</li>
            <li><strong>Analytical capacity:</strong> Expert in turning data into strategic insights through segmentation, inference, and modeling.</li>
            <li><strong>Results communication:</strong> Clear report writing, executive presentations, and data visualization.</li>
            <li><strong>Technological integration:</strong> Proficient in Python, Streamlit, AI, and report automation.</li>
            <li><strong>Training & collaboration:</strong> Team coordination and methodological leadership.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Skills</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="subtitulo">General Competencies</p>', unsafe_allow_html=True)
        st.markdown("""
        <ul class="texto">
            <li>Analytical, strategic, and critical thinking.</li>
            <li>Design of evaluation instruments.</li>
            <li>Strategic indicator development.</li>
            <li>Evaluation of educational public policies.</li>
            <li>Effective written and oral communication.</li>
            <li>Ethical approach and social sensitivity.</li>
        </ul>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown('<p class="subtitulo">Technical Skills</p>', unsafe_allow_html=True)
        st.markdown("""
        <ul class="texto">
            <li>Python: pandas, matplotlib, NumPy, Streamlit, PySide6, PyQt5/6, scikit-learn.</li>
            <li>SPSS, R, Advanced Excel.</li>
            <li>ATLAS.ti, LimeSurvey, Moodle, GitHub, PowerPoint.</li>
            <li>Database design & interactive dashboards.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Education</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Bachelor's Degree in Psychology</strong>, UNAM, Faculty of Psychology (1999–2004).</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Work Experience</p>', unsafe_allow_html=True)
    with st.expander("**2023 – 2025: MEJOREDU - Directorate for the Evaluation of the Improvement of Public Educational Policies**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Development of educational infrastructure indicators.</li>
            <li>Report automation with Python and pandas.</li>
            <li>Interactive data visualizations.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2019 – 2023: MEJOREDU - Directorate of Teacher and Principal Evaluation**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Design and validation of teacher evaluation instruments.</li>
            <li>Management of quantitative and qualitative data.</li>
            <li>Executive reporting and presentations.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2017 – 2019: INEE - National Institute for Educational Evaluation**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Compiled materials for international assessments.</li>
            <li>Supervised PISA coding teams.</li>
            <li>Psychometric quality control & standardization.</li>
        </ul>
        """, unsafe_allow_html=True)

    # Additional Experience
    with st.expander("**2014 – 2016: BS Marketing - National Research Studies Coordinator**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Consumer habits and brand perception studies.</li>
            <li>Field team coordination.</li>
            <li>Survey platforms maintenance.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2013: UNADM, SEP - Instructional Designer**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Online course content design.</li>
            <li>Methodological advice for learning style surveys.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2011 – 2013: UNAM b@unam - Instructional Designer**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Science course design (chemistry, biology, physics).</li>
            <li>Moodle assessments and surveys.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2011: CAME - Market Intelligence Coordinator**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Qualitative & quantitative research.</li>
            <li>Focus group moderation.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2008 – 2011: Esfera Social SC - Research Project Manager**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Social and consumer studies.</li>
            <li>Ethnography & projective techniques.</li>
        </ul>
        """, unsafe_allow_html=True)
    with st.expander("**2004 – 2006: Institute of Clinical & Social Psychology Research AC - Researcher / Teaching Assistant**", expanded=False):
        st.markdown("""
        <ul class="texto">
            <li>Psychological instrument validation.</li>
            <li>Statistical advising & teaching.</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown('<p class="seccion">Projects & Portfolio (2022–2025)</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Python apps (PyQt5/6, PySide6).</li>
        <li>Streamlit dashboards: <a href="https://share.streamlit.io/user/raulcamaracarreon" target="_blank">Streamlit Profile</a></li>
        <li>LLM Engineering course.</li>
        <li>AI projects: chatbots, sales agent, FAISS-based chat.</li>
        <li>SIMEPP monitoring system: <a href="https://pleen.simep.info">pleen.simep.info</a></li>
        <li>Relax music web app: <a href="https://relax-music.onrender.com" target="_blank">relax-music</a></li>
        <li>Godot games (2D Shooter, RPG).</li>
        <li>GitHub: <a href="https://github.com/raulcamaracarreon" target="_blank">raulcamaracarreon</a></li>
    </ul>
    """, unsafe_allow_html=True)

# Mostrar contenido según idioma
if language == "Español":
    contenido_espanol()
else:
    contenido_english()

# Botón de descarga de CV
cv_file = "Raul_Camara_CV_EN.pdf" if language == "English" else "Raul_Camara_CV.pdf"
label = "📄 Download CV (PDF)" if language == "English" else "📄 Descargar CV (PDF)"
try:
    with open(cv_file, "rb") as file:
        st.download_button(label=label, data=file, file_name=cv_file, mime="application/pdf")
except FileNotFoundError:
    st.warning("PDF file not found." if language == "English" else "El archivo PDF no ha sido encontrado.")
