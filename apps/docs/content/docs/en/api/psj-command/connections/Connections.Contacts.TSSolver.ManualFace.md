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

<!-- @since:5.0.1 @type:String @optional @default:"ContactTSSolver _1" -->
### `strName`

- The name of the contact to be created.

<!-- @since:5.0.1 @type:List[TSSOLVER _CONTACT] @optional @default:TSSOLVER _CONTACT -->
### `tssolverContact`

- The TSSolver contact parameters.

<!-- @since:5.0.1 @type:List[Cursor Pair] @required -->
### `crplTarget`

- The list or pair of master face group and slave face group.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing contact settings item.
  - If this parameter is used, the specified contact settings item will be modified.
  - If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:16711680 -->
### `iColor`

- The contact color.

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
