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
    'text': '#FFFFFF'
}
astrometry_type = ['Differential astrometry (relative to field stars)', 'Differential astrometry (science objects relative to each other)', 'Absolute Astrometry']

app.layout = html.Div(children=[
     
    html.Div([
    html.H1('TMT-IRIS Astrometry Error budget' ,
    style={'color': 'white', 'font-style': 'italic', 'font-weight': 'bold','textAlign':'center'}
    ),

#    html.Div([
#    dcc.RadioItems(
#            id='astrometry-type-id',
#            options=[{'label': i, 'value': i} for i in astrometry_type],
#            value=astrometry_type[0],
#            labelStyle={'display': 'inline-block'}
#        ),
#    ],style={'width': '30%', 'float':'center', 'display': 'inline-block','textAlign':'center','margin-right': '500px', 'margin-top': '25px'}),
    
    html.Div([
    html.Label('Astrometry science case'),
    dcc.Dropdown(
            id='astrometry-type-id',
            options=[{'label': i, 'value': i} for i in astrometry_type],
            value=astrometry_type[0],
            multi = False,
            style={'color':'black'}
                ),
    ],
    
    style={'width': '50%', 'color': 'white','float':'center', 'display': 'inline-block','textAlign':'center','font-weight': 'bold','margin-right': '400px','margin-left': '50px','margin-bottom': '10px'}),
    # html.Div(id='blankspace1-id',
    #     style={'width': '30%', 'float':'center', 'display': 'inline-block'}),
    


############################## GLOBAL INPUTS #################################


    html.Div(children=[
    	## global header
        html.H5(children='Global inputs',
            style={ 'backgroundColor': '#FFFFFF','textAlign': 'center','font-weight': 'bold','color':'black'},
            ),
        ## wavelength input
        	# header
        html.Div(children='Wavelength  (m)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
        	# input tab
        html.Div([
        dcc.Input(id='wavelength-id', value = 0.0000025, type='number',
                  step=1e-7,min =0.0000008,max=0.0000025,
                  style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                 ]),

        ## SNR input
        	# header
        html.Div(children='SNR',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
        	# input tab
        html.Div([
        dcc.Input(id='SNR-id', value = 200, type='number',
                  style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                 ]),

        ## RNGS input
        	# header
        html.Div(children='rNGS  (arcsec)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                 ),
        	# input tab
        html.Div([
        dcc.Input(id='RNGS-id', value=30, type='number',step=0.01,min =0,
                  style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
               
                 ]),

        ## Rref input
            # header
        html.Div(children='rREF  (arcsec)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='rref-id', value=17, type='number',step=0.01,min =0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
 
                 ]),

        ## T input
            # header
        html.Div(children='T  (s)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='T-id', value=100, type='number',step=0.01,min =0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                ]),

        ## dt input
            # header
        html.Div(children='dt epoch  (yr)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='dt-id', value=1, type='number',step=0.01,min =0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),

                 ]),
            ],style={'backgroundColor': '#111111','opacity': '.8','width': '30%','float': 'right','display': 'inline-block','margin-right': '25px'}),
                  


############################## OBSERVATION FIELD ##############################



    html.Div(children=[
        ## Field of observation
        html.H5(children='Observation Field',
            style={ 'backgroundColor': '#FFFFFF','textAlign': 'center','font-weight': 'bold','color':'black'},
               ),
        
                ## rsep input
            # header
        html.Div(children='rSEP (arcsec) ',
         
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']
                  }
                 ),
            # input tab
        html.Div([
        dcc.Input(id='rsep-id', value = 1, type='number',step=0.01,min =0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
         
                 ]),

        
        ## Nref input
            # header
        html.Div(children='Number of reference stars',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='Nref-id', value = 1, type='number',min=0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                  
                 ]),


        ## Nfield input
            # header
        html.Div(children='Number of field stars',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='Nfield-id', value=1, type='number',min=0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                  
                 ]),

        ## Nsci input
            # header
        html.Div(children='Number of science object',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
            ),
            # input tab
        html.Div([
        dcc.Input(id='Nsci-id', value=1, type='number',min=0,
        style={'textAlign': 'center','margin-left': '100px','width':'50%'}),
                  
                ]),

            ],style={'backgroundColor': '#111111','opacity': '.8','width': '30%','float': 'left','display': 'inline-block','margin-left': '25px','height': '420px'}),


###################### USER DEFINED VARIANCES ##############################

    html.Div(children=[
        ## User defined variances
        html.H5(children='User defined variances',
            style={ 'backgroundColor': '#FFFFFF','textAlign': 'center','font-weight': 'bold','color':'black'},
               ),
       
        ## Confusion input
            # header
        html.Div(children='Confusion',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='confusion-id', value = 5, type='number',step =5,min=0,
        style={'textAlign': 'center','margin-left': '70px','width':'70%'}),
          
                 ]),

        ## OSD input
            # header
        html.Div(children='Object Spectra dispersion (micro arcsec)',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text'],'margin-left': '15px'}
                ),
            # input tab
        html.Div([
        dcc.Input(id='OSD-id', value = 5, type='number',step=1,min=1,max=50,
        style={'textAlign': 'center','margin-left': '70px','width':'70%'}),
        
                 ]),

        ## Halo Effect input
            # header
        html.Div(children='Halo Effect',
            style={'textAlign': 'center', 'font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='HE-id', value=3, type='number',step=0.01,min=0,max=5,
        style={'textAlign': 'center','margin-left': '70px','width':'70%'}),
        
                 ]),

       ## Turbulance variability
            # header
        html.Div(children='Turbulance variability',
            style={'textAlign': 'center','font-weight': 'bold','color': colors['text']}
                ),
            # input tab
        html.Div([
        dcc.Input(id='TV-id', value=1, type='number',min=1,max=1,
        style={'textAlign': 'center','margin-left': '70px','width':'70%'}),
           
                ]),

            ],style={'backgroundColor': '#111111','opacity': '.8','width': '32%','float': 'right','display': 'inline-block','margin-right': '25px','margin-left': '25px','height': '420px'}),
    
###################### output ############################################
    
    html.Button(id = 'Calculate',n_clicks=0,children='Calculate', style={'width': '10%','backgroundColor': 'white','opacity': '1','font-weight': 'bold','color': 'black', 'float':'center', 'display': 'inline-block'}),

    html.Div(id='ls-id',
        style={'width': '30%', 'color': 'white','font-weight': 'bold','float':'center', 'display': 'inline-block'}),

    html.Div(id='final_output-id',
#        style={'width': '30%', 'float':'right', 'display': 'inline-block'}),
        style={'color': 'white', 'font-weight': 'bold','textAlign':'center','font-size':'25px','margin-top': '-15px'}),

    
    
    html.Div(id='butt-state')

    # 

        ], style={'background-image': 'url(https://www.ipac.caltech.edu/system/activities/images/20/large/thirty-meter-telescope-illustration-nao-japan.jpg)',}),


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
#    Output('tabs-content', 'children'),
#              [Input('tabs', 'value')]
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
    return 'Final astrometry error is {}'.format(Final_error)

# @app.callback(
#     Output(component_id='Butt', component_property='children'),
#     Input(component_id='Calculate', component_property= 'n_clicks')
# )

# def update_buttonstate(value):
#     return 'Button state is {}'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)


