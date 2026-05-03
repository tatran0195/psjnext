---
title: "dlg.add_richeditbox()"
description: "Add a rich edit box to the dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a rich edit box to the dialog.

## Syntax

```psj
dlg.add_richeditbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `text` @type(String) @default("")

- Text displayed by default.

### `width` @type(Integer) @default(60)

- The width of the rich edit box.

### `height` @type(Integer) @default(22)

- The height of the rich edit box.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_richeditbox(name="RichEditBox17",text="RichEditBox content",
        width=200,height=200,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
