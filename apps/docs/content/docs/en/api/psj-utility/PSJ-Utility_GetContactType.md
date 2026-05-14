---
title: "JPT.GetContactType()"
description: "Get Abaqus contact type after inputting contact ID"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get Abaqus contact type after inputting contact ID.

## Syntax

```psj
JPT.GetContactType(contactID)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `contactID`

- The Abaqus contact ID.

## Return Code

- **-1**: Inputted _contactID_ does not exist on the model.
- **0**: Inputted _contactID_ is a _General_ contact type.
- **1**: Inputted _contactID_ is a _Tied_ contact type.
- **2**: Inputted _contactID_ is a _All with self_ contact type.

## Sample Code

```psj {3}
# Make a function to return detail description of contact type
def contact _case(iContactID: int) -> int:
    iContactType = JPT.GetContactType(iContactID)
    switch = {-1: "Error - Inputted contact ID {} does not exist on the model".format(iContactID),
              0: "Inputted contact ID {} - Type = General Contact".format(iContactID),
              1: "Inputted contact ID {} - Type = Tied Contact".format(iContactID),
              2: "Inputted contact ID {} - Type = All with self Contact".format(iContactID)}
    return switch.get(iContactType)

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _3", iPartColor=13259210)
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _2_Manual _Face _M", crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _2_Manual _Face _S", crlTargets=[Face(76)])
Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus _2", dAdjustWidth=DFLT _DBL, dExtensionZone=DFLT _DBL,
    dMaxPenetration=DFLT _DBL, dSmoothAngle=DFLT _DBL, iFrictionType=-1, dFrictionCoeff1=DFLT _DBL,
    dFrictionCoeff2=DFLT _DBL, dShearStressLimit=DFLT _DBL, dSlipTolerance=DFLT _DBL, dStaticFrictionCoeff=DFLT _DBL,
    dKineticFrictionCoeff=DFLT _DBL, dDecayCoeff=DFLT _DBL, bAdjustPosition=True, dPositionTolerance=DFLT _DBL,
    iFormulationType=-1, iPressureOverclosureType=-1, dContactStiffness=DFLT _DBL, tshPressureOverclosure=[0, 0],
    iThermalConductanceDef=-1, tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
    tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL], crplTargets=[CursorPair(Group(1), Group(2))],
    iContactColor=16711680)
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _3_Manual _Face _M", crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _3_Manual _Face _S", crlTargets=[Face(75)])
Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus _3", iContactType=1, dAdjustWidth=DFLT _DBL,
    dExtensionZone=DFLT _DBL, dMaxPenetration=DFLT _DBL, dSmoothAngle=DFLT _DBL, iFrictionType=-1,
    dFrictionCoeff1=DFLT _DBL, dFrictionCoeff2=DFLT _DBL, dShearStressLimit=DFLT _DBL, dSlipTolerance=DFLT _DBL,
    dStaticFrictionCoeff=DFLT _DBL, dKineticFrictionCoeff=DFLT _DBL, dDecayCoeff=DFLT _DBL, bAdjustPosition=True,
    dPositionTolerance=DFLT _DBL, iFormulationType=-1, iPressureOverclosureType=-1, dContactStiffness=DFLT _DBL,
    tshPressureOverclosure=[0, 0], iThermalConductanceDef=-1, tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
    tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL], crplTargets=[CursorPair(Group(3), Group(4))],
    iContactColor=16711680)

# Output of the JPT.GetContactType utilities
JPT.Debugger(contact _case(2))
```
