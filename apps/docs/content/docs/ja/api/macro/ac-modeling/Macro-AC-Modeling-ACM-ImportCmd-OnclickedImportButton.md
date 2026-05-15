---
title: "ACM _ImportCmd _OnclickedImportButton()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

ACM\_ImportCmd\_OnclickedImportButton

## Syntax

```psj
ACM _ImportCmd _OnclickedImportButton(string filePath, double dFaceAngle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

File path directory

<!-- @since:5.0.1 -->
### 2. Double

Nastran data face angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACM _ImportCmd _OnclickedImportButton("D:/tri6.bdf", 15)
```
