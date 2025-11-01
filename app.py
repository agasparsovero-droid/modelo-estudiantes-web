import streamlit as st
import pandas as pd

st.set_page_config(page_title="Modelo Estudiantes Web", page_icon="🎓", layout="centered")

st.title("🎓 Promedio de Notas de Estudiantes")
st.write("Esta aplicación muestra los datos y el promedio calculado desde Google Colab.")

# Cargar datos desde el CSV del repositorio
df = pd.read_csv("predicciones.csv")

# Mostrar la tabla de datos
st.subheader("📋 Datos de Predicciones")
st.dataframe(df)

# Calcular promedio (ajusta el nombre de la columna de notas)
columna_nota = "nota_final"  # 🔁 cambia esto si tu columna tiene otro nombre

if columna_nota in df.columns:
    promedio_general = df[columna_nota].mean()
    st.metric(label="Promedio General de Notas", value=f"{promedio_general:.2f}")
else:
    st.warning(f"No se encontró la columna '{columna_nota}' en el archivo CSV.")

st.markdown("---")
st.caption("📅 Página generada automáticamente desde Google Colab y Streamlit")
