from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def get_main():
    return render_template('youtubeprac.html')

@app.route('/breakfast')
def get_breakfast_page():
    return render_template('calculator1.html')

@app.route('/lunch')
def get_lunch_page():
    breakfast = request.args['breakfast']
    return render_template('calculator2.html', breakfast=breakfast)

@app.route('/dinner')
def get_dinner_page():
    breakfast = request.args['breakfast']
    lunch = request.args['lunch']
    return render_template('calculator3.html', breakfast=breakfast, lunch=lunch)

if __name__ == '__main__':
    app.run()
