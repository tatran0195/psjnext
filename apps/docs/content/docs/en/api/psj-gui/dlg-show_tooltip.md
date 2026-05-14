---
title: "dlg.show _tooltip()"
description: "Show tooltip when user hover the mouse to a UI component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show tooltip when user hovers the mouse to a UI component.

## Syntax

```psj
dlg.show _tooltip(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the UI component.

<!-- @since:5.0.1 @type:String @required -->
### `tip`

- The text appears when mouse hovers.

## Return Code

This function does not have output value.

## Sample Code

```psj {24-32}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _label(name="Label1",text="Label",layout="Window")
    dlg.add _textbox(name="TextBox2",layout="Window")
    dlg.add _richeditbox(name="RichEditBox3",text="RichEditBox",
        width=200,height=200,layout="Window")
    dlg.add _combobox(name="ComboBox4",layout="Window")
    dlg.add _checkbox(name="CheckBox5",text="CheckBox",layout="Window")
    dlg.add _radiobutton(name="RadioButton6",text="RadioButton",
        layout="Window")
    dlg.add _button(name="Button7",text="Button",width=60,height=22,
        layout="Window")
    dlg.add _spin(name="Spin8",layout="Window")
    dlg.add _slider(name="Slider9",width=100,height=30,min=0,max=100,pos=0,
        layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.show _tooltip(name="Label1",tip="Tooltip for Label1")
    dlg.show _tooltip(name="TextBox2",tip="Tooltip for TextBox2")
    dlg.show _tooltip(name="RichEditBox3",tip="Tooltip for RichEditBox3")
    dlg.show _tooltip(name="ComboBox4",tip="Tooltip for ComboBox4")
    dlg.show _tooltip(name="CheckBox5",tip="Tooltip for CheckBox5")
    dlg.show _tooltip(name="RadioButton6",tip="Tooltip for RadioButton6")
    dlg.show _tooltip(name="Button7",tip="Tooltip for Button7")
    dlg.show _tooltip(name="Spin8",tip="Tooltip for Spin8")
    dlg.show _tooltip(name="Slider9",tip="Tooltip for Slider9")

if __name__=='__main__':
    main()
```
