---
title: "ImportFromMLIB()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import materials from a .mlib file into the library database.

## Syntax

```psj
ImportFromMLIB(string fileName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Path of .mlib file.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImportFromMLIB("//NetworkMachine/shared _folder/sample.mlib")
```
