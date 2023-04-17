from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text,
                       nullable=False)
    size = db.Column(db.Text,
                       nullable=False)
    rating = db.Column(db.Float,
                       nullable=False)
    image = db.Column(db.Text,
                      default='https://tinyurl.com/demo-cupcake',
                       nullable=False)
    
    def serialize(self):
        '''Returns Cupcake data as a dictionary which can be converted into JSON'''
        return {
            'id' : self.id,
            'flavor' : self.flavor,
            'size' : self.size,
            'rating' : self.rating,
            'image' : self.image
        }
    
    def __repr__(self):
        return f'<Cupcake: ID = {self.id}; Flavor = {self.flavor}; Size = {self.size}; Rating = {self.rating}; Image = {self.image}>'