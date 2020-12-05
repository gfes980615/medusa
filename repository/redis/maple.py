from database.redis import r


def redis_cache_maple_bulletin(items):
    for item in items:
        r.set(item.url, 'true')
