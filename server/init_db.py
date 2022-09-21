import sys
from app import create_app, db

def main():
    app = create_app('development')

    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()

if __name__ == "__main__":
    main()