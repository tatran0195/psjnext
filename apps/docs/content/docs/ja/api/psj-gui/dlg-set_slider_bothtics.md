---
title: "dlg.set _slider _bothtics()"
description: "Show tick marks on both/one side of the SliderBar"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show tick marks on both/one side of the SliderBar.

## Syntax

```psj
dlg.set _slider _bothtics(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the SliderBar.

<!-- @since:5.0.1 @required -->
### enabled

- Specify the way to display tick mark:
  - _True_: show tick mark on both side of the SliderBar.
  - _False_: show tick mark only on one side of the SliderBar.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _slider(name="Slider3",width=200,height=100,min=0,max=100,pos=0,layout="Layout1")
    dlg.set _slider _bothtics(name="Slider3",enabled=True)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
