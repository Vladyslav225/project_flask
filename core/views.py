from crypt import methods
from flask import Flask, request, render_template, url_for, send_from_directory
from flask import Response, request, jsonify

from app import app

from core.models import User


#Основная страница
@app.route('/')
def main_page():
    return render_template('main_page.html')


#Каталог
@app.route('/catalogue')
def catalogue():
    data = request.args
    # print(data)
    return render_template('catalogue.html')


# Доствка
@app.route('/delivery')
def delivery():
    return render_template('delivery.html')


#Коллекции
@app.route('/collections')
def collections():
    return render_template('collections.html')

#Контакты
@app.route('/contacts')
def contacts():
    return render_template('contacts.html') 


#Винная карты
#TODO list wines
@app.route('/wine_list',  methods=['GET'])
def wine_list():

    # TODO get models with wine list
    # list_wine = [
    #     {
    #         'name': 'qqq',
    #         'price': 123
    #     }
    # ]

    some = User.objects

    return render_template('wine_list.html', n = some)

@app.route('/wine_list/', methods=['POST'])
def func():
    d = request.json
    # print(d)
    User.objects.create(**d)
    return jsonify(**d)


#Дегустация
@app.route('/tasting')
def tasting():
    return render_template('tasting.html')


# #TODO serializer users
# def serializer(models_object):
#     list_data = []
#     for object in models_object:
#         keys = object._db_field_map.keys()
#         dict_object = {}
#         for key in keys:
#             value =getattr(object, key)
#             if type(value) == BaseList:
#                 value = serializer(value)

#             else:
#                 if value:
#                     value = str(value).rstrip()

#             dict_object[key] = value

#         list_data.append(dict_object)

#     return list_data


# @app.route('/user/', methods=['POST'])
# def func():
#     d = request.json
#     # print(d)
#     User.objects.create(**d)
#     return jsonify(**d)


# @app.route('/user/')
# def get_list_user():
#     query_params = dict(request.args)
#     print(query_params)
#     # query page param
#     users = User.objects.filter(**query_params)
#     # pagination
#     # create serializer or use lib after
#     # return Response(users)
#     return jsonify(users)

# @app.route('/user/<id_user>')
# def get_user_by_id(id_user):
#     print('aaaaaaaaaaa')
#     print(id_user)
#     data = User.objects.get(id=id_user)
#     # FIX IT
#     # create serializer or use lib after
#     # data = serializer = Srializer(user)
#     # return Response(users)
#     return jsonify(data)


# @app.route('/user/<id_user>', methods=['DELETE'])
# def delete_user_by_id(id_user):
#     User.objects.get(id=id_user).delete()
#     # FIX it bad id
#     # create serializer or use lib after
#     # return Response(users)
#     return Response({'status': 'deleted'}, status=200)

# @app.route('/user/<id_user>', methods=['PUT'])
# def put_user_by_id(id_user):
#     # For rewrite obj
#     data = request.json
#     user = User.objects.get(id=id_user).update(**data)
#     # create serializer or use lib after
#     # return Response(users)
#     return Response(user, status=200)

# @app.route('/user/<id_user>', methods=['PATCH'])
# def patch_user_by_id(id_user):
#     # For one field or some
    
#     # FIX it bad data - request.json
#     data = request.json
#     user = User.objects.get(id=id_user).update(**data)
#     # create serializer or use lib after
#     # return Response(users)
#     return Response(user, status=200)

