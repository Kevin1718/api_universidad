import web # pip install web.py
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append ('Constant')

urls = (
    '/pageutec', 'application.controllers.pageutec.ArchivoUtec',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = False
    app.run()
