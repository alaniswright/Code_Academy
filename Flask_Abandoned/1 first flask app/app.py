# Import Flask class
from flask import Flask


# Create an instance of the flask class
"""
The value of __name__ depends on how the Python script is executed. 
If we run a Python script directly, such as with python app.py in the terminal, then __name__ is equal to the string '__main__'. 
On the other hand, if the script is being imported as a module into another Python script, then __name__ would be equal to its filename.
"""
app = Flask(__name__)

# Create an endpoint that returns "Hello World". Route requests from the root URL to the endpoint 
@app.route('/')
def home():
    return "Hello, World"

"""# Create an endpoint that returns "Reporter bio". Route requests from the /reporter path to the endpoint 
@app.route('/reporter')
def reporter():
  return "Reporter Bio"

# Render HTML
@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p>My first paragraph.</p>
    <a href="https://www.codecademy.com">CODECADEMY</a>
    '''

# Variables
# make any section of the path between the slashes into a variable
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'


@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.title().replace('-', ' ')}</h2>
  <a href="/">Return back to home page</a>
  '''"""
