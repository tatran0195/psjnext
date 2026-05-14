---
title: "BoundaryConditions.Convection.SurfaceMapping()"
description: "Create load boundary condition of convection surface mapping"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Convection > SurfaceMapping"
---

## Description

Create load boundary condition of convection surface mapping.

## Syntax

```psj
BoundaryConditions.Convection.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MappingConvection _1" -->
### `strName`

- The Mapping Convection name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The targets.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPos`

- The MAP position.
  - 0: MAP\_POS\_SURFACE\_NODE.
    - 1: MAP\_POS\_SOLID\_NODE.
    - 2: MAP\_POS\_SURFACE\_ELEM.
    - 3: MAP\_POS\_SOLID\_ELEM.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iViewCp`

- The component index that to be previewed.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCp`

- The component.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSrcType`

- The source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: CSV.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndex0`

- The mapped component index0.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndex1`

- The mapped component index1.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dRScale`

- The rotation scale.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posOffset`

- The offset.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posAxis`

- The axis.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTScale`

- The translation scale.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dSearchRange`

- The search range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iHTCUnit`

- The HTC unit.
  - 0: mW/mm^2.
  - 1: W/mm^2.
  - 2: miuW/mm^2.
  - 3: lcal/mm^2\*h.
  - 4: lbf/ft\*s.
  - 5: lbf/in\*s.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTempUnit`

- The temperature unit.
  - 0: degree Kenvil (K).
  - 1: degree Celsius (deg C).
  - 2: degree Fahrenheit (deg F).

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The cursor of boundary condition need editing.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection _5",
    crlTargets=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0,
    iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0,
    dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)

print(result) #for checking return value
```
