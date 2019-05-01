# This script mplements the UI and is the main python script to run, 
# this is to test local merge
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from inputs import *
from error_calculator import Error_calculator

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions']=True
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
astrometry_type = ['Diff. w.r.t ref stars', 'Diff. w.r.t Sci. Objects', 'Absolute Astrometry']
app.layout = html.Div(children=[

    html.Div([
        dcc.RadioItems(
                id='astrometry-type-id',
                options=[{'label': i, 'value': i} for i in astrometry_type],
                value=astrometry_type[0],
                labelStyle={'display': 'inline-block'}
            ),
        ],style={'width': '30%', 'float':'left', 'display': 'inline-block'}),

    # html.Div(id='blankspace1-id',
    #     style={'width': '30%', 'float':'center', 'display': 'inline-block'}),
    html.Button(id = 'Calculate',n_clicks=0,children='Calculate', style={'width': '10%', 'float':'center', 'display': 'inline-block'}),

    html.Div(id='ls-id',
        style={'width': '30%', 'float':'center', 'display': 'inline-block'}),

    html.Div(id='final_output-id',
        style={'width': '30%', 'float':'right', 'display': 'inline-block'}),

    html.Div(children=[
    	## global header
        html.H1(children='Global inputs',
            style={
                'textAlign': 'left',
                # 'color': colors['text']
            }
        ),
        ## wavelength input
        	# header
        html.Div(children='Wavelength m',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
        	# input tab
        html.Div([
        dcc.Input(id='wavelength-id', value = 0.0000022, type='number'),
        ]),

        ## SNR input
        	# header
        html.Div(children='SNR',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
        	# input tab
        html.Div([
        dcc.Input(id='SNR-id', value = 200, type='number'),
        ]),

        ## RNGS input
        	# header
        html.Div(children='rNGS',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
        	# input tab
        html.Div([
        dcc.Input(id='RNGS-id', value=30, type='number'),
        ]),

        ## Rref input
            # header
        html.Div(children='Rref',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='rref-id', value=17, type='number'),
        ]),

        ## T input
            # header
        html.Div(children='T',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='T-id', value=100, type='number'),
        ]),

        ## dt input
            # header
        html.Div(children='dt epoch',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='dt-id', value=1, type='number'),
        ]),
    ],style={'width': '30%', 'display': 'inline-block'}),

    html.Div(children=[
        ## Field of observation
        html.H1(children='Observation Field',
            style={
                'textAlign': 'left',
                # 'color': colors['text']
            }
        ),
        ## Nref input
            # header
        html.Div(children='Number of reference stars',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
         ),
            # input tab
        html.Div([
        dcc.Input(id='Nref-id', value = 1, type='number'),
        ]),

        ## rsep input
            # header
        html.Div(children='reference field seperation',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='rsep-id', value = 1, type='number'),
        ]),

        ## Nfield input
            # header
        html.Div(children='Number of field stars',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='Nfield-id', value=1, type='number'),
        ]),

        ## Nsci input
            # header
        html.Div(children='Number of science object',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='Nsci-id', value=1, type='number'),
        ]),

      ],style={'width': '30%','float': 'center', 'display': 'inline-block'}),

    html.Div(children=[
        ## User defined variances
        html.H1(children='User defined variances',
            style={
                'textAlign': 'left',
                # 'color': colors['text']
            }
        ),
        # ## Noise input
        #     # header
        # html.Div(children='Noise',
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text']
        #     }
        #  ),
        #     # input tab
        # html.Div([
        # dcc.Input(id='Noise-id', value = 37.5, type='number'),
        # ]),

        ## Confusion input
            # header
        html.Div(children='Confusion',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='confusion-id', value = 5, type='number'),
        ]),

        ## OSD input
            # header
        html.Div(children='Object Spectra dispersion',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='OSD-id', value = 5, type='number'),
        ]),

        # ## PST input
        #     # header
        # html.Div(children='Plate Scale Turbulance',
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text']
        #     }
        # ),
        #     # input tab
        # html.Div([
        # dcc.Input(id='PST-id', value=15.0, type='number'),
        # ]),

        # ## HOT input
        #     # header
        # html.Div(children='Higher Order Turbulance',
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text']
        #     }
        # ),
        #     # input tab
        # html.Div([
        # dcc.Input(id='HOT-id', value=10.5, type='number'),
        # ]),

        # ## PSI input
        #     # header
        # html.Div(children='PSF irregularitues',
        #     style={
        #         'textAlign': 'left',
        #         'color': colors['text']
        #     }
        # ),
        #     # input tab
        # html.Div([
        # dcc.Input(id='PSI-id', value=5.5, type='number'),
        # ]),

        ## Halo Effect input
            # header
        html.Div(children='Halo Effect',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='HE-id', value=3, type='number'),
        ]),

       ## Turbulance variability
            # header
        html.Div(children='Turbulance variability',
            style={
                'textAlign': 'left',
                'color': colors['text']
            }
        ),
            # input tab
        html.Div([
        dcc.Input(id='TV-id', value=1, type='number'),
        ]),

       # ## Proper motion error
       #      # header
       #  html.Div(children='Proper Motion Error',
       #      style={
       #          'textAlign': 'left',
       #          'color': colors['text']
       #      }
       #  ),
       #      # input tab
       #  html.Div([
       #  dcc.Input(id='PM-id', value=500, type='number'),
       #  ]),
    ],style={'width': '30%', 'float':'right', 'display': 'inline-block'}),
    
    html.Div(id='butt-state')

    # 

    

    # style={'width': '48%', 'float': 'center', 'display': 'inline-block'}),
])


@app.callback(
    Output(component_id='final_output-id', component_property='children'),
    [Input(component_id='Calculate', component_property='n_clicks')],
    [State(component_id='wavelength-id', component_property='value'),
    State(component_id='SNR-id', component_property='value'),
    State(component_id='RNGS-id', component_property='value'),
    State(component_id='rref-id', component_property='value'),
    State(component_id='T-id', component_property='value'),
    State(component_id='dt-id', component_property='value'),
    State(component_id='Nref-id', component_property='value'),
    State(component_id='rsep-id', component_property='value'),
    State(component_id='Nfield-id', component_property='value'),
    State(component_id='Nsci-id', component_property='value'),
    # Input(component_id='Noise-id', component_property='value'),
    State(component_id='confusion-id', component_property='value'),
    State(component_id='OSD-id', component_property='value'),
    # Input(component_id='PST-id', component_property='value'),
    # Input(component_id='HOT-id', component_property='value'),
    # Input(component_id='PSI-id', component_property='value'),
    State(component_id='HE-id', component_property='value'),
    State(component_id='TV-id', component_property='value'),
    # Input(component_id='PM-id', component_property='value'),
    State(component_id='astrometry-type-id', component_property='value')
    ]

)

def update_output_div(n_clicks,wavelength,SNR,rNGS,Rref,T,dt,Nref,rsep,Nfield,Nsci,Confusion,OSD,HE,TV,astrometry_type):
    # The variables are already imported from input.py. Update the variables the are fed from the UI
    global_inputs['wavelength'] = wavelength
    global_inputs['SNR'] = SNR
    global_inputs['rngs'] = rNGS
    global_inputs['rref'] = Rref
    global_inputs['T'] = T
    global_inputs['dt_epoch'] = dt

    field['Nref'] = Nref
    field['rsep'] = rsep
    field['Nfield'] = Nfield
    field['Nsci'] =Nsci

    # sigma_x['Focal-plane measurement errors']['Noise'] = Noise
    sigma_x['Focal-plane measurement errors']['Confusion'] = Confusion
    sigma_x['Opto-mechanical errors']['Dispersion obj spectra'] = OSD
    # sigma_x['Opto-mechanical errors']['Diff TTJ plate scale'] = PST
    # sigma_x['Opto-mechanical errors']['Diff TTJ higher order'] = HOT
    # sigma_x['Opto-mechanical errors']['PSF irregularities'] = PSI
    sigma_x['Opto-mechanical errors']['Halo effect'] = HE
    sigma_x['Opto-mechanical errors']['Turb conditions variability'] = TV
    # sigma_t['Opto-mechanical errors']['Proper motion errors'] = PM

    # send the unpdated inputs to calculate the astrometry error
    Final_error=0
    if int(n_clicks)>=1:
        Final_error = Error_calculator(global_inputs,field,sigma_x,sigma_t,astrometry_type)
    return 'Astrometry error is {}'.format(Final_error)

# @app.callback(
#     Output(component_id='Butt', component_property='children'),
#     Input(component_id='Calculate', component_property= 'n_clicks')
# )

# def update_buttonstate(value):
#     return 'Button state is {}'.format(value)
if __name__ == '__main__':
    app.run_server(debug=True)


