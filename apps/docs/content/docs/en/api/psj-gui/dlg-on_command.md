---
title: "dlg.on _command()"
description: "Bind a created def function to a component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Bind a created function to a component.

## Syntax

```psj
dlg.on _command(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the component using for binding a created def function.

<!-- @since:5.0.1 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {18}
from pyjdg import *

def onApplyButtonClicked(dlg):
    Geometry.Part.Cube()
    print("--- Cube created! ---")

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[80,0,50,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Click on Apply button!",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="ButtonApply",callfunc=onApplyButtonClicked)

if __name__=='__main__':
    main()
```
