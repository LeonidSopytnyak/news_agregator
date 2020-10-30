import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('signin.html')
async def user_registration(request):
    data = await request.post()
    print(await request.post())
