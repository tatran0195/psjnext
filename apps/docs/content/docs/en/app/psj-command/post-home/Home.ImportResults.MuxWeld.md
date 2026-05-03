---
title: "Home.ImportResults.MuxWeld()"
description: "Import Mux-Weld result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > MuxWeld"
macro_link: "[ImportMuxWeld](../../macro/home/ImportMuxWeld)"
---

## Description

Import Mux-Weld result file.

## Syntax

```psj
Home.ImportResults.MuxWeld(...)
```

## Inputs

### `strPath` @type(String) @required

- Mux-Weld result file path.

### `iImportType` @type(Integer) @default(1)

- Import type. For LS-Dyna, it is always set to 1.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

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
