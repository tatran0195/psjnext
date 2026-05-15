---
title: "SaveDB()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Save Current Document

## Syntax

```psj
SaveDB(string strPath, string strHistoryTree)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Directory path name

<!-- @since:5.0.1 -->
### 2. String

History tree

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SaveDB("D:/Test.jtdb", "")
```
