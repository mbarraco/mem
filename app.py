from flask import (
    Flask,
    render_template,
    request
)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/anova_01', methods=['GET', 'POST'])
def anova_01():
    return render_template('anova_01.html')


@app.route('/anova_02', methods=['GET', 'POST'])
def anova_02():
    return render_template('anova_02.html')


@app.route('/anova_03', methods=['GET', 'POST'])
def anova_03():
    return render_template('anova_03.html')


@app.route('/practica_4_II_2', methods=['GET'])
def practica_4_II_2():
    return render_template('practica_4_II_2.html')


@app.route('/practica_4_II_3', methods=['GET'])
def practica_4_II_3():
    return render_template('practica_4_II_3.html')


@app.route('/practica_4_II_4', methods=['GET'])
def practica_4_II_4():
    return render_template('practica_4_II_4.html')


@app.route('/practica_4_II_5', methods=['GET'])
def practica_4_II_5():
    return render_template('practica_4_II_5.html')


@app.route('/practica_4_II_6', methods=['GET'])
def practica_4_II_6():
    return render_template('practica_4_II_6.html')


@app.route('/practica_4_II_7', methods=['GET'])
def practica_4_II_7():
    return render_template('practica_4_II_7.html')


@app.route('/practica_4_II_8', methods=['GET'])
def practica_4_II_8():
    return render_template('practica_4_II_8.html')


@app.route('/diagnostico', methods=['GET'])
def diagnostico():
    return render_template('diagnostico.html')


@app.route('/tp-4-5', methods=['GET', 'POST'])
def tp_4_5():
    return render_template('tp_4.5.html')


@app.route('/error', methods=['GET'])
def error():
    return render_template('landing.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5999, debug=True)