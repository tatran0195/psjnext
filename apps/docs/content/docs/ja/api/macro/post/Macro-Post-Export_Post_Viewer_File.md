---
title: "Export _Post _Viewer _File()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Export file for PV.

## Syntax

```psj
Export _Post _Viewer _File(int GroupType, string FilePath)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Output Group by 0: No specification, 1: Element, 2: Material, 3: Property.

<!-- @since:5.0.1 -->
### 2. string

Export file path.

## Return Code

Nothing.

## Sample Code

```psj
Export _Post _Viewer _File(1, "C:/Temp/Data.tspv")
```
