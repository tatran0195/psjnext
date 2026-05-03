---
title: "BoundaryConditions.LoadCase()"
description: "Create a load case that bundles loads and constraints. Load cases can be referenced when creating analysis solver input data"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > LoadCase"
---

## Description

Create a load case that bundles loads and constraints. Load cases can be referenced when creating analysis solver input data.

## Syntax

```psj
BoundaryConditions.LoadCase(...)
```

## Inputs

### `strName` @type(String) @default("LoadCase1")

- The name of the load case to be created.

### `dFactor` @type(Double) @default(1.0)

- The load factor for Nastran that applies to the entire load case to be created. Used when multiplying the load by a factor.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of all created boundary conditions.

### `iExportId` @type(Integer) @default(1)

- The export identity number of load case.

### `dlTargetFactor` @type(List\[Double]) @default(\[])

- The list factor of each boundary condition.

### `crEdit` @type(Cursor) @default(None)

- An existing load case. If this parameter is used, the specified load case will be modified. If it is lef&#x74;_&#x4E;one_, a new load case will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {14,15,16}
Geometry.Part.Cube()

BoundaryConditions.Pressure.General(dPressure=1000000.0, 
                                    crlTargets=[Face(24)])

BoundaryConditions.Pressure.General(strName="Pressure2", 
                                    dPressure=2000000.0,
                                    crlTargets=[Face(21)])

BoundaryConditions.Pressure.General(strName="Pressure3", 
                                    dPressure=3000000.0,
                                    crlTargets=[Face(25)])

created_bcs = BoundaryConditions.LoadCase(crlTargets=[LbcGPressure(1, 2, 3)], 
                                          iExportId=4,
                                          dlTargetFactor=[1.0, 1.0, 1.0])

JPT.Debugger(created_bcs)
```
