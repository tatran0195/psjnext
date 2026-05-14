---
title: "Home.AddResults.Universal()"
description: "Add result written in Universal file to the current Jupiter-Post Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > Universal"
macro _link: "[AddResultsUniversal](../../macro/home/AddResultsUniversal)"
---

## Description

Add result written in Universal file (\*.unv) to the current Jupiter-Post Database.

## Syntax

```psj
Home.AddResults.Universal(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The .unv file path.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifyingthe the function is executed successfully or not:
  - True: The Universal file (\*.unv file) is added successfully.
  - False: The Universal file (\*.unv file) cannot be added.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.unv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Universal(strlPaths=[Result], bMergeTree=False)
```
