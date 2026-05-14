---
title: "MidPlane.FindMidPlane()"
description: "Create mid-planes for the specified parts."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlane > FindMidPlane"
macro _link: "FindMidPlane"
---

## Description

Create mid-planes for the specified parts.

## Syntax

```psj
MidPlane.FindMidPlane(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargetParts`

- The parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6}
Geometry.Part.Cube(dlLength=[0.001, 0.01, 0.01])
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                    dlLength=[0.002, 0.01, 0.01],
                    strName="Cube _2",
                    iPartColor=6409934)
MidPlane.FindMidPlane(crlTargetParts=[Part(1, 2)])
```
