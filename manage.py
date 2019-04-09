import os
from app import create_app, db

app = create_app()

conditionally = True

if conditionally:
    @app.route('/static/<path:path>')
    def static_path(path):
        return app.send_static_file(path)
    