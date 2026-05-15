---
title: "Designer.Load.Moment()"
description: "Create moment"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Designer > Load > Moment"
---

## Description

Create moment

## Syntax

```psj
Designer.Load.Moment(strName="", crlFaces=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dlVecMomentXYZ

- Specify the vector moment x y z.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.Load.Moment(strName="", crlFaces=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```
