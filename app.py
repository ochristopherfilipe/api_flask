from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Lê o arquivo CSV
df = pd.read_csv('Celulas.csv')


# Rota para a homepage
@app.route('/')
def homepage():
    return 'Sua API está rodando'

# Rota para obter todas as entradas
@app.route('/celulas', methods=['GET'])
def get_all_celulas():
    return jsonify(df.to_dict(orient='records'))

# Rota para obter uma entrada específica por ID
@app.route('/celulas/<int:celula_id>', methods=['GET'])
def get_celula_by_id(celula_id):
    celula = df[df['id'] == celula_id]
    if celula.empty:
        return jsonify({'error': 'celula não encontrada'}), 404
    return jsonify(celula.to_dict(orient='records'))

# Rota para obter uma entrada específica pelo primeiro nome da pessoa
@app.route('/celulas/nome/<string:nome>', methods=['GET'])
def get_celula_by_nome(nome):
    celula = df[df['Nome'].str.lower().str.contains(nome.lower())]
    if celula.empty:
        return jsonify({'error': 'lider não encontrado(a)'}), 404
    return jsonify(celula.to_dict(orient='records'))

# Rota para obter uma entrada específica pelo número da célula
@app.route('/celulas/celula/<int:celula_num>', methods=['GET'])
def get_celula_by_celula(celula_num):
    celula = df[df['Celula'] == celula_num]
    if celula.empty:
        return jsonify({'error': 'celula não encontrada'}), 404
    return jsonify(celula.to_dict(orient='records'))

# Rota para obter uma entrada específica pelo número da coordenacao
@app.route('/celulas/coordenacao/<int:coordenacao_num>', methods=['GET'])
def get_celula_by_coordenacao(coordenacao_num):
    celula = df[df['Coordenacao'] == coordenacao_num]
    if celula.empty:
        return jsonify({'error': 'Coordenacao não encontrada'}), 404
    return jsonify(celula.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
