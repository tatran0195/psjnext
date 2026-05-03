---
title: "Home.ImportResults.Permas()"
description: "Import Permas result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Permas"
macro_link: "[ImportPermas](../../macro/home/ImportPermas)"
---

## Description

Import Permas result file.

## Syntax

```psj
Home.ImportResults.Permas(...)
```

## Inputs

### `strPath` @type(String) @required

- Nastran result file path.

### `iImportType` @type(Integer) @default(1)

- Import type.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

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
