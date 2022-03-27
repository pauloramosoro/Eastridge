from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_invoice'

mysql = MySQL(app)

# setting
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM invoice_items')
    data = cur.fetchall()
    return render_template('index.html', invoice_items = data)

@app.route('/add_item', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        date = request.form['date']
        units = request.form['units']
        description = request.form['description']
        amount = request.form['amount']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO invoice_items (Date, Units, Description, Amount) VALUES (%s, %s, %s, %s)', 
        (date, units, description, amount))
        mysql.connection.commit()
        flash('Items Added Successfully')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_items(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM invoice_items WHERE invoiceid = %s', (id))
    data = cur.fetchall()
    return render_template('edit_items.html', invoice = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_items(id):
    if request.method == 'POST':
        date = request.form['date']
        units = request.form['units']
        description = request.form['description']
        amount = request.form['amount']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE invoice_items
        SET Date = %s,
        Units = %s,
        Description = %s,
        Amount = %s
        WHERE invoiceid = %s""", (date, units, description, amount, id))
        mysql.connection.commit()
        flash('Item Updated Successfully')
        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM invoice_items WHERE invoiceid = {0}'.format(id))
    mysql.connection.commit()
    flash('Item Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)