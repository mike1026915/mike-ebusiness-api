# -*- coding:utf-8 -*-  
from flask import Flask
from flask_cors import CORS
from flask_restful  import Resource, Api, reqparse
from model.product import Product
from model.order import Order
from model.orderhasproduct import OrderHasProduct
from model.db_init import db_init, db

from config import config


app = Flask(__name__, static_url_path='/static')
CORS(app)
app.config.from_object(config['default'])
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
db_init(app)
api = Api(app)

class ProductEndpoint(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('pid', type=int, help='product id')

        args = parser.parse_args()

        pid = args['pid']
    
        if not pid:
            products = Product.query.all()
        else:
            products = Product.query.filter_by(id=pid)

        products = [p.data for p in products]
        print(products)

        return products

class OrderEndpoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('phone', type=str, help='phone')
        parser.add_argument('address', type=str, help='address')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('bankAccount', type=str, help='bank account')
        parser.add_argument('itemList', type=list, help='item list', location="json")
        args = parser.parse_args()
        print(args)
        
        with app.app_context():
            order = Order(args['name'], args['address'], args['phone'], args['email'], args['bankAccount'])
            order.save_to_db()
            for pid in args['itemList']:
                ohp = OrderHasProduct(order.data['id'], pid, 1)
                ohp.save_to_db()

            return order.id

with app.app_context():
    try:
        db.drop_all()
    except: 
        pass
    try:
        db.create_all()
    except Exception as e:
        print(e)

    products = Product.query.all()
    if len(products) == 0:
        try:
            img_url = 'https://cf-assets2.tenlong.com.tw/products/images/000/130/414/original/9789864776283.jpg?1551941737'
            p1 = Product(u'萌貓投資偵探所', 100, 264, u'商周出版', u'繁體中文', img_url, '9789864776283')
            p2 = Product(u'萌貓投資偵探所', 100, 264, u'商周出版', u'繁體中文', img_url, '9789864776283')
            p1.save_to_db()
            p2.save_to_db()
        except Exception as e:
            pass

#print(Product.query.all())

api.add_resource(ProductEndpoint,'/api/v1/product')
api.add_resource(OrderEndpoint,'/api/v1/order')

if __name__ == '__main__':
    app.run(debug = True)


