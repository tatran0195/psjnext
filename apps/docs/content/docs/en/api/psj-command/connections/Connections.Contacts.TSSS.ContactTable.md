---
title: "Connections.Contacts.TSSS.ContactTable()"
description: "Create contacts for TS Sunshine solver by using table"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > TSSS > ContactTable"
---

## Description

Create contacts for TS Sunshine solver by using table.

## Syntax

```psj
Connections.Contacts.TSSS.ContactTable(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactTS _SS _1" -->
### `strName`

- The contact name.

<!-- @since:5.0.1 @type:SUNSHINE _CONTACT @optional @default:SUNSHINE _CONTACT -->
### `nastranContact`

- The Sunshine contact parameters.

<!-- @since:5.0.1 @type:List[Cursor Pair] @optional @default:[] -->
### `crplTarget`

- The list or pair of group master face and group slave face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {17,18,19,20,21,22,23,24,25,26,27,28,29,30,37,38,39,40,41,42,43,44,45,46,47,48,49,50,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,117,118,119,120,121,122,123,124,125,126,127,128,129,130}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube _3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube _4", 
                   iPartColor=6053060)

Tools.Group.CreateGroup(strGroupName="Cube _3(73)-G0002", 
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Cube _1(22)-G0001", 
                        crlTargets=[Face(22)])

created _contact _1 = Connections.Contacts.TSSS.ContactTable(strName="C0001 _Cube _3-G0002 _Cube _1-G0001", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(1), 
                                                                                  Group(2))], 
                                                           iColor=65280)

Tools.Group.CreateGroup(strGroupName="Cube _4(99)-G0004", 
                        crlTargets=[Face(99)])
Tools.Group.CreateGroup(strGroupName="Cube _2(48)-G0003", 
                        crlTargets=[Face(48)])

created _contact _2 = Connections.Contacts.TSSS.ContactTable(strName="C0002 _Cube _4-G0004 _Cube _2-G0003", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(3), 
                                                                                  Group(4))], 
                                                           iColor=65280)

Tools.Group.CreateGroup(strGroupName="Cube _2(49)-G0006", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="Cube _1(24)-G0005", 
                        crlTargets=[Face(24)])

created _contact _3 = Connections.Contacts.TSSS.ContactTable(strName="C0003 _Cube _2-G0006 _Cube _1-G0005", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT,
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(5), 
                                                                                  Group(6))], 
                                                           iColor=65280)

Tools.Group.CreateGroup(strGroupName="Cube _3(76)-G0007", 
                        crlTargets=[Face(76)])
Tools.Group.CreateGroup(strGroupName="Cube _4(101)-G0008", 
                        crlTargets=[Face(101)])

created _contact _4 = Connections.Contacts.TSSS.ContactTable(strName="C0004 _Cube _3-G0007 _Cube _4-G0008", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(7), 
                                                                                  Group(8))], 
                                                           iColor=65280)

Tools.Group.CreateGroup(strGroupName="Cube _4(99)-G0010", 
                        crlTargets=[Face(99, 101)])
Tools.Group.CreateGroup(strGroupName="Cube _1(22)-G0009", 
                        crlTargets=[Face(22, 24)])

created _contact _5 = Connections.Contacts.TSSS.ContactTable(strName="C0005 _Cube _4-G0010 _Cube _1-G0009", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(9), 
                                                                                  Group(10))], 
                                                           iColor=65280)

Tools.Group.CreateGroup(strGroupName="Cube _3(73)-G0012", 
                        crlTargets=[Face(73, 76)])
Tools.Group.CreateGroup(strGroupName="Cube _2(48)-G0011", 
                        crlTargets=[Face(48, 49)])

created _contact _6 = Connections.Contacts.TSSS.ContactTable(strName="C0006 _Cube _3-G0012 _Cube _2-G0011", 
                                                           sunshineContact=SUNSHINE _CONTACT(iType=1, 
                                                                                            dERROR=0.001, 
                                                                                            dFRIC=DFLT _DBL, 
                                                                                            dSLIDE=DFLT _DBL, 
                                                                                            iICOORD=DFLT _INT, 
                                                                                            dSFACT=DFLT _DBL, 
                                                                                            dSFACTT=0.5, 
                                                                                            dCDAMP=DFLT _DBL, 
                                                                                            iIshellelemfaceSlave=1, 
                                                                                            iIshellelemfaceMaster=1), 
                                                           crplTarget=[CursorPair(Group(11), 
                                                                                  Group(12))], 
                                                           iColor=65280)

JPT.Debugger(created _contact _1)
JPT.Debugger(created _contact _2)
JPT.Debugger(created _contact _3)
JPT.Debugger(created _contact _4)
JPT.Debugger(created _contact _5)
JPT.Debugger(created _contact _6)
```
