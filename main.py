from flask import Flask, request, jsonify
import sympy as sym

app = Flask(__name__)


#Defino my SCALING_FACTOR que en sí es el factor por el cual se va 
#a escalar el valor pasado por el potenciometro

SCALING_FACTOR = 3.017
NUM_POINTS = 250
BASE_POINT = 5

x = sym.symbols('x')

des = 'i'
func = 'sin(x)'
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
        scale_fac = SCALING_FACTOR**self.x_scale
        x_initial = self.x_pos
        #Primero defino todos los puntos negativos
        for i in range(NUM_POINTS):
            scale = BASE_POINT/NUM_POINTS
            scale *= scale_fac
            punto = -scale*i+x_initial
            self.points.append(func.evalf(subs={x: punto}))
        
        #Una vez definidos los puntos negativos defino los positivos
        for i in range(NUM_POINTS-1):
            scale = BASE_POINT/NUM_POINTS
            scale *= scale_fac
            punto = scale*(i+1)+x_initial
            self.points.append(func.evalf(subs={x: punto}))


Plot = ploter(0, 1, 0)
Plot.plot(func)
print(Plot.points[1])
print(Plot.points[250])
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
   