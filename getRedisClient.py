import redis

#连接Redis服务器
class getRC():
    def getRedisClient():
        rdconn = redis.Redis(host='127.0.0.1', port=6379)
        return rdconn