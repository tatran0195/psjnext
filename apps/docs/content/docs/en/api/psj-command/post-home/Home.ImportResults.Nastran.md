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

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strPath`

- The nastran result file path.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlPaths`

- The nastran hdf5 result file paths.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type:
  - 1: Standard Nastran Op2 by Property
  - 2: Simple Topology

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

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bIsVibro`

- Whether or not the file is Vibro Acoustic.

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
