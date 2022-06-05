###############################################################################
#                            RUN MAIN                                         #
###############################################################################

# setup
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from python.model import Model
from settings import config
from flask import Flask

# App Instance
server = Flask(__name__)
app = dash.Dash(server=server, name=config.app_name, assets_folder="static", external_stylesheets=[dbc.themes.LUX, config.fontawesome])
app.title = config.app_title

place_dict = {
    1: 'Retiro, San Nicolás, Puerto Madero, San Telmo, Montserrat y Constitución.',
    2: 'Recoleta.',
    3: 'Balvanera y San Cristóbal.',
    4: 'La Boca, Barracas, Parque Patricios y Nueva Pompeya.',
    5: 'Almagro y Boedo.',
    6: 'Caballito.',
    7: 'Flores y Parque Chacabuco.',
    8: 'Villa Soldati, Villa Riachuelo y Villa Lugano.',
    9: 'Liniers, Mataderos y Parque Avellaneda.',
    10: 'Villa Real, Monte Castro, Versalles, Floresta, Vélez Sarsfield y Villa Luro.',
    11: 'Villa General Mitre, Villa Devoto, Villa del Parque y Villa Santa Rita.',
    12: 'Coghlan, Saavedra, Villa Urquiza y Villa Pueyrredón.',
    13: 'Núñez, Belgrano y Colegiales.',
    14: 'Palermo.',
    15: 'Chacarita, Villa Crespo, La Paternal, Villa Ortúzar, Agronomía y Parque Chas.'
}

########################## Navbar ##########################
# Input
## none


# Output
navbar = html.Div([

        html.Div([], className = 'col-3'),

        html.Div([
            dbc.NavItem(html.Div([
                dbc.NavLink("About", className="fa fa-question-circle", href="/", id="about-popover", active=False),
                dbc.Popover(id="about", is_open=False, target="about-popover", children=[
                    dbc.PopoverHeader("Como funciona?"), dbc.PopoverBody(config.about)
                ])
            ]))
        ],
        className='col-2'),

        html.Div([
            dbc.NavItem(html.Div([
                dbc.NavLink([html.I(className="fa fa-linkedin"), "  Contacts"], href=config.contacts, target="_blank"),
            ]))
        ],
        className='col-2'),

        html.Div([
            dbc.NavItem(html.Div([
                dbc.NavLink([html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank"),
            ]))
        ],
        className='col-2'),

        html.Div([], className = 'col-3')

    ],
    className = 'row',
    style = {'background-color' : '#03a1fc',
            'box-shadow': '2px 5px 5px 1px rgba(3, 252, 136, .5)'}
    )

# Callbacks
@app.callback(output=[Output(component_id="about", component_property="is_open"), 
                      Output(component_id="about-popover", component_property="active")], 
              inputs=[Input(component_id="about-popover", component_property="n_clicks")], 
              state=[State("about","is_open"), State("about-popover","active")])
def about_popover(n, is_open, active):
    if n:
        return not is_open, active
    return is_open, active



########################## Body ##########################
# Input
inputs = dbc.FormGroup([

    html.Div(children=[

        dbc.Label("Ubicación", html_for="n-ubicacion"),
        dcc.Dropdown(id="n-ubicacion",
                options=[{'label': l, 'value': v}
                    for v, l in place_dict.items()],
                placeholder='Seleccione una comuna', value="1"
        ),

        dbc.Label("Tipos de propiedad", html_for="n-tipo"),
        dcc.Dropdown(id="n-tipo", options= [
            {"label": "PH", "value": "1"},
            {"label": "Casa", "value": "2"},
            {"label": "Departamento", "value": "3"},
        ], value="1"),

        dbc.Label("Cantidad de Ambientes", html_for="n-ambientes"), 
        dcc.Slider(id="n-ambientes", min=1, max=20, step=1, marks={1:"1", 2:"2", 3:"3", 4:"4", 10:"10", 20:"20"}, value=3, tooltip={'always_visible':False}),

        dbc.Label("Cantidad de Habitaciones", html_for="n-habitaciones"), 
        dcc.Slider(id="n-habitaciones", min=1, max=10, step=1, marks={1:"1", 2:"2", 3:"3", 4:"4", 10:"10"}, value=2, tooltip={'always_visible':False}),

        dbc.Label("Cantidad de Baños", html_for="n-baños"), 
        dcc.Slider(id="n-baños", min=1, max=10, step=1, marks={1:"1", 2:"2", 3:"3", 4:"4", 10:"10"}, value=1, tooltip={'always_visible':False}),

        dbc.Label("Superficie cubierta", html_for="n-supcub"), 
        dbc.Input(id="n-supcub", placeholder="Superficie en m2", type="number", value="10"),

        dbc.Label("Superficie total", html_for="n-suptot"), 
        dbc.Input(id="n-suptot", placeholder="Superficie en m2", type="number", value="10")
    ], style={'display':'block'}),
    
    ## run button
    html.Br(),
    dbc.Col(dbc.Button("run", id="run", color="primary"))
])


# Output
body = dbc.Row([
        ## input
        dbc.Col(md=3, children=[
            inputs
        ]),
        ## output
        dbc.Col(md=9, children=[
            dbc.Spinner([
                ### Espacio Vacio
                dbc.Row([
                    dbc.Col(md=9, children=[html.Br()])
                    ]),
                ### title
                dbc.Row([
                    html.Br(),html.Br(),html.Br(),html.Br(),
                    html.H3(config.titulo_resultado, id="title")
                    ]),
                
                ### Resultado
                dbc.Row([
                    dbc.Col(md=4),
                    dbc.Col(md=4, children=[
                        html.H3(id="result")
                        ]),
                    dbc.Col(md=4)
                    ])
            ], 
            color="primary", type="grow"), 
        ])
])

# Callbacks

@app.callback(output=[Output(component_id="result", component_property="children")],
              inputs=[Input(component_id="run", component_property="n_clicks")],
              state=[State("n-tipo","value"), State("n-ubicacion","value"), State("n-baños","value"), State("n-habitaciones","value"), State("n-ambientes","value"), State("n-supcub","value"), 
                State("n-suptot","value")])
#entrego los datos para el modelo y devuelvo el precio
def update_result(n_clicks, n_tipo, n_ubicacion, n_baños, n_habitaciones, n_ambientes, n_supcub, n_suptot):
    modelo = Model()
    price = modelo.run(n_tipo, n_ubicacion, float(n_baños), float(n_habitaciones), float(n_ambientes), float(n_supcub), float(n_suptot))
    return price



########################## App Layout ##########################
app.layout = dbc.Container(fluid=True, children=[
    html.Div([
        #Fila de Encabezado e icono.
        html.Div([], className = 'col-2'), 

        html.Div([
            html.H1(config.app_name, id="nav-pills",
                    style = {'textAlign' : 'center'}
            )],
            className='col-8',
            style = {'padding-top' : '1%'}
        ),

        html.Div([
            html.Img(
                    src = app.get_asset_url("logo.PNG"),
                    height = '73 px',
                    width = 'auto')
            ],
            className = 'col-2',
            style = {
                    'align-items': 'center',
                    'padding-top' : '1%',
                    'height' : 'auto'})

        ],
        className = 'row',
        style = {'height' : '4%'}
        ),
    navbar,
    html.Br(),
    body
])

########################## Run ##########################
if __name__ == "__main__":
    debug = True if config.ENV == "DEV" else False
    app.run_server(debug=debug, host=config.host, port=config.port)