import os
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.property import Property
from app.forms.property_form import PropertyForm
from app import db
from app.routes.utils import allowed_file
from flask import current_app
from werkzeug.utils import secure_filename

property_bp = Blueprint('property', __name__, template_folder='templates')

@property_bp.route('/properties')
def all_properties():
    properties = Property.query.order_by(Property.created_at.desc()).all()
    return render_template('home.html', properties=properties)

@property_bp.route('/properties/new', methods=['GET', 'POST'])
@login_required
def new_property():
    form = PropertyForm()
    if form.validate_on_submit():
        image = form.image.data
        image_data = None
        image_mimetype = None
        image_filename = None
        
        if image and allowed_file(image.filename):
            # Read the file data
            image_data = image.read()
            image_mimetype = image.mimetype
            image_filename = secure_filename(image.filename)

        new_prop = Property(
            title=form.title.data,
            description=form.description.data,
            location=form.location.data,
            price=form.price.data,
            area=form.area.data,
            city=form.city.data,
            max_guests=form.max_guests.data,
            status=form.status.data,
            image_data=image_data,
            image_mimetype=image_mimetype,
            image_filename=image_filename,
            user_id=current_user.id,
            host_id=current_user.id
        )
        
        db.session.add(new_prop)
        db.session.commit()
        flash("Property listed successfully.", "success")
        return redirect(url_for('property.all_properties'))
    
    return render_template('new_property.html', form=form)

@property_bp.route('/properties/<int:property_id>')
def property_detail(property_id):
    prop = Property.query.get_or_404(property_id)
    return render_template('property_detail.html', prop=prop)

@property_bp.route('/property/<int:property_id>')
@login_required
def view_property(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('property_details.html', property=property)

from io import BytesIO
from flask import send_file,abort

@property_bp.route('/image/<int:property_id>')
def property_image(property_id):
    property = Property.query.get_or_404(property_id)
    if not property.image_data:
        abort(404)
    return send_file(
        BytesIO(property.image_data),
        mimetype=property.image_mimetype
    )  