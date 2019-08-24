import json
import config, models
from aiohttp import web, ClientSession


routes = web.RouteTableDef()


@routes.get('/posts')
async def posts(request):
    """Get and transform blog posts
    
    This function also stores the posts in cache, and retrieves if exists.
    """
    redis = request.app['redis']
    posts = []

    if await redis.execute('exists', 'posts'):
        posts_cache = await redis.execute('get', 'posts')
        posts = json.loads(posts_cache)
    else:
        blog_posts_url = '{api}/ghost/api/v2/content/posts'.format(api=config.GHOST_URL)
        limit = request.query.get('limit', 5)

        async with ClientSession() as session:
            response = await session.get(blog_posts_url, params={
                'key': config.GHOST_CONTENT_KEY,
                'limit': limit })

            data = await response.json()
            posts = [models.transform_post(post) for post in data['posts']]

            redis.execute('setex', 'posts', 86400, json.dumps(posts))
    
    return web.json_response(posts)
