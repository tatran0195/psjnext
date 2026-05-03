---
title: "Home.ImportResults.Nastran()"
description: "Import Nastran / Vibro result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Nastran"
macro_link: "[ImportNastran](../../macro/home/ImportNastran)"
---

## Description

Import Nastran / Vibro result file.

## Syntax

```psj
Home.ImportResults.Nastran(...)
```

## Inputs

### `strPath` @type(String) @default("")

- Nastran result file path.

### `strlPaths` @type(List\[String]) @default(\[])

- Nastran hdf5 result file paths.

### `iImportType` @type(Integer) @default(1)

- Import type:
  - 1: Standard Nastran Op2 by Property
  - 2: Simple Topology

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

### `bIsVibro` @type(Boolean) @default(False)

- Whether or not the file is Vibro Acoustic.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran file (\*.op2 file) is imported successfully.
  - False: The Nastran file (\*.op2 file) cannot be imported.

## Sample Code

```psj {5}
import os
NastranFile = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH), 
    'SampleData/PSJ/PSJ-Utility/PostSample/101_solid.op2')
Home.ImportResults.Nastran(strPath=NastranFile)
```
