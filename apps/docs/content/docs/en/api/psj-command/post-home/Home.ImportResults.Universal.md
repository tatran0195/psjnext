---
title: "Home.ImportResults.Universal()"
description: "Import Universal result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > Universal"
macro _link: "[ImportUniversal](../../macro/home/ImportUniversal)"
---

## Description

Import Universal result file.

## Syntax

```psj
Home.ImportResults.Universal(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The Universal result file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. For Universal file, it is always set to 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is imported successfully.
  - False: The Universal file (\*.unv file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample universal file.
filepath="C:/Temp/Sample.unv"

Home.ImportResults.Universal(filepath)
```
