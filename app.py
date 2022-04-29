import flask

server = flask.Flask(__name__)

@server.route('/')
def hello_world():
    return 'Hello, world!'


@server.route('/data')
def return_data():
    return flask.jsonify({
        'time': [1, 2, 3, 4, 5],
        'value': [3, 1, 2, 3, 4]
    })

'''
Alternatively, if you want to add Dash routes to your app, you might have:

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('My Dash App')
])
server = app.server

@server.route('/')
def hello_world():
    return 'Hello, world!'
'''


if __name__ == '__main__':
    server.run(debug=True, host="0.0.0.0", port=8050)
