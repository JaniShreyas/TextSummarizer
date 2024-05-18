from flask import Flask, request, render_template, redirect
from summarizers import summarize_bart

app = Flask(__name__)

@app.route('/')
def home():
    # Front Page
    return render_template('home.html')

@app.route('/summarize/')
def summarize():
    return render_template('summarize.html')
    
def output_summary(text):
    text = request.args.get("text", default = "")
    summary = summarize_bart(text)
    return render_template('output_summary.html', text = text, summary = summary)