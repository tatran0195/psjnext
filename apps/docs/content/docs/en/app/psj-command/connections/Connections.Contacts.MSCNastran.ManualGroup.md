---
title: "Connections.Contacts.MSCNastran.ManualGroup()"
description: "Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ManualGroup"
macro_link: "[ContactMSCNastran](../../macro/connections/ContactMSCNastran)"
---

## Description

Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.MSCNastran.ManualGroup(...)
```

## Inputs

### `strName` @type(String) @default("ContactMSCNastran\_1")

- The name of the contact to be created.

### `nastranContact` @type(NASTRAN\_CONTACT) @default(NASTRAN\_CONTACT)

- The Nastran contact parameters.

### `crplTarget` @type(Cursor Pair List) @required

- The list or pair of master face group and slave face group.

### `crEdit` @type(Cursor) @default(None)

- An existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `iColor` @type(Integer) @default(65280)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.MSCNastran.ManualGroup(strName="ContactMSCNastran_1", 
                                                              nastranContact=NASTRAN_CONTACT(dRROR=0.0005), 
                                                              crplTarget=[CursorPair(Group(1), 
                                                                                     Group(2))], 
                                                              iColor=16711680)

JPT.Debugger(created_contact)
```
