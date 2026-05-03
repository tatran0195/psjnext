---
title: "Designer.Load.Moment()"
description: "Create moment"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Designer > Load > Moment"
---

## Description

Create moment

## Syntax

```psj
Designer.Load.Moment(strName="", crlFaces=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The face.

### `dlVecMomentXYZ` @type(Double List) @default(\[0.0,0.0,0.0])

- The vector moment x y z.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.Load.Moment(strName="", crlFaces=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```
