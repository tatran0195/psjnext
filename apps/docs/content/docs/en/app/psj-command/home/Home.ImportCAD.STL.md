---
title: "Home.ImportCAD.STL()"
description: "Import a Standard Tessellation Language file (*.stl) to the Jupiter Database"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportCAD > STL"
---

## Description

Import a Standard Tessellation Language file (\*.stl) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.STL(...)
```

## Inputs

### `strlPath` @type(List\[String])

- A list of the Standard Tessellation Language files (\*.stl files) which will be used for importing.
- This is the required input.

### `dScale` @type(Double) @default(0.001)

- The unit ratio imported from the file's unit into the document's unit.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Standard Tessellation Language file (\*.stl file) is imported successfully.
- False: The Standard Tessellation Language file (\*.stl file) cannot be imported.

## Sample Code

```psj {1,2,3}
imported_status = Home.ImportCAD.STL(strlPaths=[JPT.GetProgramPath() +
                                                "SampleData/CAD_Model/STL/Macbook Pro 15.stl"],
                                     dScale=0.001)
JPT.Debugger(imported_status)
```
