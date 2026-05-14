---
title: "Home.AddResults.Nastran()"
description: "Add Nastran Op2 results to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > Nastran"
macro _link: "[AddResultsNastran](../../macro/home/AddResultsNastran)"
---

## Description

Add Nastran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
Home.AddResults.Nastran(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the Nastran files (\*.op2 files) which will be used for importing.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bCreateResultAtMidNode`

- Whether or not create result at Mid Nodes.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran result is added to the document successfully.
  - False: The Nastran result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result.op2"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Nastran(strlPaths=[Result], bMergeTree=False)
```
