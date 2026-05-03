---
title: "Home.ImportResults.SunShineUStar()"
description: "Import a SunShine UStar file to the Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > SunShineUStar"
macro_link: "[ImportSunShineUStar](../../macro/home/ImportSunShineUStar)"
---

## Description

Import a SunShine UStar file (\*.op2) to the Jupiter Database.

## Syntax

```psj
Home.ImportResults.SunShineUStar(...)
```

## Inputs

### `strPath` @type(String) @required

- Specifying

### `iImportType` @type(Integer) @default(1)

- Import type:
  - 1: Standard SunShine Op2 by Property
  - 2: Simple Topology

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The SunShine UStar file (\*.op2 file) is imported successfully.
  - False: The SunShine Star file (\*.op2 file) cannot be imported.

## Sample Code

```psj {3}
import os
UstarFile = os.path.join(JPT.GetAppPathInfo(JPT.PathType.APPDATA_PATH), 'SampleData/PSJ/PSJ-Utility/PostSample/plate_beam_ustar.op2')
Home.ImportResults.SunShineUStar(strPath=UstarFile)
```
