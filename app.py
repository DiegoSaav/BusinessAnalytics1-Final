import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import figure
from PIL import Image 


######################## CONFIGURACIÓN DE LA CONFIGURACIÓN DE LA PÁGINA EN MODO ANCHO Y ADICIÓN DE UN TÍTULO Y FAVICON#############################################
st.set_page_config(
    layout="wide", 
    page_title="Conectividad y Conflicto armado en Colombia ", 
    page_icon=":bar_chart:",
    initial_sidebar_state = 'collapsed'
    )

################################################################################CARGAR DATOS#####################################################################
@st.cache
def load_data1():
    data = pd.read_csv(
        "rural_urbana.csv"
        )
    return data

@st.cache
def load_data2():
    data = pd.read_csv(
        "conflicto.csv"
    )
    return data

df = load_data1() 
co = load_data2()

##############################################################TITULOS Y TEXTOS INTRODUCTORIOS####################################################

c1, c2 = st.columns(2) # Dividir el ancho en 2 columnas de igual tamaño

with c1:
    c1.title('\U0001f50e Análisis exploratorio de la conectividad y las víctimas del conflicto armado en Colombia')

with c2:
    c2.markdown("""

    El acceso a internet se ha vuelto esencial, pues le ha abierto camino a nuevas formas de crear conocimiento y de relacionarse, 
    en países como el nuestro, que estamos en una transición a una cultura más digital, lo que nos lleva a múltiples cambios en todas las 
    esferas sociales, además de ser un país golpeado fuertemente por la violencia. 

    Por esta razón se desea analizar las diferencias que hay en las zonas rurales y urbanas en colombia con respecto a la violencia 
    (conflicto armado) y si este problema tiene influencia sobre la tendencia del internet.

        """)

st.write('')
st.write('')
st.write('')
##########################################################################FILA############################################################

total = 250770

#Imagen
img = Image.open("bandera.png")
st.image(img, width=None)


text = 'Víctimas del conflicto armado en Colombia'
st.markdown(f"<h2 style='text-align: center; color:white;'>{text}</h2>", unsafe_allow_html=True)

number = total
st.markdown(f"<h1 style='text-align: center; color:red;'>{number}</h1>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')

##########################################################################SUMMARY############################################################


c1, c2, c3 = st.columns(3)


with c1:
    text = 'Víctimas x modalidad más violenta'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h5>", unsafe_allow_html=True)

    number = 37125
    st.markdown(f"<h1 style='text-align: center; color:red;'>{number}</h1>", unsafe_allow_html=True)

    porc = round((number / total)*100 ,1)
    st.markdown(f"<h6 style='text-align: center; color:white;'>({porc}%)</h6>", unsafe_allow_html=True)

    text = 'Retención/Ejecución'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h4>", unsafe_allow_html=True)

    #Imagen 
    img = Image.open("1.png") 
    st.image(img, width=None)


with c2:
    text = 'Víctimas x presunto más violento'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h5>", unsafe_allow_html=True)

    number = 32179
    st.markdown(f"<h1 style='text-align: center; color:red;'>{number}</h1>", unsafe_allow_html=True)

    porc = round((number / total)*100 ,1)
    st.markdown(f"<h6 style='text-align: center; color:white;'>({porc}%)</h6>", unsafe_allow_html=True)

    text = 'Autodefensas unidas de Colombia (AUC)'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h4>", unsafe_allow_html=True)

    #Imagen
    img = Image.open("2.png") 
    st.image(img, width=None)

with c3:
    text = 'Víctimas x dpto. más violento'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h5>", unsafe_allow_html=True)

    number = 71899
    st.markdown(f"<h1 style='text-align: center; color:red;'>{number}</h1>", unsafe_allow_html=True)

    porc = round((number / total)*100 ,1)
    st.markdown(f"<h6 style='text-align: center; color:white;'>({porc}%)</h6>", unsafe_allow_html=True)

    text = 'Antioquia'
    st.markdown(f"<h5 style='text-align: center; color:white;'>{text}</h4>", unsafe_allow_html=True)

    #Imagen
    img = Image.open("3.jpg") 
    st.image(img, width=None)





#########################################################GRAFICAS DE CONFLICTO ARMADO####################################################################################

########################################################################FILA 1 ############################################################################
st.write('')
st.write('')
st.write('')


c1, c2 = st.columns(2)

with c1:
    c1.markdown("<h3 style='text-align: center; color: white;'> EVOLUCIÓN ANUAL DE LAS VÍCTIMAS DEL CONFLICTO ARMADO EN COLOMBIA </h3>", unsafe_allow_html=True)

    #Base de datos para la gráfica
    base = co.groupby('año')  [['Total de Víctimas del Caso']].sum().sort_values(by='año', ascending=False).reset_index()

    #Creación de gráfica
    fig = px.line(base, 
            x='año', 
            y = 'Total de Víctimas del Caso',
            width=600, height=600)

    #Detalles
    fig.update_layout(
        xaxis_title = 'AÑOS',
        yaxis_title = 'VÍCTIMAS',
        template = 'simple_white',
        title_x = 0.5)

    c1.write(fig)

with c2:

    c2.markdown("<h3 style='text-align: center; color: white;'> EVOLUCIÓN ANUAL DE LAS VÍCTIMAS POR DEPARTAMENTO </h3>", unsafe_allow_html=True)


    #Agrupamos por categoria
    an = co[co['DEPARTAMENTO'] == 'ANTIOQUIA'].groupby(['año']) [['Total de Víctimas del Caso']].sum().reset_index().rename(columns = {'Total de Víctimas del Caso':'ANTIOQUIA'}) 
    ce = co[co['DEPARTAMENTO'] == 'CESAR'].groupby(['año']) [['Total de Víctimas del Caso']].sum().reset_index().rename(columns = {'Total de Víctimas del Caso':'CESAR'}) 
    sa = co[co['DEPARTAMENTO'] == 'SANTANDER'].groupby(['año']) [['Total de Víctimas del Caso']].sum().reset_index().rename(columns = {'Total de Víctimas del Caso':'SANTANDER'}) 
    va = co[co['DEPARTAMENTO'] == 'VALLE DEL CAUCA'].groupby(['año']) [['Total de Víctimas del Caso']].sum().reset_index().rename(columns = {'Total de Víctimas del Caso':'VALLE DEL CAUCA'}) 
    me = co[co['DEPARTAMENTO'] == 'META'].groupby(['año']) [['Total de Víctimas del Caso']].sum().reset_index().rename(columns = {'Total de Víctimas del Caso':'META'}) 



    #Unimos las bases y los NAN se reemplazan por 0
    base = pd.merge(an, ce, how = 'outer', on = 'año').merge(sa, how = 'outer', on = 'año'
                                                    ).merge(va, how = 'outer', on = 'año'
                                                    ).merge(me, how = 'outer', on = 'año').fillna(0)

    # definir gráfica
    fig = px.line(base, 
                    x='año', 
                    y=['ANTIOQUIA', 'CESAR', 'SANTANDER', 'VALLE DEL CAUCA','META'],
                    width=650, height=600)

    # agregar detalles
    fig.update_layout(
        xaxis_title = 'AÑOS',
        yaxis_title = 'VICTIMAS',
        template = 'simple_white',
        title_x = 0.5,
        legend_title = 'Víctimas según barrio:')

    c2.write(fig)



############################################################################FILA 2####################################################################
st.markdown(f"<h2 style='text-align: center; color:white;'>{'TOP 5 EN CADA AÑO'}</h2>", unsafe_allow_html=True)


###########Creacion de filtro con slider
year = st.slider('Año en el que se presentó el suceso', 1958, 2022) # Crear variable que me almacene el año seleccionado
df2 = co[co['año']==year] #Año que se selecciona con el slider



c1, c2, c3 = st.columns(3)


with c1:
    # crear dataset
    base = df2.groupby(['Modalidad'])[['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending = False)[1:].head(5)

    fig = px.bar(base, 
                x='Total de Víctimas del Caso', 
                y='Modalidad', 
                color = 'Modalidad', 
                title ='<b>TOP 5 MODALIDADES <b>',
                width=380,  height=480, 
                orientation='h')

    # agregar detalles a la gráfica
    fig.update_layout(
        xaxis_title = '',
        yaxis_title = '',
        template = 'simple_white',
        title_x = 0.5,
        showlegend=False,
        legend_xanchor='right')

    c1.write(fig)

with c2:

    # crear dataset
    base = df2.groupby(['Descripción Presunto Responsable'])[['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending = False)[2:].head(5)

    # crear gráfica
    fig = px.bar(base, 
                x='Total de Víctimas del Caso', 
                y='Descripción Presunto Responsable', 
                color = 'Descripción Presunto Responsable', 
                title ='<b>TOP 5 PRESUNTOS RESPONSABLES<b>',
                width=480,  height=480, 
                orientation='h')

    # agregar detalles a la gráfica
    fig.update_layout(
        xaxis_title = '',
        yaxis_title = '',
        template = 'simple_white',
        title_x = 0.5,
        showlegend=False,)

    c2.write(fig)


with c3:

    base = df2.groupby(['DEPARTAMENTO'])[['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending = False).head(5)


    fig = px.bar(base, 
                x='Total de Víctimas del Caso', 
                y='DEPARTAMENTO', 
                color = 'DEPARTAMENTO', 
                title ='<b>TOP 5 DEPARTAMENTOS<b>',
                width=380,  height=480, 
                orientation='h')

    # agregar detalles a la gráfica
    fig.update_layout(
        xaxis_title = '',
        yaxis_title = '',
        template = 'simple_white',
        title_x = 0.5,
        showlegend=False,
        )

    c3.write(fig)



st.write('')
st.write('')
st.write('')


############################################################################FILA 3####################################################################

#División de columnas
c1, c2 = st.columns(2)


with c1:
    #Titulo
    c1.markdown("<h3 style='text-align: center; color: white;'> ¿CUÁLES SON LOS DPTOS. MÁS CRÍTICOS? </h3>", unsafe_allow_html=True)

    #Base para figura
    base = co.groupby(['DEPARTAMENTO'])[['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending = False).head(5)

    #Crear figura
    fig = px.pie(base, 
                values = 'Total de Víctimas del Caso', 
                names="DEPARTAMENTO",
                width=600, height=600)

    #Detalles figura
    fig.update_layout(
        template = 'simple_white',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5))

    # Enviar gráfica a streamlit
    c1.plotly_chart(fig)

with c2:
    #Titulo
    c2.markdown("<h3 style='text-align: center; color: white;'> ¿CUÁLES SON LOS MUNICIPIOS MÁS CRÍTICOS? </h3>", unsafe_allow_html=True)
    

    dep_options = co['DEPARTAMENTO'].unique().tolist() #Lista para el desplegable
    dep = c2.selectbox('¿Cuál departamento desea observar?', sorted(dep_options)) #Desplegable de los departamentos
    df2 = co[co['DEPARTAMENTO']==dep] # Filtrar DataFrame con el departamento seleccionado en la lista desplegable


    # Código para crear el mapa
    c2.write(pdk.Deck( 
        
        # Set up del mapa
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state={
            'latitude' : df2['latitude'].mean(),
            'longitude': df2['longitude'].mean(),
            'zoom' : 7.5, 
            'pitch': 50 #Elevación
            },
        
        # Capa con información
        layers = [pdk.Layer(
            'HexagonLayer',
            data = df2[['Total de Víctimas del Caso','latitude','longitude']],
            get_position = ['longitude','latitude'],
            auto_highlight=True,
            radius = 100,
            extruded = True,
            elevation_scale = 100,
            elevation_range = [0,1000],
            stroked=True,)]
        ))

############################################################FILA 5######################################################################################
st.write('')
st.write('')
st.write('')

#Titulo
st.markdown(f"<h1 style='text-align: center; color:white;'>{dep} </h1>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')

#División de columnas
c1, c2, c3 = st.columns(3)



with c1:
    #Titulo
    c1.markdown(f"<h4 style='text-align: center; color:white;'>TOP 10 MUNICIPIOS CON MÁS VÍCTIMAS </h4>", unsafe_allow_html=True)


    #Base para Gráfica
    base = df2.groupby(['MUNICIPIO'])  [['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending=False).head(10)

    #Gráfica
    fig = px.bar(base, 
                x='MUNICIPIO', 
                y='Total de Víctimas del Caso', 
                color = 'MUNICIPIO',
                width=475,  height=600)

    # agregar detalles a la gráfica
    fig.update_layout(
        xaxis_title = '',
        yaxis_title = 'VÍCTIMAS',
        template = 'simple_white',
        title_x = 0.5,
        showlegend=False,
        )

    #Gráfica a dash
    c1.write(fig)

    #Calcular el total
    total = df2['Total de Víctimas del Caso'].sum()
    #Mostrar el total
    c1.markdown(f"<h5 style='text-align: center; color:white;'>Total = {total} víctimas en {dep} </h5>", unsafe_allow_html=True)


with c2:
    #Titulo
    c2.markdown(f"<h4 style='text-align: center; color:white;'>AÑOS CON MÁS VÍCTIMAS </h4>", unsafe_allow_html=True)

    #Base para gráfica
    base = df2.groupby(['año'])  [['Total de Víctimas del Caso']].sum().reset_index()

    #Gráfica
    fig = px.line(base, 
                    x='año', 
                    y = 'Total de Víctimas del Caso',
                    width=485,  height=600)

    #Detalles
    fig.update_layout(
        xaxis_title = 'AÑOS',
        yaxis_title = 'VÍCTIMAS',
        template = 'simple_white',
        title_x = 0.5)

    #Gráfica a dash
    c2.write(fig)

with c3:

    c3.markdown(f"<h4 style='text-align: center; color:white;'>TABLA DE AÑOS CON MÁS VÍCTIMAS </h4>", unsafe_allow_html=True)

    base = df2.groupby(['año', 'MUNICIPIO'])  [['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending=False).head(10)

    fig = go.Figure(data=[go.Table(
            header=dict(values=list(base.columns),
            fill_color='black',
            font_color='white',
            line_color='darkslategray'),
            cells=dict(values=[base['año'], base['MUNICIPIO'],base['Total de Víctimas del Caso']],
            fill_color='black',
            font_color='white',
            line_color='darkslategray'))
        ])

    fig.update_layout(width=450, height=700)


    c3.write(fig)
