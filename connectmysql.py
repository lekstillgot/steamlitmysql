import pymysql

# สร้างฟังก์ชั่นเชือมต่อ


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='testpython',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor

    )
    return connection


# ทดสอบ connection
print(connectdb())
