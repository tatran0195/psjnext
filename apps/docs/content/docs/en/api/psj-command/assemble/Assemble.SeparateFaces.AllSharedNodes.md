---
title: "Assemble.SeparateFaces.AllSharedNodes()"
description: "Separate all shared nodes existing on the current model (Also separate all the existing shared faces)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Separate Faces > All Shared Nodes"
macro _link: "[ASMSeparateAll2](../../macro/assemble/ASMSeparateAll2)"
---

## Description

Separate all shared nodes existing on the current model (Also separate all the existing shared faces).

## Syntax

```psj
Assemble.SeparateFaces.AllSharedNodes(...)
```

## Inputs

This function does not contains any input values.

## Return Code

A _Boolean_ specifying whether the shared nodes are separated successfully or not:

- _True_: All the shared nodes are separated successfully.
- _False_: Cannot separate shared nodes/The model does not contains any shared nodes.

## Sample Code

```psj {13}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)

Assemble.FindMatingFaceEx(crlTaBodies=[Part(1, 2)], 
                          dMatingTol=0.000222222)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.000222222, 
                        iTypeConnectPos=0, 
                        bFitEdge=True)

separate _nodes = Assemble.SeparateFaces.AllSharedNodes()

JPT.Debugger(separate _nodes)
```
