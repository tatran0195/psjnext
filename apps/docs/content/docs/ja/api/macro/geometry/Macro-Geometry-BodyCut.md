---
title: "BodyCut()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

## Syntax

```psj
BodyCut(int method,double offset,int shareFace,int separateFace,int splitOnly,
    int makeSectionFace,Cursor coord,Cursor[] targets, Cursor[] cutter)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

method used for body cut, 0: YZ plane, 1: XZ plane, 2: XY plane, 3: by 3 points, 4: by surface

<!-- @since:5.0.1 -->
### 2. Double

offset value from cut plane

<!-- @since:5.0.1 -->
### 3. Int

whether share face or not, 0 : no, 1: yes

<!-- @since:5.0.1 -->
### 4. Int

Whether separate face or not, 0: no, 1: yes

<!-- @since:5.0.1 -->
### 5. Int

Whether split only, 0: no, 1: yes

<!-- @since:5.0.1 -->
### 6. Int

Make section face or not, 0: no, 1: yes

<!-- @since:5.0.1 -->
### 7. Cursor

The coordinate system used in plane cut

<!-- @since:5.0.1 -->
### 8. Cursor\[]

Targets to be cutted

<!-- @since:5.0.1 -->
### 9. Cursor\[]

Cutter entity, available for 3 points and surface option

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code
