import logging;logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	retuen web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv = yeild from loop.create_server(app.make_handler(), '127.0.0.1',9000)
	logging.info('server started ar http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_level_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
