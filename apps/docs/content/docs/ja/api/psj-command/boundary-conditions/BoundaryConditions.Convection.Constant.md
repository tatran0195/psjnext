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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of convection setting.
- The default value is "Convection\_1".

<!-- @since:5.0.1 @required -->
### dExternalTemp

- Specify the external temperature (default unit: Kelvin).

<!-- @since:5.0.1 @optional -->
### crTableTimeTemp

- Specify the table of dependency between time and external temperature. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### dConvectionCoef

- Specify the convection coefficient (default unit: W/m^2\*K).

<!-- @since:5.0.1 @optional -->
### crTableTimeCoeff

- Specify the table of dependency between time and convection coefficient. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crTableTempCoeff

- Specify the table of dependency between temperature and convection coefficient. This table can be created using_[BoundaryConditions.FieldData](BoundaryConditions.FieldData)_.
- The default value is _None_.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of targets for convection boundary condition. Target can be faces, elements or groups.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing convection setting (constant).
  - If this parameter is used, the specified convection setting (constant) will be modified.
  - If it is left _None_, a new convection setting (constant) will be created.
- The default value is _None_.

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
