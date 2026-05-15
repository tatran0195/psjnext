---
title: "ImportGroup()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Import Group written in CSV file.

## Syntax

```psj
ImportGroup(String filePath, Cursor SubGroup)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String\[]

Specify the csv file of group definition.

<!-- @since:5.1.0 -->
### 2. Cursor

Specify the subGroup by cursor.

## Return Code

None.

## Sample Code

```psj
ImportGroup(["C:/Temp/group _file.csv"], 0:0)
```
