---
title: "Home.AddResults.Nastran()"
description: "Add Nastran Op2 results to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > Nastran"
macro_link: "[AddResultsNastran](../../macro/home/AddResultsNastran)"
---

## Description

Add Nastran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
Home.AddResults.Nastran(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Nastran files (\*.op2 files) which will be used for importing.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

### `bCreateResultAtMidNode` @type(Boolean) @default(True)

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
