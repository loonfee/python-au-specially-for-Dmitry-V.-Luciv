from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/pic')
def pic():
    return render_template("pic.html")


@app.route('/game', methods=['GET'])
def game():
    if request.method == 'GET':
        name_param = request.args.get('name')

    if name_param is None:
        name_param = "?"

    else:
        if name_param == "21":
            name_param = "Правильно:)"
        else:
            name_param = "Неа, 21"


    return render_template(
        'game.html',
        name=name_param,
        method=request.method
    )




@app.context_processor
def inject_globals():
    return {
        "greeting": [
            "Привет   (＠＾－＾)",
            "Привет   <(￣︶￣)>",
            "Привет   (*¯︶¯*)"
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)