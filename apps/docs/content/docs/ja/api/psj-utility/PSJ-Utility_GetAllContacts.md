---
title: "JPT.GetAllContacts()"
description: "Get all the information of all existing contacts."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all existing contacts.

## Syntax

```psj
JPT.GetAllContacts()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[ContactVector](../data-type/psj-utility/pre-utility/built-in-types/DContactVector)_ object or _List of [DContact](../data-type/psj-utility/pre-utility/built-in-types/DContact)_ objects containing all the information of all the existing custom notes.

## Sample Code

```psj {35}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
JPT.ViewFitToModel()

Tools.Group.CreateGroup(strGroupName="Cube _2(49)-G0002", crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="Cube _1(24)-G0001", crlTargets=[Face(24)])

Connections.Contacts.TSSS.ContactTable(
    strName="C0001 _Cube _2-G0002 _Cube _1-G0001", 
    sunshineContact=SUNSHINE _CONTACT(
        iType=1, 
        dERROR=0.001, 
        dFRIC=DFLT _DBL, 
        dSLIDE=DFLT _DBL, 
        iICOORD=1, 
        dSFACT=DFLT _DBL, 
        dSFACTT=DFLT _DBL), 
    crplTarget=[CursorPair(Group(1), Group(2))], iColor=65280)
Tools.Group.CreateGroup(strGroupName="Cube _3(75)-G0004", crlTargets=[Face(75)])
Tools.Group.CreateGroup(strGroupName="Cube _2(50)-G0003", crlTargets=[Face(50)])
Connections.Contacts.TSSS.ContactTable(strName="C0002 _Cube _3-G0004 _Cube _2-G0003", 
    sunshineContact=SUNSHINE _CONTACT(
        dERROR=0.001, 
        dFRIC=DFLT _DBL, 
        dSLIDE=DFLT _DBL, 
        iICOORD=1, 
        dSFACT=DFLT _DBL, 
        dSFACTT=DFLT _DBL), 
    crplTarget=[CursorPair(Group(3), Group(4))], iColor=65280)

# Get the information of all existing contacts
listDContacts=JPT.GetAllContacts() 
JPT.Debugger(listDContacts)

# Print all the related information of each existing contact 
for contact in listDContacts:
    JPT.Debugger(contact)
```
