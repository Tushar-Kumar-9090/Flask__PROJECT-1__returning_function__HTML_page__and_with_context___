from flask import Flask, render_template
app = Flask(__name__)   ## __name__ --> it will take the  file into Flask



@app.route('/wish')     ## -->  for urlmapping
#$ here we returning a function
def wish():
    return "<center><h1>Hii GoodAfternoon how are you</h1></center>"


@app.route('/display')      ## -->  for urlmapping
#$ here we returning a html page
def display():
    return render_template('index.html')


@app.route('/show')         ## -->  for urlmapping
#$ here we returning a html page with context
def show():
    return render_template('index_context.html',name='Tushar',state='Odisha')


if __name__ == '__main__':
    app.run(debug=True)     ## --> for runserver


# app.run(debug=True)     ## --> for runserver