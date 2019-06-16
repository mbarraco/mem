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


@app.route('/tp-4-5', methods=['GET', 'POST'])
def tp_4_5():
    return render_template('tp_4.5.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5999, debug=True)