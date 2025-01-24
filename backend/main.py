from flask import request, jsonify
from config import app, db
from models import Contact

# Entry point of program
if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Initialise database

    app.run(debug=True)
