---
title: "CentrifugalForce2Positions()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create centrifugal force by 2 positions

## Syntax

```psj
CentrifugalForce2Positions(String m _strName,double fBasePoint[0],double fBasePoint[1],
    double fBasePoint[2],double fTipPoint[0],double fTipPoint[1],double fTipPoint[2],
    double fVelocity,double fAcceleration,int iVelocityUnit,int iAccelerationUnit,
    cursor[] m _taTarget,cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of centrifugal force

<!-- @since:5.0.1 -->
### 2. Double

base point x

<!-- @since:5.0.1 -->
### 3. Double

base point y

<!-- @since:5.0.1 -->
### 4. Double

base point z

<!-- @since:5.0.1 -->
### 5. Double

tip point x

<!-- @since:5.0.1 -->
### 6. Double

tip point y

<!-- @since:5.0.1 -->
### 7. Double

tip point z

<!-- @since:5.0.1 -->
### 8. Double

rotational velocity

<!-- @since:5.0.1 -->
### 9. Double

rotational acceleration

<!-- @since:5.0.1 -->
### 10. Int

unit of velocity

<!-- @since:5.0.1 -->
### 11. Int

unit of acceleration

<!-- @since:5.0.1 -->
### 12. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 13. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CentrifugalForce2Positions("CentrifugalForce1", 0.01, 0.0022222, 0.01, 0.01,
    0.0044444, 0.01, 0.174533, 0.0872665, 0, 0, [3:1, 10:82, 10:84], 0:0)
```
