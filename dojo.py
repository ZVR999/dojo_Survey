from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = '1ond1n13!@#R$1n22cncqcasn23#$scscas'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['your_name']
    session['location'] = request.form['dojo_location']
    session['language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    
    if session['name'] == '':
        flash('Your Name: Can not be blank')
        return redirect('/')
    elif session['location'] == '':
        flash('Dojo Location: Can not be blank')
        return redirect('/')
    elif session['language'] == '':
        flash('Favorite Language: Can not be blank')
        return redirect('/')
    elif len(session['comment']) > 120:
        flash('Comment field can not exceed 120 characters') 
        return redirect('/')

    return render_template('result.html')


app.run(debug=True)