
# SQL

## Table of Contents

[TOC]


## Question 1

```sql
-- Example case create statement:
CREATE TABLE sessions (
  id INTEGER NOT NULL PRIMARY KEY,
  userId INTEGER NOT NULL,
  duration DECIMAL NOT NULL
);

INSERT INTO sessions(id, userId, duration) VALUES(1, 1, 10);
INSERT INTO sessions(id, userId, duration) VALUES(2, 2, 18);
INSERT INTO sessions(id, userId, duration) VALUES(3, 1, 14);

-- Expected output:
-- UserId  AverageDuration
-- -----------------------
-- 1       12
```

ANS:
```sql
SELECT userId, AVG(duration) FROM sessions GROUP BY userId HAVING COUNT(userID)>1;
```

## Question Set

https://www.cnblogs.com/jpfss/p/6613611.html

## bytedance question

- 给一个id，科目；成绩的表. 搜索不及格科目大于两门课的学生id
- https://blog.csdn.net/koreyoshi326/article/details/60870042
```sql
CREATE TABLE class (
    id INTEGER NOT NULL,
    subject VARCHAR(10) NOT NULL,
    grade INTEGER NOT NULL
)
```

```sql
SELECT id FROM class GROUP BY id HAVING SUM(grade<60)>=2; 
```


