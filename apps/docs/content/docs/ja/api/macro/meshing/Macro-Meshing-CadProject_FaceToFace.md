---
title: "CadProject _FaceToFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Project nodes in Meshed Faces toward CAD Faces

## Syntax

```psj
CadProject _Face(int method, cursor[] taCadFaces, cursor[] meshedFaces, bool bForceProject,
    bool bProjectCornerNodes, bool bProjectMidNodes, bool bIDCheck)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Method = 3

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target reference CAD faces (\[15:RefFace ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target meshed faces (\[6:Face ID])

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
CadProject _FaceToFace(3, [15:5], [6:5], 1, 0, 1, 1)
```
