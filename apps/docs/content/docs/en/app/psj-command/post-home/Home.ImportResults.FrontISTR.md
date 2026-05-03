---
title: "Home.ImportResults.FrontISTR()"
description: "Import FrontISTR result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > FrontISTR"
macro_link: "[ImportFrontISTR](../../macro/home/ImportFrontISTR)"
---

## Description

Import FrontISTR result file.

## Syntax

```psj
Home.ImportResults.FrontISTR(...)
```

## Inputs

### `strPath` @type(String) @required

- FrontISTR result folder path.

### `iImportType` @type(Integer) @default(1)

- Import type.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

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
