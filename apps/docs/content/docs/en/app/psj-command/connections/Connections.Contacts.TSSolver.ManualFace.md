---
title: "Connections.Contacts.TSSolver.ManualFace()"
description: "Define contact settings between specified faces for the TS solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > TSSolver > ManualFace"
---

## Description

Define contact settings between specified faces for the TS solver.

## Syntax

```psj
Connections.Contacts.TSSolver.ManualFace(...)
```

## Inputs

### `strName` @type(String) @default("ContactTSSolver\_1")

- The name of the contact to be created.

### `tssolverContact` @type(List\[TSSOLVER\_CONTACT]) @default(TSSOLVER\_CONTACT)

- The TSSolver contact parameters.

### `crplTarget` @type(List\[Cursor Pair]) @required

- The list or pair of master face group and slave face group.

### `crEdit` @type(Cursor) @default(None)

- An existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `iColor` @type(Integer) @default(16711680)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)

Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualFace(tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0, 
                                                                                            iIshellelemfaceMaster=0), 
                                                           crplTarget=[CursorPair(Group(1), 
                                                                                  Group(2))])

JPT.Debugger(created_contact)
```
