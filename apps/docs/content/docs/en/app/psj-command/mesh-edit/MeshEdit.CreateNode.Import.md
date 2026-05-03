---
title: "MeshEdit.CreateNode.Import()"
description: "Create node by importing CSV file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > CreateNode > Import"
macro_link: "[CreateNodeImport](../../macro/mesh-edit/CreateNodeImport)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create node by importing CSV file","Create node by importing CSV file"]}
   [param_rename_candidate] 'strFilePath' may be a rename of 'strCSVFilePath' (79% similar)
     context: {"from":"strCSVFilePath","to":"strFilePath","similarity":0.7857142857142857}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create node by importing CSV file.

## Syntax

```psj
MeshEdit.CreateNode.Import(...)
```

## Inputs

### `strFilePath` @type(String) @required @since(5.1.0)

- The path of CSV file.

### `strCSVFilePath` @type(String) @required @deprecated @until(5.1.0)

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
