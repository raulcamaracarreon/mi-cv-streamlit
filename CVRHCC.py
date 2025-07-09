import streamlit as st

# ---------------------------
# Configuración de la página
# ---------------------------
st.set_page_config(page_title="Raúl Cámara Carreón - CV", layout="wide")

# ---------------------------
# Selector de idioma
# ---------------------------
language = st.selectbox("🌐 Select language / Selecciona idioma:", ["Español", "English"], index=0)

# ---------------------------
# Estilos CSS personalizados
# ---------------------------
st.markdown(
    """
    <style>
    .titulo {font-size:30px;font-weight:bold;}
    .subtitulo {font-size:24px;font-weight:bold;margin-top:10px;}
    .texto {font-size:18px;}
    .respuesta {font-size:18px;font-weight:bold;}
    .seccion {font-size:22px;font-weight:bold;color:#2e7bcf;margin-top:20px;}
    ul.texto {margin-left:15px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Logo en la esquina superior derecha
# ---------------------------
st.markdown(
    """
    <div style="position:absolute; top:0; right:0; padding:10px;">
        <img src="https://raw.githubusercontent.com/raulcamaracarreon/mi-cv-streamlit/main/RHCC_BN.png" width="80">
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Contenido en Español
# ---------------------------

def contenido_espanol():
    # Encabezado
    st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
    st.write('*Actualizado a junio de 2025*')

    # Datos de contacto
    st.markdown(
        '<p class="texto">📧 raul.camara76@gmail.com &nbsp;&nbsp; 📞 (+52) 55 3287 4013 &nbsp;&nbsp; 🏠 Tlalpan, CDMX</p>',
        unsafe_allow_html=True,
    )

    # Perfil profesional
    st.markdown('<p class="subtitulo">Perfil Profesional</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="respuesta">Especialista en análisis de datos, estudios de mercado y desarrollo de soluciones digitales. Más de 18 años de experiencia en investigación de mercados, coordinación de encuestas, análisis estadístico (SPSS, Python), visualización interactiva (Streamlit, Power BI) y desarrollo de aplicaciones en Python (PySide6, Flask) y Flutter. Capacidad para liderar proyectos desde el diseño metodológico hasta la implementación tecnológica. Perfil híbrido técnico‑analítico con enfoque en innovación, eficiencia y comunicación clara de hallazgos.</p>',
        unsafe_allow_html=True,
    )

    # Habilidades
    st.markdown('<p class="seccion">Habilidades</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="subtitulo">Competencias Generales</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <ul class="texto">
                <li>Pensamiento analítico, estratégico y crítico.</li>
                <li>Diseño de instrumentos de evaluación y encuestas.</li>
                <li>Diseño de indicadores estratégicos.</li>
                <li>Evaluación de políticas educativas.</li>
                <li>Comunicación efectiva escrita y oral.</li>
                <li>Liderazgo y coordinación de equipos multidisciplinarios.</li>
                <li>Ética profesional y sensibilidad social.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown('<p class="subtitulo">Habilidades Técnicas</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <ul class="texto">
                <li><strong>Programación:</strong> Python, R, SQL, Dart, JavaScript (básico).</li>
                <li><strong>Librerías Python:</strong> pandas, NumPy, scikit‑learn, matplotlib, Plotly.</li>
                <li><strong>Frameworks / GUI:</strong> Streamlit, PySide6, PyQt5/6, Flask, Android Studio, Flutter.</li>
                <li><strong>Visualización:</strong> Power BI, Tableau, Streamlit, Matplotlib.</li>
                <li><strong>Análisis estadístico:</strong> SPSS, Excel avanzado.</li>
                <li><strong>IA & NLP:</strong> OpenAI, Hugging Face, FAISS, embeddings, generación de PDFs.</li>
                <li><strong>Dev & Control de versiones:</strong> GitHub.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Formación Académica
    st.markdown('<p class="seccion">Formación Académica</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>Licenciatura en Psicología</strong>, UNAM, Facultad de Psicología (1999–2004).<br>Cédula profesional: 5586797 &nbsp; | &nbsp; Promedio: 8.8/10</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Cursos y Certificaciones
    st.markdown('<p class="seccion">Cursos y Certificaciones</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Hootsuite Social Media Management Certified Professional.</li>
            <li>Social Network Analysis – University of Michigan (MOOC).</li>
            <li>Manejo estadístico con SPSS – UNAM (40 h).</li>
            <li>Curso de Ingeniería de LLMs (IA aplicada).</li>
            <li>Cursos de desarrollo de apps en Flutter y análisis de datos en Python.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Experiencia Profesional
    st.markdown('<p class="seccion">Experiencia Profesional</p>', unsafe_allow_html=True)

    # --- MEJOREDU 2023‑2025
    with st.expander("**Oct. 2023 – May 2025 | MEJOREDU – Dirección para la Evaluación de la Mejora de Políticas Públicas Educativas**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Diseño y desarrollo de indicadores estratégicos: <em>Índice de Mejora</em> y <em>Coeficiente de Mejora de Infraestructura</em>.</li>
                <li>Análisis estadístico avanzado y elaboración de reportes.</li>
                <li>Desarrollo de dashboards y soluciones digitales (Python, Streamlit, PySide6).</li>
                <li>Automatización de informes y sistemas de captura digital con LimeSurvey.</li>
                <li><strong>Logros:</strong> Reducción de costos y tiempos de recolección de datos; creación de módulos interactivos para el programa PLEEN.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- MEJOREDU 2019‑2023
    with st.expander("**Oct. 2019 – Oct. 2023 | MEJOREDU – Dirección de Evaluación para la Mejora de Docentes y Directivos**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Diseño de instrumentos para evaluar la función docente.</li>
                <li>Entrevistas cualitativas y moderación de grupos de enfoque.</li>
                <li>Análisis estadístico y gestión de bases de datos.</li>
                <li>Dashboards con Streamlit para presentación de resultados.</li>
                <li>Elaboración de informes cualitativos y cuantitativos.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- INEE 2017‑2019
    with st.expander("**Abr. 2017 – Oct. 2019 | INEE – Instituto Nacional para la Evaluación de la Educación (Jefe de Proyecto A)**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Adaptación y conformación de materiales para evaluaciones internacionales (PISA).</li>
                <li>Integración de traducciones y ajustes psicométricos.</li>
                <li>Capacitación y supervisión de codificadores de respuestas abiertas.</li>
                <li>Aseguramiento de comparabilidad conforme a estándares internacionales.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- Cinco Business Group 2014‑2016
    with st.expander("**May 2014 – Oct. 2016 | Cinco Business Group S.C. – Líder de Proyecto**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Coordinación de estudios cuantitativos y cualitativos a nivel nacional (clientes: Cinépolis, etc.).</li>
                <li>Diseño de cuestionarios, validación de bases y análisis estadístico.</li>
                <li>Coordinación de campo y capacitación de encuestadores.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- UNADM 2013
    with st.expander("**May 2013 – Dic. 2013 | UNADM – Consultor / Diseñador Instruccional**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Diseño instruccional para tres licenciaturas en línea.</li>
                <li>Consultoría en encuestas en línea con LimeSurvey.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- b@unam 2011‑2013
    with st.expander("**Abr. 2011 – Mar. 2013 | UNAM b@unam – Investigador y Analista Estadístico**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Análisis estadístico y generación de reportes para programas educativos.</li>
                <li>Diseño de instrumentos de evaluación y encuestas.</li>
                <li>Coordinación de servicio social y elaboración de infografías.</li>
                <li><strong>Logros:</strong> Publicaciones en revistas científicas; mejoras académicas implementadas.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- CAME 2011
    with st.expander("**Ene. 2011 – Abr. 2011 | CAME – Coordinador de Inteligencia de Mercados**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Diseño de investigaciones de mercado y análisis de datos en SPSS.</li>
                <li>Coordinación de equipos de campo y asesores telefónicos.</li>
                <li><strong>Logros:</strong> Modelos para emisarios bancarios e incentivos que incrementaron productividad.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- Esfera Social 2008‑2011
    with st.expander("**Mar. 2008 – Ene. 2011 | Esfera Social SC – Coordinador de Proyectos de Investigación**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Diseño y coordinación de estudios de consumo y comunicación publicitaria.</li>
                <li>Presentación de hallazgos a clientes nacionales e internacionales.</li>
                <li><strong>Logros:</strong> Plataformas publicitarias para Cheetos, Rexona Teens, Tix‑Tix (Pepsico).</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # --- Instituto de Investigación 2004‑2006
    with st.expander("**Feb. 2004 – Ene. 2006 | Instituto de Investigación en Psicología Clínica y Social – Investigador / Docente Auxiliar**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Asesoría estadística, análisis psicométrico y entrevistas clínicas.</li>
                <li>Participación en la validación y estandarización de la Prueba de Afectos de González Padilla.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Proyectos Independientes
    st.markdown('<p class="seccion">Proyectos Independientes</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>Encuesta Nacional de Percepción de Trabajo Infantil 2012 (OIT):</strong> coordinación completa del proyecto.</li>
            <li>Asesoría metodológica y estadística en más de 10 tesis de licenciatura, maestría y doctorado (2005‑presente).</li>
            <li>Desarrollo de apps educativas, videojuegos 2D en Godot y herramientas IA (RAG, LLMs, embeddings) para análisis documental.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Portafolio tecnológico (2022‑2025)
    st.markdown('<p class="seccion">Portafolio Tecnológico (2022–2025)</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Apps en Python (PyQt5/6, PySide6).</li>
            <li>Dashboards Streamlit: <a href="https://share.streamlit.io/user/raulcamaracarreon" target="_blank">Perfil Streamlit</a></li>
            <li>Curso LLM Engineering.</li>
            <li>Proyectos IA: chatbots, agente de ventas, RAG con FAISS.</li>
            <li>Sistema SIMEPP (<a href="https://pleen.simep.info" target="_blank">pleen.simep.info</a>).</li>
            <li>Relax Music (<a href="https://relax-music.onrender.com" target="_blank">Web app</a>).</li>
            <li>Juegos con Godot (Shooter 2D, RPG).</li>
            <li>Repositorios GitHub: <a href="https://github.com/raulcamaracarreon" target="_blank">raulcamaracarreon</a></li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Tecnologías y Herramientas
    st.markdown('<p class="seccion">Tecnologías y Herramientas</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>Lenguajes:</strong> Python, R, SQL, SPSS, Excel, Dart, JavaScript.</li>
            <li><strong>Visualización:</strong> Power BI, Tableau, Plotly, Matplotlib, Streamlit.</li>
            <li><strong>Frameworks / IDE:</strong> PySide6, Flask, Android Studio, Godot, Unreal Engine.</li>
            <li><strong>IA:</strong> OpenAI, Hugging Face, FAISS, embeddings.</li>
            <li><strong>Plataformas educativas:</strong> Moodle, LimeSurvey, SurveyMonkey.</li>
            <li><strong>Otras herramientas:</strong> Gephi, NodeXL, Illustrator, Hootsuite, Prezi, Infogram.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Idiomas y Distinciones
    st.markdown('<p class="seccion">Idiomas</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Inglés: Avanzado (90%)</p>', unsafe_allow_html=True)

    st.markdown('<p class="seccion">Distinciones</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Desarrollador del sistema SIMEP‑PLEEN para Mejoredu.</li>
            <li>Proyectos publicados en GitHub y desplegados en Streamlit y Render.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# English content
# ---------------------------

def contenido_english():
    st.markdown('<p class="titulo">Raúl Cámara Carreón</p>', unsafe_allow_html=True)
    st.write('*Updated June 2025*')

    # Contact information
    st.markdown(
        '<p class="texto">📧 raul.camara76@gmail.com &nbsp;&nbsp; 📞 +52 55 3287 4013 &nbsp;&nbsp; 🏠 Tlalpan, Mexico City</p>',
        unsafe_allow_html=True,
    )

    # Professional Profile
    st.markdown('<p class="subtitulo">Professional Profile</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="respuesta">Data‑analysis and digital‑solutions specialist with 18+ years of experience in market research, survey coordination, advanced statistics (SPSS, Python), interactive visualization (Streamlit, Power BI), and app development in Python (PySide6, Flask) and Flutter. Able to lead projects from methodological design to technological implementation. Hybrid technical‑analytical profile focused on innovation, efficiency, and clear communication of insights.</p>',
        unsafe_allow_html=True,
    )

    # Skills
    st.markdown('<p class="seccion">Skills</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="subtitulo">General Competencies</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <ul class="texto">
                <li>Analytical, strategic, and critical thinking.</li>
                <li>Design of evaluation instruments and surveys.</li>
                <li>Development of strategic indicators.</li>
                <li>Evaluation of educational public policies.</li>
                <li>Effective written and verbal communication.</li>
                <li>Leadership and coordination of multidisciplinary teams.</li>
                <li>Professional ethics and social awareness.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown('<p class="subtitulo">Technical Skills</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <ul class="texto">
                <li><strong>Coding:</strong> Python, R, SQL, Dart, basic JavaScript.</li>
                <li><strong>Python libs:</strong> pandas, NumPy, scikit‑learn, matplotlib, Plotly.</li>
                <li><strong>Frameworks / GUI:</strong> Streamlit, PySide6, PyQt, Flask, Android Studio, Flutter.</li>
                <li><strong>Data viz:</strong> Power BI, Tableau, Streamlit, Matplotlib.</li>
                <li><strong>Statistical analysis:</strong> SPSS, advanced Excel.</li>
                <li><strong>AI & NLP:</strong> OpenAI, Hugging Face, FAISS, embeddings.</li>
                <li><strong>Dev & version control:</strong> GitHub.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Education
    st.markdown('<p class="seccion">Education</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>Bachelor's Degree in Psychology</strong>, UNAM – Faculty of Psychology (1999–2004).<br>Professional license: 5586797 &nbsp; | &nbsp; GPA: 8.8/10</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Courses & Certifications
    st.markdown('<p class="seccion">Courses & Certifications</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Hootsuite Social Media Management Certified Professional.</li>
            <li>Social Network Analysis – University of Michigan (MOOC).</li>
            <li>Statistical analysis with SPSS – UNAM (40 h).</li>
            <li>LLM Engineering (Applied AI).</li>
            <li>Courses on Flutter app development and Python data analysis.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Work Experience
    st.markdown('<p class="seccion">Work Experience</p>', unsafe_allow_html=True)

    with st.expander("**Oct 2023 – May 2025 | MEJOREDU – Directorate for the Evaluation of the Improvement of Educational Public Policies**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Designed strategic indicators: <em>Infrastructure Improvement Index</em> and <em>Infrastructure Improvement Coefficient</em>.</li>
                <li>Performed advanced statistical analysis and report writing.</li>
                <li>Developed dashboards and digital solutions (Python, Streamlit, PySide6).</li>
                <li>Automated reporting and digital data capture with LimeSurvey.</li>
                <li><strong>Achievements:</strong> Reduced data‑collection costs and time; built interactive modules for PLEEN program.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Oct 2019 – Oct 2023 | MEJOREDU – Directorate of Teacher & Principal Evaluation**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Designed teacher‑function evaluation instruments.</li>
                <li>Conducted qualitative interviews and focus groups.</li>
                <li>Statistical analysis and database management.</li>
                <li>Built Streamlit dashboards for data presentation.</li>
                <li>Produced qualitative and quantitative reports.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Apr 2017 – Oct 2019 | INEE – National Institute for Educational Evaluation (Project Lead A)**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Adapted and compiled materials for international assessments (PISA).</li>
                <li>Integrated translations and psychometric adjustments.</li>
                <li>Trained and supervised open‑response coding teams.</li>
                <li>Ensured cross‑country comparability to international standards.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**May 2014 – Oct 2016 | Cinco Business Group – Project Lead**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Coordinated nationwide quantitative & qualitative studies (e.g., Cinépolis).</li>
                <li>Questionnaire design, data validation, statistical analysis.</li>
                <li>Fieldwork coordination and interviewer training.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**May 2013 – Dec 2013 | UNADM – Consultant / Instructional Designer**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Instructional design for three online bachelor's degrees.</li>
                <li>Survey consulting with LimeSurvey.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Apr 2011 – Mar 2013 | UNAM b@unam – Researcher & Statistical Analyst**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Statistical analysis and reporting for educational programs.</li>
                <li>Designed evaluation instruments and surveys.</li>
                <li>Coordinated social service teams and created infographics.</li>
                <li><strong>Achievements:</strong> Scientific publications and academic improvements implemented.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Jan 2011 – Apr 2011 | CAME – Market Intelligence Coordinator**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Designed market‑research studies and analyzed data in SPSS.</li>
                <li>Coordinated field teams and call‑center advisors.</li>
                <li><strong>Achievements:</strong> Developed models for banking emissaries and incentive studies boosting productivity.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Mar 2008 – Jan 2011 | Esfera Social SC – Research Project Coordinator**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Designed and coordinated consumer and advertising‑communication studies.</li>
                <li>Presented findings to national and international clients.</li>
                <li><strong>Achievements:</strong> Developed advertising platforms for brands such as Cheetos, Rexona Teens, and Sonric’s Tix‑Tix (Pepsico).</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("**Feb 2004 – Jan 2006 | Institute of Clinical & Social Psychology Research – Researcher / Teaching Assistant**", expanded=False):
        st.markdown(
            """
            <ul class="texto">
                <li>Statistical advice, psychometric analysis, and clinical interviews.</li>
                <li>Participated in validation and standardization of the González Padilla Affect Test.</li>
            </ul>
            """,
            unsafe_allow_html=True,
        )

    # Independent Projects
    st.markdown('<p class="seccion">Independent Projects</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>National Child Labor Perception Survey 2012 (ILO):</strong> full project coordination.</li>
            <li>Methodological & statistical advising on 10+ theses (2005‑present).</li>
            <li>Development of educational apps, 2D Godot games, and AI tools (RAG, LLMs, embeddings).</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Tech Portfolio
    st.markdown('<p class="seccion">Tech Portfolio (2022–2025)</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Python apps (PyQt, PySide6).</li>
            <li>Streamlit dashboards: <a href="https://share.streamlit.io/user/raulcamaracarreon" target="_blank">Streamlit Profile</a></li>
            <li>LLM Engineering course.</li>
            <li>AI projects: chatbots, sales agent, FAISS‑based RAG.</li>
            <li>SIMEPP monitoring system: <a href="https://pleen.simep.info" target="_blank">pleen.simep.info</a></li>
            <li>Relax Music web app: <a href="https://relax-music.onrender.com" target="_blank">relax-music</a></li>
            <li>Godot games (2D Shooter, RPG).</li>
            <li>GitHub repos: <a href="https://github.com/raulcamaracarreon" target="_blank">raulcamaracarreon</a></li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Tech & Tools
    st.markdown('<p class="seccion">Technologies & Tools</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li><strong>Languages:</strong> Python, R, SQL, SPSS, Excel, Dart, JavaScript.</li>
            <li><strong>Visualization:</strong> Power BI, Tableau, Plotly, Matplotlib, Streamlit.</li>
            <li><strong>Frameworks / IDE:</strong> PySide6, Flask, Android Studio, Godot, Unreal Engine.</li>
            <li><strong>AI:</strong> OpenAI, Hugging Face, FAISS, embeddings.</li>
            <li><strong>Educational platforms:</strong> Moodle, LimeSurvey, SurveyMonkey.</li>
            <li><strong>Other tools:</strong> Gephi, NodeXL, Illustrator, Hootsuite, Prezi, Infogram.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Languages & Honors
    st.markdown('<p class="seccion">Languages</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto">English: Advanced (≈ C1, 90%)</p>', unsafe_allow_html=True)

    st.markdown('<p class="seccion">Distinctions</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <ul class="texto">
            <li>Developer of the SIMEP‑PLEEN interactive analysis system for Mejoredu.</li>
            <li>Projects published on GitHub and deployed via Streamlit and Render.</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# Render según idioma
# ---------------------------
if language == "Español":
    contenido_espanol()
else:
    contenido_english()

# ---------------------------
# Botón de descarga de CV en PDF
# ---------------------------
cv_file = "Raul_Camara_CV_EN.pdf" if language == "English" else "Raul_Camara_CV_ES.pdf"
label = "📄 Download CV (PDF)" if language == "English" else "📄 Descargar CV (PDF)"

try:
    with open(cv_file, "rb") as file:
        st.download_button(label=label, data=file, file_name=cv_file, mime="application/pdf")
except FileNotFoundError:
    st.warning("PDF file not found." if language == "English" else "El archivo PDF no ha sido encontrado.")

