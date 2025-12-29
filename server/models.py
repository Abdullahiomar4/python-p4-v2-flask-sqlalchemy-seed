from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Pet {self.id}, {self.name}, {self.species}>"
