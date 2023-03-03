from flask import Flask, request, jsonify
import sympy as sym

app = Flask(__name__)

x, y, z = sym.symbols('x y z')

des = 'i'
func = 'sin(2*x)'
var = x

def differ(f):
    differ = sym.diff(sym.simplify(f), var)
    return str(differ)

def inte(f):
    inte = sym.integrate(sym.simplify(f), var)
    return str(inte)

@app.route('/')
def initialize():
    return "Flask inicializado!"

@app.route('/send', methods=['GET', 'POST'])
def calculate():
    try:
        data = request.get_json()
        # process the received data
        if data['des']=='d':
            return f"Función derivada resultante: {differ(data['func'])}"
        elif data['des']=='i':
            return f"Función integrada resultante: {inte(data['func'])}"
        
        #return f"{jsonify(result)}, la data pasada es {data}"
    except:
        return "Ningun parametro pasado"
    """
    if des=='d':
        return differ(func)
    else:
        return inte(func)
    """