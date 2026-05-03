---
title: "Home.ImportResults.Radioss()"
description: "Import Open Radioss result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Radioss"
macro_link: "[ImportRadioss](../../macro/home/ImportRadioss)"
---

## Description

Import Open Radioss result file.

## Syntax

```psj
Home.ImportResults.Radioss(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- Open Radioss result file path.

### `iImportType` @type(Integer) @default(1)

- Import type.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

### `bReadLoadAndConstraint` @type(Boolean) @default(False)

- Whether or not to read loads and constraint.

### `bReadConnection` @type(Boolean) @default(False)

- Whether or not to read connections.

### `bCreateResultsAtMidNode` @type(Boolean) @default(False)

- Whether or not create result at Mid Nodes.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Open Radioss file is imported successfully.
  - False: The Open Radioss cannot be imported.

## Sample Code

```psj {4}
# Please set path to your sample radioss file.
filepath="C:/Temp/result.A001"

Home.ImportResults.Radioss(filepath)
```
