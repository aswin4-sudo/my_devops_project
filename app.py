import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Configure PostgreSQL from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('POSTGRES_USER', 'default_user')}:{os.environ.get('POSTGRES_PASSWORD', 'default_password')}@{os.environ.get('POSTGRES_HOST', 'localhost')}:{os.environ.get('POSTGRES_PORT', '5432')}/{os.environ.get('POSTGRES_DB', 'default_db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Message Model
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    
    def __init__(self, message):
        self.message = message

def init_db():
    """Initialize database - create tables if they don't exist"""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created/verified")

@app.route('/')
def hello():
    messages = Message.query.with_entities(Message.message).all()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message_text = request.form.get('new_message')
    
    # Create new message and save to database
    new_message = Message(message=new_message_text)
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({'message': new_message_text})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)