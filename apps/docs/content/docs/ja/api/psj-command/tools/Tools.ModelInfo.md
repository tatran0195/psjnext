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

<!-- @since:5.0.1 @required -->
### strPath

- Specify the path.

<!-- @since:5.0.1 @optional -->
### strPathName

- Specify the path name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### listMeshPartInfoTool

- Specify the mesh part info tool.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bPropertyAssignedPart

- Specify the property assigned part.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bPropertyAssignedSummary

- Specify the property assigned summary.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iModelNode

- Specify the model node.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iNmodelnodeWithprop

- Specify the nmodelnode withprop.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilModelElement

- Specify the model element.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilNmodelelemWithprop

- Specify the nmodelelem withprop.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilModelLBC

- Specify the model load boundary condition.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iModelContact

- Specify the model contact.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### ilModelConnection

- Specify the model connection.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### ilModelProperty

- Specify the model property.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[])
```
