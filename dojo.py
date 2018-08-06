from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    your_name = request.form['your_name']
    dojo_location = request.form['dojo_location']
    fav_language = request.form['favorite_language']
    your_comment = request.form['comment']
    print your_name, dojo_location, fav_language, your_comment
    return render_template('result.html', name=your_name, location=dojo_location,
    language=fav_language, comment=your_comment)
app.run(debug=True)