---
title: "ExportAbaqusInp()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export Abaqus Inp

## Syntax

```psj
ExportAbaqusInp(cursor m _crAbaJob,cursor[] m _taSelectBody,string strPath)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Abaqus Job Cursor

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Select Body Cursors to output

<!-- @since:5.0.1 -->
### 3. String

output directory for INP

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportAbaqusInp(143:2, [], "D:/Abaqus.inp")
```
