from flask import Flask, render_template

# Also run SASS watcher (bottom of VSC)

# ON PC:
# To run app server, run following command in cmd in the webapp dir: python app.py
# http://127.0.0.1:5000/

# ON RPI:
# Run following command: sudo python app.py
# http://192.168.0.33/

# HTML/CSS references
# https://www.w3schools.com/tags/default.asp

# https://www.youtube.com/watch?v=D-h8L5hgW-w
# 1:13:00
# https://fonts.google.com/

# https://css-tricks.com/snippets/css/a-guide-to-flexbox/

app = Flask(__name__)

@app.route('/') #determines entry point, where / is root
def home(): #name given to the route
    return render_template('home.html')

@app.route('/page_1') #determines entry point, where / is root
def page_1(): #name given to the route
    return render_template('page_1.html')

# #dynamic page
# @app.route('/hello/<name>')
# def hello(name):
#     return render_template('dynamic_page.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)