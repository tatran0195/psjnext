---
title: "Assembly.RightClick.ExportMeasureNote()"
description: "Export content of measure notes to csv files."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assembly > RightClick > ExportMeasureNote"
macro_link: "[ExportMeasureNote]"
---

## Description

Export content of measure notes to csv files.

## Syntax

```psj
Assembly.RightClick.ExportMeasureNote(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- Measure notes.

### `strlPaths` @type(List\[String]) @required

- Export file paths.

### `iEncode` @type(Integer) @default(-1)

- Encoding.
  - 0: UTF-8
  - 1: SJIS

### `bWithBOM` @type(Boolean) @default(False)

- Whether or not export csv with BOM.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj{16-20}
import os

#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance1", 
    crFirstNode=Node(7), 
    crSecondNode=Node(5))

path_to_temp=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Assembly.RightClick.ExportMeasureNote(
    crlTargets=[MeasureNote(1)], 
    strlPaths=[os.path.join(path_to_temp,"Distance.csv")], 
    iEncode=0, 
    bWithBOM=True)
```
