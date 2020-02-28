from flask import Flask
from getRedisClient import getRC
app = Flask(__name__)

# chouJiangEDredis：redis计数器名称
@app.route('/choujiang/<username>')
def chouJiang(username):
    amountL = 400  # 奖金总额度
    getrc = getRC.getRedisClient()
    if getrc.exists("chouJiangEDredis"):
        pass
    else:
        getrc.setnx("chouJiangEDredis", 0)  # 抽奖额度计数器（redis计数器名称为chouJiangEDredis）
    reseltchoujiangED = getrc.incrby("chouJiangEDredis", 20)
    if (reseltchoujiangED > amountL):
        writeLog("很抱歉，您- "+username+" 未中奖，奖金额度已用完。额度已到:"+str(reseltchoujiangED))
        return '很抱歉，您- %s 未中奖，奖金额度已用完。' % username
    else:
        writeLog("恭喜你，"+username+" 抽奖成功。额度到了 %s " % str(reseltchoujiangED))
        return '恭喜你， %s 抽奖成功。' % username


def writeLog(message):
    myLogFile = open("logChouJiang.log", mode='a+')
    myLogFile.writelines(message + "\n")


app.run()
