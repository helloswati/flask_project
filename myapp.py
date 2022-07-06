from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


#@app.route('/ml')
def machine_learning():
    return'Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.'


@app.route('/nlp')
def NLP():
    return'NLP is a part of Computer Science and Artificial Intelligence which deals with human languages.'
    

app.add_url_rule('/ml', 'ml', machine_learning) 

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

@app.route('/number/<int:num>')
def hello_number(num):
    salary = 20000 + num
    return 'salary is  %d' % salary


if __name__ == '__main__':
    app.run() 

