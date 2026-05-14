---
title: "JPT.RemoveAllContacts()"
description: "Remove all the existing contacts"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove all the existing contacts.

## Syntax

```psj
JPT.RemoveAllContacts()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {65}
# Prepare model
Geometry.Part.Cube(iPartColor=7011837)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=6351851)
Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0], strName="Cube _3", iPartColor=16543085)
Geometry.Part.Cube(dlOrigin=[0.04, 0.01, 0.0], strName="Cube _4", iPartColor=11948369)
Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.0], strName="Cube _5", iPartColor=12079955)
Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.01], strName="Cube _6", iPartColor=14837474)
Tools.Group.CreateGroup(strGroupName="Cube _5-G0001", crlTargets=[Face(130)])
Tools.Group.CreateGroup(strGroupName="Cube _6-G0002", crlTargets=[Face(155)])
Connections.Contacts.Abaqus.ContactTable(
    strName="C0001 _Cube _5-G0001 _Cube _6-G0002",
    iContactType=1,
    dAdjustWidth=DFLT _DBL,
    dExtensionZone=DFLT _DBL,
    dMaxPenetration=DFLT _DBL,
    dSmoothAngle=DFLT _DBL,
    iFrictionType=-1,
    dFrictionCoeff1=DFLT _DBL,
    dFrictionCoeff2=DFLT _DBL,
    dShearStressLimit=DFLT _DBL,
    dSlipTolerance=DFLT _DBL,
    dStaticFrictionCoeff=DFLT _DBL,
    dKineticFrictionCoeff=DFLT _DBL,
    dDecayCoeff=DFLT _DBL,
    bAdjustPosition=True,
    dPositionTolerance=DFLT _DBL,
    iFormulationType=-1,
    iPressureOverclosureType=-1,
    dContactStiffness=DFLT _DBL,
    tshPressureOverclosure=[0, 0],
    tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
    tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL],
    crplTargets=[CursorPair(Group(1), Group(2))],
    iContactColor=65280,
)
Tools.Group.CreateGroup(strGroupName="Cube _5-G0004", crlTargets=[Face(125)])
Tools.Group.CreateGroup(strGroupName="Cube _2-G0003", crlTargets=[Face(48)])
Connections.Contacts.Abaqus.ContactTable(
    strName="C0002 _Cube _5-G0004 _Cube _2-G0003",
    iContactType=1,
    dAdjustWidth=DFLT _DBL,
    dExtensionZone=DFLT _DBL,
    dMaxPenetration=DFLT _DBL,
    dSmoothAngle=DFLT _DBL,
    iFrictionType=-1,
    dFrictionCoeff1=DFLT _DBL,
    dFrictionCoeff2=DFLT _DBL,
    dShearStressLimit=DFLT _DBL,
    dSlipTolerance=DFLT _DBL,
    dStaticFrictionCoeff=DFLT _DBL,
    dKineticFrictionCoeff=DFLT _DBL,
    dDecayCoeff=DFLT _DBL,
    bAdjustPosition=True,
    dPositionTolerance=DFLT _DBL,
    iFormulationType=-1,
    iPressureOverclosureType=-1,
    dContactStiffness=DFLT _DBL,
    tshPressureOverclosure=[0, 0],
    tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
    tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL],
    crplTargets=[CursorPair(Group(3), Group(4))],
    iContactColor=65280,
)
# Remove all created contacts (Here is Abaqus's contact type)
JPT.RemoveAllContacts()
```
