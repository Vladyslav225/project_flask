from flask import Flask, request, render_template, url_for
from flask.json import jsonify
from jinja2 import Markup

from app import app


#Основная страница
@app.route('/')
@app.route('/home')
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
@app.route('/wine_list')
def wine_list():
    return render_template('wine_list.html')


#Дегустация 
@app.route('/tasting')
def tasting():
    return render_template('tasting.html')
