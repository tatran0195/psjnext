---
title: "CmdOptimizeOuterShellExport()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export topology optimization surface

## Syntax

```psj
CmdOptimizeOuterShellExport(string fileName, cursor[] parts, float tol)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Export file name

<!-- @since:5.1.0 -->
### 2. cursor\[]

target parts

<!-- @since:5.1.0 -->
### 3. float

Tolerance of density

## Return Code

Nothing.

## Sample Code

```psj
CmdOptimizeOuterShellExport(C:/Temp/export.stl, [3:1], 0.670000)
```
