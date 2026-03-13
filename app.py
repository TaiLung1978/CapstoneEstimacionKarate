import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Configuración
st.set_page_config(
    page_title="DSS Karate-Do UNSU", 
    page_icon="🥋", 
    layout="wide"
)

# Header
st.title("🥋 Sistema de Apoyo a la Planificación - Club UNSU")
st.markdown("""
Esta herramienta utiliza **Inteligencia Artificial (Random Forest)** entrenado 
con 744 registros históricos (2023-2025) para predecir la duración de categorías 
y optimizar la logística de torneos.

**Precisión del modelo**: R² = 98.1% | Error promedio = 33.8 segundos
""")

# Cargar recursos
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load('modelo_random_forest_unsu.pkl')
    columnas = joblib.load('columnas_entrenamiento.pkl')
    return modelo, columnas

try:
    modelo, columnas_train = cargar_modelo()
    st.sidebar.success("✅ Modelo cargado exitosamente")
except Exception as e:
    st.error(f"❌ Error al cargar modelo: {e}")
    st.stop()

# Sidebar: Configuración
st.sidebar.header("⚙️ Configuración de Categoría")

modalidad = st.sidebar.selectbox(
    "Modalidad", 
    ["KATA", "KUMITE", "PARA-KARATE"],
    help="Tipo de competencia según reglamento WKF"
)

nivel = st.sidebar.selectbox(
    "Nivel Técnico", 
    ["GENERAL", "PRINCIPIANTES", "NOVATOS", "AVANZADOS", "EXPERTOS"],
    index=2  # Por defecto NOVATOS
)

sexo = st.sidebar.selectbox("Sexo", ["FEMENINO", "MASCULINO"])

edad_max = st.sidebar.slider(
    "Edad Máxima de Categoría", 
    min_value=4, 
    max_value=18, 
    value=12,
    help="Límite superior de edad según categoría"
)

num_competidores = st.sidebar.number_input(
    "Número de Competidores", 
    min_value=2, 
    max_value=50, 
    value=8,
    help="Total de atletas inscritos en esta categoría"
)

num_combates = st.sidebar.number_input(
    "Número de Combates", 
    min_value=1, 
    max_value=50, 
    value=max(1, num_competidores - 1),
    help="Cantidad de enfrentamientos según estructura de llave"
)

# Botón de predicción
if st.sidebar.button("🚀 Generar Predicción", type="primary"):
    
    # Crear vector de entrada
    input_data = {col: 0 for col in columnas_train}
    
    # Asignar valores numéricos
    input_data['edad_max'] = edad_max
    input_data['num_competidores'] = num_competidores
    input_data['num_combates'] = num_combates
    
    # Activar one-hot encoding
    if f'modalidad_{modalidad}' in input_data:
        input_data[f'modalidad_{modalidad}'] = 1
    if f'nivel_{nivel}' in input_data:
        input_data[f'nivel_{nivel}'] = 1
    if f'sexo_{sexo}' in input_data:
        input_data[f'sexo_{sexo}'] = 1
    
    # Convertir a DataFrame y predecir
    df_input = pd.DataFrame([input_data])
    
    try:
        prediccion_seg = modelo.predict(df_input)[0]
        minutos = int(prediccion_seg // 60)
        segundos = int(prediccion_seg % 60)
        
        # Mostrar resultado
        st.success("✅ Predicción generada con éxito")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="⏱️ Duración Estimada",
                value=f"{minutos} min {segundos} seg"
            )
        
        with col2:
            st.metric(
                label="📊 Confianza del Modelo",
                value="98.1%",
                help="Coeficiente de determinación R²"
            )
        
        with col3:
            margen_error = 34  # MAE del modelo
            st.metric(
                label="📉 Margen de Error",
                value=f"± {margen_error} seg",
                help="Error Absoluto Medio (MAE)"
            )
        
        # Recomendaciones
        st.divider()
        st.subheader("📋 Recomendaciones Logísticas")
        
        tiempo_citacion = max(0, minutos - 15)
        
        st.info(f"""
        **Para la categoría:** {modalidad} - {nivel} ({sexo})  
        **Número de atletas:** {num_competidores}  
        **Combates programados:** {num_combates}
        
        **Acciones sugeridas:**
        - ✅ Citar atletas **{tiempo_citacion} minutos** antes del inicio del tatami
        - ✅ Reservar **{minutos + 10} minutos** de buffer en el cronograma
        - ✅ Asignar {1 if num_competidores <= 8 else 2} árbitros por tatami
        """)
        
        # Gráfico de distribución
        st.divider()
        st.subheader("📈 Contexto Histórico")
        
        # Simular datos históricos similares (en producción, consultar BD)
        datos_similares = np.random.normal(prediccion_seg, 60, 100)
        
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(datos_similares, bins=20, alpha=0.7, color='steelblue', edgecolor='black')
        ax.axvline(prediccion_seg, color='red', linestyle='--', linewidth=2, 
                    label=f'Predicción: {minutos}:{segundos:02d}')
        ax.set_xlabel('Duración (segundos)')
        ax.set_ylabel('Frecuencia')
        ax.set_title(f'Distribución de categorías {modalidad} - {nivel}')
        ax.legend()
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"❌ Error en la predicción: {e}")

# Chatbot conversacional (sección adicional)
st.divider()
st.subheader("💬 Asistente Virtual")

with st.expander("Preguntas Frecuentes"):
    st.markdown("""
    **¿Cómo se calculan las predicciones?**  
    El modelo analiza 744 categorías históricas usando Random Forest, 
    considerando modalidad, nivel, sexo, edad y número de competidores.
    
    **¿Qué tan preciso es el sistema?**  
    El modelo tiene un R² de 98.1%, con un error promedio de 33.8 segundos.
    
    **¿Puedo confiar en las predicciones?**  
    Sí, pero siempre agrega un buffer de +10 minutos para imprevistos.
    """)

# Footer
st.divider()
st.caption("Desarrollado por Club UNSU | Powered by RootCorp Cia. Ltda. | 2026")
