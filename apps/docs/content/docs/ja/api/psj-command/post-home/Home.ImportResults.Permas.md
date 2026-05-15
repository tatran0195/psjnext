---
title: "Home.ImportResults.Permas()"
description: "Import Permas result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > Permas"
macro _link: "[ImportPermas](../../macro/home/ImportPermas)"
---

## Description

Import Permas result file.

## Syntax

```psj
Home.ImportResults.Permas(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify nastran result file path.

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

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Permas file is imported successfully.
  - False: The Permas file cannot be imported.

## Sample Code

```psj {4}
# Please set path to your sample permas file.
filepath="C:/Temp/result.post.gz"

Home.ImportResults.Permas(filepath)
```
