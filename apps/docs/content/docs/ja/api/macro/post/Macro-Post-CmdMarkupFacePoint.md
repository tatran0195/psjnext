---
title: "CmdMarkupFacePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add note to selected FacePoint.

## Syntax

```psj
CmdMarkupFacePoint([int Element, float xpos, float ypos, float zpos])
```

## Inputs

List of set of 1-4.

<!-- @since:5.0.1 -->
### 1. int

Element ID where indicated position belongs to.

<!-- @since:5.0.1 -->
### 2. float

x position in the view (global coordinate).

<!-- @since:5.0.1 -->
### 3. float

y position in the view (global coordinate).

<!-- @since:5.0.1 -->
### 4. float

z position in the view (global coordinate).

## Return Code

Nothing.

## Sample Code

```psj
CmdMarkupFacePoint([[2746, 7.959929, 4.940016, 10.000000]])
```
