---
title: "dlg.add _condition _selector()"
description: "Add \"Condition\" to the selection list, allowing user to select condition and store the condition to the selection list"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add "Condition" to the selection list, allowing user to select condition and store the condition to the selection list.

## Syntax

```psj
dlg.add _condition _selector(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### text

- Specify the title of selector.
- The default value is "Condition".

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Value",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _condition _selector(text="Condition 1")
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
