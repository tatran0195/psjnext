---
title: "Assembly.RightClick.ExportMeasureNote()"
description: "Export content of measure notes to csv files."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assembly > RightClick > ExportMeasureNote"
macro _link: "[ExportMeasureNote]"
---

## Description

Export content of measure notes to csv files.

## Syntax

```psj
Assembly.RightClick.ExportMeasureNote(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify measure notes.

<!-- @since:5.1.0 @required -->
### strlPaths

- Specify export file paths.

<!-- @since:5.1.0 @optional -->
### iEncode

- Specify encoding.
  - 0: UTF-8
  - 1: SJIS
- The default value is -1.

<!-- @since:5.1.0 @optional -->
### bWithBOM

- Specify whether or not export csv with BOM.
- The default value is _False_.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```pj {16-20}
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

path _to _temp=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)

Assembly.RightClick.ExportMeasureNote(
    crlTargets=[MeasureNote(1)], 
    strlPaths=[os.path.join(path _to _temp,"Distance.csv")], 
    iEncode=0, 
    bWithBOM=True)
```
