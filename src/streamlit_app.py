import streamlit as st


st.set_page_config(page_title="Acceso a Hospitales Públicos en Perú", layout="wide")

tab1, tab2, tab3 = st.tabs(["📂 Descripción de Datos", "🗺️ Mapas Estáticos", "🌐 Mapas Dinámicos"])

with tab1:

        st.markdown(
        """
- **Unidad de análisis**: Hospitales públicos en operación en Perú.  
- **Fuentes**: MINSA – IPRESS (subset operativo), Centros Poblados.  
- **Reglas**: Solo establecimientos operativos con coordenadas válidas.  
        """
        )
        col1, col2 = st.columns([1, 2])
        st.write("---")

        with col1:
                st.markdown("### Resumen")
                st.markdown(
            """
Este análisis utiliza los hospitales en funcionamiento registrados en la base del MINSA.  
El objetivo es estudiar su distribución espacial a nivel nacional y departamental,  
así como su proximidad a centros poblados en **Lima** y **Loreto**.
Los principales hallazgos son:

- **Desigualdad territorial:** Cajamarca y Lima concentran más de 1,600 hospitales en conjunto, mientras que departamentos como Tumbes, Moquegua y Madre de Dios tienen menos de 70 cada uno.  
- **Vacíos críticos:** se identificaron **62 distritos sin ningún hospital**, lo que refleja brechas graves en acceso a salud.  
- **Concentración urbana (Lima):** zonas céntricas como *Barrio Obrero Industrial* tienen una densidad extrema (265 hospitales en 10 km), mientras que áreas rurales como *Yanapampa* carecen totalmente de servicios.  
- **Dispersión amazónica (Loreto):** aunque existen focos de acceso (ej. *Tres de Octubre* con 29 hospitales en 10 km), la mayoría de centros poblados enfrenta dificultades debido a la geografía y aislamiento.  

            """
        )

# Columna derecha: imagen descriptiva (ejemplo: hospitales por departamento)
        with col2:
                st.markdown("### Gráfico de referencia")
                st.image("./assets/hospitals_per_departament.png", caption="Número de hospitales por departamento")


with tab2:
    st.markdown("## 🗺️ Mapas Estáticos y Análisis por Departamento")

    st.markdown(
        """
En esta sección se presentan los **mapas estáticos** elaborados con **GeoPandas**,
así como un análisis exploratorio de la distribución de hospitales a nivel departamental.
        """
    )

    # Mapa nacional: hospitales por departamento
    st.image("./assets/hospitals_per_departament_map.png", caption="Mapa de hospitales por departamento")

    st.write("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # Tabla resumen 
        st.markdown("### 📋 Resumen por Departamento")
        st.image("./assets/hospitals_per_departament.png", caption="Hospitales por Departamento")

    with col2:
        # Otro gráfico estático: hospitales por distrito
        st.markdown("### 📊 Hospitales por Distrito")
        st.image("./assets/hospitals_per_district.png", caption="Distribución de hospitales por distrito")

    with col3:
        # Otro gráfico estático: hospitales por distrito
        st.markdown("### 🥇 Distrito con más hospitales")
        st.image("./assets/hospitals_top_10_.png", caption="Distribución de hospitales por distrito")
    with col4:
        # Otro gráfico estático: hospitales por distrito
        st.markdown("### 🚫 Distrito con ningún hospital")
        st.image("./assets/hospitals_zero.png", caption="Distribución de hospitales por distrito")

from pathlib import Path

with tab3:
    st.markdown("## 🌐 Mapas Dinámicos")
    st.markdown(
        """
En esta sección se incrustan mapas **Folium** ya generados:
- **Coropleta nacional** (hospitales por distrito).
- **Proximidad (10 km)** para **Lima** y **Loreto**:  
  círculo **rojo** = menos hospitales cercanos, círculo **verde** = más hospitales cercanos.
        """
    )

    # Altura configurable de los iframes
    altura = st.slider("Altura de los mapas (px)", 400, 900, 600, 50)

    def mostrar_html(path_str, titulo):
        path = Path(path_str)
        st.markdown(f"### {titulo}")
        if path.exists():
            html = path.read_text(encoding="utf-8")
            st.components.v1.html(html, height=altura, scrolling=True)
        else:
            st.warning(f"No se encontró `{path.name}` en la raíz del proyecto.")

    # 1) Coropleta nacional
    mostrar_html("Coropleta_Distrital.html", "Coropleta Nacional (Hospitales por Distrito)")

    st.write("---")

    # 2) Proximidad: Lima & Loreto
    c1, c2 = st.columns(2)

    with c1:
        mostrar_html("Lima_min.html", "Lima — Menos hospitales (radio 10 km)")
        mostrar_html("Lima_max.html", "Lima — Más hospitales (radio 10 km)")

    with c2:
        mostrar_html("Loreto_min.html", "Loreto — Menos hospitales (radio 10 km)")
        mostrar_html("Loreto_max.html", "Loreto — Más hospitales (radio 10 km)")
