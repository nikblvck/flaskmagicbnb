from .db import db

class Review(db.Model):
  __tablename__ = 'reviews'

  id = db.Column(db.Integer, primary_key=True)
  rating = db.Column(db.Integer, nullable=False)
  comment = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  spot_id = db.Column(db.Integer, db.ForeignKey('spots.id'), nullable=False)



  def to_dict(self):
    return {
      'id': self.id,
      'rating': self.rating,
      'comment': self.comment,
      'user_id': self.user_id,
      'spot_id': self.spot_id
    }
