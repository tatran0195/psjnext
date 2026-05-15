---
title: "BoundaryConditions.LoadCase()"
description: "Create a load case that bundles loads and constraints. Load cases can be referenced when creating analysis solver input data"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > LoadCase"
---

## Description

Create a load case that bundles loads and constraints. Load cases can be referenced when creating analysis solver input data.

## Syntax

```psj
BoundaryConditions.LoadCase(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the load case to be created.
- The default value is "LoadCase1".

<!-- @since:5.0.1 @optional -->
### dFactor

- Specify the load factor for Nastran that applies to the entire load case to be created. Used when multiplying the load by a factor.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of all created boundary conditions.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iExportId

- Specify the export identity number of load case.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dlTargetFactor

- Specify the list factor of each boundary condition.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing load case. If this parameter is used, the specified load case will be modified. If it is left _None_, a new load case will be created.
- The default value is _None_.

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

created _bcs = BoundaryConditions.LoadCase(crlTargets=[LbcGPressure(1, 2, 3)], 
                                          iExportId=4,
                                          dlTargetFactor=[1.0, 1.0, 1.0])

JPT.Debugger(created _bcs)
```
