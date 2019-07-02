---
layout: post
title:  "MySQL InnoDB Notes"
subtitle: 'MySQL技术内幕(InnoDB存储引擎)第2版 - 笔记'
date:   2019-06-24 20:52:40 +0800
author: "DoNG"
catalog: true
tags: 
    - MySQL
    - database
    - InnoDB
    - notes
---

## Chapter 2 InnoDB Engine

### Key characteristics

- Insert buffer
- Double Write
- Adaptive Hash Index
- Async IO
- Flush Neighbor Page

#### Insert buffer

> CRUD: create, read, update, delete
> DML: Data Manipulation Language: INSERT, DELETE, UPDATE [1]
> DDL: Data Define language: CREATE, DROP, ALTER
> TCL: Transaction Control Language: COMMIT, ROLLBACK

Insert buffer only can work for non-unique secondary (non-clustered) keys because until the merge is performed it is impossible to check if the value is unique.<sup>[2]</sup>

if secondary index in Buffer Pool -> insert
if not -> pretend insert -> wait until many keys -> merge

#### Double Write

When InnoDB write `Page` into `Table`, 1 Page is 16Kb, when only 4Kb finished, powered down, *partial page write* will occur.

#### Adaptive hash Index (AHI)

AHI constructed from buffer pool B+ tree page

TO allow AHI:
- pattern to consecutively visit the page must be the same, same `WHERE` clause
- And AHI can only be used for `=` search, cannot used for range search

## Chapter 6 Lock

### Lock in InnoDB

#### Shared and Exclusive Locks (Row Level Lock)

`InnoDB` implements standard row-level locking:<sup>[3]</sup>

- A shared (S) lock permits the transaction that holds the lock to **read** a row.
- An exclusive (X) lock permits the transaction that holds the lock to **update or delete** a row.

#### Intention Lock (Table Level Lock)

- An intention shared lock (IS) indicates that a transaction intends to set a shared lock on individual rows in a table.
- An intention exclusive lock (IX) indicates that a transaction intends to set an exclusive lock on individual rows in a table.


#### Record Lock - single row lock

A record lock is a lock on an **index record**. For example, `SELECT c1 FROM t WHERE c1 = 10 FOR UPDATE`; prevents any other transaction from inserting, updating, or deleting rows where the value of `t.c1` is `10`.

#### Gap Lock - a range, but exclude records themselves

A gap lock is a lock on a gap between index records, or a lock on the gap before the first or after the last index record. For example, `SELECT c1 FROM t WHERE c1 BETWEEN 10 and 20 FOR UPDATE`; prevents other transactions from inserting a value of `15` into column `t.c1`, whether or not there was already any such value in the column, because the gaps between all existing values in the range are locked.

[TODO](https://dev.mysql.com/doc/refman/5.5/en/innodb-locking.html#innodb-gap-locks)

#### Next-Key Lock - lock range and the record

next-key 是因为它是右面闭区间， `(]`; 对应的，有previous-key lock, 是 `[)`

当index record是unique的时候，next-key lock 自动降级成 record lock

```sql
CREATE TABLE t (a INT PRIMARY KEY);
INSERT INTO t SELECT 1;
INSERT INTO t SELECT 2;
INSERT INTO t SELECT 5;
```

此时在事务A中，`SELECT * FROM t WHERE t=2 FOR UPDATE`但是不commit. 与此同时另一个事务B开始`INSERT INTO t SELECT 4`并不会阻塞。因为t是主键，所以lock已经降级为record lock。

下面来看next-key lock的一般情况
```sql
CREATE TABLE t (a INT, b INT, PRIMARY KEY(a), KEY(b));
INSERT INTO t SELECT 1, 1;
INSERT INTO t SELECT 3, 1;
INSERT INTO t SELECT 5, 3;
INSERT INTO t SELECT 7, 6;
INSERT INTO t SELECT 10,8;
```

此时在事务A中，`SELECT * FROM t WHERE b=3 FOR UPDATE`. 这一行有两个索引(a=5, b=3)，分别锁定。对于聚集索引，加Record Lock。对于辅助索引，先加next-key lock,是 `(1,3]`,InnoDB还会对辅助索引下一个键值加一个Gap Lock,是`(3,6)`.所以最终锁住的范围是`(1,6)`。

所以如果此时在事务B中，以下三种均会被堵塞

```sql
SELECT * FROM t WHERE a=5 FOR SHARE; -- 5 already been X locked
INSERT INTO t SELECT 4,2; -- 2 within range(3,6)
INSERT INTO t SELECT 6,5; -- 5 within range(3,6)
```

#### 事务的四种隔离级别<sup>[4]</sup>

| 隔离级别 | 脏读（Dirty Read） | 不可重复读（NonRepeatable Read） | 幻读（Phantom Read） |
|----------------|----------|------------|-------------|
| 未提交读（Read uncommitted） | 可能 | 可能 | 可能 |
| 已提交读（Read committed） | 不可能 | 可能 | 可能 |
| 可重复读（Repeatable read） | 不可能 | 不可能 | 可能 |
| 可串行化（Serializable ） | 不可能 | 不可能 | 不可能 |

- Repeatable read - use Next-key Locking
- Read committed - use Record Locking
- Dirty Read - Read uncommitted data from another transaction
- NonRepeatable Read
    + Occurs under Read committed LEVEL, because this level always read fresh snapshot


### Consistent Nonblocking Read (一致性非锁定读)

A consistent read means that `InnoDB` uses multi-versioning to present to a query a snapshot of the database at a point in time. 

Currently the row want to read is X locked (DELECT or UPDATE), read from snapshot.

| Session A | Session B |
|------------------|-------------------------|
| BEGIN; SET autocommit=0; | BEING; SET autocommit=0; |
| SELECT * FROM parent WHERE id=1; |  |
|  | UPDATE parent  SET id=3 WHERE id=1; |
| SELECT * FROM parent WHERE id=1;<br><br>**For both Read Commit  & Repeatable Read, id=1**|  |
|  | COMMIT; |
| SELECT * FROM parent WHERE id=1;<br><br>For Read Commit, Empty Set; For Repeatable Read, id=1. |  |
| COMMIT; |  |
                                                               
- For Repeatable Read, all reads within the same transaction read the snapshot established by the first such read in that transaction. 每次读都根据第一次读到的snapshot
- For Read committed, always read a new fresh snapshot. 每次都读最新的snapshot

#### Locking Read

If you query data and then insert or update related data within the same transaction, the regular `SELECT` statement does not give enough protection. Other transactions can update or delete the same rows you just queried

- `SELECT ... FOR SHARE` - add S lock
    + if you want to insert a child for one certain parent; if you just select that parent and then insert child, its NOT safe; cause some other session could delete the parent row in the moment between your `SELECT` and your `INSERT`
- `SELECT ... FOR UPDATE` - add X lock

#### AUTO-INC Locking

An AUTO-INC lock is a special **table-level** lock taken by transactions inserting into tables with `AUTO_INCREMENT` columns. 

- Lock is released directly after the insertion SQL, not after the transaction is finished
- Each table can have only one `AUTO_INCREMENT` column. It must defined as a key (not necessarily the `PRIMARY KEY` or `UNIQUE` key).
- For `MyISAM` tables, you can specify `AUTO_INCREMENT` on a secondary column in a multiple-column index. But for `InnoDB`, it must be th first column in multiple-column index

[more about `AUTO_INCREMENT`](https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html)



[1]: https://www.geeksforgeeks.org/sql-ddl-dml-dcl-tcl-commands/
[2]: https://www.percona.com/blog/2009/01/13/some-little-known-facts-about-innodb-insert-buffer/
[3]: https://dev.mysql.com/doc/refman/5.5/en/innodb-locking.html
[4]: https://tech.meituan.com/2014/08/20/innodb-lock.html




















