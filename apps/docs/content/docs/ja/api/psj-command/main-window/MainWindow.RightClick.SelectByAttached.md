---
title: "MainWindow.RightClick.SelectByAttached()"
description: "Select all attachments from the specified targets"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectByAttached"
macro _link: "[ViewSelectByAttached](../../macro/main-window/ViewSelectByAttached)"
---

## Description

Select all attachments from the specified targets

## Syntax

```psj
MainWindow.RightClick.SelectByAttached(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### iTargetType

- Specify the target type to be selected.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the targets to select the attached ones from them. The target can only be face or 2D element.

## Return Code

A _List of Cursor_ specifying the selected targets (faces or 2D elements).

## Sample Code

```psj {8}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
JPT.ViewFitToModel()

# Select on displaying faces  
attachFaces = MainWindow.RightClick.SelectByAttached(iTargetType=3, crlTargets=[Face(26)])
if attachFaces is None:
    print("There is no selected face")
elif len(attachFaces) == 1:
    print("One face was selected")
    print(attachFaces)
else:
    print(str(len(attachFaces)) + " faces were selected")
    print(attachFaces)
```
