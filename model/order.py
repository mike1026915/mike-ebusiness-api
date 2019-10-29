from model.db_init import db

class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(300))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    bank_account = db.Column(db.String(50))

    def __init__(self, name, address, phone, email, bank_account):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.bank_account = bank_account

    def __repr__(self):
        return '<Order %r>' % self.name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def data(self):
        return {
            'id': self.id,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'bank_account': self.bank_account,
        }