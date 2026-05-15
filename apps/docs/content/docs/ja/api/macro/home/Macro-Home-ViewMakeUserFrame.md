---
title: "ViewMakeUserFrame()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a new user frame

## Syntax

```psj
ViewMakeUserFrame(string nameOfFrame, int StartPointX, int StartPointY, int endPointX, int EndPointY, bool Mode )
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Name of the user frame.

<!-- @since:5.1.0 -->
### 2. int

Specify start point in x direction.

<!-- @since:5.1.0 -->
### 3. int

Specify start point in y direction.

<!-- @since:5.1.0 -->
### 4. int

Specify end point in x direction (start point x + width).

<!-- @since:5.1.0 -->
### 5. int

Specify end point in y direction (start point y + height).

<!-- @since:5.1.0 -->
### 6. bool

Specify Single or Mutiple mode.

- 0 : Single
- 1 : Multiple

## Return Code

No return value.

## Sample Code

```psj
ViewMakeUserFrame("New _Frame _1 ((Multiple))", 294, 128, 588, 257, 1)
```
