---
title: "Assemble.FindMatingFaceEx()"
description: "Find the mating faces which can be used in Assemble.AssembleFaceEx() function"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Find Mating Face"
---

## Description

Find the mating faces which can be used in [Assemble.AssembleFaceEx()](Assemble.AssembleFaceEx) function.

## Syntax

```psj
Assemble.FindMatingFaceEx(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlTaBodies`

- The parts to make assemble faces.
- This is the required input.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterFace`

- The master faces.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveFace`

- The slave faces.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dTolerance`

- The tolerance.

## Return Code

A list of pair mating faces ID found.

## Sample Code

```psj {6,7}
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube _2", 
                           iPartColor=6409934)

pair _faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2], 
                                      dMatingTol=0.001)

JPT.Debugger(pair _faces)
```
