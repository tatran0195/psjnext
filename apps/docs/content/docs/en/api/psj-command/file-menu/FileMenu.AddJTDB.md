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

<!-- @since:5.0.1 @type:String @required -->
### `strFileName`

- The file name.

<!-- @since:5.0.1 @type:String @optional @default:"AUTO" -->
### `strMethod`

- The method.

<!-- @since:5.0.1 @type:String @optional @default:"IMPORTED" -->
### `strTargetModel`

- The target model.

<!-- @since:5.0.1 @type:String @optional @default:"OFFSET" -->
### `strOption`

- The option.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInputNode`

- The input node.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInputElem`

- The input element.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInputPart`

- The input part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInputMaterial`

- The input material.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInputProperty`

- The input property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```
