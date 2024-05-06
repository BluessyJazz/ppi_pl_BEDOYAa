import streamlit as st
import matplotlib.pyplot as plt

def plot_budget(necesidades, deseos, ahorros):
    plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico (ancho, alto) en pulgadas
    labels = ['Necesidades', 'Deseos', 'Ahorros']
    sizes = [necesidades, deseos, ahorros]
    total = sum(sizes)  # Total para calcular porcentajes
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # Resalta la primera porción (Necesidades)

    # Función para formatear las etiquetas con porcentajes y valores con separadores de miles
    def make_autopct(values):
        def my_autopct(pct):
            val = int(round(pct*total/100.0))
            return '{p:.1f}%  (${v:,.0f})'.format(p=pct, v=val)
        return my_autopct

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=make_autopct(sizes), shadow=True, startangle=90)
    plt.axis('equal')  # Asegura que el gráfico de pie sea dibujado como un círculo.
    plt.title('Distribución del Presupuesto', fontsize=16)  # Añade un título al gráfico
    st.pyplot(plt)