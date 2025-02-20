import dash
from dash import html, dcc

# Initialize the Dash app
app = dash.Dash(__name__) # Basic Dash app

# Define the layout
app.layout = html.Div([
    
    # bigger text
    html.H1("Dash App Demo!"),

    # smaller text
    html.P("This is a basic Dash app to demonstrate components and deployment."),

    # input 1 - text box
    html.Div([
         html.Label([
            "What is your name? ",
            html.Span("*", style={'color': 'red'})  # Red asterisk for required field
            ]),

        dcc.Input(
            id='username',
            type='text',
            placeholder='Enter your name...',
            required=True,
            className='custom-input1'  # Apply the custom CSS class
        ),
        
        # render textbox below the label
    ], style={'display': 'flex', 'flexDirection': 'column'}),


    # input 2 - number box
    html.Div([
        html.Label([
            "What is your age? ",
            html.Span("*", style={'color': 'red'})  # Red asterisk for required field
            ]),

        dcc.Input(
            id='age',
            type='number',
            placeholder='Enter your age...',
            min=1,  # Minimum allowed age
            max=120,  # Maximum allowed age
            required=True,
            className='custom-input1'  # Apply the custom CSS class
        )
    ], style={'display': 'flex', 'flexDirection': 'column'}),

    # input 3 - dropdown
    html.Div([
        html.Label("What is your biological sex?"),
        dcc.Dropdown(
            id='gender',
            options=[
                {'label': 'Male', 'value': 'male'},
                {'label': 'Female', 'value': 'female'},
                {'label': 'Intersex', 'value': 'intersex'}
            ],
            placeholder='Select a sex...',

            style={
                'marginTop': '8px',  # Adjusts the margin above the box
                'marginBottom': '12px', # Adjusts the margin below the box
                'width': '260px'  # Adjusts the width
                }
        )
    ]),

    # input 4 - radio buttons
    html.Div([
        html.Label("Highest level of education"),
        dcc.RadioItems(
            id='education',
            options=[
                {'label': 'Primary', 'value': 'primary'},
                {'label': 'Secondary', 'value': 'secondary'},
                {'label': 'Tertiary', 'value': 'tertiary'}
            ],
            value='primary',  # Default value
            labelStyle={'display': 'inline-block', 'margin-right': '10px'},  # Adjusts the space between the label and radio button
            style={
                'marginTop': '8px',# Adjusts the margin above the radio buttons
                'marginBottom': '12px' # Adjusts the margin above the radio buttons
                }  
        )
    ]),

    # input 5 - checkbox
    html.Div([
        html.Label("Select your favorite colors:"),
        dcc.Checklist(
            id='colors',
            options=[
                {'label': 'Red', 'value': 'red'},
                {'label': 'Green', 'value': 'green'},
                {'label': 'Blue', 'value': 'blue'}
            ],
            value=['red'],  # Default value
            labelStyle={'display': 'inline-block', 'margin-right': '10px'},  # Displays the options horizontally
            style={
                'marginTop': '8px',# Adjusts the margin above the radio buttons
                'marginBottom': '12px' # Adjusts the margin above the radio buttons
                } 
        )
    ]),

    # input 6 - textarea
    html.Div([
        html.Label("Tell me about yourself:"),
        dcc.Textarea(
            id='yourself',
            placeholder='Enter your comments...',
            className='custom-input2'  # Apply the custom CSS class
        )
    ], style={'display': 'flex', 'flexDirection': 'column'}),

    # adjust layout margins
], style={
    'margin': '15px',  # Adjust the margin to control the starting position
    'padding': '5px',  # Optional: Add padding for inner spacing
    'border': '1px solid #ccc'  # Optional: Add a border for visual reference
})

# This line is crucial for Gunicorn (deployment on Render)
server = app.server

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)