---
title: "LoadDB()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

LoadDB

## Syntax

```psj
LoadDB(string PathFile, bool bUseTmpTable)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

jtdb import file path

<!-- @since:5.0.1 -->
### 2. Bool

bool Use Temp Table flag true=1, false=0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
LoadDB("D:/Test.jtdb", 0)
```
