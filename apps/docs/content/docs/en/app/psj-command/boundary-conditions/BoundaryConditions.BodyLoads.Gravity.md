---
title: "BoundaryConditions.BodyLoads.Gravity()"
description: "Define the acceleration load of gravity to the selected part. User inputs the value of the acceleration load of gravity and it will return the acceleration load of gravity to the selected parts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Body Loads > Gravity"
---

## Description

Define the acceleration load of gravity to the selected part. User inputs the value of the acceleration load of gravity and it will return the acceleration load of gravity to the selected parts.

## Syntax

```psj
BoundaryConditions.BodyLoads.Gravity(...)
```

## Inputs

### `strName` @type(String) @default("Gravity1")

- The name of gravity load to be created.

### `dlGravity` @type(Double List) @required

- The list of acceleration value of each direction (X,Y,Z).

### `crCurCoord` @type(Cursor) @default(None(global coordinate system))

- The coordinate system for the load.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of target parts for creating the acceleration load of gravity.

### `crEdit` @type(Cursor) @default(None)

- An existing gravity load. If this parameter is used, the specified gravity load will be modified. If it is lef&#x74;_&#x4E;one_, a new gravity load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.BodyLoads.Gravity(strName="Gravity1", 
                                                   dlGravity=[0.0, 0.0, -9810.0],
                                                   crlTargets=[Part(1)])

JPT.Debugger(created_bcs)
```
