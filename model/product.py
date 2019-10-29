from model.db_init import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    publisher = db.Column(db.String(50))
    language = db.Column(db.String(10))
    image_url = db.Column(db.String(1024))
    isbn = db.Column(db.String(20))
    category = db.Column(db.String(10))

    def __init__(self, name, price, pages, publisher, language, image_url, isbn):
        self.name = name
        self.price = price
        self.pages = pages
        self.publisher = publisher
        self.language = language
        self.image_url = image_url
        self.isbn = isbn

    def __repr__(self):
        return '<Product %r>' % self.name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def find_by_id(self, goodId):
        return db.session.query.filter_by(goodId=goodId).first()

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'publisher': self.publisher,
            'language': self.language,
            'pages': self.pages,
            'isbn': self.isbn,
            'imgUrl': self.image_url
        }