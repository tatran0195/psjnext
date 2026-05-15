---
title: "Home.AddResults.Abaqus()"
description: "Add Abaqus .odb results to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > Abaqus"
macro _link: "[AddResultsAbaqus](../../macro/home/AddResultsAbaqus)"
---

## Description

Add Abaqus .odb results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.Abaqus(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strlPaths

- Specify a list of the Abaqus files (\*.odb files) which will be used for importing.

<!-- @since:5.1.0 @optional -->
### bMergeTree

- Specify whether or not the differences not included in the existing document will be added.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### iVersion

- Specify version of Abaqus file.
- The default value is 2019.

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
