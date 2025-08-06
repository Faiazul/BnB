from app import db
from datetime import datetime
from flask import url_for
from io import BytesIO

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200))  
    price = db.Column(db.Float)  
    photos = db.Column(db.Text)  
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    max_guests = db.Column(db.Integer)
    status = db.Column(db.String(20), default='active')  # active, inactive, pending, rejected

    area = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    image_data = db.Column(db.LargeBinary)
    image_mimetype = db.Column(db.String(50)) 
    image_filename = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def get_image_url(self):
        if self.image_data:
            return url_for('property.property_image', property_id=self.id)
        return None
    def __repr__(self):
        return f'<Property {self.title}>'
