import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps, loads



# creates an instance of flask and assign it to the app variable
app = Flask(__name__)


# ---------Environment variables-----------------------------------
app.config["MONGO_DBNAME"] = 'coworkingSpacesDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')


mongo = PyMongo(app)



# -----Home page. this will be the default function that will be called when the application is run-----
@app.route('/')
@app.route('/get_coworkingspaces')
def get_coworkingspaces():
    coworkingspaces = mongo.db.coworkingspaces.find()
    return render_template('home.html', cities=mongo.db.cities.find(), coworkingspaces=loads(dumps(coworkingspaces)))


# ------------------------Show results page------------------------
@app.route('/show_results', methods=['POST'])
def show_results():
    
     city_name = request.form['city_name'] 
     city_results = mongo.db.coworkingspaces.find({"city_name": (city_name)})
     
     
     return render_template('home.html', cities=mongo.db.cities.find(), coworkingspaces=loads(dumps(city_results)))



# ---------------------About page--------------------------------
@app.route("/about")
def about():
    return render_template("about.html")
  
  
  
# ---------------Add coworking spaces page-----------------------
@app.route('/add_coworkingspace')
def add_coworkingspace():
    return render_template('addspace.html', cities=mongo.db.cities.find())


    
@app.route('/insert_coworkingspace', methods=['GET', 'POST'])
def insert_coworkingspace():

    image_url = request.form.get("image_url") if request.form.get("image_url") is not None else "https://images.pexels.com/photos/7097/people-coffee-tea-meeting.jpg"

    coworkingspace = {
        'city_name':request.form.get('city_name'),
        'coworking_name':request.form.get('coworking_name'),
        'coworking_description': request.form.get('coworking_description'),
        'coworking_address': request.form.get('coworking_address'),
        'opening_hours':request.form.get('opening_hours'),
        'website_url':request.form.get('website_url'),
        'image_url': image_url
    }
    
    coworkingspaces = mongo.db.coworkingspaces
    coworkingspaces.insert_one(coworkingspace)
    return redirect(url_for('get_coworkingspaces'))
  
    

# ----------Edit, update and delete coworking space page----------------
@app.route('/edit_coworkingspace/<coworkingspace_id>')
def edit_coworkingspace(coworkingspace_id):
    the_coworkingspace =  mongo.db.coworkingspaces.find_one({"_id": ObjectId(coworkingspace_id)})
    all_cities =  mongo.db.cities.find()
    return render_template('editspace.html', coworkingspace=the_coworkingspace,
                           cities=all_cities)
                          
    
@app.route('/update_coworkingspace/<coworkingspace_id>', methods=["POST"])
def update_coworkingspace(coworkingspace_id):
    coworkingspaces = mongo.db.coworkingspaces
    
    image_url = request.form.get("image_url") if request.form.get("image_url") is not None else "https://images.pexels.com/photos/7097/people-coffee-tea-meeting.jpg"

    
    coworkingspaces.update( {'_id': ObjectId(coworkingspace_id)},
    {
        'city_name':request.form.get('city_name'),
        'coworking_name':request.form.get('coworking_name'),
        'coworking_description': request.form.get('coworking_description'),
        'coworking_address': request.form.get('coworking_address'),
        'opening_hours':request.form.get('opening_hours'),
        'website_url':request.form.get('website_url'),
        'image_url': image_url
    })
    return redirect(url_for('get_coworkingspaces'))



@app.route("/delete_coworkingspace/<coworkingspace_id>")
def delete_coworkingspace(coworkingspace_id):
    mongo.db.coworkingspaces.remove({'_id': ObjectId(coworkingspace_id)})
    return redirect(url_for('get_coworkingspaces'))



#--------------------------------Contact page----------------------------

@app.route('/contact_page', methods=['GET', 'POST'])
def contact_page():
    return render_template('contact.html')


    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            