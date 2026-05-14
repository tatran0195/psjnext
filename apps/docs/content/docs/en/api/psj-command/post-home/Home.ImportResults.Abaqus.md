---
title: "Home.ImportResults.Abaqus()"
description: "Import Abaqus result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > Abaqus"
macro _link: "[ImportAbaqus](../../macro/home/ImportAbaqus)"
---

## Description

Import Abaqus result file.

## Syntax

```psj
Home.ImportResults.Abaqus(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The abaqus result file path.

<!-- @since:5.1.0 @type:Integer @required -->
### `iVersion`

- The version of abaqus file to import.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type:

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

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
