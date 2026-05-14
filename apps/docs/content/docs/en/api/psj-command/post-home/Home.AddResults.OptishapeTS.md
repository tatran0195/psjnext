---
title: "Home.AddResults.OptishapeTS()"
description: "Add Optishape-TS results to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > OptishapeTS"
macro _link: "[AddResultsOptishapeTS](../../macro/home/AddResultsOptishapeTS)"
---

## Description

Add Optishape-TS results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.OptishapeTS(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the Optishape-TS files (\*.op2 files)

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMergeTree`

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Optishape-TS result is added to the document successfully.
  - False: The Optishape-TS result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Result1 = "C:/Temp/topo.op2"
Result2 = "C:/Temp/topo _result.op2"

Home.ImportResults.OptishapeTS(strlPaths=[Result1])
Home.AddResults.OptishapeTS(strlPaths=[Result2])
```
