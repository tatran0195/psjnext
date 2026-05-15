---
title: "dlg.set _slider _vertical()"
description: "Show the SliderBar in the vertical or horizontal direction"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show the SliderBar in the vertical or horizontal direction.

## Syntax

```psj
dlg.set _slider _vertical(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the SliderBar.

<!-- @since:5.0.1 @required -->
### enabled

- Specify the direction of the SliderBar:
  - _True_: creating SliderBar will be put in the vertical direction.
  - _False_: creating SliderBar will be put in the horizontal direction.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _slider(name="Slider3",width=100,height=100,min=0,max=100,pos=0,layout="Layout1")
    dlg.set _slider _vertical(name="Slider3",enabled=True)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
