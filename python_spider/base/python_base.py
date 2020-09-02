#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "wang";
'''
python注释
'''

#导包
import re,math;
import mysql_util;
# import utils.mysql_util;

# ----------------------输入输出----------------------
# a=input();
# print(a);
a=1996;
b = "wangjianbiao";
print(a);
print("hello world");
print("hello","world","and wang");
print("birthday %s"%a);
print("birthday %s"%(a,));
print("birthday %s - %s"%(a,b));

# ----------------------数据类型----------------------
a = 11;
print("a = %s,数据类型：%s"%(a, type(a)));
a = 11.11;
print("a = %s,数据类型：%s"%(a, type(a)));
a = None;
print("a = %s,数据类型：%s"%(a, type(a)));
a = 1 > 2;
print("a = %s,数据类型：%s"%(a, type(a)));
a = ['aaa',32,32.1];
print("a = %s,数据类型：%s"%(a, type(a)));
a  = ('AAA',33,12.3);
print("a = %s,数据类型：%s"%(a, type(a)));
a = {"name":"wangjianbiao","birthday":"1996"}
print("a = %s,数据类型：%s"%(a, type(a)));
a = set(["aaa",True,None,222,23.45]);
print("a = %s,数据类型：%s"%(a, type(a)));

# ----------------------运算符----------------------
print((2+44/12)*3);
print(15 // 2); # 地板除，取整
print(12 % 5);
print(2 ** 3);

# ----------------------字符串----------------------
print(u'王建');
print(r'王建');
print(b'wangjian');

# ----------------------ASCII转换----------------------
print("98-->%s;A-->%s"%(chr(98),ord('a')));

# ----------------------encode && decode----------------------
print("aaa".encode("ascii"));
print("王建标".encode("utf-8"));
print(b'aaa'.decode("ascii"));
print(b'\xe7\x8e\x8b\xe5\xbb\xba\xe6\xa0\x87'.decode("utf8"));

# ----------------------function----------------------
print(len("aaa"));
print(len("中文")); # 2，对于str计算字符数
print(len("aaa".encode("utf-8")));
print(len("中文".encode("utf-8"))); # 6，对于bytes计算字节数
print("sdfswangfnjnfdjjwang".replace("wang", "---"));# 替换
print("sdfswangfnjnfdjjwang".find("wang"));
print("sdfswangfnjnfdjjwang".rfind("wang"));
print("cdacsacd".isspace());# 是否为空
print("%s ---- %3d ---- %04d"%(11, 4, 3)); # 2d（不足两位左边补空格）、02d（不足两位，左边补0）
print("%f ---- %.2f"%(32.3242, 42123.797987897)); # .2f（保留两位小数，四舍五入）
print("%x"%333); # 格式化为十六进制
print("%d %% %d"%(3, 5));# %%转义输出%
l = list(range(1, 10));
print(l);
print(list("%d" % x for x in range(1, 10)));
print("Hi {0}, 成绩提高了{1:.1f}%".format("小明", 1.254));
print("Hi {0}, 成绩提高了{1}%".format("小明", 1.254));
print("Hi {0}, 成绩提高了{1}%".format("小明", "%.1f"%1.254));
print("=".join(["cdsac","cdsa","dewqd"]));

# ----------------------正则表达式----------------------
email_re = "^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$";
if re.match(email_re, "1071590730@qq.com"):
    print("ok");
else:
    print("error");
# ---- 切分字符串 ----
print("a b c".split(" "));
print(re.split(r'\s+',"a b c"));
print(re.split(r"[\s\,\;]+", "a,b;; c   d"));
# ---- 分组 ----
match = re.match(r'^(\d{3})-(\d{3,8})$', "020-123456")
print(match.group());
print(match.group(0));
print(match.group(1));
print(match.group(2));
new_line = r'截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例653例(其中境外输入112例），' \
    r'累计治愈出院626例，死亡3例，目前在院隔离治疗24例，964人尚在接受医学观察';
new_line_re = r'^截至9月2日0时，全省累计报告新型冠状病毒肺炎确诊病例(\d+)例\(其中境外输入(\d+)例\），' \
    r'累计治愈出院(\d+)例，死亡(\d+)例，目前在院隔离治疗(\d+)例，(\d+)人尚在接受医学观察$';
new_line_math = re.match(new_line_re, new_line);
print(new_line_math.group(0));
print(new_line_math.group(1));
print(new_line_math.group(2));
print(new_line_math.group(3));
print(new_line_math.group(4));
print(new_line_math.group(5));
print(new_line_math.group(6));
new_line_compile = re.compile(new_line_re);
print(re.search(new_line_compile, new_line).group(1));
print(re.search(new_line_compile, new_line).group(2));
print(re.search(new_line_compile, new_line).group(3));
print(re.search(new_line_compile, new_line).group(4));
print(re.search(new_line_compile, new_line).group(5));
print(re.search(new_line_compile, new_line).group(6));
print(re.match(r"^(\d+?)(0*)$", "102300").groups()); # ('1023', '00')

# ---- list & tuple ----
l = ["cdsa", 32, 33.2, None, True];
print(l);
l2 = list(range(1, 10));
print(l2);
l.append("wang");
print(l);
l.insert(2, "wangjianbiao");
print(l);
l.pop();
print(l);
l.pop(2);
print(l);
l.append(l2);
print(l);
l += l2;
print(l);
l[0] = "qqqq";
print(l);
l = list(range(1, 10));
t = ("aaa", 12, 12.2, True, None, l);
l[1] = 22;
print(t);
t2 = tuple(range(1,10));
print(t2);
print((1));
print((1,))

# ---- dict & set ----
d = {"name":"wangjianbiao","age":33};
print(d.get("name1", "aaaaa"));
d["name"] = "wang";
d["aaa"] = "111dasa";
print(d);
d.pop("aaa");
print(d);
print(len(d));
s = set(["cds", True, None, 212, 22.3]);
s2 = {"cds", 212, 22.22, "asdasfdg"};
s.add("wang");
print(s);
# s.pop();
print(s);
# s.remove("cds");
print(s);
print(s & s2);
print(s | s2);

# ----------------------判断语句----------------------
a = 10;
if a <= 10:
    print("aaa");
elif 10 <= a <= 20:
    print("bbb");
else:
    print("ccc");
a, b, c = 1, 3, 2;
print(a if b > c else c);

# ----------------------循环语句----------------------
l = list(range(1, 10));
for i in l:
    print(i);
i = 0;
while (i < 10):
    print(i);
    i += 1;

# ----------------------函数----------------------
def test(a):
    a += 3;
    return a;

print(test(8));
f = test(8);
print(f);

def test_2(x, y="wangjianbiao"):
    print(x, y);

def test_3(*num):
    count = 0;
    for i in num:
        count += i;
    return count;

def test_4(name, **kv):
    if "city" in kv:
        print("name:%s, city:%s"%(name,kv.get("city")));
    else:
        print("name:%s, city:%s" % (name, "sichuan"));

def test_5(name, *, city):
    if not isinstance(name, (str,)):
        raise TypeError("Type error");
    print("name:%s, city:%s"%(name, city));


if __name__ == "__main__":
    test_2("hello", "wang");
    test_2("hello");
    print(test_3());
    print(test_3(*list(range(1, 9))));
    print(test_3(1,2,3,4,5));
    test_4("wangjianbiao", **{"age":33});
    test_4("wangjianbiao", **{"age":33,"city":"cd"});
    test_5("wangjianbiao", city="cd");
    # test_5(111, city="cd");

# ----------------------内置函数----------------------
print(int("22")); # 数据类型转换函数，注意，如果定义变量名和函数名一样，则不会调用该函数，会报错
print(float("22.2"));
print(str(22));
print(abs(-111)); # abs函数，求绝对值
print(max(12, 34, 123.4)); # max函数，求最大值
print(min(-21, -11, 0, 22.3)); # min函数，求最小值
print(" aa bb  cc  ".strip()); # 字符串去前后空格
print("['6K-8K']".strip('[\'\']')); # 移除字符串头尾指定的字符
print(hex(12)); # hex函数，将十进制数转十六进制
print(math.sqrt(3)); # 求平方根
print(sum(range(1, 101))); # 求和
print(sum(list(range(101))));
print("cdaDcdsa".capitalize()); # 将字符串第一个字符变成大写，其他小写