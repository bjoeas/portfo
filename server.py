# http://www.mashup-template.com/templates.html
# http://www.mashup-template.com/preview.html?template=univers
# https://blog.jetbrains.com/pycharm/2014/09/feature-spotlight-multiple-selections-in-pycharm/
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
# https://docs.python.org/3/library/csv.html
# https://help.pythonanywhere.com/
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_txt(data)
            write_to_csv(data)
            return redirect('/thanks.html')  # or we can use 'render_template('thank_you.html')'
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


def write_to_txt(data):  # .txt
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # file = database.write(f'\n{email},{subject},{message}')
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):  # .csv
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# @app.route('/index.html')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')


'''
set FLASK_APP=server.py
set FLASK_ENV=development
flask run

http://127.0.0.1:5000/ => localhost:5000
'''
