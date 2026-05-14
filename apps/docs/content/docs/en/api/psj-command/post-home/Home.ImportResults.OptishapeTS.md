---
title: "Home.ImportResults.OptishapeTS()"
description: "Import Optishape-TS result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > OptishapeTS"
macro _link: "[ImportOptishapeTS](../../macro/home/ImportOptishapeTS)"
---

## Description

Import Optishape-TS result file.

## Syntax

```psj
Home.ImportResults.OptishapeTS(...)
```

## Inputs

### `strlPaths`

- A List of _String_ specifying Optishape-TS result file paths.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. For Optishape-TS, it is always set to 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Optishape file is imported successfully.
  - False: The Optishape file cannot be imported.

## Sample Code

```psj {5-6}
import os
#Put your result
result _data='C:/Temp/OptiShapeResult'

Home.ImportResults.OptishapeTS(
    strlPaths=[os.path.join(result _data,"sample.op2")])
```
