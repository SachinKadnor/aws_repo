from flask import Flask,render_template, request,jsonify

app = Flask(__name__)


@app.route('/')
def Hello():
    return "<html><body><h2>Hello Flask World</h2></body></html>"
    #return "Hello World"

@app.route('/Hello')
def Hello_html():
    return render_template('hello.html')

@app.route('/HelloUser/<user>')
def Hello_html_user(user):
    return render_template('user.html',name=user)

@app.route('/Result/<int:num>')
def Result_html(num):
    return render_template('marks.html',marks=num)

@app.route('/Result1')
def Result1_html():
    marks_dict = {"Sub1":34,"Sub2":94,"Sub3":54,"Sub4":84}
    return render_template('result.html',result = marks_dict)

@app.route('/Result2',methods = ['POST','GET'])
def Result2_html():
    if request.method == 'POST':
        result = request.form

        return render_template('result1.html', result = result)
    

@app.route('/get_input',methods = ['POST','GET'])
def get_input_html():
    if request.method == 'POST':
        result = request.form
        #return render_template('result1.html', result = result)
        #return jsonify({"The value from server = ":result})
        #return result.keys()
        return list(result.values())
    return render_template('student.html')



if __name__ == '__main__':
    app.run()