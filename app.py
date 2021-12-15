from flask import Flask, render_template, json, redirect, url_for
from flask.helpers import flash
from flask_mysqldb import MySQL
from flask import request
from flask_bootstrap import Bootstrap
import os

# Configuration

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'UID'
app.config['MYSQL_PASSWORD'] = 'PW'
app.config['MYSQL_DB'] = 'UID'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


# Routes


# @app.route('/http://web.engr.oregonstate.edu/~hussamas/templates/index.html')
@app.route('/')
def root():
    return render_template('index.html')


@app.route('/add')
def add_page():
    return render_template('add.html')


#
# ANIMAL METHODS
#

@app.route('/animals', methods=['GET', 'POST'])
def animals():

    if request.method == 'POST':
        if 'add_animal' in request.form:
            print('------- method called = ADD ANIMAL -------')
            # Get data from add form
            species = request.form['species']
            name = request.form['name']
            volunteer = request.form['foster']
            location = request.form['location']
            arrival_date = request.form['arrival_date']

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO animals (species, name, volunteer_id, location_id, arrival_date) VALUES (%s, %s, %s, %s, %s)',
                           (species, name, volunteer, location, arrival_date))
            mysql.connection.commit()
            return redirect((url_for('animals')))

    cursor = mysql.connection.cursor()

    cursor.execute(
        'SELECT animal_id, species, name, volunteer_id, location_id, arrival_date FROM animals')
    data = cursor.fetchall()

    return render_template('animals.html', output_data=data)


# ANIMAL EDIT

@app.route('/animals/animal_edit/<int:animal_id>', methods=['POST'])
def animal_edit(animal_id):
    print('method called = animal edit')

    if 'edit' in request.form:
        print('EDIT STARTED')
        # Get data from the update form
        # animal_id = request.form['animal_id']
        species = request.form['beforespecies']
        name = request.form['beforename']
        volunteer = request.form['beforefoster']
        location = request.form['beforelocation']
        arrival_date = request.form['beforedate']

        # Update query using animal_id
        query = 'UPDATE animals SET species=%s, name=%s, volunteer_id=%s, location_id=%s, arrival_date=%s WHERE animal_id = %s;'

        # Query variables to be updated
        data = (species, name, volunteer,
                location, arrival_date, animal_id)

        # Create cursor and execute SQL query
        cursor = mysql.connection.cursor()
        cursor.execute(query, data)

        # Commit SQL Changes
        mysql.connection.commit()

        print('EDIT COMPLETE')
        # Refresh page
        return redirect(url_for('animals'))

    print('RENDER INITIAL EDIT TEMPLATE')
    query = 'SELECT animal_id, species, name, volunteer_id, location_id, arrival_date FROM animals WHERE animal_id = %s;'
    var = (animal_id,)
    # Create cursor and execute SQL query
    cursor = mysql.connection.cursor()
    cursor.execute(query, var)

    # Commit SQL Changes
    mysql.connection.commit()

    data = cursor.fetchall()

    return render_template('animal_edit.html', output_data=data)


# ANIMAL DELETE

@app.route('/animals/delete/<int:animal_id>', methods=['POST'])
def delete_animal(animal_id):
    query = 'DELETE FROM animals WHERE animal_id = %s'
    data = (animal_id,)

    cursor = mysql.connection.cursor()
    cursor.execute(query, data)
    mysql.connection.commit()

    return redirect(url_for('animals'))


#
# VOLUNTEER METHODS
#

@app.route('/volunteers', methods=['GET', 'POST'])
def volunteers():

    if request.method == 'POST':
        if 'add_volunteer' in request.form:
            # Get data from add form
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            street_address = request.form['street_address']
            street_name = request.form['street_name']
            city = request.form['city']
            state = request.form['state']
            phone = request.form['phone']
            email = request.form['email']
            experience = request.form['experience_select']

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO volunteers (first_name, last_name, street_address, street_name, city, state, phone, email, exp_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           (first_name, last_name, street_address, street_name, city, state, phone, email, experience))
            mysql.connection.commit()
            return redirect((url_for('volunteers')))

    cursor = mysql.connection.cursor()

    cursor.execute(
        'SELECT volunteer_id, first_name, last_name, street_address, street_name, city, state, phone, email, exp_level FROM volunteers')
    data = cursor.fetchall()

    return render_template('volunteers.html', output_data=data)


# VOLUNTEER EDIT

@app.route('/volunteers/volunteer_edit/<int:volunteer_id>', methods=['POST'])
def volunteer_edit(volunteer_id):
    print('------- method called = VOLUNTEER EDIT -------')

    if 'edit' in request.form:
        print('EDIT STARTED')

        # Get data from the update form

        first_name = request.form['before_fname']
        last_name = request.form['before_lname']
        street_address = request.form['before_saddress']
        street_name = request.form['before_sname']
        city = request.form['before_city']
        state = request.form['before_state']
        phone = request.form['before_phone']
        email = request.form['before_email']
        experience = request.form['before_experience']

        # Update query using animal_id
        query = 'UPDATE volunteers SET first_name=%s, last_name=%s, street_address=%s, street_name=%s, city=%s, state=%s, phone=%s, email=%s, exp_level=%s WHERE volunteer_id = %s;'

        # Query variables to be updated
        data = (first_name, last_name, street_address, street_name,
                city, state, phone, email, experience, volunteer_id)

        # Create cursor and execute SQL query
        cursor = mysql.connection.cursor()
        cursor.execute(query, data)

        # Commit SQL Changes
        mysql.connection.commit()

        print('EDIT COMPLETE')
        # Refresh page
        return redirect(url_for('volunteers'))

    print('RENDER INITIAL EDIT TEMPLATE')
    query = 'SELECT volunteer_id, first_name, last_name, street_address, street_name, city, state, phone, email, exp_level FROM volunteers WHERE volunteer_id = %s;'
    var = (volunteer_id,)
    # Create cursor and execute SQL query
    cursor = mysql.connection.cursor()
    cursor.execute(query, var)

    # Commit SQL Changes
    mysql.connection.commit()

    data = cursor.fetchall()

    return render_template('volunteer_edit.html', output_data=data)


# VOLUNTEER DELETE

@app.route('/volunteers/delete/<int:volunteer_id>', methods=['POST'])
def delete_volunteer(volunteer_id):
    query = 'DELETE FROM volunteers WHERE volunteer_id = %s'
    data = (volunteer_id,)

    cursor = mysql.connection.cursor()
    cursor.execute(query, data)
    mysql.connection.commit()

    return redirect(url_for('volunteers'))


#
# MENTOR METHODS
#

@app.route('/mentors', methods=['GET', 'POST'])
def mentors():
    if request.method == 'POST':
        if 'add_mentor' in request.form:
            # Get data from add form
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            phone = request.form['phone']
            email = request.form['email']
            location = request.form['location']

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO mentors (first_name, last_name, phone, email, location_id) VALUES (%s, %s, %s, %s, %s)',
                           (first_name, last_name, phone, email, location))
            mysql.connection.commit()
            return redirect((url_for('mentors')))

    cursor = mysql.connection.cursor()

    cursor.execute(
        'SELECT mentor_id, first_name, last_name, phone, email, location_id FROM mentors')
    data = cursor.fetchall()

    return render_template('mentors.html', output_data=data)


# VOLUNTEER EDIT

@app.route('/mentors/mentor_edit/<int:mentor_id>', methods=['POST'])
def mentor_edit(mentor_id):
    print('------- method called = MENTOR EDIT -------')

    if 'edit' in request.form:
        print('EDIT STARTED')

        # Get data from the update form

        first_name = request.form['before_fname']
        last_name = request.form['before_lname']
        phone = request.form['before_phone']
        email = request.form['before_email']
        location = request.form['before_location']

        # Update query using animal_id
        query = 'UPDATE mentors SET first_name=%s, last_name=%s, phone=%s, email=%s, location_id=%s WHERE mentor_id = %s;'

        # Query variables to be updated
        data = (first_name, last_name, phone, email, location, mentor_id)

        # Create cursor and execute SQL query
        cursor = mysql.connection.cursor()
        cursor.execute(query, data)

        # Commit SQL Changes
        mysql.connection.commit()

        print('EDIT COMPLETE')
        # Refresh page
        return redirect(url_for('mentors'))

    print('RENDER INITIAL EDIT TEMPLATE')
    query = 'SELECT mentor_id, first_name, last_name, phone, email, location_id FROM mentors WHERE mentor_id = %s;'
    var = (mentor_id,)
    # Create cursor and execute SQL query
    cursor = mysql.connection.cursor()
    cursor.execute(query, var)

    # Commit SQL Changes
    mysql.connection.commit()

    data = cursor.fetchall()

    return render_template('mentor_edit.html', output_data=data)


# MENTOR DELETE

@app.route('/mentors/delete/<int:mentor_id>', methods=['POST'])
def delete_mentor(mentor_id):
    print('------- method called = MENTOR DELETE -------')
    query = 'DELETE FROM mentors WHERE mentor_id = %s'
    data = (mentor_id,)

    cursor = mysql.connection.cursor()
    cursor.execute(query, data)
    mysql.connection.commit()

    return redirect(url_for('mentors'))


#
# LOCATION METHODS
#

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    if request.method == 'POST':
        if 'add_location' in request.form:
            print('------- method called = ADD LOCATION -------')
            # Get data from add form
            location_name = request.form['location_name']
            capacity = request.form['capacity']
            street_address = request.form['street_address']
            street_name = request.form['street_name']
            city = request.form['city']
            state = request.form['state']
            phone = request.form['phone']

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO locations (location_name, capacity, street_address, street_name, city, state, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (location_name, capacity, street_address, street_name, city, state, phone))
            mysql.connection.commit()
            return redirect((url_for('locations')))

    cursor = mysql.connection.cursor()

    cursor.execute(
        'SELECT location_id, location_name, capacity, street_address, street_name, city, state, phone FROM locations')
    data = cursor.fetchall()

    return render_template('locations.html', output_data=data)


# VOLUNTEER EDIT

@app.route('/locations/location_edit/<int:location_id>', methods=['POST'])
def location_edit(location_id):
    print('------- method called = LOCATION EDIT -------')

    if 'edit' in request.form:
        print('EDIT STARTED')

        # Get data from the update form

        location_name = request.form['before_lname']
        capacity = request.form['before_capacity']
        street_address = request.form['before_saddress']
        street_name = request.form['before_sname']
        city = request.form['before_city']
        state = request.form['before_state']
        phone = request.form['before_phone']

        # Update query using animal_id
        query = 'UPDATE locations SET location_name=%s, capacity=%s, street_address=%s, street_name=%s, city=%s, state=%s, phone=%s  WHERE location_id = %s;'

        # Query variables to be updated
        data = (location_name, capacity, street_address,
                street_name, city, state, phone, location_id)

        # Create cursor and execute SQL query
        cursor = mysql.connection.cursor()
        cursor.execute(query, data)

        # Commit SQL Changes
        mysql.connection.commit()

        print('EDIT COMPLETE')
        # Refresh page
        return redirect(url_for('locations'))

    print('RENDER INITIAL EDIT TEMPLATE')
    query = 'SELECT location_id, location_name, street_address, street_name, city, state, phone FROM locations WHERE location_id = %s;'
    var = (location_id,)
    # Create cursor and execute SQL query
    cursor = mysql.connection.cursor()
    cursor.execute(query, var)

    # Commit SQL Changes
    mysql.connection.commit()

    data = cursor.fetchall()

    return render_template('location_edit.html', output_data=data)


# LOCATION DELETE

@app.route('/locations/delete/<int:location_id>', methods=['POST'])
def delete_location(location_id):
    print('------- method called = LOCATION DELETE -------')
    query = 'DELETE FROM locations WHERE location_id = %s'
    data = (location_id,)

    cursor = mysql.connection.cursor()
    cursor.execute(query, data)
    mysql.connection.commit()

    return redirect(url_for('locations'))


@app.route('/link_foster', methods=['GET'])
def link_foster():

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT animal_id, volunteer_id FROM animals_volunteers')

    data = cursor.fetchall()
    return render_template('link_foster.html', output_data=data)


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113))
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port, debug=True)
