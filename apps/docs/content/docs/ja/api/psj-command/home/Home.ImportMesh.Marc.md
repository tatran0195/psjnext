---
title: "Home.ImportMesh.Marc()"
description: "Import a Marc file (*.t16, *.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportMesh > Marc"
macro _link: "[ImportMarcMesh](../../macro/home/ImportMarcMesh)"
---

## Description

Import a Marc file (\*.t16, \*.t19) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
Home.ImportMesh.Marc(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify the Marc file (\*.t16, \*.t19 files) which will be used for importing.

## Return Code

A _Boolean_ specifying

## Sample Code

```pj {4}
#Prepare your data
marc _file _path="C:/Temp/sample.t16"

import _status = Home.ImportMesh.Marc(strPath=marc _file _path)
JPT.Debugger(import _status)
```
