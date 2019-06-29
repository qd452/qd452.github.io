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

## Chapter 3 File

### Error Log




[1]: https://www.geeksforgeeks.org/sql-ddl-dml-dcl-tcl-commands/
[2]: https://www.percona.com/blog/2009/01/13/some-little-known-facts-about-innodb-insert-buffer/
