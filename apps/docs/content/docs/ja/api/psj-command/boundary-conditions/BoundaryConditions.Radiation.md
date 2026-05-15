---
title: "BoundaryConditions.Radiation()"
description: "Create a radiation applied to the selected Face or Element or Group. User inputs the radiation value and it will apply the radiation to the selected items"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "BoundaryConditions > Radiation"
macro _link: ""
---

## Description

Create a radiation applied to the selected Face or Element or Group. User inputs the radiation value and it will apply the radiation to the selected items

## Syntax

```psj
BoundaryConditions.Radiation(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strName

- Specify name of radiation.
- The default value is "Radiation".

<!-- @since:5.1.0 @optional -->
### radiation

- Specify radiation
- The default value is LBC\_RADIATION\_DATA().

  #### `dAmbientTemp`

  - A _Double_ specifying the value of Ambient Temperature.
  - This is a required input.

  #### `crTimeDependAm`

  - A _Cursor_ of FieldData specifying information of Time Dependence Ambient in a table format
  - The default value is 0:0 (no reference).

  #### `dEmissivity`

  - A _Double_ specifying the value of Emissivity.
  - This is a required input.

  #### `crTimeDependEm`

  - A _Cursor_ of FieldData specifying information of Time Dependence Emissivity in a table format
  - The default value is 0:0 (no reference).

  #### `crTempDependEm`

  - A _Cursor_ of FieldData specifying information of Temp Dependence Emissivity in a table format
  - The default value is 0:0 (no reference).

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify target to set Radiation.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify existing Radiation when edit it.
- The default value is _None_ (create mode).

## Return Code

A _Cursor_ specifying created / edited Radiation.

## Sample Code

```psj {2-10}
Geometry.Part.Cube()
BoundaryConditions.Radiation(
    strName="Radiation _1", 
    radiation=LBC _RADIATION _DATA(
        dAmbientTemp=373.15, 
        crTimeDependAm=None, 
        dEmissivity=0.5, 
        crTimeDependEm=None, 
        crTempDependEm=None), 
    crlTargets=[Face(26), Elem(301, 341)])
```
