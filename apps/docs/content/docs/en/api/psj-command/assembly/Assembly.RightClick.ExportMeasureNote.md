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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The measure notes.

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The export file paths.

<!-- @since:5.1.0 @type:Integer @optional @default:-1 -->
### `iEncode`

- The encoding.
  - 0: UTF-8
  - 1: SJIS

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bWithBOM`

- Whether or not export csv with BOM.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {16-20}
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
