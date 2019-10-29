from model.db_init import db

class OrderHasProduct(db.Model):
    __tablename__ = "orderproductrelation"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, )

    def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return '<OrderHasProduct %r>' % self.name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @property
    def data(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
        }