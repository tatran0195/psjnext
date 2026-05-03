---
title: "Home.AddResults.MappedMeshResult()"
description: "Add mapped mesh result to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > MappedMeshResult"
macro_link: "[AddResultsMappedMeshFile](../../macro/home/AddResultsMappedMeshFile)"
---

## Description

Add mapped mesh result to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.MappedMeshResult(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- Mapped mesh files.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The mapped mesh result is added to the document successfully.
  - False: The mapped mesh result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.dat"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.MappedMeshResult(strlPaths=[Result], bMergeTree=False)
```
