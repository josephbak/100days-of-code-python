from flask import Flask
app = Flask(__name__)

#print(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif" width=200px>'


def make_bold(function):
    def wrapper():
        function_output = function()
        return '<b>' + function_output + '</b>'
    return wrapper


def make_emphasis(function):
    def wrapper():
        function_output = function()
        return '<em>' + function_output + '</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        function_output = function()
        return '<u>' + function_output + '</u>'
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "bye"

@app.route("/username/<name>/<int:number>")
def great(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
