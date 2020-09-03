#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "wang";

'''
mysql_test
'''

# import pymysql;
import mysql_util;

# 使用mysql_util重构#单插入
def inset_resource():
    conn, cur = mysql_util.get_connect_cursor();#获取连接器、游标
    sql = "insert into resource (resource_uri, resource_name, permission) values ('www','wang2', '/baidu')";
    mysql_util.execute_insert_update_delete(cur,sql);#执行
    mysql_util.commit_(conn);#提交
    mysql_util.close_connect_cursor(conn,cur);#关闭

def query_resource():  # 重构 单查询
    conn, cur = mysql_util.get_connect_cursor();  # 获取连接器、游标
    sql = "select * from user";
    result = mysql_util.execute_query(cur, sql);  # 执行
    print(result);
    # mysql_util.commit_(conn);  # 提交
    mysql_util.close_connect_cursor(conn, cur);  # 关闭

if __name__ == "__main__":
    # inset_resource();
    query_resource();


# def inset_resource():#单插入
#     conn = pymysql.connect(host='localhost',user='root',passwd='root',db='hqyj',charset='utf8');#连接器
#     cur = conn.cursor();#获取游标
#     result = cur.execute("insert into resource (resource_uri, resource_name, permission) values ('www','wang', 'baidu')");#执行SQL
#     print(result);
#     conn.commit();#提交
#     cur.close();
#     conn.close();

# def query_resource():  # 单查询
#     conn = pymysql.connect(host='localhost', user='root', passwd='root', db='hqyj', charset='utf8');  # 连接器
#     cur = conn.cursor();  # 获取游标
#     result = cur.execute("select * from user");  # 执行SQL
#     print(cur.fetchall());#获取结果集
#     conn.commit();#提交
#     cur.close();
#     conn.close();