---
title: "Home.AddResults.Abaqus()"
description: "Add Abaqus .odb results to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > Abaqus"
macro_link: "[AddResultsAbaqus](../../macro/home/AddResultsAbaqus)"
---

## Description

Add Abaqus .odb results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.Abaqus(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Abaqus files (\*.odb files) which will be used for importing.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

### `iVersion` @type(Integer) @default(2019)

- Version of Abaqus file.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Abaqus result is added to the document successfully.
  - False: The Abaqus result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.inp"
Result = "C:/Temp/result.odb"

# Import mesh file
Home.ImportResults.ImportMesh.Abaqus(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Abaqus(strlPaths=[Result], bMergeTree=False)
```
