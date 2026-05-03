---
title: "Home.ImportResults.STDFile()"
description: "Import std result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > STDFile"
macro_link: "[ImportSTDFile](../../macro/home/ImportSTDFile)"
---

## Description

Import std result file.

## Syntax

```psj
Home.ImportResults.STDFile(...)
```

## Inputs

### `strPath` @type(String) @required

- Std result file path.

### `iImportType` @type(Integer) @default(1)

- Import type. For STDFile, it is always set to 1.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

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
