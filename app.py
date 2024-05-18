from flask import Flask, request, render_template, redirect
from summarizers import summarize_bart

app = Flask(__name__)

@app.route('/')
def home():
    # Front Page
    return render_template('home.html')

@app.route('/summarize/', methods = ['GET', 'POST'])
def summarize():
    if request.method == 'GET':
        return render_template('summarize.html')
    text = request.form['text']
    summary = output_summary(text)
    return render_template('summarize.html', text = text, summary = summary)
    
def output_summary(text):
    print("This be my text", text)
    return summarize_bart(text)

if __name__ == "__main__":
    app.run()