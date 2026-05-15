---
title: "ACM _ImportCommand()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

ACM\_ImportCommand

## Syntax

```psj
ACM _ImportCommand(bool bOutShelFile, string srtImportFilePathTri6, string strImportFilePathTri3)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Bool

Output Shell File bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 2. String

bdf file path of Tri6 model exported using bdf export

<!-- @since:5.0.1 -->
### 3. String

bdf file path of Tri3 model exported using bdf export

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACM _ImportCommand(1, "D:/tri6.bdf", "D:/tri3.bdf")
```
