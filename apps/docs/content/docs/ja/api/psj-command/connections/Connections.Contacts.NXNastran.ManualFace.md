---
title: "Connections.Contacts.NXNastran.ManualFace()"
description: "Define contact settings between specified faces for the NX Nastran solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NX Nastran > Manual Face"
---

## Description

Define contact settings between specified faces for the NX Nastran solver.

## Syntax

```psj
Connections.Contacts.NXNastran.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaceMasters

- Specify the faces to be the master faces.

<!-- @since:5.0.1 @required -->
### crlFaceSlaves

- Specify the faces to be the slave faces.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactNXNastran\_1".

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of contact definition.
  - If _iContactType=0_, sliding contact.
  - If _iContactType=1_, tied contact.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactAlgorithm

- Specify the type of contact connection.
  - If _iContactAlgorithm=0_, contact between shell or solid element faces and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dNormalPenaltyFactor

- Specify the penalty factor for the normal direction. This argument is to be used if _iContactType=0_.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dTangentialPenaltyFactor

- Specify the penalty factor for the tangential direction. This argument is to be used if _iContactType=0_.
- The default value is 1.

### `dForceConvergenceTol`

- A _Double_ designating the Contact Force convergence tolerance. This argument is to be used if _iContactType=0_.
- The default value is 0.01.

### `dMaxForceIteration`

- A _Double_ designating the maximum number of iterations for a force (inner) loop. This argument is to be used if _iContactType=0_.
- The default value is 10.

### `dMaxStatusIteration`

- A _Double_ designating the maximum number of iterations for a status (outer) loop. This argument is to be used if _iContactType=0_.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### dNumberOfChange

- Specify the allowable number of contact changes. This argument is to be used if _iContactType=0_.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### dMinContactPercentage

- Specify the minimum contact set percentage. This argument is to be used if _iContactType=0_.
- The default value is 100.

<!-- @since:5.0.1 @optional -->
### iShellThickness

- Specify whether to include shell thickness for plate elements. The gap between connection regions will be independent of plate element thickness if this option is turned off. This argument is to be used if _iContactType=0_.
  - If _iShellThickness=0_, include half shell thickness as surface offset.
  - If _iShellThickness=1_, does not include thickness offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactStatus

- Specify the flag to indicate if the contact status for a specific sub-case is to start from the final status of the previous subcase. This argument is to be used if _iContactType=0_.
  - If _iContactStatus=0_, starts from previous subcase.
  - If _iContactStatus=1_, starts from initial state.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitGapOrPenetration

- Specify how Nastran handles initial gap or penetration of the generated contact elements. This setting is particularly useful if some of your elements unintentionally penetrate each other and you do not wish to modify or rebuild your model. This argument is to be used if _iContactType=0_.
  - If _iInitGapOrPenetration=0_, use the value calculated from the grid coordinates.
  - If _iInitGapOrPenetration=1_, sets the penetration to zero for all contact elements.
  - If _iInitGapOrPenetration=2_, sets the both penetration and gap to zero for all contact elements.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRegionRefine

- Specify whether or not the source region is refined. This argument is to be used if _iContactType=0_.
  - If _iRegionRefine=0_, refines the source region based on target surface definition.
  - If _iRegionRefine=1_, does not refine the source region based on target surface definition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEvaluateOrder

- Specify the number of “Linear Contact Points” for a single element on the source region.
  - If _iEvaluateOrder=0_, lowest order of points on source region.
  - If _iEvaluateOrder=1_, medium order of points on source region.
  - If _iEvaluateOrder=2_, highest order of points on source region.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dMinSearchDist

- Specify the minimum distance for searching the contact elements. This argument is to be used if _iContactType=0_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxSearchDist

- Specify the maximum distance for searching the contact elements. This argument is to be used if _iContactType=0_.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dFrictionCoeff

- Specify the static coefficient of friction for the contact pair. This argument is to be used if _iContactType=0_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSearchDist

- Specify the search range. This argument is to be used if _iContactType=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPenaltyFactor

- Specify the penalty proportional coefficient. This argument is to be used if _iContactType=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iShellZOffset

- Specify whether the Z-Offset on shell elements should be included in the contact analysis.
  - If _iShellZOffset=0_, Z offset of shells is included as surface offset.
  - If _iShellZOffset=1_, Z offset of shells is NOT included as surface offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactColor

- Specify the contact-to-display marker color.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crContactNXNastran

- Specify an existing contact setting (NX Nastran). If this parameter is used, the specified contact setting (NX Nastran) will be modified. Whe the default value is used, a new contact setting (NX Nastran) will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {7,8,9,10,11}
Geometry.Part.Cube(iPartColor=4962231)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2", 
                   iPartColor=4803000)

creating _status = Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)], 
                                                            crlFaceSlaves=[Face(49)],
                                                            dSearchDist=10.0, 
                                                            dPenaltyFactor=1.0, 
                                                            iContactColor=16711680)

JPT.Debugger(creating _status)
```
