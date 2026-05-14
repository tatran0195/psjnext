---
title: "BoundaryConditions.Convection.Constant()"
description: "Create natural convection condition on selected face, element or group. User inputs external temperature and convection coefficient in scalar or in a table format, then it will return convection load to the specified location"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Convection > Constant"
---

## Description

Create natural convection condition on selected face, element or group. User inputs external temperature and convection coefficient in scalar or in a table format, then it will return convection load to the specified location.

## Syntax

```psj
BoundaryConditions.Convection.Constant(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Convection _1" -->
### `strName`

- The name of convection setting.

<!-- @since:5.0.1 @type:Double @required -->
### `dExternalTemp`

- The external temperature (default unit: Kelvin).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTableTimeTemp`

- The table of dependency between time and external temperature. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

<!-- @since:5.0.1 @type:Double @required -->
### `dConvectionCoef`

- The convection coefficient (default unit: W/m^2\*K).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTableTimeCoeff`

- The table of dependency between time and convection coefficient. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTableTempCoeff`

- The table of dependency between temperature and convection coefficient. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The list of targets for convection boundary condition. Target can be faces, elements or groups.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing convection setting (constant).
  - If this parameter is used, the specified convection setting (constant) will be modified.
  - If it is left _None_, a new convection setting (constant) will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.Convection.Constant(strName="Convection _26",
                                                     dExternalTemp=373.15, 
                                                     dConvectionCoef=1E-3, 
                                                     crlTargets=[Face(26)])

JPT.Debugger(created _bcs)
```
