---
title: "Home.ImportResults.ADVC()"
description: "Import ADVC result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > ADVC"
macro_link: "[ImportADVC](../../macro/home/ImportADVC)"
---

## Description

Import ADVC result file.

## Syntax

```psj
Home.ImportResults.ADVC(...)
```

## Inputs

### `strPath` @type(String) @required

- ADVC result folder path.

### `iImportType` @type(Integer) @default(1)

- Import type:
  - 1: Standard ADVC2 by Property
  - 2: Simple Topology

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

### `bADVCProcessNameRule` @type(Boolean) @default(False)

- Whether or not ADVC process IDs defined on the ADVC side are displayed.

### `bDisplayNAResult` @type(Boolean) @default(False)

- Whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

### `strSelectResultFilePath` @type(String) @default("")

- .xml file that defines which result is imported.

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
