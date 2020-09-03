#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "wang";

import excel_util;
import random;

def write_excel():#使用工具类重构write_excel()生成表
    header = ["第一季度", "第二季度", "第三季度", "第四季度"]
    file_path = "D:\log\write_excel2.xlsx";
    body = list();
    for item in range(1, 10):
        line = list();
        for i in range(1, len(header) + 1):
            line.append(i * random.randint(1, 10));
        body.append(line);
    excel_util.create_excel(header, body, file_path);

if __name__ == "__main__":
    write_excel();


# import openpyxl;
# import random;

# def write_excel(): #单表格生成
#     # 获取 Workbook 对象
#     workbook = openpyxl.Workbook();
#     # 获取 sheet 对象
#     active_sheet = workbook.get_active_sheet();
#     # 操作数据
#     active_sheet.append(["第一季度", "第二季度", "第三季度", "第四季度"]);
#     for i in range(1,10):
#         active_sheet.append([i*random.randint(1,10),i*random.randint(1,10),
#                              i*random.randint(1,10),i*random.randint(1,10)])
#     #文件保存
#     workbook.save(filename="D:\log\write_excel.xlsx")