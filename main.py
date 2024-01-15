from flask import Flask,redirect,url_for,render_template,request;

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/success/<int:marks>')
def success(marks):
    res=""
    if marks>=50:
        res="PASS"
    else:
        res="FAIL"    
    return render_template('result.html',result=res,marks=marks)

@app.route('/faill/<int:marks>')
def faill(marks):
    res=""
    if marks>=50:
        res="PASS"
    else:
        res="FAIL"    
    return render_template('result.html',result=res,marks=marks)

@app.route('/checker/<int:marks>')
def checker(marks):
    result=""
    if marks>=40:
        result="success"
    else:
        result="faill"
    return redirect(url_for(result,marks=marks))


##Result Checker Html Page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
    total_score=(science+maths+c+data_science)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="faill"
    return redirect(url_for(res,marks=total_score))

if __name__ == '__main__':
    app.run(debug=True)
