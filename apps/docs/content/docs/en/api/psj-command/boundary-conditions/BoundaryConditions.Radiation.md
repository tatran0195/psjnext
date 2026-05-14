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

<!-- @since:5.1.0 @type:String @optional @default:"Radiation" -->
### `strName`

- The name of radiation.

<!-- @since:5.1.0 @type:LBC _RADIATION _DATA @optional @default:LBC _RADIATION _DATA() -->
### `radiation`

- The radiation

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target to set Radiation.

<!-- @since:5.1.0 @type:Cursor @optional @default:None (create mode) -->
### `crEdit`

- The existing Radiation when edit it.

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
