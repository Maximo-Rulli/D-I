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
    def __init__(self, x_scale:float, y_scale:float, x_pos:float) :
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.x_pos = x_pos
        self.points = []

    def plot(self, func:str) -> None:
        func = sym.sympify(func)
        for i in range(100):
            self.points.append(func.evalf(subs={x: i}))

Plot = ploter(1, 1, 1)
Plot.plot(func)
print(Plot.points)

@app.route('/')
def initialize():
    return "Flask inicializado!"

@app.route('/send', methods=['GET', 'POST'])
def calculate():
    try:
        data = request.get_json()
        # process the received data
        print(type(data['func']))
        if data['des']=='d':
            return f"Función derivada resultante: {differ(data['func'])}"  
        elif data['des']=='i':
            return f"Función integrada resultante: {type(inte(data['func']))}"
        
    except:
        return "Los parametros fueron mal ingresados"
   