from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"]) # Function decorator
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}) # Return list of contact objects in json format

@app.route("/create_contact", methods=["POST"]) # Function decorator
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name and email"}), 400
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email) # Create python class to create a new contact
    try:
        db.session.add(new_contact)
        db.session.commit() # Commit new contact to database
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "New contact created!"}), 201
        
# Entry point of program
if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Initialise database

    app.run(debug=True)
