---
title: "Home.ImportResults.Nastran()"
description: "Import Nastran / Vibro result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > Nastran"
macro _link: "[ImportNastran](../../macro/home/ImportNastran)"
---

## Description

Import Nastran / Vibro result file.

## Syntax

```psj
Home.ImportResults.Nastran(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strPath

- Specify nastran result file path.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strlPaths

- Specify nastran hdf5 result file paths.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type:
  - 1: Standard Nastran Op2 by Property
  - 2: Simple Topology
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

<!-- @since:5.1.0 @optional -->
### bIsVibro

- Specify whether or not the file is Vibro Acoustic.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran file (\*.op2 file) is imported successfully.
  - False: The Nastran file (\*.op2 file) cannot be imported.

## Sample Code

```psj {5}
import os
NastranFile = os.path.join(
    JPT.GetAppPathInfo(JPT.PathType.PROGRAM _PATH), 
    'SampleData/PSJ/PSJ-Utility/PostSample/101 _solid.op2')
Home.ImportResults.Nastran(strPath=NastranFile)
```
