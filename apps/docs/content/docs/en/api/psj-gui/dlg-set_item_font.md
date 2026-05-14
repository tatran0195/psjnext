---
title: "dlg.set _item _font()"
description: "Set font properties to the text inside the component"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set font properties to the text inside the component.

## Syntax

```psj
dlg.set _item _font(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the component which you want to set the font properties.

<!-- @since:5.1.0 @type:Class @required -->
### `font`

- The of[PSJFont](../data-type/psj-gui/PSJFont) specifying font properties.

## Return Code

This function does not have output value.

## Sample Code

```psj {19}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _textbox(name="TextBox2",layout="Window", width=350, 
        height=35, text _color=255)
    font _TextBox2=PSJFont()
    font _TextBox2.size=18
    font _TextBox2.bold=True
    font _TextBox2.italic=True
    font _TextBox2.underline=True
    font _TextBox2.strikeout=False
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _item _font(name="TextBox2",font=font _TextBox2)
    dlg.set _item _text(name="TextBox2", text="This is a sample text")
if __name__=='__main__':
    main()
```
