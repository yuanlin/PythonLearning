from flask import Flask, render_template, request, redirect, url_for
from package.ytdownloader import download

app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
    result = request.args.get('result')
    return render_template('index.html', result = result)

@app.route('/submit', methods=['POST'])
def post_submit():
    result = ''
    for i in range(0,2):
        if request.form.get('url{}'.format(i)) != '':
            result = result + download(request.form.get('url{}'.format(i))) + '|'
            print(result)

    return redirect(url_for('index', result = result))

if __name__ == '__main__':
    app.run(debug=True)