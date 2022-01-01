from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def splash():
        return 'Hello, World!'

    @app.route('/sessions', method='GET')
    def check_existing_session():
        # check if user has an existing session based on cookies
        return {
            'session_id': ''
        }

    @app.route('/sessions', method='POST')
    def create_new_session():
        # create new game/session
        # return session id so client knows what socket namespace to join
        return {
            'session_id': ''
        }

    return app