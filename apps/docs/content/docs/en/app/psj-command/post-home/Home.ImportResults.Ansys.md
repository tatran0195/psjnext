---
title: "Home.ImportResults.Ansys()"
description: "Import Ansys result file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportResults > Ansys"
macro_link: "[ImportAnsysResult](../../macro/home/ImportAnsysResult)"
---

## Description

Import Ansys result file.

## Syntax

```psj
Home.ImportResults.Ansys(...)
```

## Inputs

### `strPath` @type(String) @required

- Ansys result file path.

### `iImportType` @type(Integer) @default(1)

- Import type.

### `dFaceAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0 (degree))

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Abaqus file (\*.rst file) is imported successfully.
  - False: The Abaqus file (\*.rst file) cannot be imported.

## Sample Code

```psj {4}
#Please set path to your sample Abaqus file.
filepath="C:/Temp/Sample.rst"

Home.ImportResults.Ansys(filepath)
```
