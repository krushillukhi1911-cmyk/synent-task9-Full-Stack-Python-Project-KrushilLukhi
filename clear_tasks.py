from taskmaster import create_app, db
from taskmaster.models import Task

app = create_app()

with app.app_context():
    # Delete all tasks from the database
    num_deleted = Task.query.delete()
    db.session.commit()
    print(f"Successfully deleted {num_deleted} tasks from the database.")
