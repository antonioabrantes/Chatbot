# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# abra janela View terminal
# pip install rasa
# rasa init (crie diretorio tesauro)
# cd tesauro
# rasa shell
# pip freeze > requirements.txt

# pip install Flask
# pip install gunicorn
# pip list
# va para diretorio (GUI) PS C:\Users\otimi\PycharmProjects\GUI> cd tesauro
# rode rasa shell
# anote o arquivo com rede treinada e copie no comando abaixo
# rasa run --enable-api -m ./models/20230618-100059-terminal-content.tar.gz --cors "*"
# certifique-se do modelo ter sido lido e vir a mensagem Rasa server is up and running
# agora rode este programa main.py

# atualize diretorio "C:\Users\otimi\OneDrive\Documentos\GitHub\Chatbot"
# verifique https://www.github.com/antonioabrantes/Chatbot


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("tkinter3.htm")


@app.route("/tkinter3.htm")
def tkinter3():
    return render_template("tkinter3.htm")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
