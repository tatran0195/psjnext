---
title: "Home.ImportResults.WAON()"
description: "Import WAON result file to the Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > WAON"
macro _link: "[CmdImportTSVWAONPost](../../macro/home/CmdImportTSVWAONPost)"
---

## Description

Import WAON result file to the Jupiter Database.

## Syntax

```psj
Home.ImportResults.WAON(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify BEM file (.bdf).

<!-- @since:5.1.0 @required -->
### strFPMFilePath

- Specify FPM file (.bdf).

<!-- @since:5.1.0 @required -->
### strResultFolderPath

- Specify result folder.

<!-- @since:5.1.0 @optional -->
### iImportType

- Specify import type. For WAON file, it is always set to 1.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0 (degree).

<!-- @since:5.1.0 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0 (degree).

### `bReadLoadAndConstraint`

-A _Boolean_ specifying whether or not

- The default value is _False_.

### `bReadConnection`

-A _Boolean_ specifying whether or not

- The default value is _False_.

### `bCreateResultsAtMidNode`

-A _Boolean_ specifying whether or not

- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The WAON result is imported successfully.
- False: The WAON result cannot be imported.

## Sample Code

```psj {6-11}
#Please set path to your sample WAON file.
filepath="C:/Temp/"
bem _file = filepath + "BEM.bdf"
fpm _file = filepath + "FPM.bdf"
result = base _FILEPATH + "result/"
Home.ImportResults.WAON(bem _file, 
                        fpm _file, 
                        result, 
                        bReadLoadAndConstraint=True, 
                        bReadConnection=True, 
                        bCreateResultsAtMidNode=True)
```
