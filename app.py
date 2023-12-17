from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_greetings.db'
db = SQLAlchemy(app)

class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Greeting %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'World')
    greeting = Greeting(name=name)
    db.session.add(greeting)
    db.session.commit()
    return render_template('greet.html', name=name)

@app.route('/greetings')
def show_greetings():
    greetings = Greeting.query.all()
    return render_template('greetings.html', greetings=greetings)

@app.route('/greeting/<int:id>', methods=['DELETE'])
def delete_greeting(id):
    greeting = Greeting.query.get(id)
    if greeting:
        db.session.delete(greeting)
        db.session.commit()
        return {"message": "Greeting deleted successfully"}, 200
    return {"error": "Greeting not found"}, 404

@app.route('/greeting/<int:id>', methods=['PUT'])
def update_greeting(id):
    greeting = Greeting.query.get(id)
    if greeting:
        new_name = request.form.get('name')
        greeting.name = new_name
        db.session.commit()
        return render_template('greet.html', name=new_name)
    return {"error": "Greeting not found"}, 404

def initialize_testing_database():
    with app.app_context():
        db.create_all()
        # Add any necessa


if __name__ == '__main__':
    if app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///test_greetings.db':
        initialize_testing_database()
    app.run(debug=True)