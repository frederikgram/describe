""" """

from describe import app
from describe.processing import pipelines

if __name__ == '__main__':
    pipelines.on_startup()
    app.run()
