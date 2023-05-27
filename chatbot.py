# https://www.youtube.com/watch?v=K2ejI4z8Mbg&t=701s
# pycharm free https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
# instruçoes para o Deploy https://www.back4app.com/docs-containers/run-a-flask-container-app
# exemplo https://github.com/templates-back4app/containers-python-flask-sample

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/contatos")
def contatos():
	return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
	return render_template("usuarios.html",nome_usuario=nome_usuario)

if __name__ == "__main__":
	#app.run(debug=True)
	app.run(host='0.0.0.0', port=8080)
