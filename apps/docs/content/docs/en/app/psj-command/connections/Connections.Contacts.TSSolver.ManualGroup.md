---
title: "Connections.Contacts.TSSolver.ManualGroup()"
description: "Define contact settings between specified groups for TS SunShine solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > TSSolver > ManualGroup"
---

## Description

Define contact settings between specified groups for TS SunShine solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.TSSolver.ManualGroup(...)
```

## Inputs

### `strName` @type(String) @default("ContactTSSolver\_1")

- The name of the contact to be created.

### `tssolverContact` @type(list of TSSOLVER\_CONTACT) @default(\[])

- The TSSolver contact parameters.

### `crplTarget` @type(List\[Cursor Pair]) @required

- The list or pair of master face group and slave face group.

### `crEdit` @type(Cursor) @default(None)

- An existing contact settings item:
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `iColor` @type(Integer) @default(16711680)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_2", 
                                                            tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0, 
                                                                                             iIshellelemfaceMaster=0), 
                                                            crplTarget=[CursorPair(Group(1), 
                                                                                   Group(2))], 
                                                            iMethod=1)

JPT.Debugger(created_contact)
```
