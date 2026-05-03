---
title: "Home.AddResults.Actran()"
description: "Add Actran Op2 results to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > Actran"
macro_link: "[AddResultsActran](../../macro/home/AddResultsActran)"
---

## Description

Add Actran Op2 results to the current Jupiter Database. The Jupiter document should be Post document.

## Syntax

```psj
Home.AddResults.Actran(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Actran files (\*.op2 files) which will be used for importing.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Actran result is added to the document successfully.
  - False: The Actran result is not added to the document.

## Sample Code

```psj {6}
# Please put mesh and actran file below path
meshfile='C:/Sample/mesh.bdf'
actrandatafile= 'C:/Sample/actran.op2'

Home.ImportResults.ImportMesh.Nastran(meshfile, bReadLoadAndConstraint=True, bReadConnection=True)
Home.AddResults.Actran(strlPaths=[actrandatafile], bMergeTree=False)
```
