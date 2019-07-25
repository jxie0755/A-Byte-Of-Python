# Sams Teach yourself SQL in 10 Mins
# Chapter 2 Search Data


USE sams_teach_sql;

# The SELECT Stament

# 为了使用 SELECT 检索表数据，必须至少给出两条信息
# 想选择什么，
# 以及从什么地方选择


# 检索单个列 (未必排序了)
SELECT prod_name
FROM products;


# 检索多个列
SELECT prod_id, prod_name, prod_price
FROM products;


# 检索所有列
# 与python相同, *表示所有内容
SELECT *
FROM customers;
# 一般而言，除非你确实需要表中的每一列，否则最好别使用*通配
# 建议慎用, 会降低性能, 只找需要的内容



# 检索不同的值 (去重)
SELECT DISTINCT vend_id
FROM products;
# DISTINCT 关键字作用于所有的列，不仅仅是跟在其后的那一列
SELECT DISTINCT vend_id,
                prod_price # 这里只要价格不同就会列出, 可能导致vent_id出现重复
FROM products;


# 限制结果
SELECT prod_name
FROM products
LIMIT 5; # 前5行

SELECT prod_name
FROM products
LIMIT 5 OFFSET 5;
# 从第五行开始的前5行, 因为一共就9中产品, 所以只返回4行, 不会溢出
# 注意, 行数是从0开始算的

SELECT prod_name
FROM products
LIMIT 5, 5;
# MySql和MariaDB 的简化语法
# 以上全是按照prod_id排序执行的挑选

# 注释风格
# #号
-- --号
/* 多行
   注释 */

