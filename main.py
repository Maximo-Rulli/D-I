from flask import Flask
import sympy as sym

app = Flask(__name__)

@app.route('/')
def home():
    return "Usando Sympy"

