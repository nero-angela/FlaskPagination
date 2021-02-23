from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/all_image', methods=['GET'])
def get_all_image():
    image_list = list(db.cat.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'data': image_list})


@app.route('/image', methods=['GET'])
def get_pagination_image():
    size = int(request.args.get('size', 10))
    page = int(request.args.get('page', 1))

    n_skip = size * (page - 1)
    print(f'size : {size} / page : {page} / skip : {n_skip}')

    image_list = list(db.cat.find({}, {'_id': False}).skip(n_skip).limit(size))
    total = db.cat.count()
    print(f'total : {total}')
    print(image_list)

    return jsonify({'result': 'success', 'total': total, 'data': image_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
