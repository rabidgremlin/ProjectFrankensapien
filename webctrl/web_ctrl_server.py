import bottle
from bottle import route, run, template

from subprocess import call 

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/send/<name>')
def index(name):
    call(['C:\\WinLIRC\\Transmit','Robosapienv1',name])  
    return "done"
    
run(host='localhost', port=8080)