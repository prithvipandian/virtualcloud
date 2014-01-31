from bottle import get, post, request, route, run

@route('/hello')
def hello():
    return "Hello Danny!"

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if (username=='Danny Radding' and password=='RedSolo1'):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

port = os.environ.get('PORT', 5000)
run(host='localhost', port=port, debug=True)
