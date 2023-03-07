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


class ploter():
    def __init__(self, x_scale:float, y_scale:float, x_pos:float) -> None:
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.x_pos = x_pos

    def plot(self):
        pass

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
        
    except:
        return "Los parametros fueron mal ingresados"
   