from router.router import init_api
from router.maple import init_maple_api, init_redis_data
from router.english import init_english_api

if __name__ == "__main__":
    init_redis_data()
    init_api()
    init_maple_api()
    init_english_api()
