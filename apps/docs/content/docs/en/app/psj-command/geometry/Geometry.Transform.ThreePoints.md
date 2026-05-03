---
title: "Geometry.Transform.ThreePoints()"
description: "Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > ThreePoints"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Move the parts by selecting three pairs of nodes. The selected parts are moved onto the target position in a one-to-one correspondence between source and target.

## Syntax

```psj
Geometry.Transform.ThreePoints(...)
```

## Inputs

### `crlTargetParts` @type(List\[Cursor]) @required

- The parts to be transformed.

### `poslOriginalPoints` @type(List\[Vector]) @required

- The original points using for movement.
  Three points are required corresponding to three original points.

### `poslNextPoints` @type(List\[Vector]) @required

- The next points using for movement. Three points are required corresponding to three next points, respectively to the three original pointed defined in[`poslOriginalPoints`](#posloriginalpoints).

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to copy the transformed parts to new parts.
  - I&#x66;_&#x54;rue_, a new part is copied to new location.
  - I&#x66;_&#x46;alse_, the original part is moved to new location.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy load boundary conditions from the existing parts to new parts. This argument will only affect the functionality whe&#x6E;_`bCreateNewPart`_=_True_.

### `bCopyProperty` @type(Boolean) @default(False)

- Selecting whether to copy property from the existing part to new parts. This argument will only affect the functionality whe&#x6E;_`bCreateNewPart`_=_True_.

### `bCopyReference` @type(Boolean) @default(False)

- Selecting whether to copy reference from the existing part to new parts. This argument will only affect the functionality whe&#x6E;_`bCreateNewPart`_=_True_.

## Return Code

A _List of Cursor_ specifying the created parts.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16}
target_part = Geometry.Part.Cube()
move_part = Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], 
                               strName="Cube_2", 
                               iPartColor=6409934)

created_parts = Geometry.Transform.ThreePoints(crlTargetParts=[move_part],
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

JPT.Debugger(created_parts)
```
