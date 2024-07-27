from flask import Flask, render_template, request, jsonify, send_from_directory, session, redirect, url_for
import secrets
import mysql.connector

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Database connection
mydb = mysql.connector.connect(
    host="sql5.freemysqlhosting.net",
    user="sql5667537",
    database="sql5667537",
    passwd="npSWwqzMhz"
)

mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('Search.html')

@app.route('/home')
def home():
    selected_option = session.get('selected_option', '')
    return render_template('HomePage.html', selected_option=selected_option)

@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Extract form data
    name = request.form.get('name')
    email = request.form.get('email')
    chosen_accommodation = request.form.get('accommodation')
    start_date = request.form.get('startDate')
    end_date = request.form.get('endDate')
    comments = request.form.get('floatingTextarea')

    
    sql = "INSERT INTO students (name, email, accomodation, start_date, end_date, comments) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, email, chosen_accommodation, start_date, end_date, comments)

    mycursor.execute(sql, values)
    mydb.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
