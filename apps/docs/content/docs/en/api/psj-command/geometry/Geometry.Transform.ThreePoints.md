---
title: "Geometry.Transform.ThreePoints()"
description: "Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > ThreePoints"
---

## Description

Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.ThreePoints(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargetParts`

- The parts to be transformed.

<!-- @since:5.0.1 @type:List[Vector] @required -->
### `poslOriginalPoints`

- The original points using for movement.
  Three points are required corresponding to three original points.

<!-- @since:5.0.1 @type:List[Vector] @required -->
### `poslNextPoints`

- The next points using for movement. Three points are required corresponding to three next points, respectively to the three original pointed defined in[`poslOriginalPoints`](#posloriginalpoints).

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether to copy the transformed parts to new parts.
  - If _True_, a new part is copied to new location.
  - If _False_, the original part is moved to new location.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLBC`

- Whether to copy load boundary conditions from the existing parts to new parts. This argument will only affect the functionality when_`bCreateNewPart`_=_True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- The selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality when_`bCreateNewPart`_=_True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyReference`

- The selecting whether to copy reference from the existing part to new parts. This argument will only affect the functionality when_`bCreateNewPart`_=_True_.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16}
target _part = Geometry.Part.Cube()
move _part = Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], 
                               strName="Cube _2", 
                               iPartColor=6409934)

created _parts = Geometry.Transform.ThreePoints(crlTargetParts=[move _part],
                                               poslOriginalPoints=[[0.022, 0, 0.01], 
                                                                   [0.022, 0.01, 0.01], 
                                                                   [0.012, 0, 0.01]],
                                               poslNextPoints=[[0.01, 0, 0.01], 
                                                               [0, 0, 0.01], 
                                                               [0, 0.01, 0.01]],
                                               bCreateNewPart=True, 
                                               bCopyLBC=True, 
                                               bCopyProperty=True,
                                               bCopyReference=True)

JPT.Debugger(created _parts)
```
