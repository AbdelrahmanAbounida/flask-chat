import os
import unittest
from flask.cli import FlaskGroup
from app import create_app, db
from rich.console import Console

from dotenv import load_dotenv
load_dotenv()


app = create_app(os.getenv('CURRENT_ENV') or 'default')
cli = FlaskGroup(app)
console = Console()


@cli.command("run the app")
def run():
    PORT = int(os.getenv('PORT', '5000'))
    app.run(port=PORT,debug=True)


@cli.command("recreate_db")
def recreate_db():
    """
    Recreates the database
    """
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()
    console.print("database has been recreated successfully", style="bold green")

@cli.command("create_db")
def create_db():
    """
    Create the database
    """
    db.drop_all()
    db.create_all()
    db.session.commit()
    console.print("database has been created successfully", style="bold green")


@cli.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()


# export FLASK_DEBUG=1
# export FLASK_APP=manage.py