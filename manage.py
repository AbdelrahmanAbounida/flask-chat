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
    """ development run """
    PORT = int(os.getenv('PORT', '5000'))
    app.run(port=PORT)



@cli.command("prod_run")
def prod_run():
    """ production run >> with docker """
    host = '0.0.0.0'
    port = int(os.getenv('PORT', 5000))
    workers = int(os.getenv('GUNICORN_WORKERS', '4'))  # Number of Gunicorn worker processes

    from gunicorn.app.base import BaseApplication

    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            config = {key: value for key, value in self.options.items()
                      if key in self.cfg.settings and value is not None}
            for key, value in config.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    options = {
        'bind': f'{host}:{port}',
        'workers': workers,
        'accesslog': '-',
        'loglevel': 'debug' 
    }

    StandaloneApplication(app, options).run()


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

# ollama run gemma:2b

# docker pull ollama/ollama
# docker run -d --gpus=all -p 11434:11434 --name ollama ollama/ollama