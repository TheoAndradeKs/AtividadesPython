from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo \nUtilize /decorator para descobrir oque é o Decorator!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Um decorator (decorador) em Python é uma função especial que permite adicionar funcionalidades novas a uma função ou método existente, sem precisar alterar o código original dela. Eles são "embalagens" que envolvem outra função, permitindo executar códigos antes ou depois da função original ser chamada.\n Os decorators são usados para reutilizar código e organizar melhor a lógica, sendo ideais para: \nLogging/Auditoria: Registrar quando uma função é executada.\n\nAutenticação: Verificar se um usuário tem permissão para acessar algo.\nTemporização (Timing): Medir o tempo de execução de uma função.Caching: Armazenar resultados de funções pesadas. \nComo ele é utilizado:\n@meu_decorator\n def minha_funcao():\nprint("Executando a função original!")'

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
