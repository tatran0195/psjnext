---
title: "Home.ImportResults.Abaqus()"
description: "Import Abaqus result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Abaqus"
macro_link: "[ImportAbaqus](../../macro/home/ImportAbaqus)"
---

## Description

Import Abaqus result file.

## Syntax

```psj
Home.ImportResults.Abaqus(...)
```

## Inputs

### `strPath` @type(String) @required

- Abaqus result file path.

### `iVersion` @type(Integer) @required

- Version of abaqus file to import.

### `iImportType` @type(Integer) @default(1)

- Import type:

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Abaqus file (\*.odb file) is imported successfully.
  - False: The Abaqus file (\*.odb file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample Abaqus file.
filepath="C:/Temp/Sample.odb"

Home.ImportResults.Abaqus(filepath, iVersion=2023)
```
