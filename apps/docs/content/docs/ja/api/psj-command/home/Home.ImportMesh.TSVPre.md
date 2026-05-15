---
title: "Home.ImportMesh.TSVPre()"
description: "Convert a old TSV-Pre/Designer file into one or more jtdb files."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportMesh > TSVPre"
macro _link: "[ImportVDB](../../macro/home/ImportVDB)"
---

## Description

Convert a old TSV-Pre/Designer file into one or more jtdb files.

## Syntax

```psj
Home.ImportMesh.TSVPre(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strImportPath

- Specify the import path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### strExportPath

- Specify the export path.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### ilModelIndex

- Specify the model index.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iMerge

- Specify the merge.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8}
import os

VDB _file _path = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM _PATH), 
    "SampleData/PSJ/PSJ-Utility/VDBSample/sample.vdb")

export _file _path = os.environ["Temp"] + "/TechnoStar/"
Home.ImportMesh.TSVPre(strImportPath=VDB _file _path, strExportPath=export _file _path)
```
