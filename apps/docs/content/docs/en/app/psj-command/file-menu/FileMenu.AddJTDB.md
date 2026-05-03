---
title: "FileMenu.AddJTDB()"
description: "add jtdb into model"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "FileMenu > AddJTDB"
---

## Description

Add jtdb into model

## Syntax

```psj
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```

## Inputs

### `strFileName` @type(String) @required

- The file name.

### `strMethod` @type(String) @default("AUTO")

- The method.

### `strTargetModel` @type(String) @default("IMPORTED")

- The target model.

### `strOption` @type(String) @default("OFFSET")

- The option.

### `iInputNode` @type(Integer) @default(0)

- The input node.

### `iInputElem` @type(Integer) @default(0)

- The input element.

### `iInputPart` @type(Integer) @default(0)

- The input part.

### `iInputMaterial` @type(Integer) @default(0)

- The input material.

### `iInputProperty` @type(Integer) @default(0)

- The input property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```
