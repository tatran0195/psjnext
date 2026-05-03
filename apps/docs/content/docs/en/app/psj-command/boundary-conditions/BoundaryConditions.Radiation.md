---
title: "BoundaryConditions.Radiation()"
description: "Create a radiation applied to the selected Face or Element or Group. User inputs the radiation value and it will apply the radiation to the selected items"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "BoundaryConditions > Radiation"
macro_link: ""
---

## Description

Create a radiation applied to the selected Face or Element or Group. User inputs the radiation value and it will apply the radiation to the selected items

## Syntax

```psj
BoundaryConditions.Radiation(...)
```

## Inputs

### `strName` @type(String) @default("Radiation")

- Name of radiation.

### `radiation` @type(LBC\_RADIATION\_DATA) @default(LBC\_RADIATION\_DATA())

- Radiation

### `crlTargets` @type(List\[Cursor]) @default(\[])

- Target to set Radiation.

### `crEdit` @type(Cursor) @default(None (create mode))

- Existing Radiation when edit it.

## Return Code

A _Cursor_ specifying created / edited Radiation.

## Sample Code

```psj {2-10}
Geometry.Part.Cube()
BoundaryConditions.Radiation(
    strName="Radiation_1", 
    radiation=LBC_RADIATION_DATA(
        dAmbientTemp=373.15, 
        crTimeDependAm=None, 
        dEmissivity=0.5, 
        crTimeDependEm=None, 
        crTempDependEm=None), 
    crlTargets=[Face(26), Elem(301, 341)])
```
