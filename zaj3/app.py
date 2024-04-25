from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/')
def home():
    return 'Witaj w mojej aplikacji Flask!'

@app.route('/about')
def about():
    return 'Zaprogramowano przez Han.'

@app.route('/contact')
def contact():
    return 'Email: kontakt@example.com.'

#zad2
@app.route('/formularz')
def formularz():
    return "x"


@app.route('/success/<name>')
def success(name):
    return 'witaj %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
