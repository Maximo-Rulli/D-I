from flask import Flask, request, jsonify
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


#Defino my X_FACTOR que en sí es el factor por el cual se va 
#a escalar el valor pasado por el potenciometro

X_FACTOR = 2.187
Y_FACTOR = 10
NUM_POINTS = 250
BASE_POINT_X = 5
BASE_POINT_Y = 10

x = sym.symbols('x')

des = 'i'
func = 'x**x'
var = x

def differ(f):
    differ = sym.diff(sym.simplify(f), var)
    return str(differ)

def inte(f):
    inte = sym.integrate(sym.simplify(f), var)
    return str(inte)


class ploter():
    def __init__(self, x_scale:float, y_scale:float, x_pos:float) :
        #Parametros: 
        # x_scale: valor pasado por potenciometro de escala en x 
        # y_scale: valor pasado por potenciometro de escala en y 
        # x_pos: valor pasado por potenciometro de donde empieza mi punto 0,0
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.x_pos = x_pos
        self.points = np.zeros((2, NUM_POINTS*2), dtype=float)

    def plot(self, func:str) -> None:
        #Convierto de string a sympy
        func = sym.sympify(func)
        #Obtengo el xscale_fac que es en sí mi factor de escala 
        # una vez que le pase por el potenciometro mi valor de volts, por ello se eleva
        xscale_fac = X_FACTOR**self.x_scale
        yscale_fac = Y_FACTOR**self.y_scale
        x_initial = self.x_pos
        scale_x = BASE_POINT_X/NUM_POINTS
        scale_x *= xscale_fac
        #Primero defino todos los puntos negativos
        for i in range(NUM_POINTS):
            punto = -scale_x*i+x_initial*scale_x
            try:
                self.points[1, i] = func.evalf(subs={x: punto})/yscale_fac
            except TypeError:
                self.points[1, i] = np.nan
            self.points[0, i] = punto
        
        #Una vez definidos los puntos negativos defino los positivos
        for i in range(NUM_POINTS-1):
            punto = scale_x*(i+1)+x_initial*scale_x
            try:
                self.points[1, i+249] = func.evalf(subs={x: punto})/yscale_fac
            except TypeError:
                self.points[1, i+249] = np.nan
            self.points[0, i+249] = punto


Plot = ploter(5, 5, 0)
Plot.plot(func)
fig, ax = plt.subplots()
ax.plot(Plot.points[0], Plot.points[1])
plt.show()
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