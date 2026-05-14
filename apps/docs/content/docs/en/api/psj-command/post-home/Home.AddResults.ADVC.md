---
title: "Home.AddResults.ADVC()"
description: "Add ADVC results to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > ADVC"
macro _link: "[AddResultsADVC](../../macro/home/AddResultsADVC)"
---

## Description

Add ADVC results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.ADVC(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the ADVC files which will be used for importing.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bADVCProcessNameRule`

- Whether or not ADVC process IDs defined on the ADVC side are displayed.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplayNAResult`

- Whether or not the "NA Result Display" option in ADVC is enabled. When set to true, it shows "Data: ---" for missing data and "No data available" in watch data notes, applicable only to nodal output results. When set to false, standard data display rules apply.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strPathSelectResultFile`

- The specifying

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
