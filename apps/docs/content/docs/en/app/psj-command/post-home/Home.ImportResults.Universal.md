---
title: "Home.ImportResults.Universal()"
description: "Import Universal result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Universal"
macro_link: "[ImportUniversal](../../macro/home/ImportUniversal)"
---

## Description

Import Universal result file.

## Syntax

```psj
Home.ImportResults.Universal(...)
```

## Inputs

### `strPath` @type(String) @required

- Universal result file path.

### `iImportType` @type(Integer) @default(1)

- Import type. For Universal file, it is always set to 1.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is imported successfully.
  - False: The Universal file (\*.unv file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample universal file.
filepath="C:/Temp/Sample.unv"

Home.ImportResults.Universal(filepath)
```
