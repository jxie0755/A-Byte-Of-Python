# Head First SQL

# Chapter 1
# Data and Tables: A place for everything

# 数据库是保存表和其他相关SQL结构的容器
# 在数据库查找信息的行为叫Query
# 数据库由表构成, 表则包含数据
# 表由行和列构成
# 列是储存在表中的一块数据, 一项分类信息
# 行是一组能够描述某个事物的列的集合
# 数据库中的所有表应该能以某种方式互相关联
# 数据库和表的名称不一定要大写


# 接受命令
# SQL关系型数据库管理系统 Relational Database Management System (RDBMS)


# 创建数据库
CREATE DATABASE gregs_list;
# 必须以分号结束
# 若重复创建则会收到错误信息:
# [HY000][1007] Can't create database 'gregs_list'; database exists

# 现在要告诉RDBMS进入/使用被建造出来的数据库
USE gregs_list;
# 现在开始做的每件事都在gregs_list数据库中进行

# 命名建议
# SQL本身不区分大小写, 但是建议命令用大写
# 名称不能包含空格, 可以用_替代空格
# 没有固定命名规则, 但是注意避免首字母大写
# [']符号被保留了, 有特殊作用, 建议省略


# 设定表 (同理也是不能重复创建)
CREATE TABLE doughtnut_list
(
    doughnut_name VARCHAR(10), # 可变字符,最多10个字符
    doughnut_type VARCHAR(6)
);


CREATE TABLE my_contacts
(
    last_name  VARCHAR(30),
    first_name VARCHAR(20) NOT NULL,
    # null表示空, 就像未打开的盒子, 可能装有任何事物, 所以null之间无法比较
    # 在数据类型之后标记 NOT NULL 表示不可为空
    # 如果设置了, 此后INSERT时必须包含这个列的值, 不然报错
    email      VARCHAR(50),
    gender     CHAR(1),
    birthday   DATE,
    profession VARCHAR(50),
    location   VARCHAR(50),
    status     VARCHAR(20) DEFAULT 'Single',
    # 可以设定默认值, 如果缺省的话
    interest   VARCHAR(100),
    seeking    VARCHAR(100)
);
# 注意! 不能随意追加列! 如果要追加, 可以删了旧表重建
# TODO 未来会有不破坏数据而改变表的方式


# 查看表 Describe
DESC my_contacts;
# 注意这里只提供列表的列名和数据类型, 并不会显示列表的数据内容


# 删除表 (删除表和表内的所有数据, 务必小心, 这里无法挽回)
# DROP TABLE my_contacts;


# 插入值
INSERT INTO my_contacts
(last_name, first_name, email, gender, birthday, profession, location, status, interest, seeking)
VALUES # 注意换行 (注意, VALUE和VALUES 都是可以的, 作用完全相同
       ('Anderson', 'Jillian', 'jill_anderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');
# 数据值得顺序必须和列的顺序完全一样!


# 其他Insert变体
# 改变列顺序
INSERT INTO my_contacts # 交换first和last name
(first_name, last_name, email, gender, birthday, profession, location, status, interest, seeking)
VALUES ('Gillian', 'Banderson', 'gill_banderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');

# 省略列名
INSERT INTO my_contacts # 交换first和last name
VALUES ('Baanderson', 'GGillian', 'ggill_baanderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');

# 选择性省略一部分列
INSERT INTO my_contacts
    (first_name, email, profession, location)
VALUES ('Pat', 'patpost@breakingpizza.com', 'Postal Worker', 'Princeton, NJ');


# Fruit table example
CREATE TABLE easy_drinks
(
    drink_name VARCHAR(20),
    main       VARCHAR(20),
    amount1    DECIMAL(4, 2),
    second     VARCHAR(20),
    amount2    DECIMAL(4, 2),
    directions VARCHAR(250)
);

# 另一种批量插入的形式
INSERT INTO easy_drinks
VALUES ('Blackthorn', 'tonic water', 1.5, 'pineapple juice', 1,
        'stir with ice, strain into cocktail glass with lemon twist'), # 这里接着用逗号分隔
       ('Blue Moon', 'soda', 1.5, 'blueberry juice', .75,
        'stir with ice, strain into cocktail glass with lemon twist'),
       ('Oh My Gosh', 'peach nectar', 1, 'pineapple juice', 1,
        'stir with ice, strain into shot glass'),
       ('Lime Fizz', 'Sprite', 1.5, 'lime juice', .75,
        'stir with ice, strain into cocktail glass'),
       ('Kiss on the Lips', 'cherrry juice', 2, 'apricot nectar', 7,
        'serve over ice with straw'),
       ('Hot Gold', 'peach nectar', 3, 'orange juice', 6,
        'pour hot orange juice in mug and add peach nectar'),
       ('Lone Tree', 'soda', 1.5, 'cherry juice', 0.75,
        'stir with ice, strain into cocktail glass'),
       ('Greyhound', 'soda', 1.5, 'grapefruit juice', 5, 'serve over ice, stir well'),
       ('Indian Summer', 'apple juice', 2, 'hot tea', 6, 'add juice to mug and top off with hot tea'),
       ('Bull Frog', 'iced tea', 1.5, 'lemonade', 5, 'serve over ice with lime\'s slice');
# 最后才用分号 # 记住数据中用引号要用\转义


# 主键
# 表中每一行都应该有一列（或几列）可以唯一标识自己
# 主键用来表示一个特定的行。
# 没有主键，更新或删除表中特定行就极为困难，因为你不能保证操作只涉及相关的行

# 表中的任何列都可以作为主键, 只要它满足以下条件:
# 任意两行都不具有相同的主键值；
# 每一行都必须具有一个主键值（主键列不允许 NULL 值）；
# 主键列中的值不允许修改或更新；
# 主键值不能重用（如果某行从表中删除，它的主键不能赋给以后的新行）
CREATE TABLE `customers`
(
    `cust_id`      CHAR(10) NOT NULL,
    `cust_name`    CHAR(50) NOT NULL,
    `cust_address` CHAR(50)  DEFAULT NULL,
    `cust_city`    CHAR(50)  DEFAULT NULL,
    `cust_state`   CHAR(5)   DEFAULT NULL,
    `cust_zip`     CHAR(10)  DEFAULT NULL,
    `cust_country` CHAR(50)  DEFAULT NULL,
    `cust_contact` CHAR(50)  DEFAULT NULL,
    `cust_email`   CHAR(255) DEFAULT NULL,
    PRIMARY KEY (`cust_id`) # 设置主键
);

# 注意反引号是mysql特色, 用于标注列名, 表名, 库名, 可以省略
# 但是如果这些命名与mysql保留字段冲突则用反引号可以避免矛盾
# 更好的建议是, 不要使用能产生冲突的命名, 然后避免使用反引号, 但是系统生成的代码必将使用反引号, 来保证避免冲突