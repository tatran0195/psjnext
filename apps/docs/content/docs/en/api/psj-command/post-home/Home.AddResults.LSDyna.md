---
title: "Home.AddResults.LSDyna()"
description: "Add LS-Dyna's d3plot results to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > LSDyna"
macro _link: "[AddResultsLSDyna](../../macro/home/AddResultsLSDyna)"
---

## Description

Add LS-Dyna's d3plot results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.LSDyna(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The specifying a list of the d3plot files which will be used for importing.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The LS-Dyna result is added to the document successfully.
  - False: The LS-Dyna result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/d3plot"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.LSDyna(strlPaths=[Result], bMergeTree=False)
```
