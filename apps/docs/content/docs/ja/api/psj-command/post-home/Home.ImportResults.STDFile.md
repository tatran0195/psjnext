---
title: "Home.ImportResults.STDFile()"
description: "Import std result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > STDFile"
macro _link: "[ImportSTDFile](../../macro/home/ImportSTDFile)"
---

## Description

Import std result file.

## Syntax

```psj
Home.ImportResults.STDFile(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify std result file path.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type. For STDFile, it is always set to 1.
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
  - True: The STD file (\*.std file) is imported successfully.
  - False: The STD file (\*.std file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample std file.
filepath="C:/Temp/Sample.std"

Home.ImportResults.STDFile(filepath)
```
