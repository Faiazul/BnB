from app import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, success, failed
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)

    booking = db.relationship('Booking', back_populates='payments')

    def __repr__(self):
        return f'<Payment {self.id} - Booking {self.booking_id} - {self.status}>'
