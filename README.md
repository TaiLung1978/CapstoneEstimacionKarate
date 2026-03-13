# 🥋 Sistema de Apoyo a la Planificación Logística - Karate-Do

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Sistema inteligente de apoyo a la toma de decisiones basado en modelos predictivos de Inteligencia Artificial para la optimización de la planificación logística en eventos deportivos de Karate-Do**

[🚀 Demo en Vivo](#instalación) | [📊 Resultados](#resultados) | [📖 Documentación](#metodología)

</div>

---

## 📋 Descripción del Proyecto

Este sistema utiliza **Machine Learning** para predecir con alta precisión la duración de categorías en torneos de Karate-Do, resolviendo el problema de retrasos acumulados (20-35%) que afectan a organizadores, atletas y familias.

### 🎯 Problema Identificado

- **Retrasos históricos:** 2-4 horas por torneo
- **Impacto:** 680+ participantes anuales afectados
- **Causa raíz:** Estimaciones empíricas sin sustento estadístico

### 💡 Solución Desarrollada

Sistema de Apoyo a la Toma de Decisiones (DSS) basado en:
- **Modelo:** Random Forest Regressor
- **Datos:** 744 registros históricos (2023-2025)
- **Metodología:** CRISP-ML(Q)
- **Interfaz:** Streamlit Low-Code

---

## 🏆 Resultados Clave

| Métrica | Valor Obtenido | Objetivo | Estado |
|---------|----------------|----------|--------|
| **Error Absoluto Medio (MAE)** | 31.85 seg | < 15% | ✅ **7.19%** |
| **Coeficiente R²** | 0.9777 | > 0.85 | ✅ **97.77%** |
| **RMSE** | 67.08 seg | - | ✅ Bajo |
| **Validación Cruzada** | 34.65 ± 5.50 seg | Estable | ✅ Consistente |

### 📊 Comparativa con Baseline
```
Regresión Lineal (Baseline):  MAE = 108.39 seg | R² = 0.89
Random Forest (Propuesto):    MAE = 31.85 seg  | R² = 0.9777
Mejora:                       ↓ 70.6%          | ↑ 9.8%
```

### 💰 Impacto Operativo

- **Reducción de retrasos:** 85% (de 2-4h a 25-30 min)
- **Ahorro estimado:** 3 horas de sobrecosto de alquiler por torneo
- **Mejora en satisfacción:** 95% de confiabilidad en horarios comunicados

---

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Python 3.11+
- pip (gestor de paquetes)

### Pasos de Instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/TaiLung1978/CapstoneEstimacionKarate.git
cd CapstoneEstimacionKarate

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

---

## 📊 Metodología

### CRISP-ML(Q) - Proceso Iterativo
```
┌─────────────────────┐
│ 1. Comprensión      │ → Análisis del problema de retrasos
│    del Negocio      │   (Diagrama de Ishikawa)
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ 2. Comprensión      │ → EDA: 744 registros, sesgo positivo
│    de los Datos     │   (skewness = 2.43)
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ 3. Preparación      │ → Limpieza (IQR), One-Hot Encoding,
│    de Datos         │   Split 70/30
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ 4. Modelado         │ → Random Forest (n=100, max_depth=15)
│                     │   XGBoost, Regresión Lineal
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ 5. Evaluación       │ → Validación Cruzada 5-Fold
│                     │   LIME para explicabilidad
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ 6. Despliegue       │ → Interfaz Streamlit + joblib
│                     │   Documentación técnica
└─────────────────────┘
```

### Variables Predictoras Clave

| Variable | Importancia | Descripción |
|----------|-------------|-------------|
| `num_competidores` | 44.96% | Cantidad de atletas en la categoría |
| `num_combates` | 44.72% | Número de enfrentamientos |
| `edad_max` | 9.94% | Edad máxima de la categoría |
| Otras | <1% | Modalidad, sexo, nivel técnico |

**Insight:** Solo 2 variables explican el **90%** de la variabilidad temporal.

---

## 🖼️ Capturas de Pantalla

### Interfaz Principal
![Interfaz](https://via.placeholder.com/800x400?text=Agregar+screenshot+de+app.py)

### Predicción con Recomendaciones
![Predicción](https://via.placeholder.com/800x400?text=Agregar+screenshot+de+predicción)

### Feature Importance
![Features](feature_importance.png)

### Comparación de Modelos
![Comparación](comparacion_modelos_cv.png)

---

## 📁 Estructura del Proyecto
```
CapstoneEstimacionKarate/
│
├── 📊 Visualizaciones
│   ├── analisis_exploratorio.png      # EDA inicial
│   ├── comparacion_modelos_cv.png     # Validación cruzada
│   └── feature_importance.png         # Variables influyentes
│
├── 🤖 Modelo Entrenado
│   ├── modelo_random_forest_unsu.pkl  # Modelo serializado
│   └── columnas_entrenamiento.pkl     # Configuración de features
│
├── 📓 Notebooks
│   └── PrediccionKarate.ipynb         # Pipeline completo ML
│
├── 🐍 Aplicación
│   └── app.py                         # Interfaz Streamlit
│
├── 📁 Datos
│   └── dataset_karate.csv             # 744 registros históricos
│
├── 🌐 Explicabilidad
│   └── lime_explicacion.html          # Análisis LIME interactivo
│
└── 📄 Documentación
    ├── README.md                      # Este archivo
    ├── requirements.txt               # Dependencias Python
    └── LICENSE                        # MIT License
```

---

## 🔬 Tecnologías Utilizadas

### Machine Learning
- **Scikit-Learn 1.4.0:** Random Forest, métricas, validación cruzada
- **XGBoost:** Modelo comparativo de ensamble
- **LIME:** Explicabilidad de predicciones individuales

### Desarrollo de Aplicación
- **Streamlit 1.30.0:** Framework low-code para UI
- **Pandas 2.1.4:** Manipulación de datos
- **NumPy 1.26.3:** Operaciones numéricas

### Visualización
- **Matplotlib 3.8.2:** Gráficos estáticos
- **Seaborn:** Visualizaciones estadísticas

### Serialización
- **Joblib:** Persistencia de modelos entrenados

---

## 📖 Uso de la Aplicación

### Caso de Uso: Predicción de Categoría

1. **Seleccionar parámetros:**
   - Modalidad: KUMITE / KATA / PARA-KARATE
   - Nivel: PRINCIPIANTES / NOVATOS / AVANZADOS / EXPERTOS
   - Sexo: MASCULINO / FEMENINO
   - Edad Máxima: 4-18 años
   - Número de Competidores: 2-50

2. **Generar predicción:**
   - Click en "🚀 Generar Predicción"

3. **Interpretar resultados:**
   - Duración estimada (min:seg)
   - Confianza del modelo (97.77%)
   - Margen de error (±31.85 seg)
   - Recomendaciones logísticas automáticas

### Ejemplo Real

**Input:**
```
Modalidad: KUMITE
Nivel: EXPERTOS
Sexo: MASCULINO
Edad Máxima: 18
Competidores: 12
Combates: 11
```

**Output:**
```
⏱️ Duración Estimada: 18 min 23 seg
📊 Confianza: 97.77%
📉 Margen de Error: ± 31 seg

📋 Recomendaciones:
✅ Citar atletas 3 minutos antes
✅ Reservar 28 minutos de buffer
✅ Asignar 2 árbitros por tatami
```

---

## 🧪 Validación del Modelo

### Protocolo de Testing
```python
# Validación Cruzada Estratificada
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(
    modelo, X_train, y_train,
    cv=5,
    scoring='neg_mean_absolute_error'
)

print(f"MAE CV: {-cv_scores.mean():.2f} ± {cv_scores.std():.2f}")
# Output: MAE CV: 34.65 ± 5.50 seg
```

### Métricas por Modalidad

| Modalidad | MAE (seg) | R² | N° Registros |
|-----------|-----------|----|--------------| 
| KUMITE | 35.2 | 0.976 | 504 |
| KATA | 28.1 | 0.981 | 192 |
| PARA-KARATE | 22.7 | 0.985 | 48 |

---

## 🔮 Trabajo Futuro

### Mejoras Técnicas Planificadas

- [ ] **Integración en tiempo real:** API REST para actualización de inscripciones
- [ ] **Multi-tatami optimization:** Algoritmo de asignación óptima de categorías
- [ ] **Deep Learning:** Explorar LSTM para secuencias temporales
- [ ] **Dashboard analítico:** Monitoreo en vivo del progreso del torneo

### Escalabilidad

- [ ] **Generalización:** Validar en otros clubes/federaciones
- [ ] **Multideporte:** Extender a Judo, Taekwondo, Boxeo
- [ ] **Cloud deployment:** Migrar a AWS/Azure/GCP
- [ ] **Mobile app:** Versión nativa iOS/Android

---

## 👥 Autores

**Carla Stephanya López Arboleda**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/tu-perfil)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:tu-email@ejemplo.com)

**Daniela Stephania Martínez Porte**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/tu-perfil)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail)](mailto:tu-email@ejemplo.com)

### Asesor Académico
**Víctor Gómez Regalado**  
Universidad de Las Américas - Maestría en Inteligencia Artificial Aplicada

---

## 🏫 Institución

**Universidad de Las Américas (UDLA)**  
Facultad de Ingeniería y Ciencias Aplicadas  
Maestría en Inteligencia Artificial Aplicada  
Quito, Ecuador | 2026

---

## 🙏 Agradecimientos

- **Club de Karate-Do UNSU:** Por proporcionar datos históricos reales
- **RootCorp Cia. Ltda.:** Soporte técnico y validación del prototipo
- **Comunidad Open Source:** Scikit-Learn, Streamlit, LIME

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Contacto

**¿Preguntas o colaboraciones?**

- 📧 Email: [tu-email@udla.edu.ec](mailto:tu-email@udla.edu.ec)
- 🐛 Issues: [GitHub Issues](https://github.com/TaiLung1978/CapstoneEstimacionKarate/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/TaiLung1978/CapstoneEstimacionKarate/discussions)

---

<div align="center">

**⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub ⭐**

[![GitHub stars](https://img.shields.io/github/stars/TaiLung1978/CapstoneEstimacionKarate?style=social)](https://github.com/TaiLung1978/CapstoneEstimacionKarate)

</div>