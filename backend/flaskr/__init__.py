import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category



QUESTIONS_PER_PAGE = 10

def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    items = [item.format() for item in selection]
    current_items = items[start:end]
    return current_items


# run with
# $ export FLASK_APP=flaskr
# $ export FLASK_ENV=development
# $ flask run


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)


    ##TODO##
    # Set up CORS. Allow '*' for origins. 
    # Delete the sample route after completing the TODOs
    ########
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 
            'Content-Type, Authorization'
            )
        response.headers.add(
            'Access-Control-Allow-Methods', 
            'GET, POST, PATCH, DELETE, OPTIONS'
            )
        return response



    ##TODO##
    # Use the after_request decorator to set Access-Control-Allow
    ########
    
    
    
    
    ########
    # a placeholder homepage
    ########
    @app.route('/')
    def homepage():
        return jsonify({})
    


    ##TODO##
    # Create an endpoint to handle GET requests 
    # for all available categories.
    ########
    @app.route('/categories')
    def all_categories():
        try:
            categories = Category.query.order_by(Category.id).all()
            categories = [category.format() for category in categories]    
            return jsonify({
                'success': True,
                'categories': categories,
            })
        except:
            abort(404)
    # to check:
    # $ curl http://127.0.0.1:5000/categories



    ##TODO##
    # Create an endpoint to handle GET requests for questions,
    # including pagination (every 10 questions).
    # This endpoint should return a list of questions,
    # number of total questions, current category, categories.
    #
    # TEST: At this point, when you start the application
    # you should see questions and categories generated,
    # ten questions per page and pagination at the bottom of the screen for three pages.
    # Clicking on the page numbers should update the questions.
    ########
    @app.route('/questions', methods=['GET'])
    def all_questions():
        try:
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate(request, questions)
            categories = Category.query.order_by(Category.id).all()
            categories = [category.format() for category in categories]
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'categories': categories,
                #'current_category': 1
            })
        except:
            abort(404)
    # to check:
    # $ curl http://127.0.0.1:5000/questions
    
    
    
    ##TODO##
    # Create an endpoint to DELETE question using a question ID.
    #
    # TEST: When you click the trash icon next to a question, the question will be removed.
    # This removal will persist in the database and when you refresh the page.
    ########
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id==question_id).one_or_none()
            if question is None:
                abort(404)
            else:
                question.delete()
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate(request, questions)
            return jsonify({
                'success': True,
                'id': question.id,
                'questions': current_questions,
                'total_questions': len(questions),
                'categories': categories,
            })
        except:
            abort(422)
    # to check:
    # $ curl -X DELETE http://127.0.0.1:5000/questions/<question_id>
    
    

    ##TODO##
    # Create an endpoint to POST a new question,
    # which will require the question and answer text,
    # category, and difficulty score.
    #
    # TEST: When you submit a question on the "Add" tab,
    # the form will clear and the question will appear at the end of the last page
    # of the questions list in the "List" tab.
    ########
    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)
        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                difficulty=new_difficulty,
                category=new_category
            )
            question.insert()
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate(request, questions)
            return jsonify({
                'success': True,
                'id': question.id,
                'questions': current_questions,
                'total_questions': len(questions)
            })
        except:
            abort(422)
    # to check:
    # $ curl -X POST -H "Content-Type: application/json" -d '{"question":"who is the biggest bleh", "answer":"thog", "difficulty":"2", "category": "3"}' http://127.0.0.1:5000/questions
        
    

    ##TODO##
    # Create a POST endpoint to get questions based on a search term.
    # It should return any questions for whom the search term
    # is a substring of the question.
    #
    # TEST: Search by any phrase. The questions list will update to include
    # only question that include that string within their question.
    # Try using the word "title" to start.
    ########
    @app.route('/questions/search_result', methods=['POST'])
    def search_question():
        body = request.get_json()
        search = body.get('searchTerm', None)
        try:
            questions = Question.query.order_by(Question.id) \
                .filter(Question.question.ilike('%{}%'.format(search))).all()
            current_questions = paginate(request, questions)
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions)
            })
        except:
            abort(400)
    # to check:
    # $ curl -X POST -H "Content-Type: application/json" -d '{"search":"thing"}' http://127.0.0.1:5000/questions/search_result
    

    ##TODO##
    # Create a GET endpoint to get questions based on category.
    #
    # TEST: In the "List" tab / main screen, clicking on one of the
    # categories in the left column will cause only questions of that
    # category to be shown.
    ########
    @app.route('/categories/<int:category_id>')
    def one_category(category_id):
        try:
            categories = Category.query.order_by(Category.id).all()
            categories = [category.format() for category in categories]
            category = categories[category_id]
            questions = Question.query.filter(Question.category==category_id) \
                .order_by(Question.id).all()
            current_questions = paginate(request, questions)
            if category is None:
                abort(404)
            else:
                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(questions),
                    'categories': categories,
                    'current_category': category
                })
        except:
            abort(400)
    # to check:
    # $ curl http://127.0.0.1:5000/categories/<category_id>
    


    ##TODO##
    # Create a POST endpoint to get questions to play the quiz.
    # This endpoint should take category and previous question parameters
    # and return a random questions within the given category,
    # if provided, and that is not one of the previous questions.
    #
    # TEST: In the "Play" tab, after a user selects "All" or a category,
    # one question at a time is displayed, the user is allowed to answer
    # and shown whether they were correct or not.
    ########



    ##TODO##
    # Create error handlers for all expected errors
    # including 404 and 422.
    ########
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unable to process"
        }), 422
        
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400
        
    @app.errorhandler(405)
    def bad_method(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405
        
        

    return app

