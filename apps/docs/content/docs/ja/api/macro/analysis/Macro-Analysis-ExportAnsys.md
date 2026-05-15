---
title: "ExportAnsys()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export Ansys file

## Syntax

```psj
ExportAnsys(String m _strName,Cursor m _crAbaJob)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Export file name

<!-- @since:5.0.1 -->
### 2. Cursor

Ansys Job Cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportAnsys("D:/Ansys.dat", 146:1)
```
