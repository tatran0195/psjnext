---
title: "Home.ExportVTFx()"
description: "Export Geometry information or Geometry and Result information for the active document in Web Viewer format(*.vtfx)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ExportVTFx"
macro_link: "[ExportVTFxFile](../../macro/home/ExportVTFxFile)"
---

## Description

Export Geometry information or Geometry and Result information for the active document in Web Viewer format(\*.vtfx).

## Syntax

```psj
Home.ExportVTFx(...)
```

## Inputs

### `strPath` @type(String) @default("")

- The file path to be exported.

### `iModelType` @type(Integer) @default(1)

- The exporting model type.
  - 0: Pre - Export only geometry
  - 1: Post - Export geometry and selected result

### `bExcludeBarPart` @type(Boolean) @default(False)

- Whether to exclude the bar parts when exporting.

### `bSurfaceElementOnly` @type(Boolean) @default(False)

- Not to export the 3D elements or result on 3D elements.

### `iData2D` @type(Integer) @default(0)

- The result position of 2D shell.
  - 0: Top
  - 1: Bottom
  - 3: Average

### `lSelectedResults` @type(List\[POST\_STEP\_ITEM]) @default(\[])

- The information of the selected result.

### `bDisplayPostAddTrescaStress` @type(Boolean) @default(False)

- Whether to display post add Tresca stress.

### `iCurUnitLength` @type(Integer) @default(0)

- The current unit of length.

### `iCurUnitTime` @type(Integer) @default(0)

- The current unit of length.

### `iCurUnitMass` @type(Integer) @default(0)

- The current unit of mass.

### `iCurUnitForce` @type(Integer) @default(0)

- The current unit of force.

### `iCurUnitAngle` @type(Integer) @default(1)

- The current unit of angle.

### `iCurUnitTemperature` @type(Integer) @default(1)

- The current unit of temperature.

### `bSetDefaultResult` @type(Boolean) @default(False)

- Whether to set the default result.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-20}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
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
