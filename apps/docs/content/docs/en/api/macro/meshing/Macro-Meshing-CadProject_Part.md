---
title: "CadProject _Part()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Project nodes in Meshed Part toward CAD Part

## Syntax

```psj
CadProject _Part(int method, cursor taCadBody, cursor meshedBody, bool bForceProject,
    bool bProjectCornerNodes, bool bProjectMidNodes, bool bIDCheck)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Method = 1

<!-- @since:5.0.1 -->
### 2. Cursor

Target reference CAD body (12:RefPart ID)

<!-- @since:5.0.1 -->
### 3. Cursor

Target meshed body (3:Part ID)

<!-- @since:5.0.1 -->
### 4. Bool

Force project = 0

<!-- @since:5.0.1 -->
### 5. Bool

Project corner nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Project mid nodes bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

ID check bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CadProject _Part(1, 12:1, 3:1, 0, 0, 1, 1)
```
