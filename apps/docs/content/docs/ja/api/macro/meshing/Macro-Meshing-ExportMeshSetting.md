---
title: "ExportMeshSetting()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Save local setting

## Syntax

```psj
ExportMeshSetting(string fname,int type)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

the file name to save local setting

<!-- @since:5.0.1 -->
### 2. Int

the save mode, in this function the value is fixed to 3

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportMeshSetting("D:/test.xml", 3)
```
