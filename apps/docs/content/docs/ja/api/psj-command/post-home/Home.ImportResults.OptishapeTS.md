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

<!-- @since:5.1.0 @required -->
### strlPaths

- Specify Optishape-TS result file paths.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type. For Optishape-TS, it is always set to 1.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

<!-- @since:5.1.0 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

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
