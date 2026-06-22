from taskmaster import create_app, db
from taskmaster.models import User, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Task': Task}

if __name__ == '__main__':
    app.run(debug=True)
