---
title: "Home.ImportCAD.STL()"
description: "Import a Standard Tessellation Language file (*.stl) to the Jupiter Database"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportCAD > STL"
---

## Description

Import a Standard Tessellation Language file (\*.stl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.STL(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strlPath

- Specify a list of the Standard Tessellation Language files (\*.stl files) which will be used for importing.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the unit ratio imported from the file's unit into the document's unit.
- The default value is 0.001.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Standard Tessellation Language file (\*.stl file) is imported successfully.
- False: The Standard Tessellation Language file (\*.stl file) cannot be imported.

## Sample Code

```psj {1,2,3}
imported _status = Home.ImportCAD.STL(strlPaths=[JPT.GetProgramPath() +
                                                "SampleData/CAD _Model/STL/Macbook Pro 15.stl"],
                                     dScale=0.001)
JPT.Debugger(imported _status)
```
