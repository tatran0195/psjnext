---
title: "Connections.Contacts.TSSolver.ManualFace()"
description: "Define contact settings between specified faces for the TS solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > TSSolver > ManualFace"
---

## Description

Define contact settings between specified faces for the TS solver.

## Syntax

```psj
Connections.Contacts.TSSolver.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the contact to be created.
- The default value is "ContactTSSolver\_1".

<!-- @since:5.0.1 @optional -->
### tssolverContact

- Specify the TSSolver contact parameters.
- The default value is _[TSSOLVER\_CONTACT](./../../data-type/psj-command/parameter-types/TSSOLVER _CONTACT)_.

<!-- @since:5.0.1 @required -->
### crplTarget

- Specify the list or pair of master face group and slave face group.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the contact color.
- The default value is 16711680.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)

Tools.Group.CreateGroup(strGroupName="ContactTSSolver _1_Manual _Face _M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactTSSolver _1_Manual _Face _S", 
                        crlTargets=[Face(24)])

created _contact = Connections.Contacts.TSSolver.ManualFace(tssolverContact=TSSOLVER _CONTACT(iIshellelemfaceSlave=0, 
                                                                                            iIshellelemfaceMaster=0), 
                                                           crplTarget=[CursorPair(Group(1), 
                                                                                  Group(2))])

JPT.Debugger(created _contact)
```
