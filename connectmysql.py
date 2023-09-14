import pymysql

# สร้างฟังก์ชั่นเชือมต่อ


def connectdb():
    connection = pymysql.connect(
        host='bhf1chtp9awshsyetbec-mysql.services.clever-cloud.com',
        user='uu7fbjp9eelrhbpu',
        password='Z7MWbtqCaI6GtdNWl2lp',
        db='bhf1chtp9awshsyetbec',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor

    )
    return connection


# ทดสอบ connection
print(connectdb())
