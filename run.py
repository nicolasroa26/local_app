from app import app
import os

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port =port, debug=True)


from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)