---
title: "Home.ExportGeometrySurface()"
description: "Export the file in Geometry Surface for Post format (*.stl)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ExportGeometrySurface"
macro_link: "[PostExportGeom](../../macro/home/PostExportGeom)"
---

## Description

Export the file in Geometry Surface for Post format (\*.stl)

## Syntax

```psj
Home.ExportGeometrySurface(...)
```

## Inputs

### `strFolderName` @type(String) @required

- The path of folder.

### `bUseUnit` @type(Boolean) @default(True)

- Whether to use unit when exporting.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not.
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export Geometry Surface for Post
exportFile = Home.ExportGeometrySurface(strFolderName="C:\\temp")
JPT.Debugger(exportFile)
```
