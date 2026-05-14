---
title: "Home.ImportResults.ADVC()"
description: "Import ADVC result file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > ADVC"
macro _link: "[ImportADVC](../../macro/home/ImportADVC)"
---

## Description

Import ADVC result file.

## Syntax

```psj
Home.ImportResults.ADVC(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The ADVC result folder path.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type:
  - 1: Standard ADVC2 by Property
  - 2: Simple Topology

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bADVCProcessNameRule`

- Whether or not ADVC process IDs defined on the ADVC side are displayed.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplayNAResult`

- Whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strSelectResultFilePath`

- The .xml file that defines which result is imported.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The ADVC file is imported successfully.
  - False: The ADVC file cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample ADVC folder.
folderpath="C:/Temp/SampleADVC"

Home.ImportResults.ADVC(folderpath)
```
