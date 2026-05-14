---
title: "BoundaryConditions.BoundaryTemperature.SurfaceMapping()"
description: "Create surface mapping boundary temperature"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > BoundaryTemperature > SurfaceMapping"
---

## Description

Create surface mapping boundary temperature.

## Syntax

```psj
BoundaryConditions.BoundaryTemperature.SurfaceMapping(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MappingTemperature" -->
### `strName`

- The mapping temperature name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The targets.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMAPPos`

- The map position.
  - 0: MAP\_POS\_SURFACE\_NODE.
    - 1: MAP\_POS\_SOLID\_NODE.
    - 2: MAP\_POS\_SURFACE\_ELEM.
    - 3: MAP\_POS\_SOLID\_ELEM.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iViewCp`

- The component index that to be previewed.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCp`

- The component.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSrcType`

- The source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: Convection Text.
    - 3: SZText.
    - 4: ADVC.
    - 5: SubmodelBC ADVC.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndexArr0`

- The mapped component index arr0.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappedCpIndexArr1`

- The mapped component index arr1.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dScaleFactor`

- The scale factor.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posOffset`

- The offset.

<!-- @since:5.0.1 @type:Position @optional @default:[0,0,0] -->
### `posRotate`

- The rotate.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dCorScale`

- The coordinate scale.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSearchRange`

- The search range.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUnit`

- The unit.
  \- 0: degree Kenvil (K).
  - 1: degree Celsius (deg C).
  - 2: degree Fahrenheit (deg F).

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The cursor of boundary condition need editing.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappingMethod`

- The mapping method.
  - 0: Mapping Nearest.
    - 1: Mapping CMLS.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iSubmodeLBCMappingType`

- The submode load boundary condition mapping type.
  - 0: Mapping type FORCED DISPLACEMENT.
    - 1: Mapping type LOAD FORCE.
    - 2: Mapping type EMPERATURE.
    - 3: Mapping type FORCED TEMPERATURE.
    - 4: Mapping type HEAT FLUX.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMappingFromStepNo`

- The mapping from step number.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetADVCFile`

- Whether set ADVC file.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strADVCResultFile`

- The ADVC result file.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetDetATol`

- Whether set det a tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDetATol`

- The det a tolerance.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetElementSet`

- Whether set element set.

<!-- @since:5.0.1 @type:String @optional @default:"all" -->
### `strElementSet`

- The element set.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.BoundaryTemperature.SurfaceMapping(strName="MappingTemperature",
        crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0,
        iMappedCpIndexArr1=0, dScaleFactor=1.0, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1.0,
        dSearchRange=0.0, iUnit=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=3,
        iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False,
        dDetATol=DFLT _DBL, bSetElementSet=False, strElementSet="all")
        
print(result) #for checking return value
```
