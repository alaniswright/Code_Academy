from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a pet</h1>
  <p>Browse through the links below to find your new furry friend: </p>
  <ul>
  <li><a href='animals/dogs'>Dogs</a></li>
  <li><a href='animals/cats'>Cats</a></li>
  <li><a href='animals/rabbits'>Rabbit</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += "<ul>"
  for index, pet in enumerate(pets[pet_type]):
    html += "<li><a href='" + pet_type + "/" + str(index) + "'>" + pet["name"] + "</a></li>"
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  html = '<h1>' + pet['name'] + '</h1>'
  html += '<img src="' + pet['url'] + '"></img>'
  html += '<p>' + pet['description'] + '</p>'
  html += "<ul><li>Breed: " + pet['breed'] + "</li><li>Age: " + str(pet['age']) + "</li></ul>"
  return html