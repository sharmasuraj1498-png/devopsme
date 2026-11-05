from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/task', methods=['GET', "POST"])
def home():
    return 'Hello World'
if __name__=='__main__':
    app.run()