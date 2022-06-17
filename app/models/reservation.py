from .db import db

class Reservation(db.Model):
  __tablename__ = 'reservations'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'), nullable=False)
  start_date = db.Column(db.DateTime, nullable=False)
  end_date = db.Column(db.DateTime, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  total = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  updated_at = db.Column(db.DateTime, nullable=False)

  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'spot_id': self.spot_id,
      'start_date': self.start_date,
      'end_date': self.end_date,
      'price': self.price,
      'total': self.total,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }

    
