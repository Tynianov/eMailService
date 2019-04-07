from flask import Flask, redirect, url_for, request, render_template,flash
from sending_email import send_email
from pymysql import IntegrityError
from email_database import open_connection,insert,close_connection
from form import InputForm
from flask_bootstrap import Bootstrap

app = Flask('__main__')
db_connection = None
app.config['SECRET_KEY'] = 'S_key'
Bootstrap(app)

@app.route('/',methods = ['GET', 'POST'])
def form_render():

    main_page = InputForm()
    global db_connection
    db_connection = open_connection()

    if main_page.validate_on_submit():
        email = main_page.email.data
        message = main_page.message.data
        send_email(email, message)
        try:
            insert(db_connection, email, message)
        except IntegrityError:
            pass
        return redirect(url_for('successful_sent'))

    return render_template('main_page.html',form=main_page)

@app.route('/successful_sent')
def successful_sent():
    close_connection(db_connection)
    return render_template('successful_sent.html')

if __name__ == '__main__':
    app.run(debug=True)

