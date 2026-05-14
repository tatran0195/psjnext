---
title: "Home.ImportCAD.VRML()"
description: "Import a Virtual Reality Modeling Language file (*.wrl) to the Jupiter Database"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportCAD > VRML"
---

## Description

Import a Virtual Reality Modeling Language file (\*.wrl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.VRML(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlPaths`

- A list of the Virtual Reality Modeling Language files (\*.wrl files) which will be used for importing.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iVRMLColorGroups`

- The option that using color information:
  - 0: Do not use
  - 1: Use color information

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dScale`

- The unit ratio imported from the file's unit into the document's unit.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Virtual Reality Modeling Language file (\*.wrl file) is imported successfully.
- False: The Virtual Reality Modeling Language file (\*.wrl file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported _status = Home.ImportCAD.VRML(strlPaths=[JPT.GetProgramPath() +
                                                 "SampleData/CAD _Model/WRML/GrabCAD 2-SHIP.wrl"],
                                      iVRMLColorGroups=1,
                                      dScale=0.001)
JPT.Debugger(imported _status)
```
