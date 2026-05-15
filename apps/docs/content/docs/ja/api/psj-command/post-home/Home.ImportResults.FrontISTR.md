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

<!-- @since:5.1.0 @required -->
### strPath

- Specify FrontISTR result folder path.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

<!-- @since:5.1.0 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

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
