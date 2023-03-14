from __init__ import *

from flask import request
from flask_restful import Api, Resource, reqparse, abort
from flask_cors import CORS
from models.models import User, Exercise, Nutrition
from collections import defaultdict

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app

class UserResource(Resource):
    def get(self, id=None):
        if id is None:
            users = User.query.all()
            return {'users': [{'id': u.id, 'name': u.name} for u in users]}, 200
        else:
            user = User.query.get(id)
            if user is None:
                abort(404, message = "User not found")
            return {'id': user.id, 'name': user.name}, 200

    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="User name is required")
        args = parser.parse_args()

        user = User(name=args['name'])
        db.session.add(user)
        db.session.commit()

        return {'id': user.id, 'name': user.name}, 201

# TODO
# class UserAuth(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('username', required=True, help="Username is required")
#         parser.add_argument('password', required=True, help="Password is required")
#         args = parser.parse_args()

#         user = User.query.filter_by(username=args['username']).first()

#         if user is None or user.password != args['password']:
#             abort(401, message="Invalid username or password")

#         return {'token': 'TODO'}, 200

class ExerciseResource(Resource):
    def get(self, id=None):
        if id is None:
            exercises = Exercise.query.all()
            user_exercises = defaultdict(list)
            for e in exercises:
                user_exercises[str(e.user_id)].append({'id': e.id, 'name': e.name, 'duration': e.duration, 'calories': e.calories})
            response = {'users': {}}
            for user_id, exercise_list in user_exercises.items():
                response['users'][user_id] = exercise_list
            return response, 200
        exercise = Exercise.query.get(id)
        if exercise is None:
            abort(404, message="Exercise not found")
        return {'id': exercise.id, 'name': exercise.name, 'duration': exercise.duration, 'calories': exercise.calories}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True, help="User ID is required")
        parser.add_argument('name', required=True, help="Exercise name is required")
        parser.add_argument('duration', required=True, help="Exercise duration is required")
        parser.add_argument('calories', required=True, help="Exercise calories is required")
        args = parser.parse_args()

        user = User.query.get(args['user_id'])
        if user is None:
            abort(404, message="User not found")
        exercise = Exercise(name=args['name'], duration=args['duration'], calories=args['calories'], user_id=user.id)
        db.session.add(exercise)
        db.session.commit()

        return {'id': exercise.id, 'name': exercise.name, 'duration': exercise.duration, 'calories': exercise.calories}, 201

class NutritionResource(Resource):
    def get(self, id=None):
        if id is None:
            nutritions = Nutrition.query.all()
            user_nutritions = defaultdict(list)
            for n in nutritions:
                user_nutritions[str(n.user_id)].append({'id': n.id, 'name': n.name, 'calories': n.calories})
            response = {'users': {}}
            for user_id, nutrition_list in user_nutritions.items():
                response['users'][user_id] = nutrition_list
            return response, 200
        nutrition = Nutrition.query.get(id)
        if nutrition is None:
            abort(404, message="Nutrition not found")
        return {'id': nutrition.id, 'name': nutrition.name, 'calories': nutrition.calories}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True, help="User ID is required")
        parser.add_argument('name', required=True, help="Nutrition name is required")
        parser.add_argument('calories', required=True, help="Nutrition calories is required")
        args = parser.parse_args()
        user = User.query.get(args['user_id'])
        if user is None:
            abort(404, message="User not found")
        nutrition = Nutrition(name=args['name'], calories=args['calories'], user_id=user.id)
        db.session.add(nutrition)
        db.session.commit()

        return {'id': nutrition.id, 'name': nutrition.name, 'calories': nutrition.calories}, 201

class Analysis(Resource):
    def get(self):
        # TODO: Implement data analysis logic
        return {'analysis': 'TODO'}, 200


if __name__ == '__main__':
    app = create_app()
    api = Api(app)
    api.add_resource(UserResource, '/api/users', '/api/users/<int:id>')
    api.add_resource(ExerciseResource, '/api/exercises', '/api/exercises/<int:id>')
    api.add_resource(NutritionResource, '/api/nutrition', '/api/nutrition/<int:id>')
    api.add_resource(Analysis, '/api/analysis')
    app.run(debug=True)
