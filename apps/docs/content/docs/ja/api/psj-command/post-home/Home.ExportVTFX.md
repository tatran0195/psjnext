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

<!-- @since:5.1.0 @optional -->
### strPath

- Specify the file path to be exported.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iModelType

- Specify the exporting model type.
  - 0: Pre - Export only geometry
  - 1: Post - Export geometry and selected result
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bExcludeBarPart

- Specify whether to exclude the bar parts when exporting.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bSurfaceElementOnly

- Specify not to export the 3D elements or result on 3D elements.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iData2D

- Specify the result position of 2D shell.
  - 0: Top
  - 1: Bottom
  - 3: Average
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### lSelectedResults

- Specify the information of the selected result.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bDisplayPostAddTrescaStress

- Specify whether to display post add Tresca stress.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iCurUnitLength

- Specify the current unit of length.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iCurUnitTime

- Specify the current unit of length.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iCurUnitMass

- Specify the current unit of mass.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iCurUnitForce

- Specify the current unit of force.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iCurUnitAngle

- Specify the current unit of angle.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iCurUnitTemperature

- Specify the current unit of temperature.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bSetDefaultResult

- Specify whether to set the default result.
- The default value is _False_.

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
