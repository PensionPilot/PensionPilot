from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        age = int(request.form['age'])
        salary = float(request.form['salary'])
        contribution = float(request.form['contribution'])

        result = salary * (contribution / 100) * (65 - age)
        return render_template('home.html', result=round(result, 2))
    except:
        return render_template('home.html', result="Something went wrong.")

if __name__ == '__main__':
    app.run(debug=True)
