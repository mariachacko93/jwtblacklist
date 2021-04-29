from bson import ObjectId
from .extensions import mongo
from flask import Blueprint
from flask import jsonify, request
from bson.json_util import dumps

bp = Blueprint('books', __name__, url_prefix='/api/v1/book')


@bp.route('/bookadd', methods=['POST'])
def add_book():
    _json = request.json
    _book_name = _json['book_name']
    _author_name = _json['author_name']
    _pub_year = _json['pub_year']

    if _book_name and _author_name and _pub_year and request.method == 'POST':
        mongo.db.books.insert({'book_name': _book_name, 'author_name': _author_name, 'pub_year': _pub_year})
        resp = jsonify("Book Added Successfully")
        resp.status_code = 201
        return resp

    else:
        return not_found()


@bp.route('/booklist', methods=['GET'])
def list_book():
    book_name = request.headers.get('book_name')
    author_name = request.headers.get('author_name')
    if book_name or author_name:
        output = []
        for q in mongo.db.books.find({"$or": [{'book_name': book_name}, {'author_name': author_name}]}):
            output.append({'book_name': q['book_name'], 'author_name': q['author_name'], 'pub_year': q['pub_year']})
        if len(output) != 0:
            return jsonify({'result': output})
        else:
            return jsonify({'result': 'No Results'})
    else:
        book_list = mongo.db.books.find()
        resp = dumps(book_list)
        return resp


@bp.route('/booklist/<id1>', methods=['GET'])
def list_book_id(id1):
    book_list = mongo.db.books.find_one({'_id': ObjectId(id1)})
    resp = dumps(book_list)
    return resp


@bp.route('/bookdelete/<id1>', methods=['DELETE'])
def delete_book(id1):
    mongo.db.books.delete_one({'_id': ObjectId(id1)})
    resp = jsonify("Book deleted successfully")
    resp.status_code = 204
    return resp


@bp.route('/bookupdate/<id1>', methods=['PUT', 'PATCH'])
def update_book(id1):
    _id = id1
    _json = request.json
    if _json and (request.method == 'PUT' or request.method == 'PATCH'):
        mongo.db.books.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                  {'$set': _json})
        resp = jsonify("Book Updated Successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()


@bp.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
