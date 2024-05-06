"""
"""

# Importar librerías
# - streamlit para la interfaz gráfica
import streamlit as st
from budget_manager import calcular_presupuesto
from visualization import plot_budget


def main():
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
            porcentaje_necesidades = st.slider('Porcentaje de gastos esenciales',
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

        if submit_button:

            necesidades, deseos, ahorro = calcular_presupuesto(ingresos,
                                                            gastos_esenciales)

            st.write('Necesidades: ${:,.0f}'.format(necesidades))
            st.write('Deseos: ${:,.0f}'.format(deseos))
            st.write('Ahorro: ${:,.0f}'.format(ahorro))

            plot_budget(necesidades, deseos, ahorro)
                                                     
if __name__ == "__main__":
    main()
