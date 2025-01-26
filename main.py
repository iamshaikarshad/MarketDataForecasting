from app import create_app, db
from sqlalchemy import inspect
from app.models import NeopOutageData, Location, LocationDetail, Opzones

app = create_app()

# Create database tables if they don't exist
@app.before_request
def create_tables():
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        with app.app_context():
            db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
