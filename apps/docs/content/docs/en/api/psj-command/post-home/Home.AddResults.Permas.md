---
title: "Home.AddResults.Permas()"
description: "Add permas result to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > Permas"
macro _link: "[AddResultsPermas](../../macro/home/AddResultsPermas)"
---

## Description

Add permas result to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.Permas(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The permas result files.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether or not the function is executed successfully or not:
  - True: The permas result is added to the document successfully.
  - False: The permas result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
mesh = "C:/Temp/mesh.dat"
result = "C:/Temp/result.post.gz"

# Import mesh file
Home.ImportResults.Permas(mesh)
# Add result to the mesh file.
Home.AddResults.Permas(strlPaths=[result], bMergeTree=False)
```
