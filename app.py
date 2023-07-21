from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://essienbenjamin:yankees44@localhost:5432/events'

db = SQLAlchemy(app)
ma = Marshmallow(app)


# Event Model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id


# Event Schema
class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'user_id')


event_schema = EventSchema()
events_schema = EventSchema(many=True)


# Home Page
@app.route('/')
def home():
    return "Welcome to the Event Tracker App!"


# Create a new event
@app.route('/events', methods=['POST'])
def add_event():
    title = request.json['title']
    description = request.json['description']
    user_id = request.json['user_id']

    new_event = Event(title, description, user_id)

    db.session.add(new_event)
    db.session.commit()

    return event_schema.jsonify(new_event)


# Get all events that have been created
@app.route('/events/all', methods=['GET'])
def get_all_events():
    events = Event.query.all()
    return events_schema.jsonify(events)


# Get all events for a specific user
@app.route('/events/user/<int:user_id>', methods=['GET'])
def get_user_events(user_id):
    events = Event.query.filter_by(user_id=user_id).all()
    return events_schema.jsonify(events)


# Get a specific event
@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    return event_schema.jsonify(event)


# Delete a specific event
@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    return event_schema.jsonify(event)


# Search events by title or description
@app.route('/events/search', methods=['GET'])
def search_events():
    search_term = request.args.get('term')

    events = Event.query.filter(
        (Event.title.contains(search_term)) | (Event.description.contains(search_term))
    ).all()

    return events_schema.jsonify(events)


