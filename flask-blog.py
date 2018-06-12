from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Hello world",
        'author': "Siddhartha",
        'created_on': "April 21, 2018"
    },
    {
        'title': "Hello world2",
        'author': "Siddhartha",
        'created_on': "April 21, 2018"
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
