---
title: "Home.AddResults.UsersResult()"
description: "Add user result to the current Jupiter Database."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > AddResults > UsersResult"
macro _link: "[AddUserResultDefine](../../macro/home/AddUserResultDefine)"
---

## Description

Add user result to the current Jupiter Database.

## Syntax

```psj
Home.AddResults.UsersResult(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strlPath

- Specify user result files.

### `bExportLog`

-A _Boolean_ specifying whether or not

- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether or not the function is executed successfully or not:
  - True: The user result is added to the document successfully.
  - False: The user result is not added to the document.

## Sample Code

```psj {8}
# Put your sample files
mesh = "C:/Temp/mesh.bdf"
result = "C:/Temp/result.csv"

# Import mesh file
Home.ImportResults.ImportMesh.Nastran(mesh)
# Add result to the mesh file.
Home.AddResults.UsersResult(strlPath=result)
```
