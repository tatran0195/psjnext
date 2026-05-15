---
title: "ACM _ShowAdjacent()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Select face(s) then it results the Adjacent faces with the given constrainsts

## Syntax

```psj
ACM _ShowAdjacent(double stopAngle,bool IncludeStopFace,int Layer,bool IsPreview,
    bool bStopByNonma, bool bShowPartOnly,cursor[] startFaceCursor, cursor[] stopFaceCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Stop Angle value

<!-- @since:5.0.1 -->
### 2. Bool

Include stop faces bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 3. Int

Number of Layers

<!-- @since:5.0.1 -->
### 4. Bool

Whether the result is preview or Run

<!-- @since:5.0.1 -->
### 5. Bool

Stop by nonmanifold bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Show part only bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Cursor\[]

List of Start face cursor(\[11:Elem ID])

<!-- @since:5.0.1 -->
### 8. Cursor\[]

List of Stop face cursor(\[11:Elem ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACM _ShowAdjacent(0, 0, 100, 0, 0, 0, [6:22], [])
```
