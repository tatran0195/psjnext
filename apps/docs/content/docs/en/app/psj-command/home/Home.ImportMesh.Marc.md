---
title: "Home.ImportMesh.Marc()"
description: "Import a Marc file (*.t16, *.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportMesh > Marc"
macro_link: "[ImportMarcMesh](../../macro/home/ImportMarcMesh)"
---

## Description

Import a Marc file (\*.t16, \*.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
Home.ImportMesh.Marc(...)
```

## Inputs

### `strPath` @type(String) @required

- The Marc file (\*.t16, \*.t19 files) which will be used for importing.

## Return Code

A _Boolean_ specifying

## Sample Code

```psj{4}
#Prepare your data
marc_file_path="C:/Temp/sample.t16"

import_status = Home.ImportMesh.Marc(strPath=marc_file_path)
JPT.Debugger(import_status)
```
