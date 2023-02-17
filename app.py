# importing libraries

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# creating the flask application and the database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
db = SQLAlchemy(app)

# function to initialize the database object

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task %r>' % self.id

# creating the tables

db.create_all()

# fetch the content (todo items) from the database or add new ones

@app.route('/api/todo', methods=['GET', 'POST'])
def api_todo():
    if request.method == 'POST':
        task_content = request.json['content']
        new_task = TodoItem(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            print(e)
            return jsonify({'success': False, 'error': 'There was an issue adding your task'})

    else:
        tasks = TodoItem.query.order_by(TodoItem.date_created).all()
        items = []
        for task in tasks:
            items.append({
                'id': task.id,
                'content': task.content,
                'completed': task.completed,
                'date_created': task.date_created.isoformat()
            })
        return jsonify(items)


# updating the todo items or deleting them

@app.route('/api/todo/<int:id>', methods=['PUT', 'DELETE'])
def api_todo_item(id):
    task = TodoItem.query.get_or_404(id)

    if request.method == 'PUT':
        task.content = request.json['content']

        try:
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            print(e)
            return jsonify({'success': False, 'error': 'There was an issue updating your task'})

    elif request.method == 'DELETE':
        try:
            db.session.delete(task)
            db.session.commit()
            return jsonify({'success': True})
        except Exception as e:
            print(e)
            return jsonify({'success': False, 'error': 'There was a problem deleting that task'})

# mark todo items as complete

@app.route('/api/todo/<int:id>/complete', methods=['PUT'])
def api_todo_complete(id):
    task = TodoItem.query.get_or_404(id)

    task.completed = True

    try:
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': 'There was an issue completing your task'})


# used for debugging the flask application in case of any errors

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port='9999')
