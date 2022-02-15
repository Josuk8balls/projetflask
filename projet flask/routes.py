from flask import *
import forms


#news user
def index():
    form = forms.LoginForm()
    return render_template('index.html', form=form)


#all rows from database
def view_database():
    from app import get_all_rows_from_table
    rows = get_all_rows_from_table()
    
    return render_template('entire_database.html', rows=rows)

def modify_database(the_id ,modified_category):
    if request.method == 'POST':
        from app import modify_data
        # Get data from the form on database page
        user_input = request.form[modified_category]
        # modify the row from the database
        modify_data(the_id, modified_category, user_input)
        # redirect back to the database page
        return redirect(url_for('view_database'))
    return redirect(url_for('index'))

def delete(the_id):
    if request.method == 'POST':
        from app import delete_data
        # if the checkbox was selected (for deleting entire row)
        if 'remove' in request.form:
            delete_data(the_id)
    return redirect(url_for('view_database'))

def submitted():
    from app import insert_data
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        job = request.form['job']

        # insert data into database
        insert_data(name, phone, email, job)

    return render_template('submitted.html')