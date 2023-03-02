from flask import Flask
import sympy as sym

app = Flask(__name__)

x, y, z = sym.symbols('x y z')

des = 'd'
func = 'cos(x**2)'
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
def calculate():
    if des=='d':
        return differ(func)
    else:
        return inte(func)
