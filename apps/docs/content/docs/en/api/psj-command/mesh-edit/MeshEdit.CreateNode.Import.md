---
title: "MeshEdit.CreateNode.Import()"
description: "Create node by importing CSV file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Import"
macro _link: "[CreateNodeImport](../../macro/mesh-edit/CreateNodeImport)"
---

## Description

Create node by importing CSV file.

## Syntax

```psj
MeshEdit.CreateNode.Import(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strFilePath`

- The path of CSV file.

<!-- @since:5.0.1 @type:String @removed:5.1.0 @required @deprecated -->
### `strCSVFilePath`

- The CSV file path.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Put your sample CSV file
csvFile = "C:/temp/NodeData.csv"

# Import nodes
newNode = MeshEdit.CreateNode.Import(strFilePath = csvFile)
JPT.Debugger(newNode) # for checking the return value
```
