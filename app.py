from flask import Flask, render_template, request

app = Flask(Estoque)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        cidade = request.form['cidade']
        estado = request.form['estado']
        pais = request.form['pais']
        idade = request.form['idade']
        return f"Nome: {nome}, Cidade: {cidade}, Estado: {estado}, País: {pais}, Idade: {idade}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
