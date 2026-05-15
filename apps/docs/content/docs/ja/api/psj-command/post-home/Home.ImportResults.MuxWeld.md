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

<!-- @since:5.1.0 @required -->
### strPath

- Specify Mux-Weld result file path.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type. For LS-Dyna, it is always set to 1.
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

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The MuxWeld result is imported successfully.
- False: The MuxWeld result cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample mux-weld file.
filepath="C:/Temp/Sample.wsi"

Home.ImportResults.MuxWeld(filepath)
```
