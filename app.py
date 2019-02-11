import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

############# Make changes here


app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Foods of Provincial France'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Slop', 'Porridge', 'Mush'], 'y': [2, 7, 4], 'type': 'bar', 'name': 'Taste'},
                {'x': ['Slop', 'Porridge', 'Mush'], 'y': [7, 5, 5], 'type': 'bar', 'name': 'Consistancy'},
            ],
            'layout': {
                'title': "Its nice we have McDonalds",
                'xaxis':{'title':'the important taste factors'},
                'yaxis':{'title':'What the common folk say'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
