import uvloop

import aiohttp_jinja2
import jinja2
from aiohttp import web
from news_aggregator.routes import setup_routes
from config.config_loader import ConfigLoader
from aiopg.sa import create_engine


class Application:
    @staticmethod
    def run():
        uvloop.install()
        app = web.Application()
        app['config'] = ConfigLoader.load_config()
        aiohttp_jinja2.setup(
            app=app,
            loader=jinja2.PackageLoader('news_aggregator', 'templates')
        )
        setup_routes(app)
        app.on_startup.append(init_pg)
        app.on_cleanup.append(close_pg)
        web.run_app(
            app=app,
            host='127.0.0.1',
            port=5050
        )


async def init_pg(app):
    conf = app['config']
    engine = create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()


if __name__ == '__main__':
    application = Application()
    application.run()
