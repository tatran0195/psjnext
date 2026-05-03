---
title: "Home.ImportResults.Marc()"
description: "Import Marc result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Marc"
macro_link: "[ImportMarc](../../macro/home/ImportMarc)"
---

## Description

Import Marc result file.

## Syntax

```psj
Home.ImportResults.Marc(...)
```

## Inputs

### `strPath` @type(String) @required

- Marc result file path.

### `iImportType` @type(Integer) @default(1)

- Import type:

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Marc result is imported successfully.
- False: The Marc result cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample marc file.
filepath="C:/Temp/Sample.t16"

Home.ImportResults.Marc(filepath)
```
