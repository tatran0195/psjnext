---
title: "Geometry.Transform.Position()"
description: "Transform parts by changing their position"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Position"
macro _link: "[PositionBody](../../macro/geometry/PositionBody)"
---

## Description

This method moves the parts by selecting three pairs of nodes. The given parts move onto a target position in a one-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.Position(crlParts, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False,
    bCopyProperty=False)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to be transformed.

<!-- @since:5.0.1 @optional -->
### veclPoint

- Specify the points using for movement. Six points are required corresponding to three pairs of nodes respectively. Each pair is in a one-one correspondence between target and source.
- The default value is \[\[0.0,0.0,0.0]].

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether to copy the transformed parts to new parts.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy load boundary conditions from the existing part to new parts. This argument will only affect the functionality when _bCreateNewPart=True_.
- The default value is _False_.

### `bCopyProperty`

- A _Boolean_ selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality when _bCreateNewPart=True_.
- The default value is _False_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=14540142)

Geometry.Part.Wedge(vecOrigin=[0.01, 0.01, 0.01], iPartColor=6678885)

Geometry.Transform.Position(crlParts=[Part(1)], veclPoint=[[0.0, 0.0, 10.0], [10.0, 0.0, 10.0],
    [0.0, 10.0, 10.0], [10.0, 10.0, 20.0], [20.0, 10.0, 20.0], [10.0, 20.0, 20.0]])
```
