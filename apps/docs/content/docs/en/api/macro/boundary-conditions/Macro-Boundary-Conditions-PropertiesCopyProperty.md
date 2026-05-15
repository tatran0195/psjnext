---
title: "PropertiesCopyProperty()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Copy properties by translation

## Syntax

```psj
PropertiesCopyProperty(String strPathSource,String strPathTarget,int[] keyTarget,int axis,
    Cursor crCoord,Vector transVec,double dMag,double dOffset,double dTol)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

source file path

<!-- @since:5.0.1 -->
### 2. String

target file path

<!-- @since:5.0.1 -->
### 3. int\[]

property key need copy

<!-- @since:5.0.1 -->
### 4. int

Axis \[0:Arbitrary Axis; 1:X Axis; 2:Y Axis; 3:Z Axis; 4:2Nodes; 5:Edge]

<!-- @since:5.0.1 -->
### 5. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 6. Vector

translate vector

<!-- @since:5.0.1 -->
### 7. double

magnitude

<!-- @since:5.0.1 -->
### 8. double

offset

<!-- @since:5.0.1 -->
### 9. double

tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PropertiesCopyProperty("D:/Source","D:/Target",[1,2],1,1:11,,0.001,0.001,0.001)
```
