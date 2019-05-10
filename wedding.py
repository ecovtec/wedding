from app import app, db
from app.models import Guest


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Guest': Guest}


