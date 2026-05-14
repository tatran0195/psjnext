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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:Double List @optional @default:[0.0,0.0,0.0] -->
### `dlVecMomentXYZ`

- The vector moment x y z.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.Load.Moment(strName="", crlFaces=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```
