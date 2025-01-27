from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"]) # Function decorator
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}) # Return list of contact objects in json format

# Entry point of program
if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Initialise database

    app.run(debug=True)
