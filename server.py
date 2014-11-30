from flask import Flask, render_template, request

# Setup App Server #

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/resume/')
def resume():
	return app.send_static_file('pdf/Resume.pdf')

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=80)
