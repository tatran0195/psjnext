---
title: "CentrifugalForceCoordinateSystem()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create centrifugal force by coordinate system

## Syntax

```psj
CentrifugalForceCoordinateSystem(String m _strName,double fVelocity,double fAcceleration,
    int iAxisDirection,int iVelocityUnit,int iAccelerationUnit,Cursor curCoord,
    Cursor[] m _taTarget,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of centrifugal force

<!-- @since:5.0.1 -->
### 2. Double

rotational velocity

<!-- @since:5.0.1 -->
### 3. Double

rotational acceleration

<!-- @since:5.0.1 -->
### 4. Int

axis\[0:X; 1:Y; 2:Z]

<!-- @since:5.0.1 -->
### 5. Int

unit of velocity

<!-- @since:5.0.1 -->
### 6. Int

unit of acceleration

<!-- @since:5.0.1 -->
### 7. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 8. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 9. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CentrifugalForceCoordinateSystem("Test",0.001,0.001,1,1,1,1:11,[1:11,2:12],1:11)
```
