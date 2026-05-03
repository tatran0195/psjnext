---
title: "Properties.Section.Delete()"
description: "Delete the create property sections in 1D properties section library"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section > Delete"
---

## Description

Delete the create property sections in 1D properties section library.

## Syntax

```psj
Properties.Section.Delete(...)
```

## Inputs

### `crlSections` @type(List\[Cursor]) @required

- The list of property sections will be deleted.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {5}
Properties.Section.AddGeneral(strName="abc", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.02)

creating_status = Properties.Section.Delete(crlSections=[SectionGeneral(1)])

JPT.Debugger(creating_status)
```
