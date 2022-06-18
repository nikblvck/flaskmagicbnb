from .db import db

class Spot(db.Model):
  __tablename__ = 'spots'

  id = db.Column(db.Integer, primary_key=True)
  home_type = db.Column(db.String(50), nullable=False)
  room_type = db.Column(db.String(50), nullable=False)
  total_occupancy = db.Column(db.Integer, nullable=False)
  total_beds = db.Column(db.Integer, nullable=False)
  total_bathrooms = db.Column(db.Integer, nullable=False)
  summary = db.Column(db.String(450), nullable=False)
  address = db.Column(db.String(100), nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  latitude = db.Column(db.Float, nullable=False)
  price = db.Column(db.Integer, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  house_style = db.Column(db.Integer, db.ForeignKey('houses.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
  updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

  images = db.relationship('Image', back_populates='spot', lazy=True)
  reviews = db.relationship('Review', back_populates='spot', lazy=True)

  def to_dict(self):
    return {
      'id': self.id,
      'home_type': self.home_type,
      'room_type': self.room_type,
      'total_occupancy': self.total_occupancy,
      'total_beds': self.total_beds,
      'total_bathrooms': self.total_bathrooms,
      'summary': self.summary,
      'address': self.address,
      'longitude': self.longitude,
      'latitude': self.latitude,
      'price': self.price,
      'owner_id': self.owner_id,
      'house_style': self.house_style,
      'created_at': self.created_at,

      'updated_at': self.updated_at,
      'images': [image.to_dict() for image in self.images],
      'reviews': [review.to_dict() for review in self.reviews],
      'has_amenities': [amenity.to_dict() for amenity in self.has_amenities],
    }
