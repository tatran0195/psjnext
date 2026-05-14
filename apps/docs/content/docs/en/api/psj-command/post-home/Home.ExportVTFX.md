---
title: "Home.ExportVTFx()"
description: "Export Geometry information or Geometry and Result information for the active document in Web Viewer format(*.vtfx)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ExportVTFx"
macro _link: "[ExportVTFxFile](../../macro/home/ExportVTFxFile)"
---

## Description

Export Geometry information or Geometry and Result information for the active document in Web Viewer format(\*.vtfx).

## Syntax

```psj
Home.ExportVTFx(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strPath`

- The file path to be exported.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iModelType`

- The exporting model type.
  - 0: Pre - Export only geometry
  - 1: Post - Export geometry and selected result

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bExcludeBarPart`

- Whether to exclude the bar parts when exporting.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSurfaceElementOnly`

- The not to export the 3D elements or result on 3D elements.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iData2D`

- The result position of 2D shell.
  - 0: Top
  - 1: Bottom
  - 3: Average

<!-- @since:5.1.0 @type:List[POST _STEP _ITEM] @optional @default:[] -->
### `lSelectedResults`

- The information of the selected result.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplayPostAddTrescaStress`

- Whether to display post add Tresca stress.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCurUnitLength`

- The current unit of length.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCurUnitTime`

- The current unit of length.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCurUnitMass`

- The current unit of mass.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCurUnitForce`

- The current unit of force.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iCurUnitAngle`

- The current unit of angle.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iCurUnitTemperature`

- The current unit of temperature.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSetDefaultResult`

- Whether to set the default result.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-20}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export VTFx
exportFile = Home.ExportVTFx(strPath="C:/temp/ExportVTFX.vtfx", 
                            iModelType=1, 
                            bExcludeBarPart=True, 
                            iData2D=1, 
                            lSelectedResults=[PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                iResultType=6, 
                                strResultName="Displacement", 
                                strResultCompName="Translational", 
                                iResultPos=1)], 
                            bDisplayPostAddTrescaStress=True, 
                            iCurUnitAngle=0, 
                            iCurUnitTemperature=0)
JPT.Debugger(exportFile)
```
