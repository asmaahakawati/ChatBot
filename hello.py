from flask import Flask, render_template, request,redirect,url_for
from chatbot import *
app = Flask(__name__,template_folder='templates')
@app.route("/")
def home():
	return render_template("api.html")

@app.route('/process',methods=['POST'])
def process():

  user_input=request.form['user_input']
  #a=ChatBot.string_to_matrix(user_input)
  #bot_response=ChatBot.generate_response(a,user_input)
  bot_response=ChatBot.generate_response(ChatBot(),user_input)
  print("Friend: "+bot_response)
  return bot_response
        



        



        
@app.route("/product/<text>")
def product(text):
  return "enter for chat with chatbot :"+ text


@app.route("/ae")
def index2():
  return "<html> <body> <h1>hello from index </h1> </body>  </html>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True)       