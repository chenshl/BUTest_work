# coding:utf-8
# @author : csl
# @date   : 2018/07/05 11:58
# 数据库查询封装

import pymysql

class connect_mysql():

    def __init__(self):

        # 连接数据库
        try:
            self.connect = pymysql.Connect(
                host='192.168.1.240',
                port=3306,
                user='root',
                passwd='111111',
                db='jinvovo_bu',
                charset='utf8'
            )
        except Exception as e:
            print("连接数据库失败", e)

    # 连接操作
    def connect2mysql(self, complySql):

        try:
            # 获取游标
            self.cursor = self.connect.cursor()
            self.cursor.execute(complySql)
        except Exception as e:
            self.connect.rollback()
            print("事务处理失败。。。", e)
        else:
            self.connect.commit()
            self.mysql_result = self.cursor.fetchall()
            return self.mysql_result
            # return self.mysql_result
            print("事务处理成功。。。")
        finally:
            # 关闭游标，关闭连接
            self.cursor.close()
            self.connect.close()

if __name__ == "__main__":
    sql = "SELECT * FROM assert_flow_log WHERE user_id = '18716200006' ORDER BY id DESC;"
    result = connect_mysql().connect2mysql(sql)
    print(result)
    print(type(result))

