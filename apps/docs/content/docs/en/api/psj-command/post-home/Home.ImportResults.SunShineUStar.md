---
title: "Home.ImportResults.SunShineUStar()"
description: "Import a SunShine UStar file to the Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > SunShineUStar"
macro _link: "[ImportSunShineUStar](../../macro/home/ImportSunShineUStar)"
---

## Description

Import a SunShine UStar file (\*.op2) to the Jupiter Database.

## Syntax

```psj
Home.ImportResults.SunShineUStar(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The specifying

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type:
  - 1: Standard SunShine Op2 by Property
  - 2: Simple Topology

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The SunShine UStar file (\*.op2 file) is imported successfully.
  - False: The SunShine Star file (\*.op2 file) cannot be imported.

## Sample Code

```psj {3}
import os
UstarFile = os.path.join(JPT.GetAppPathInfo(JPT.PathType.APPDATA _PATH), 'SampleData/PSJ/PSJ-Utility/PostSample/plate _beam _ustar.op2')
Home.ImportResults.SunShineUStar(strPath=UstarFile)
```
