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

<!-- @since:5.0.1 @optional -->
### crlTaBodies

- Specify the parts to make assemble faces.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crlMasterFace

- Specify the master faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveFace

- Specify the slave faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.1.

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
