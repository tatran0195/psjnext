---
title: "BoundaryConditions.TemperatureLoads.WholeMapping()"
description: "Map temperagure load from solver data or csv."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > WholeMapping"
---

## Description

Map temperagure load from solver data or csv.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.WholeMapping(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"TemperatureLoadsWholeMapping" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMAPPos`

- The m a p position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iViewCp`

- The view component.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCp`

- The component.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSrcType`

- The source type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndexArr0`

- The mapped component index arr0.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndexArr1`

- The mapped component index arr1.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iDScaleFactor`

- The d scale factor.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posOffset`

- The offset.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posRotate`

- The rotate.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dCorScale`

- The cor scale.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSearchRange`

- The search range.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappingMethod`

- The mapping method.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iSubmodelBCMappingType`

- The submodel c mapping type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappingFromStepNo`

- The mapping from step no.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetADVCFile`

- The set ADVC file.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strADVCResultFile`

- The ADVC result file.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetDetATol`

- The set det a tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDetATol`

- The det a tolerance.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetElementSet`

- The set element set.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strElementSet`

- The element set.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTemperature`

- The unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-11}
# Put solver data that includes temperature data.
mapping _data _file = "C:/Temp/sol159.op2"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

# Map temperature load
BoundaryConditions.TemperatureLoads.WholeMapping(
    strName = "TemperatureLoadsWholeMapping _1", 
    strPath = mapping _data _file, 
    iMappingFromStepNo = 0)
```
