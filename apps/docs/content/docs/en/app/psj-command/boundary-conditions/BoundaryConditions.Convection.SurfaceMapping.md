---
title: "BoundaryConditions.Convection.SurfaceMapping()"
description: "Create load boundary condition of convection surface mapping"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Convection > SurfaceMapping"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create load boundary condition of convection surface mapping.

## Syntax

```psj
BoundaryConditions.Convection.SurfaceMapping(...)
```

## Inputs

### `strName` @type(String) @default("MappingConvection\_1")

- The Mapping Convection name.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets.

### `iPos` @type(Integer) @default(0)

- The MAP position.
  - 0: MAP\_POS\_SURFACE\_NODE.
    - 1: MAP\_POS\_SOLID\_NODE.
    - 2: MAP\_POS\_SURFACE\_ELEM.
    - 3: MAP\_POS\_SOLID\_ELEM.

### `iViewCp` @type(Integer) @default(0)

- The component index that to be previewed.

### `iCp` @type(Integer) @default(0)

- The component.

### `iSrcType` @type(Integer) @default(0)

- The source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: CSV.

### `iMappedCpIndex0` @type(Integer) @default(0)

- The mapped component index0.

### `iMappedCpIndex1` @type(Integer) @default(0)

- The mapped component index1.

### `dRScale` @type(Double) @default(1.0)

- The rotation scale.

### `posOffset` @type(Position) @default(\[0,0,0])

- The offset.

### `posAxis` @type(Position) @default(\[0,0,0])

- The axis.

### `dTScale` @type(Double) @default(1.0)

- The translation scale.

### `dSearchRange` @type(Double) @default(1.0)

- The search range.

### `iHTCUnit` @type(Integer) @default(0)

- The HTC unit.
  - 0: mW/mm^2.
  - 1: W/mm^2.
  - 2: miuW/mm^2.
  - 3: lcal/mm^2\*h.
  - 4: lbf/ft\*s.
  - 5: lbf/in\*s.

### `iTempUnit` @type(Integer) @default(0)

- The temperature unit.
  - 0: degree Kenvil (K).
  - 1: degree Celsius (deg C).
  - 2: degree Fahrenheit (deg F).

### `strPath` @type(String) @default("")

- The path.

### `crEdit` @type(Cursor) @default(None)

- The cursor of boundary condition need editing.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection_5",
    crlTargets=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0,
    iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0,
    dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)

print(result) #for checking return value
```
