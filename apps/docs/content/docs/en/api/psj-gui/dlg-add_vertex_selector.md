---
title: "dlg.add _vertex _selector()"
description: "Add \"Vertex\" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add "Vertex" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list.

## Syntax

```psj
dlg.add _vertex _selector(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `text`

- The title of selector.

## Return Code

This function does not have output value.

## Sample Code

```psj {10}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _vertex _selector()
    dlg.generate _window()

if __name__=='__main__':
    main()
```
