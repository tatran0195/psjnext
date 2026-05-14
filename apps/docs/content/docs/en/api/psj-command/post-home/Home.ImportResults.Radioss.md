---
title: "Home.ImportResults.Radioss()"
description: "Import Open Radioss result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > Radioss"
macro _link: "[ImportRadioss](../../macro/home/ImportRadioss)"
---

## Description

Import Open Radioss result file.

## Syntax

```psj
Home.ImportResults.Radioss(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The Open Radioss result file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadLoadAndConstraint`

- Whether or not to read loads and constraint.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadConnection`

- Whether or not to read connections.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateResultsAtMidNode`

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
