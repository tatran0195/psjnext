---
title: "FileMenu.AddJTDB()"
description: "add jtdb into model"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "FileMenu > AddJTDB"
---

## Description

Add jtdb into model

## Syntax

```psj
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strFileName

- Specify the file name.

<!-- @since:5.0.1 @optional -->
### strMethod

- Specify the method.
- The default value is "AUTO".

<!-- @since:5.0.1 @optional -->
### strTargetModel

- Specify the target model.
- The default value is "IMPORTED".

<!-- @since:5.0.1 @optional -->
### strOption

- Specify the option.
- The default value is "OFFSET".

<!-- @since:5.0.1 @optional -->
### iInputNode

- Specify the input node.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInputElem

- Specify the input element.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInputPart

- Specify the input part.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInputMaterial

- Specify the input material.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInputProperty

- Specify the input property.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```
