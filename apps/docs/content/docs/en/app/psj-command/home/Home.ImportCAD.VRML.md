---
title: "Home.ImportCAD.VRML()"
description: "Import a Virtual Reality Modeling Language file (*.wrl) to the Jupiter Database"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportCAD > VRML"
---

## Description

Import a Virtual Reality Modeling Language file (\*.wrl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.VRML(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Virtual Reality Modeling Language files (\*.wrl files) which will be used for importing.

### `iVRMLColorGroups` @type(Integer) @default(0)

- The option that using color information:
  - 0: Do not use
  - 1: Use color information

### `dScale` @type(Double) @default(1.0)

- The unit ratio imported from the file's unit into the document's unit.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Virtual Reality Modeling Language file (\*.wrl file) is imported successfully.
- False: The Virtual Reality Modeling Language file (\*.wrl file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported_status = Home.ImportCAD.VRML(strlPaths=[JPT.GetProgramPath() +
                                                 "SampleData/CAD_Model/WRML/GrabCAD 2-SHIP.wrl"],
                                      iVRMLColorGroups=1,
                                      dScale=0.001)
JPT.Debugger(imported_status)
```
