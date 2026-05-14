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

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The BEM file (.bdf).

<!-- @since:5.1.0 @type:String @required -->
### `strFPMFilePath`

- The FPM file (.bdf).

<!-- @since:5.1.0 @type:String @required -->
### `strResultFolderPath`

- The result folder.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. For WAON file, it is always set to 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

### `bReadLoadAndConstraint`

-A _Boolean_ specifying whether or not



### `bReadConnection`

-A _Boolean_ specifying whether or not



### `bCreateResultsAtMidNode`

-A _Boolean_ specifying whether or not



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
