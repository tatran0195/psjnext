---
title: "Geometry.Transform.Position()"
description: "Transform parts by changing their position"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Position"
macro_link: "[PositionBody](../../macro/geometry/PositionBody)"
---

## Description

This method moves the parts by selecting three pairs of nodes. The given parts move onto a target position in a one-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.Position(crlParts, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False,
    bCopyProperty=False)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to be transformed.

### `veclPoint` @type(List\[Vector]) @default(\[\[0.0,0.0,0.0]])

- The points using for movement. Six points are required corresponding to three pairs of nodes respectively. Each pair is in a one-one correspondence between target and source.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to copy the transformed parts to new parts.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy load boundary conditions from the existing part to new parts. This argument will only affect the functionality whe&#x6E;_&#x62;CreateNewPart=True_.

### `bCopyProperty` @type(Boolean) @default(False)

- Selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality whe&#x6E;_&#x62;CreateNewPart=True_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=14540142)

Geometry.Part.Wedge(vecOrigin=[0.01, 0.01, 0.01], iPartColor=6678885)

Geometry.Transform.Position(crlParts=[Part(1)], veclPoint=[[0.0, 0.0, 10.0], [10.0, 0.0, 10.0],
    [0.0, 10.0, 10.0], [10.0, 10.0, 20.0], [20.0, 10.0, 20.0], [10.0, 20.0, 20.0]])
```
