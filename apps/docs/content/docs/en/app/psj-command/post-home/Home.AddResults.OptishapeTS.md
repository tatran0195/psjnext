---
title: "Home.AddResults.OptishapeTS()"
description: "Add Optishape-TS results to the current Jupiter Database."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > AddResults > OptishapeTS"
macro_link: "[AddResultsOptishapeTS](../../macro/home/AddResultsOptishapeTS)"
---

## Description

Add Optishape-TS results to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.OptishapeTS(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Optishape-TS files (\*.op2 files)

### `bMergeTree` @type(Boolean) @default(True)

- Whether or not the differences not included in the existing document will be added.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Optishape-TS result is added to the document successfully.
  - False: The Optishape-TS result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
Result1 = "C:/Temp/topo.op2"
Result2 = "C:/Temp/topo_result.op2"

Home.ImportResults.OptishapeTS(strlPaths=[Result1])
Home.AddResults.OptishapeTS(strlPaths=[Result2])
```
