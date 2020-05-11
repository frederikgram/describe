""" """

from describe import app
from describe.processing.pipelines import on_startup

if __name__ == '__main__':
    on_startup()
    app.run()
