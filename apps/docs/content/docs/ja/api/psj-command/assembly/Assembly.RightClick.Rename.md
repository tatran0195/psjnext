---
title: "Assembly.RightClick.Rename()"
description: "Rename a specified entity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > RightClick > Rename"
macro _link: "RenameItem"
---

## Description

Rename a specified entity.

## Syntax

```psj
Assembly.RightClick.Rename(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strNewName

- Specify the new name for item.
- The default value is "New name".

<!-- @since:5.0.1 @required -->
### crItem

- Specify the item which name will be changed.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

rename _status = Assembly.RightClick.Rename(strNewName="Box", 
                                           crItem=Part(1))

JPT.Debugger(rename _status)
```
