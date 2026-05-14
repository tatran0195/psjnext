---
title: "Home.AddResults.MappedMeshResult()"
description: "Add mapped mesh result to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > MappedMeshResult"
macro _link: "[AddResultsMappedMeshFile](../../macro/home/AddResultsMappedMeshFile)"
---

## Description

Add mapped mesh result to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.MappedMeshResult(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The mapped mesh files.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

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
