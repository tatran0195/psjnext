---
title: "BoundaryConditions.Convection.Constant()"
description: "Create natural convection condition on selected face, element or group. User inputs external temperature and convection coefficient in scalar or in a table format, then it will return convection load to the specified location"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Convection > Constant"
---

## Description

Create natural convection condition on selected face, element or group. User inputs external temperature and convection coefficient in scalar or in a table format, then it will return convection load to the specified location.

## Syntax

```psj
BoundaryConditions.Convection.Constant(...)
```

## Inputs

### `strName` @type(String) @default("Convection\_1")

- The name of convection setting.

### `dExternalTemp` @type(Double) @required

- The external temperature (default unit: Kelvin).

### `crTableTimeTemp` @type(Cursor) @default(None)

- The table of dependency between time and external temperature. This table can be created usin&#x67;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

### `dConvectionCoef` @type(Double) @required

- The convection coefficient (default unit: W/m^2\*K).

### `crTableTimeCoeff` @type(Cursor) @default(None)

- The table of dependency between time and convection coefficient. This table can be created usin&#x67;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

### `crTableTempCoeff` @type(Cursor) @default(None)

- The table of dependency between temperature and convection coefficient. This table can be created usin&#x67;_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets for convection boundary condition. Target can be faces, elements or groups.

### `crEdit` @type(Cursor) @default(None)

- An existing convection setting (constant).
  - If this parameter is used, the specified convection setting (constant) will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new convection setting (constant) will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Convection.Constant(strName="Convection_26",
                                                     dExternalTemp=373.15, 
                                                     dConvectionCoef=1E-3, 
                                                     crlTargets=[Face(26)])

JPT.Debugger(created_bcs)
```
