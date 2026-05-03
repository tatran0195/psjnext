---
title: "Home.AddResults.Sysnoise()"
description: "Add sysnoise result to the current Jupiter Database"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > Sysnoise"
macro_link: "[AddResultsSysnoise](../../macro/home/AddResultsSysnoise)"
---

## Description

Add sysnoise result to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.Sysnoise(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- Sysnoise result files.

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The sysnoise result is added to the document successfully.
- False: The sysnoise result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Mesh = "C:/Temp/mesh.bdf"
Result = "C:/Temp/result"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(Mesh, bReadLoadAndConstraint=True, bReadConnection=True)
# Add result to the mesh file.
Home.AddResults.Sysnoise(strlPaths=[Result], bMergeTree=False)
```
