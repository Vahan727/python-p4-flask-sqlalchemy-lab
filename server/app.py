#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    resp = f''
    resp += f'<ulID: {animal.id}</ul>'
    resp += f'<ul>Name: {animal.name}</ul>'
    resp += f'<ul>Species: {animal.species}</ul>'
    resp += f'<ul>Zookeeper: {animal.zookeeper.name}</ul>'
    resp += f'<ul>Enclosure: {animal.enclosure.environment}</ul>'

    return make_response(resp)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    resp = f''
    resp += f'<ul>ID: {zookeeper.id}</ul>'
    resp += f'<ul>Name: {zookeeper.name}</ul>'
    resp += f'<ul>Birthday: {zookeeper.birthday}</ul>'

    for animal in zookeeper.animals:
        resp += f'<ul>Animal: {animal.name}</ul>'

    return make_response(resp)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    resp = f''
    resp += f'<ul>ID: {enclosure.id}</ul>'
    resp += f'<ul>Environment: {enclosure.environment}</ul>'
    resp += f'<ul>Open to Visitors: {enclosure.open_to_visitors}</ul>'

    for animal in enclosure.animals:
        resp += f'<ul>Animal: {animal.name}</ul>'
    
    return make_response(resp)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
