---
title: "Tools.ModelInfo()"
description: "export model info file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > ModelInfo"
---

## Description

Export model info file

## Syntax

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```

## Inputs

### `strPath` @type(String) @required

- The path.

### `strPathName` @type(String) @default("")

- The path name.

### `listMeshPartInfoTool` @type(MESH\_PART\_INFO\_TOOL List) @default(\[])

- The mesh part info tool.

### `bPropertyAssignedPart` @type(Boolean) @default(False)

- The property assigned part.

### `bPropertyAssignedSummary` @type(Boolean) @default(False)

- The property assigned summary.

### `iModelNode` @type(Integer) @default(0)

- The model node.

### `iNmodelnodeWithprop` @type(Integer) @default(0)

- The nmodelnode withprop.

### `ilModelElement` @type(List\[Integer]) @default(\[])

- The model element.

### `ilNmodelelemWithprop` @type(List\[Integer]) @default(\[])

- The nmodelelem withprop.

### `ilModelLBC` @type(List\[Integer]) @default(\[])

- The model load boundary condition.

### `iModelContact` @type(Integer) @default(0)

- The model contact.

### `ilModelConnection` @type(List\[Integer]) @default(\[])

- The model connection.

### `ilModelProperty` @type(List\[Integer]) @default(\[])

- The model property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```
