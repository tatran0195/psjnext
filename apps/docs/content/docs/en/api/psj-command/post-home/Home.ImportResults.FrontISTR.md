---
title: "Home.ImportResults.FrontISTR()"
description: "Import FrontISTR result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > FrontISTR"
macro _link: "[ImportFrontISTR](../../macro/home/ImportFrontISTR)"
---

## Description

Import FrontISTR result file.

## Syntax

```psj
Home.ImportResults.FrontISTR(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The FrontISTR result folder path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Front ISTR file is imported successfully.
  - False: The Front ISTR file cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample FrontISTR folder.
folderpath="C:/Temp/SampleFrontISTR"

Home.ImportResults.FrontISTR(folderpath)
```
