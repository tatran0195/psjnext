---
title: "BoundaryConditions.BodyLoads.Gravity()"
description: "Define the acceleration load of gravity to the selected part. User inputs the value of the acceleration load of gravity and it will return the acceleration load of gravity to the selected parts"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Body Loads > Gravity"
---

## Description

Define the acceleration load of gravity to the selected part. User inputs the value of the acceleration load of gravity and it will return the acceleration load of gravity to the selected parts.

## Syntax

```psj
BoundaryConditions.BodyLoads.Gravity(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Gravity1" -->
### `strName`

- The name of gravity load to be created.

<!-- @since:5.0.1 @type:Double List @required -->
### `dlGravity`

- The list of acceleration value of each direction (X,Y,Z).

<!-- @since:5.0.1 @type:Cursor @optional @default:None(global coordinate system) -->
### `crCurCoord`

- The coordinate system for the load.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of target parts for creating the acceleration load of gravity.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing gravity load. If this parameter is used, the specified gravity load will be modified. If it is left _None_, a new gravity load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.BodyLoads.Gravity(strName="Gravity1", 
                                                   dlGravity=[0.0, 0.0, -9810.0],
                                                   crlTargets=[Part(1)])

JPT.Debugger(created _bcs)
```
