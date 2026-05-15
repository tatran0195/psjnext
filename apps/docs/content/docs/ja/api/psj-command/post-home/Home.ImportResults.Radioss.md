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

<!-- @since:5.1.0 @required -->
### strlPaths

- Specify Open Radioss result file path.

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

<!-- @since:5.1.0 @optional -->
### bReadLoadAndConstraint

- Specify whether or not to read loads and constraint.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bReadConnection

- Specify whether or not to read connections.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bCreateResultsAtMidNode

- Specify whether or not create result at Mid Nodes.
- The default value is _False_.
- The default value is _False_.

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
