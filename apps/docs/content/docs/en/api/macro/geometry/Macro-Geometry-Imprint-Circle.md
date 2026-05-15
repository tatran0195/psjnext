---
title: "Imprint _Circle()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint circle line

## Syntax

```psj
Imprint _Circle(double[] Point _xyz,int[] Face _ID,double Inner _Radius,double Outer _Radius,
    int No _of _Layers,int No _of _Divisions,bool BreakFace,Cursor[] bodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Point xyz \[\[x1,y1,z1]]

<!-- @since:5.0.1 -->
### 2. Int\[]

Face ID Array

<!-- @since:5.0.1 -->
### 3. Double

Inner Radius

<!-- @since:5.0.1 -->
### 4. Double

Outer Radius

<!-- @since:5.0.1 -->
### 5. Int

No of Layers

<!-- @since:5.0.1 -->
### 6. Int

No of Divisions

<!-- @since:5.0.1 -->
### 7. Bool

Flag true = 1,false=0

<!-- @since:5.0.1 -->
### 8. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _Circle([[0.00555556, 0.00444444, 0.01]], [26], 0.001, 0.002, 1, 30, 1, [3:1])
```
