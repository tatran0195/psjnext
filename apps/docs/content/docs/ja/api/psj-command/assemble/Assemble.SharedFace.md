---
title: "Assemble.SharedFace()"
description: "Create an assembled face/shared face group"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Shared Face"
macro _link: "[CreateSharedFace](../../macro/assemble/CreateSharedFace)"
---

## Description

Create an assembled face/shared face group.

## Syntax

```psj
Assemble.SharedFace(...)
```

## Inputs

This function does not contains any input values.

## Return Code

A _List of Cursor_ specifying the created shared faces.

## Sample Code

```psj {21}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube _3", 
                   iPartColor=14903267)

Assemble.FindMatingFaceEx(crlTaBodies=[Part(1, 
                                            2, 
                                            3)], 
                          dMatingTol=0.000222222)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[48, 
                                                   73, 
                                                   49, 
                                                   24], 
                        dTolerance=0.000222222, 
                        iTypeConnectPos=0, 
                        bFitEdge=True)

created _shared _faces = Assemble.SharedFace()

JPT.Debugger(created _shared _faces)
```
