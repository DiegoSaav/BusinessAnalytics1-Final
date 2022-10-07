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

#Descomprime el zip y desempaqueta el csv
from zipfile import ZipFile

test_file_name = "conflicto.zip"

with ZipFile(test_file_name, 'r') as zip:
    zip.extractall() 





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

@st.cache(allow_output_mutation=True)
def load_data3():
    data = pd.read_csv(
        "red.csv"
    )
    return data

df = load_data1() 
co = load_data2()
red = load_data3()

##############################################################TITULOS Y TEXTOS INTRODUCTORIOS####################################################

c1, c2 = st.columns(2) # Dividir el ancho en 2 columnas de igual tamaño

with c1:
    c1.title('\U0001f50e Influencia del conflicto armado sobre la conectividad digital en Colombia')

with c2:
    c2.markdown("""

    El acceso a internet se ha vuelto esencial para todos, ya que abre camino a nuevas formas de crear conocimiento y de relacionarnos, 
    es por eso que en países como el nuestro, nos vemos obligados a realizar una transición prioritaria a una cultura más digital, 
    realizando cambios en todas las esferas sociales pero teniendo en cuenta que Colombia ha sido fuertemente golpeado por la violencia en su historia. 
    
    Por esta razón se desea analizar las diferencias que hay en las zonas rurales y urbanas en Colombia con respecto 
    a la violencia, en particular el conflicto armado, y si esta problemática influye en el acceso a internet.

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
    text = 'Víctimas por modalidad más violenta'
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
    text = 'Víctimas por presunto más violento'
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
    text = 'Víctimas por dpto. más violento'
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
    c1.markdown("<h3 style='text-align: center; color: white;'> EVOLUCIÓN ANUAL DE LAS VÍCTIMAS DEL CONFLICTO ARMADO EN COLOMBIA </>", unsafe_allow_html=True)

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

    c2.markdown("<h3 style='text-align: center; color: white;'> EVOLUCIÓN ANUAL DE LAS VÍCTIMAS POR DEPARTAMENTO </>", unsafe_allow_html=True)


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
        legend_title = 'Víctimas según departamento:')

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
    c1.markdown("<h4 style='text-align: center; color: white;'> ¿CUÁLES SON LOS DPTOS. MÁS CRÍTICOS? </>", unsafe_allow_html=True)

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
    c2.markdown("<h4 style='text-align: center; color: white;'> ¿CUÁLES SON LOS MUNICIPIOS MÁS CRÍTICOS? </>", unsafe_allow_html=True)
    

    dep_options = co['DEPARTAMENTO'].unique().tolist() #Lista para el desplegable
    dep = c2.selectbox('Departamento:', sorted(dep_options)) #Desplegable de los departamentos
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

#Calcular el total
total = df2['Total de Víctimas del Caso'].sum()
#Mostrar el total
st.markdown(f"<h2 style='text-align: center; color:red;'>{total} víctimas totales </>", unsafe_allow_html=True)



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

    c3.markdown(f"<h4 style='text-align: center; color:white;'>TOP 20 TABLA DE AÑOS CON MÁS VÍCTIMAS Y MUNICIPIOS </h4>", unsafe_allow_html=True)

    base = df2.groupby(['año', 'MUNICIPIO'])  [['Total de Víctimas del Caso']].sum().reset_index().sort_values('Total de Víctimas del Caso', ascending=False).head(20)

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

    fig.update_layout(width=450, height=600)


    c3.write(fig)


############################################################FILA 6######################################################################################

text = 'Acceso a internet en Colombia'
st.markdown(f"<h1 style='text-align: center; color:white;'>{text}</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)


with c1:

    #Titulo
    st.markdown("<h4 style='text-align: center; color: white;'> PARETO DE LOS USUARIOS ACTIVOS AL MES POR DPTO. </>", unsafe_allow_html=True)

    #Base para figura
    df0 = df.groupby(['DEPARTAMENTO'])[['USUARIOS_ACTIVOS_MES']].sum().sort_values('USUARIOS_ACTIVOS_MES', ascending = False)
    df0['ratio'] = df0.apply(lambda x: x.cumsum()/df0['USUARIOS_ACTIVOS_MES'].sum())

    #Crear figura
    fig = go.Figure([go.Bar(x=df0.index, y=df0['USUARIOS_ACTIVOS_MES'], yaxis='y1', name='N° Usuarios'),
                    go.Scatter(x=df0.index, y=df0['ratio'], yaxis='y2', name='Usuarios Activos', hovertemplate='%{y:.1%}', marker={'color': '#FF0000'})])
    #Detalles figura
    fig.update_layout(template='plotly_dark', showlegend=False, hovermode='x', bargap=.3, 
                    yaxis={'title': 'N° Usuarios Activos'},
                    yaxis2={'rangemode': "tozero", 'overlaying': 'y', 'position': 1, 'side': 'right', 'title': 'Ratio', 'tickvals': np.arange(0, 1.1, .2), 'tickmode': 'array', 'ticktext': [str(i) + '%' for i in range(0, 101, 20)]},
                    width=750, height=600)

    #Enviar gráfica a streamlit
    st.write(fig)

with c2:
    #Titulo
    text = 'TOTAL DE PERSONAS SENSIBILIZADAS AL USO DEL INTERNET POR DEPARTAMENTO'
    st.markdown(f"<h4 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)

    #Base para figura
    red.rename(columns = {'DEPARTAME_NOMBRE' : 'DEPARTAMENTO'}, inplace = True)
    red.rename(columns = {'INVERSION_TOTAL' : 'INVERSION'}, inplace = True)
    red.rename(columns = {'TotalPersonasSencibilizadas' : 'SENSIBILIZACION'}, inplace = True)
    red['DEPARTAMENTO'] = red['DEPARTAMENTO'].replace({'NARI�O': 'NARIÑO'})


    base = red.groupby(['DEPARTAMENTO'])[['SENSIBILIZACION']].sum().reset_index().sort_values('SENSIBILIZACION', ascending = False)

    #Crear figura
    fig = px.bar(base, x='DEPARTAMENTO', y='SENSIBILIZACION')

    #Detalles figura
    fig.update_layout(
        #xaxis_title = 'Departamentos',
        yaxis_title = 'Cantidad',
        template = 'simple_white',
        title_x = 0.5,
        width=650, height=600)

    #Enviar gráfica a streamlit
    st.write(fig)


############################################################FILA 7######################################################################################
text = 'Relación entre los centros digitales y la cantidad de victimas'
st.markdown(f"<h1 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)

#Titulo
st.markdown("<h4 style='text-align: center; color: white;'> N° DE VÍCTIMAS VS. N° DE CENTROS DIGITALES POR DEPARTAMENTO </>", unsafe_allow_html=True)

#Base para figura
CEN_T = df.groupby(['DEPARTAMENTO'])[['MUNICIPIO']].count().rename(columns = {'MUNICIPIO' : 'CANT_CENTRO_DIGITAL'}).sort_values('CANT_CENTRO_DIGITAL', ascending = False).reset_index()
VIC_T =co.groupby(['DEPARTAMENTO'])[['Total de Víctimas del Caso']].sum().rename(columns = {'Total de Víctimas del Caso' : 'CANT_VICTIMAS'}).sort_values('CANT_VICTIMAS', ascending = False).reset_index()
CDV_AR = pd.merge(VIC_T,CEN_T, on = 'DEPARTAMENTO', how = 'left' )
CDV_AR['PROP_VICT'] = (CDV_AR['CANT_VICTIMAS']-CDV_AR['CANT_VICTIMAS'].min())/(CDV_AR['CANT_VICTIMAS'].max()-CDV_AR['CANT_VICTIMAS'].min())

#Crear figura
fig9 = px.scatter(CDV_AR, x = 'CANT_VICTIMAS', y ='CANT_CENTRO_DIGITAL', color = 'DEPARTAMENTO',
           size = 'PROP_VICT')
#Detalles figura
fig9.update_layout(
    xaxis_title = 'N° de Víctimas',
    yaxis_title = 'N° de centros digitales',
    template = 'seaborn',
    title_x = 0.5,
    width=1200, height=600)

#Enviar gráfica a streamlit
st.write(fig9)

############################################################FILA 8######################################################################################
text = 'Relación entre dificultad de acceso y tipo de zona'
st.markdown(f"<h1 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)



c1, c2 = st.columns(2)

with c1:
    #Titulo
    text = 'Dificultad de acceso a internet según el departamento'
    st.markdown(f"<h4 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)


    dep_options = df['DEPARTAMENTO'].unique().tolist() #Lista para el desplegable
    dep = st.selectbox('Departamento:', sorted(dep_options)) #Desplegable de los departamentos
    df2 = df[df['DEPARTAMENTO']==dep] # Filtrar DataFrame con el departamento seleccionado en la lista desplegable

    #Base para figura
    base = df2.groupby(['DIFICULTADACCESO'])[['ZONA']].count().reset_index()
    cant=df2['ZONA'].count()

    #Crear figura
    fig = px.pie(base, values = 'ZONA',names ='DIFICULTADACCESO', hole = 0.5)

    #Detalles figura
    fig.update_layout(
        template = 'ggplot2',
        legend_title = 'DIFITULTAD DE ACCESO',
        title_x = 0.5,
        annotations =[dict(text = str(cant), x=0.5, y=0.5, font_size=40,showarrow=False)],
        legend=dict(orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5),
        width=500, height=500)

    #Enviar gráfica a streamlit
    st.write(fig)


############################################################FILA 9######################################################################################

with c2:
    st.markdown(f"<h4 style='text-align: center; color:white;'>Tabla de cantidad de zonas rurales y urbanas por departamento </>", unsafe_allow_html=True)

    #Base para la tabla
    base = df.groupby(['DEPARTAMENTO','ZONA'])[['VELOCIDAD_SUBIDA']].count().rename(columns = {'VELOCIDAD_SUBIDA' : 'CANTIDAD DE REGISTROS'}).reset_index()

    #Crear tabla
    fig = go.Figure(data=[go.Table(
                header=dict(values=list(base.columns),
                fill_color='black',
                font_color='white',
                line_color='darkslategray'),
                cells=dict(values=[base['DEPARTAMENTO'], base['ZONA'],base['CANTIDAD DE REGISTROS']],
                fill_color='black',
                font_color='white',
                line_color='darkslategray'))
            ])

    fig.update_layout(
        width=500, height=500)


    #Enviar gráfica a streamlit
    st.write(fig)


##########################################################FILA 10#####################################################################           
#Titulo
text = 'Relación entre la velocidad del internet y la zona (rural o urbana) por departamento.'
st.markdown(f"<h1 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    c1.markdown("<h4 style='text-align: center; color: white;'> 🔺 VELOCIDAD DE SUBIDA DE CADA DEPARTAMENTO POR ZONA </>", unsafe_allow_html=True)

    #Base de datos para la gráfica
    base = df.groupby(['DEPARTAMENTO','ZONA'])[['VELOCIDAD_SUBIDA']].mean().reset_index().sort_values('VELOCIDAD_SUBIDA', ascending = False)

    #Creación de gráfica
    fig1 = px.bar(base, x = 'DEPARTAMENTO', y='VELOCIDAD_SUBIDA', color ='ZONA',barmode ='group')
    
    #Detalles
    fig1.update_layout(
    xaxis_title = 'Departamento',
    yaxis_title = 'Velocidad de subida',
    template = 'plotly_dark',
    title_x = 0.5,
    legend=dict(orientation="h",
        yanchor="top",
        y=-0.5,
        xanchor="center",
        x=0.5),
    width=666, height=666)

    c1.write(fig1)

with c2:
    c2.markdown("<h4 style='text-align: center; color: white;'> 🔻 VELOCIDAD DE BAJADA DE CADA DEPARTAMENTO POR ZONA </>", unsafe_allow_html=True)

    #Base de datos para la gráfica
    base = df.groupby(['DEPARTAMENTO','ZONA'])[['VELOCIDAD_BAJADA']].mean().reset_index().sort_values('VELOCIDAD_BAJADA', ascending = False)

    #Creación de gráfica
    fig1 = px.bar(base, x = 'DEPARTAMENTO', y='VELOCIDAD_BAJADA', color ='ZONA',barmode ='group')
    
    #Detalles
    fig1.update_layout(
    xaxis_title = 'Departamento',
    yaxis_title = 'Velocidad de bajada',
    template = 'plotly_dark',
    title_x = 0.5,
    legend=dict(orientation="h",
        yanchor="top",
        y=-0.5,
        xanchor="center",
        x=0.5),
    width=666, height=666)

    c2.write(fig1)
            
##########################################################FILA 11#####################################################################
#Titulo
text = 'Relación entre el tráfico de usuarios y la zona (rural o urbana) por departamento.'
st.markdown(f"<h1 style='text-align: center; color:white;'>{text}</>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    c1.markdown("<h4 style='text-align: center; color: white;'> 🔺 TRÁFICO DE SUBIDA DE CADA DEPARTAMENTO POR ZONA </>", unsafe_allow_html=True)

    #Base de datos para la gráfica
    base = df.groupby(['DEPARTAMENTO','ZONA'])[['TRAFICO_MENSUAL_SUBIDA']].mean().reset_index().sort_values('TRAFICO_MENSUAL_SUBIDA', ascending = False)

    #Creación de gráfica
    fig1 = px.bar(base, x = 'DEPARTAMENTO', y='TRAFICO_MENSUAL_SUBIDA', color ='ZONA',barmode ='group')
    
    #Detalles
    fig1.update_layout(
    xaxis_title = 'Departamento',
    yaxis_title = 'Tráfico mensual de subida',
    template = 'plotly_dark',
    title_x = 0.5,    
    legend=dict(orientation="h",
        yanchor="top",
        y=-0.5,
        xanchor="center",
        x=0.5),
    width=666, height=666)

    c1.write(fig1)

with c2:
    c2.markdown("<h4 style='text-align: center; color: white;'> 🔻 TRÁFICO DE BAJADA DE CADA DEPARTAMENTO POR ZONA </>", unsafe_allow_html=True)

    #Base de datos para la gráfica
    base = df.groupby(['DEPARTAMENTO','ZONA'])[['TRAFICO_MENSUAL_BAJADA']].mean().reset_index().sort_values('TRAFICO_MENSUAL_BAJADA', ascending = False)

    #Creación de gráfica
    fig1 = px.bar(base, x = 'DEPARTAMENTO', y='TRAFICO_MENSUAL_BAJADA', color ='ZONA',barmode ='group')
    
    #Detalles
    fig1.update_layout(
    xaxis_title = 'Departamento',
    yaxis_title = 'Tráfico mensual de bajada',
    template = 'plotly_dark',
    title_x = 0.5,    
    legend=dict(orientation="h",
        yanchor="top",
        y=-0.5,
        xanchor="center",
        x=0.5),
    width=666, height=666)

    c2.write(fig1)









