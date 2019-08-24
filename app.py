from dotenv import load_dotenv
from handlers import routes
from aiohttp import web
import config, services
import aioredis
import asyncio


async def start_background_tasks(app):
    loop = asyncio.get_running_loop()
    
    app['redis'] = await aioredis.create_connection(config.REDIS_URL, loop=loop)


async def cleanup_background_tasks(app):
    pass


if __name__ == '__main__':
    load_dotenv(verbose=True)

    app = web.Application()
    app.add_routes(routes)

    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)

    web.run_app(app, host=config.HOST, port=config.PORT)
