"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app.form import PropertyForm
from werkzeug.utils import secure_filename
from flask.helpers import flash
from app.models import Property
from app import db
import os


###
# Routing for your application.
###
@app.route('/property',methods=['POST','GET'])
def property():
    form = PropertyForm()
    if request.method == 'GET':
        return render_template('property.html',form=form)
    elif request.method == "POST":
        if form.validate_on_submit:
            title = form.title.data
            numBeds = form.bedrooms.data
            location = form.location.data
            price = form.price.data
            desc = form.description.data
            propertyType = form.houseType.data
            
            file = request.files['photo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            newProperty = Property(title,numBeds,location,price,desc,filename,propertyType)

            db.session.add(newProperty)
            db.session.commit()



            flash("Property Sucessfully added")
            return redirect(url_for('properties'))
        else:
            flash("Data entered not valid")


@app.route('/property/<propertyid>')
def propertyid():
    return render_template('property.html')

@app.route('/properties')
def properties():
    get_uploaded_properties()
    return render_template('properties.html')



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
def get_uploaded_properties():
    propertyList = Property.query.all()
    for p in propertyList:
        print(p.title)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
