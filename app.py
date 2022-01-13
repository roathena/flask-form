from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def form_submit():
    if request.method == 'POST':
        return render_template('land.html', empid = request.form['empid'], empname = request.form['empname'], qual = request.form['qual'], desg = request.form['desg'], sal = request.form['salary'])




if __name__ == '__main__':
    app.run()