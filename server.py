from flask import Flask, render_template, request
from bin.loadstrings import load_strings
# Setup App Server #

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/resume/')
def resume():
	return app.send_static_file('pdf/Resume.pdf')
    
@app.route('/main_body.html')
def main_body():
    return render_template('main_body.html', strings=load_strings('landing'))

@app.route('/header_content.html')
def header_frame():
    return render_template('header_content.html')

@app.route('/christmas/ashley6145/')
def ashley_page():
    return render_template('christmas_template.html', strings=load_strings('ashley'))

@app.route('/christmas/sarah1567/')
def sarah_page():
    return render_template('christmas_template.html', strings=load_strings('sarah'))

@app.route('/christmas/mom3579/')
def mom_page():
    return render_template('christmas_template.html', strings=load_strings('mom'))

if __name__ == '__main__':
  app.run(debug=True)
