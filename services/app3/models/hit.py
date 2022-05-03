from database import db

class Hit(db.Model):
    __tablename__ = 'hits'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    url = db.Column(db.String, nullable=False)
    
    def format(self):
        return {
            'id': self.id,
            'url': self.url,
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

        return self.id

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
