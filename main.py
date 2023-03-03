from flask import Flask, request, jsonify
import sympy as sym

app = Flask(__name__)

x, y, z = sym.symbols('x y z')

des = 'i'
func = 'sin(2*x)'
var = x

def differ(f):
    f = sym.simplify(f)
    differ = sym.diff(f, var)
    return str(differ)

def inte(f):
    f = sym.simplify(f)
    inte = sym.integrate(f, var)
    return str(inte)

@app.route('/')
def initialize():
    return "Flask inicializado!"

@app.route('/send', methods=['GET', 'POST'])
def calculate():
    try:
        data = request.get_json()
        # process the received data
        result = {'result': 'success'}
        return f"{jsonify(result)}, la data pasada es {data}"
    except:
        return "Ningun parametro pasado"
    """
    if des=='d':
        return differ(func)
    else:
        return inte(func)
    """