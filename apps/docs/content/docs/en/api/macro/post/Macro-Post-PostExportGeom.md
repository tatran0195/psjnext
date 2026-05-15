---
title: "PostExportGeom()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export deformed shape by Post deformation as stl files.

## Syntax

```psj
PostExportGeom(string folder, bool bUseUnit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Export file path.

<!-- @since:5.1.0 -->
### 2. bool

Use document unit.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
PostExportGeom("C:/Users/TechnoStar/Desktop/temp", 1)
```
