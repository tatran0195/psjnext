---
title: "CmdShowPostContour()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Load result on model and show it as contour

## Syntax

```psj
CmdShowPostContour(TCursor crPostJob,
	PostResultKey& resKey, PostDataOp& opOut,
	bool hasResult2, PostResultKey& resKey2, PostDataOp& opOut2,
	bool hasResult3, PostResultKey& resKey3, PostDataOp& opOut3,
	bool enableMidNode, bool bApplyAll = false, bool bLogMacro = true)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. TCursor

Indicates post job = 183:1

<!-- @since:5.1.0 -->
### 2. PostResultKey::

Key ID

<!-- @since:5.1.0 -->
### 3. PostDataOp::

Group creation option

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdShowPostContour(183:1, 1, 0, 9, NodalStrain, Mises, 1, 1, 0, 0, 0, 1, 8, 0, 0.000000, 0, 0, 0, 0, 0, , , 0, 0, 0, 0, 0, 0, 0, 0, 0.000000, 0, 0, 0, 0, 0, , , 0, 0, 0, 0, 0, 0, 0, 0, 0.000000, 0, 0, 0)
```
