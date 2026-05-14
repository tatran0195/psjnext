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

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The nastran result file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

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
