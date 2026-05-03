---
title: "Home.AddResults.ADVC()"
description: "Add ADVC results to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > ADVC"
macro_link: "[AddResultsADVC](../../macro/home/AddResultsADVC)"
---

## Description

Add ADVC results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.ADVC(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the ADVC files which will be used for importing.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

### `bADVCProcessNameRule` @type(Boolean) @default(False)

- Whether or not ADVC process IDs defined on the ADVC side are displayed.

### `bDisplayNAResult` @type(Boolean) @default(False)

- Whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

### `strPathSelectResultFile` @type(String) @default("")

- Specifying

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The ADVC result is added to the document successfully.
  - False: The ADVC result is not added to the document.

## Sample Code

```psj {6}
#Please set path to your sample ADVC folder.
meshfile='C:/Sample/mesh.adx'
folderpath="C:/Temp/SampleADVC"

Home.ImportResults.ImportMesh.ADVC(folderpath)
Home.AddResults.ADVC(strlPaths=[folderpath], bMergeTree=False, bADVCProcessNameRule=False, bDisplayNAResult=False)
```
