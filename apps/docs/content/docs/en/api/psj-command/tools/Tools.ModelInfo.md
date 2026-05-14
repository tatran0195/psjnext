---
title: "Tools.ModelInfo()"
description: "export model info file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > ModelInfo"
---

## Description

Export model info file

## Syntax

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strPath`

- The path.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strPathName`

- The path name.

<!-- @since:5.0.1 @type:MESH _PART _INFO _TOOL List @optional @default:[] -->
### `listMeshPartInfoTool`

- The mesh part info tool.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPropertyAssignedPart`

- The property assigned part.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPropertyAssignedSummary`

- The property assigned summary.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iModelNode`

- The model node.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNmodelnodeWithprop`

- The nmodelnode withprop.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilModelElement`

- The model element.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilNmodelelemWithprop`

- The nmodelelem withprop.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilModelLBC`

- The model load boundary condition.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iModelContact`

- The model contact.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilModelConnection`

- The model connection.

<!-- @since:5.0.1 @type:List[Integer] @optional @default:[] -->
### `ilModelProperty`

- The model property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```
