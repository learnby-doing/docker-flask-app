from flask import Flask, render_template,abort

app = Flask(__name__)
counter = 1
@app.route("/")
def hello_world():
    global counter
    if counter == 5:
        abort("Some failure happened")
    counter += 1
    return render_template("index.html",counter=counter)

if __name__=="__main__":
    app.run('0.0.0.0',port=8080)