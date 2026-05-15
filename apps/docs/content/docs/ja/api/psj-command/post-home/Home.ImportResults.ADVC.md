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

<!-- @since:5.1.0 @required -->
### strPath

- Specify ADVC result folder path.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type:
  - 1: Standard ADVC2 by Property
  - 2: Simple Topology
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

<!-- @since:5.1.0 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

<!-- @since:5.1.0 @optional -->
### bADVCProcessNameRule

- Specify whether or not ADVC process IDs defined on the ADVC side are displayed.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bDisplayNAResult

- Specify whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### strSelectResultFilePath

- Specify .xml file that defines which result is imported.
- The default value is "".

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
