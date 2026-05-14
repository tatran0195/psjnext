---
title: "Connections.Contacts.MSCNastran.ManualGroup()"
description: "Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ManualGroup"
macro _link: "[ContactMSCNastran](../../macro/connections/ContactMSCNastran)"
---

## Description

Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.MSCNastran.ManualGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactMSCNastran _1" -->
### `strName`

- The name of the contact to be created.

<!-- @since:5.0.1 @type:NASTRAN _CONTACT @optional @default:NASTRAN _CONTACT -->
### `nastranContact`

- The Nastran contact parameters.

<!-- @since:5.0.1 @type:Cursor Pair List @required -->
### `crplTarget`

- The list or pair of master face group and slave face group.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:65280 -->
### `iColor`

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S", 
                        crlTargets=[Face(24)])

created _contact = Connections.Contacts.MSCNastran.ManualGroup(strName="ContactMSCNastran _1", 
                                                              nastranContact=NASTRAN _CONTACT(dRROR=0.0005), 
                                                              crplTarget=[CursorPair(Group(1), 
                                                                                     Group(2))], 
                                                              iColor=16711680)

JPT.Debugger(created _contact)
```
