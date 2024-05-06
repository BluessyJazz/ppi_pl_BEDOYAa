"""
Este script contiene la interfaz gráfica de usuario para el cálculo del
presupuesto 50-30-20. 

El usuario debe ingresar sus ingresos mensuales y seleccionar el método de
presupuesto a utilizar. El programa calculará cuánto dinero debe destinar a
cada categoría de su presupuesto mensual y mostrará el resultado en la
interfaz gráfica.
"""

# Importar librerías
# - streamlit para la interfaz gráfica
# - calcular_presupuesto para calcular el presupuesto
# - plot_budget para visualizar el presupuesto
import streamlit as st
from budget_manager import calcular_presupuesto
from visualization import plot_budget

# Configurar la página
st.set_page_config(page_title='Presupuesto 50-30-20',
                   page_icon='💰',
                   layout='centered',
                   initial_sidebar_state='auto'
                   )


def main():
    """
    Función principal para la interfaz gráfica de usuario

    Args:
        None

    Returns:
        None
    """
    st.title('Presupuesto 50-30-20')
    st.write('Este programa te ayudará a calcular cuánto dinero debes \
             destinar a cada categoría de tu presupuesto mensual')

    with st.form(key='my_form'):
        ingresos = st.number_input('Ingresos mensuales',
                                   min_value=0.0,
                                   help='Ingresos mensuales netos',
                                   format='%f',
                                   step=1000.0
                                   )
        metodo_presupuesto = st.selectbox('Método de presupuesto',
                                          ['50-30-20',
                                           '70-20-10',
                                           'Personalizado'])
        if metodo_presupuesto == 'Personalizado':
            porcentaje_necesidades = st.slider('Porcentaje de gastos \
                                                esenciales',
                                               min_value=50,
                                               max_value=100,
                                               value=50)

        submit_button = st.form_submit_button(label='Calcular presupuesto')

        # Calcular presupuesto
        if metodo_presupuesto == '50-30-20':
            gastos_esenciales = 50
        elif metodo_presupuesto == '70-20-10':
            gastos_esenciales = 70
        elif metodo_presupuesto == 'Personalizado':
            gastos_esenciales = porcentaje_necesidades

        if submit_button and ingresos > 0:

            necesidades, deseos, ahorro = \
                calcular_presupuesto(ingresos, gastos_esenciales)

            st.write(f'Gastos necesarios: ${necesidades:,.0f}')
            st.write(f'Gastos prescindibles: ${deseos:,.0f}')
            st.write(f'Ahorro: ${ahorro:,.0f}')

            plot_budget(necesidades, deseos, ahorro)

        elif submit_button and ingresos == 0:
            st.warning('Ingresa un valor válido para los ingresos')


if __name__ == "__main__":
    main()
