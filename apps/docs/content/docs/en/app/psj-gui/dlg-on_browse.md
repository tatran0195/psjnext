---
title: "dlg.on_browse()"
description: "Bind a created def function to a file/folder Browser component"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Bind a created function to a file/folder Browser component.

## Syntax

```psj
dlg.on_browse(...)
```

## Inputs

### `name` @type(String) @required

- The name of the file/folder Browser component using for binding a created def function.

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {15}
from pyjdg import *

def on_browse_clicked(dlg,path_list):
    print(path_list[0])

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_browser(name="Browser2",mode="file",file_filter="All Files(*.*)",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_browse(name="Browser2",callfunc=on_browse_clicked)

if __name__=='__main__':
    main()
```
