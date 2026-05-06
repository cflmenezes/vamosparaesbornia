from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Carrega a página inicial
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    # Coleta dados do formulário HTML
    corrente = float(request.form['corrente'])
    distancia = float(request.form['distancia'])
    
    # Exemplo de cálculo: Queda de Tensão (Simplificado)
    # Delta V = (2 * L * I * rho) / S
    # Vamos simular que queremos achar a Seção (S) para Delta V de 4% em 220V
    rho = 0.0178  # Resistividade do cobre
    limite_queda = 220 * 0.05
    
    secao_minima = (2 * distancia * corrente * rho) / limite_queda
    
    return f"<h1>Resultado</h1><p>A seção mínima teórica é: {secao_minima:.2f} mm²</p><a href='/'>Voltar</a>"

if __name__ == '__main__':
    # Roda o servidor localmente
    app.run(debug=True)