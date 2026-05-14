---
title: "Home.ImportResults.MuxWeld()"
description: "Import Mux-Weld result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > MuxWeld"
macro _link: "[ImportMuxWeld](../../macro/home/ImportMuxWeld)"
---

## Description

Import Mux-Weld result file.

## Syntax

```psj
Home.ImportResults.MuxWeld(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The Mux-Weld result file path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. For LS-Dyna, it is always set to 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The MuxWeld result is imported successfully.
- False: The MuxWeld result cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample mux-weld file.
filepath="C:/Temp/Sample.wsi"

Home.ImportResults.MuxWeld(filepath)
```
