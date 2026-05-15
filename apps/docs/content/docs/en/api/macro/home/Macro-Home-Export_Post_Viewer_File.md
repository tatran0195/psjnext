---
title: "Export _Post _Viewer _File()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export geometry surface.

## Syntax

```psj
Export _Post _Viewer _File(int iGroupType, str strFileName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- A integer specifying group type.

<!-- @since:5.1.0 -->
### 2. str

- A string specifying file name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Export _Post _Viewer _File(0, "strFileName")
```
