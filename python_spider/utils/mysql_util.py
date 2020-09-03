#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "wang";

'''
mysql_utils
'''

import pymysql;

def get_connect_cursor():
    conn = pymysql.connect(host='localhost', user='root', passwd='root', db='hqyj', charset='utf8');  # 连接器
    return conn,conn.cursor();

def execute_insert_update_delete(cursor,sql):
    result = cursor.execute(sql);
    return result;

def execute_query(cursor, sql):
    cursor.execute(sql);
    return cursor.fetchall();

def commit_(conn):
    conn.commit();

def close_connect_cursor(conn, cur):
    cur.close();
    conn.close();