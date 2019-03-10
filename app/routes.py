#Define de logic of the application
from app import app # app and app? : The first app is the package and the second app is the variable in __init__

@app.route('/') #first decorator
@app.route('/index') #seccond decorator
def index():
    return 'Hello, World!'