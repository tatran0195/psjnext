---
title: "ExportNastranBdf()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export Nastran bdf file

## Syntax

```psj
ExportNastranBdf(string strPath, TCursor job, int modelCheckAnswer, int deleteSlaveNodesAnswer)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

bdf file path

<!-- @since:5.0.1 -->
### 2. Double

job cursor

<!-- @since:5.0.1 -->
### 3. Int

Model Check Answer

<!-- @since:5.0.1 -->
### 4. Int

Delete Slave Nodes Answer

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ExportNastranBdf("D:/NastranBdf.bdf", 147:2, 1, 0)
```
