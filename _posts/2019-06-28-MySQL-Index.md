---
layout: post
title:  "MySQL Index"
subtitle: 'MySQL Index and SQL Recap'
date:   2019-06-28 19:30:40 +0800
author: "DoNG"
catalog: true
tags: 
    - MySQL
    - database
    - index
    - sql
---

## Range Optimization <sup>[1]</sup>

For a `BTREE` index, an interval might be usable for conditions **combined with `AND`**, where each condition compares a key part with a constant value using `=, <=>, IS NULL, >, <, >=, <=, !=, <>, BETWEEN, or LIKE 'pattern' (where 'pattern' does not start with a wildcard)`. An interval can be used as long as it is possible to determine a single key tuple containing all rows that match the condition (or two intervals if <> or != is used).

The optimizer attempts to use additional key parts to determine the interval as long as the comparison operator is `=, <=>, or IS NULL`. If the operator is `>, <, >=, <=, !=, <>, BETWEEN, or LIKE`, **the optimizer uses it but considers no more key parts**. For the following expression, the optimizer uses = from the first comparison. It also uses >= from the second comparison but considers no further key parts and does not use the third comparison for interval construction:
```sql
key_part1 = 'foo' AND key_part2 >= 10 AND key_part3 > 10

the single interval is 
('foo',10,-inf) < (key_part1,key_part2,key_part3) < ('foo',+inf,+inf)
```

总结，联合索引中从左到右只用一次range。

The `key_len` specifies the number of **bytes** that MySQL uses from the key.
Indexes are always used left_to_right.<sup>[2]</sup>

## Index Merge Optimization <sup>[3]</sup>

>以SELECT * FROM TB1 WHERE c1="xxx" AND c2=""xxx" 为例：
1、      当c1列和c2列选择性较高时，按照c1和c2条件进行查询性能较高且返回数据集较小，再对两个数据量较小的数据集求交集的操作成本也较低，最终整个语句查询高效；
2、      当c1列或c2列选择性较差且统计信息不准时，比如整表数据量2000万，按照c2列条件返回1500万数据，按照c1列返回1000条数据，此时按照c2列条件进行索引扫描+聚集索引查找的操作成本极高(可能是整表扫描的百倍消耗)，对1000条数据和1500万数据求交集的成本也极高，最终导致整条SQL需要消耗大量CPU和IO资源且相应时间超长，而如果值使用c1列的索引，查询消耗资源较少且性能较高。

## 最左匹配原则
Good Ref: https://www.cnblogs.com/developer_chan/p/9223671.html

- 在最佳左前缀法则中，如果最左前列（带头大哥）的索引失效，则后面的索引都失效。<sup>[4]</sup>

### About Explain
in `Explain`, type `ref`:
https://stackoverflow.com/questions/4508055/what-does-eq-ref-and-ref-types-mean-in-mysql-explain

## Foreign Key

### foreign key referential actions <sup>[5]</sup>

```sql
[CONSTRAINT [symbol]] FOREIGN KEY
    [index_name] (col_name, ...)
    REFERENCES tbl_name (col_name,...)
    [ON DELETE reference_option]
    [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT
```

- `CASCADE`: Delete or update the row from the parent table, and automatically delete or update the matching rows in the child table. 
- `SET NULL`: Delete or update the row from the parent table, and set the foreign key column or columns in the child table to NULL.
    + If you specify a SET NULL action, make sure that you have not declared the columns in the child table as NOT NULL.
- `RESTRICT`: (default) Rejects the delete or update operation for the parent table.
- `NO ACTION`: A keyword from standard SQL. In MySQL, equivalent to `RESTRICT`.

[foreign key example](https://dev.mysql.com/doc/mysql-tutorial-excerpt/5.7/en/example-foreign-keys.html)

[Does MySQL index foreign key columns automatically?
](https://stackoverflow.com/questions/304317/does-mysql-index-foreign-key-columns-automatically) -> **YES** for `InnoDB`

`owner SMALLINT UNSIGNED NOT NULL REFERENCES person(id),`

```sql
CREATE TABLE parent (
    id INT NOT NULL,
    PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE child (
    id INT,
    parent_id INT,
    INDEX par_ind (parent_id),
    FOREIGN KEY (parent_id)
        REFERENCES parent(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
```
---

## SQL Recap

three table：

> S(SNO, SNAME, AGE, SEX, Sdept)
> 
> SC(SNO, CNO, GRADE)
> 
> C(CNO, CNAME, TEACHER)

Below is to form the table
```sql
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (5, 'java', 59);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (5, 'math', 30);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (5, 'sql', 70);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (6, 'java', 99);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (6, 'math', 87);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (6, 'sql', 48);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (7, 'java', 33);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (7, 'sql', 86);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (8, 'sql', 93);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (8, 'math', 71);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (9, 'py', 100);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (10, 'py', 80);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (11, 'py', 70);
INSERT INTO `class`(`id`, `subject`, `grade`) VALUES (12, 'py', 23);


CREATE TABLE `qd452db`.`student` ( `id` INT NOT NULL , `name` VARCHAR(10) NOT NULL , `age` INT NOT NULL , `sex` ENUM('M','F') NOT NULL , `department` VARCHAR(10) NOT NULL ) ENGINE = InnoDB;
CREATE TABLE `qd452db`.`module` ( `id` INT NOT NULL , `name` VARCHAR(10) NOT NULL , `teacher` VARCHAR(20) NOT NULL ) ENGINE = InnoDB;

INSERT INTO `module` (`id`, `name`, `teacher`) VALUES ('1', 'math', 'mathTeacher');
INSERT INTO `module` (`id`, `name`, `teacher`) VALUES ('2', 'music', 'musicTeacher');
INSERT INTO `module` (`id`, `name`, `teacher`) VALUES ('3', 'java', 'javaTeacher');
INSERT INTO `module` (`id`, `name`, `teacher`) VALUES ('4', 'sql', 'sqlTeacher');
INSERT INTO `module` (`id`, `name`, `teacher`) VALUES ('5', 'py', 'pyTeacher');

UPDATE module SET teacher = CONCAT(name, '_Teacher');
ALTER TABLE class ADD subject_id INT;

SELECT class.id as Student_ID, class.subject as subject, module.id as Subject_id FROM class LEFT JOIN module ON class.subject = module.name ORDER BY class.id ASC;

-- Important: update field based on another table
UPDATE class 
SET class.subject_id = (SELECT module.id FROM module WHERE class.subject = module.name);

ALTER TABLE class DROP subject;
ALTER TABLE class RENAME COLUMN subject_id TO subject;

DELETE FROM student WHERE id=1;


INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('1', 'a', '13', 'M', 'AAA');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('2', 'b', '10', 'M', 'AAA');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('3', 'c', '13', 'F', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('4', 'd', '16', 'M', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('5', 'e', '13', 'F', 'AAA');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('6', 'f', '16', 'M', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('7', 'g', '18', 'F', 'CCC');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('8', 'h', '11', 'M', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('9', 'i', '18', 'M', 'CCC');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('10', 'j', '15', 'F', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('11', 'k', '18', 'M', 'BBB');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('12', 'l', '18', 'M', 'CCC');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('13', 'm', '15', 'F', 'AAA');
INSERT INTO `student` (`id`, `name`, `age`, `sex`, `department`) VALUES ('14', 'n', '18', 'M', 'BBB');
```

#### 1. select SNO where all module pass
```sql
SELECT sno 
FROM sc 
GROUP BY sno HAVING MIN(grade>=60);
```

#### 2. select sno where has module < 60 and module >90
```sql
SELECT id 
FROM class 
WHERE grade<60 
AND id IN (SELECT id FROM class WHERE grade>90);
```

#### 3. select cno, avg_grade where avg grade <60
```sql
SELECT cno, AVG(grade) FROM sc GROUP BY cno HAVING AVG(grade)<60;
```

<!-- #### 4. select sno who studied at last all the modules which student 2 learned
```sql
SELECT (SELECT cno FROM sc WHERE sno=2);
``` -->

#### 5. every module avg after remove highest and lowest
```sql
SELECT subject, AVG(grade) 
FROM class 
WHERE grade != (SELECT grade FROM class ORDER BY grade ASC LIMIT 1) 
AND grade !=(SELECT grade FROM class ORDER BY grade DESC LIMIT 1) 
GROUP BY subject;
```

#### 6. select students who do not take module 3
```sql
SELECT DISTINCT(id) 
FROM class 
WHERE id NOT IN (SELECT id FROM class WHERE subject=3);
```

#### 7. select students whose 'math' >90 or <60
```sql
SELECT DISTINCT(id) 
FROM class 
WHERE subject='math' AND grade NOT BETWEEN 60 AND 90;
```

#### 8. query subject and number of student who took it
```sql
SELECT subject, COUNT(*) as Num_Student 
FROM `class` GROUP BY subject;
SELECT subject, COUNT(id) as Num_Student 
FROM `class` GROUP BY subject;
```

#### 9. query student id, name, sex who took module num 3
```sql
SELECT student.id, student.name, student.sex 
FROM class LEFT JOIN student ON student.id = class.id 
WHERE class.subject = 3;
-- OR
SELECT student.id, name, sex 
FROM student, class 
WHERE student.id = class.id AND class.subject = 3;
```

#### 10. average age of students who took module num 3
```sql
SELECT AVG(age) 
FROM student, class 
WHERE student.id = class.id AND class.subject = 3;
```

#### 11. average age of students who took module num 3
```sql
SELECT AVG(age) 
FROM student, class 
WHERE student.id = class.id AND class.subject = 3;
```

#### 12. Many more
```sql
-- select class have more than 4 student
SELECT subject FROM class GROUP BY subject HAVING COUNT(id)>4;

-- http://www.mysqltutorial.org/mysql-delete-duplicate-rows/
-- https://dba.stackexchange.com/questions/214946/how-to-delete-duplicate-records-in-mysql-in-a-table-without-ids
CREATE TABLE temp LIKE class;
INSERT INTO temp 
    SELECT DISTINCT * FROM class;
DROP TABLE class;
RENAME TABLE temp TO class;

-- select duplicate from class
SELECT id, subject FROM class GROUP BY id, subject HAVING COUNT(*)>1;

-- add constraint to class
ALTER TABLE class 
ADD CONSTRAINT id_subject UNIQUE (id, subject);

-- select student id and name who took 'math'
SELECT student.id, student.name 
FROM student WHERE student.id 
IN (SELECT class.id 
    FROM class, module 
    WHERE class.subject=module.id and module.name='math');
-- Better
SELECT student.id, student.name 
FROM student, class, module 
WHERE student.id=class.id and class.subject=module.id and module.name='math';

-- select student who took either 1 or 2
SELECT DISTINCT id FROM class WHERE subject IN (1,2);

-- select student who took both 1 and 2
SELECT DISTINCT id FROM class WHERE subject=2 AND 
id IN (SELECT id FROM class WHERE subject=1);

-- select students who do not take module 3
SELECT DISTINCT(id) FROM class WHERE id NOT IN (SELECT id FROM class WHERE subject=3);

-- select student name, age who didn't take module 2
SELECT id, name, age 
FROM student 
WHERE 
id NOT IN (SELECT id FROM class WHERE subject = 2);
-- OR
SELECT id, name, age FROM student
WHERE NOT EXISTS 
(SELECT * FROM class WHERE id=student.id AND subject=2);

-- TODO: EXISTS: https://dev.mysql.com/doc/refman/8.0/en/exists-and-not-exists-subqueries.html

-- select female student who took math and failed <35
SELECT student.id, student.name, student.sex 
FROM student, class, module 
WHERE module.id=class.subject AND module.name='math' 
AND class.id=student.id 
AND student.sex='F' and class.grade<35;

-- query module name and avg grade for every module
SELECT module.name, AVG(class.grade) as AVG_grade 
FROM module LEFT JOIN class ON module.id=class.subject
GROUP BY module.name
ORDER BY AVG_grade ASC;
-- OR
SELECT module.name, AVG(class.grade) as AVG_grade 
FROM module, class WHERE module.id=class.subject 
GROUP BY module.name
ORDER BY AVG_grade ASC;

-- query student name and his/her average grade
SELECT student.name, AVG(grade) as grade FROM student, class
WHERE student.id=class.id 
GROUP BY student.name
ORDER BY grade DESC;
```

## Star Select SQL
https://selectstarsql.com/

```sql
-- Find the proportion of inmates with claims of innocence in their last statements.
SELECT
1.0 * COUNT(CASE WHEN last_statement LIKE '%innocent%'
    THEN 1 ELSE NULL END) / COUNT(*)
FROM executions

-- https://selectstarsql.com/longtail.html
SELECT
  county,
  COUNT(CASE WHEN last_statement IS NOT NULL 
       THEN 1 ELSE NULL END) AS with,
  COUNT(CASE WHEN last_statement IS NULL 
       THEN 1 ELSE NULL END) AS with
FROM executions
GROUP BY county
--OR
-- essentially they are the same, but just in different format
-- and below should be more efficient
SELECT
  county,
  last_statement IS NOT NULL AS has_last_statement,
  COUNT(*)
FROM executions
where county='Bexar'
GROUP BY county, has_last_statement

-- Find the first and last name of the the inmate with the longest last statement (by character count).
SELECT first_name, last_name
FROM executions
WHERE LENGTH(last_statement) =
    (SELECT LENGTH(last_statement) AS len
     FROM executions
     GROUP BY len 
     ORDER BY len DESC
     LIMIT 1)
-- Much Simpler
SELECT first_name, last_name
FROM executions
WHERE LENGTH(last_statement) =
    (SELECT MAX(LENGTH(last_statement))
     FROM executions)

-- Insert the <count-of-all-rows> query to find the percentage of executions from each county.
SELECT
  county,
  100.0 * COUNT(*) / (SELECT COUNT(*) FROM executions)
    AS percentage
FROM executions
GROUP BY county
ORDER BY percentage DESC

-- Look up the documentation to fix the query so that it returns the number of days between the dates.
-- https://www.sqlite.org/lang_datefunc.html
SELECT JULIANDAY('1993-08-10') - 
JULIANDAY('1989-07-07') AS day_difference
```

| start | end | dayDifference |
|:------:|:------:|:------:|
|1982-12-07|1984-03-14|463|
|1988-01-07|1988-11-03|301|
|2007-09-25|2008-06-11|260|


```sql
-- generate above table
SELECT
  last_ex_date AS start,
  ex_date AS end,
  JULIANDAY(ex_date) - JULIANDAY(last_ex_date) AS day_difference
FROM executions
JOIN (
    SELECT
      ex_number + 1 AS ex_number,
      ex_date AS last_ex_date
    FROM executions
  ) previous
  ON executions.ex_number = previous.ex_number
ORDER BY day_difference DESC
LIMIT 10

-- More Elegant
SELECT
  previous.ex_date AS start,
  executions.ex_date AS end,
  JULIANDAY(executions.ex_date) - JULIANDAY(previous.ex_date)
    AS day_difference
FROM executions
JOIN executions previous
  ON executions.ex_number = previous.ex_number+1
ORDER BY day_difference DESC
LIMIT 10

```


```sql
--Find the most networked senator. That is, the one with the most mutual cosponsorships.
WITH mutuals AS 
(SELECT DISTINCT a.sponsor_name, a.cosponsor_name
FROM cosponsors a
JOIN cosponsors b
ON a.cosponsor_name = b.sponsor_name
WHERE a.sponsor_name = b.cosponsor_name)

SELECT sponsor_name, COUNT(*)
FROM mutuals
GROUP BY sponsor_name
ORDER BY COUNT(*) DESC
LIMIT 1;

-- Now find the most networked senator from each state.
WITH mutual_counts AS (
  SELECT
    senator, state, COUNT(*) AS mutual_count
  FROM (
    SELECT DISTINCT
      c1.sponsor_name AS senator,
      c1.sponsor_state AS state,
      c2.sponsor_name AS senator2
    FROM cosponsors c1
    JOIN cosponsors c2
      ON c1.sponsor_name = c2.cosponsor_name
      AND c2.sponsor_name = c1.cosponsor_name
    )
  GROUP BY senator, state
),

state_max AS (
  SELECT
    state,
    MAX(mutual_count) AS max_mutual_count
  FROM mutual_counts
  GROUP BY state
)

SELECT
  mutual_counts.state,
  mutual_counts.senator,
  mutual_counts.mutual_count
FROM mutual_counts
JOIN state_max
  ON mutual_counts.state = state_max.state
  AND mutual_counts.mutual_count = state_max.max_mutual_count


-- Find the senators who cosponsored but didn't sponsor bills.
SELECT DISTINCT cosponsor_name
FROM cosponsors
WHERE
cosponsor_name NOT IN
(SELECT DISTINCT sponsor_name
FROM cosponsors)
-- MORE efficient way
SELECT DISTINCT c1.cosponsor_name
FROM cosponsors c1
LEFT JOIN cosponsors c2
 ON c1.cosponsor_name = c2.sponsor_name
 -- This join identifies cosponsors
 -- who have sponsored bills
WHERE c2.sponsor_name IS NULL
-- LEFT JOIN + NULL is a standard trick for excluding
-- rows. It's more efficient than WHERE ... NOT IN.

```



[1]: https://dev.mysql.com/doc/refman/5.5/en/range-optimization.html
[2]: https://stackoverflow.com/questions/7643491/understanding-mysql-key-len-in-explain-statement
[3]: https://www.jianshu.com/p/67b39af2f851
[4]: https://www.cnblogs.com/developer_chan/p/9223671.html
[5]: https://dev.mysql.com/doc/refman/5.6/en/create-table-foreign-keys.html#foreign-keys-referential-actions