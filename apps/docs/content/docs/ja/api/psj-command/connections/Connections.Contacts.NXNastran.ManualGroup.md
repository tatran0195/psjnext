---
title: "Connections.Contacts.NXNastran.ManualGroup()"
description: "Define contact settings between specified groups for the NX solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NXNastran > ManualGroup"
---

## Description

Define contact settings between specified groups for the NX solver.

## Syntax

```psj
Connections.Contacts.NXNastran.ManualGroup(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crFaceMaster

- Specify the group of faces to be the master faces.

<!-- @since:5.0.1 @required -->
### crFaceSlave

- Specify the group of faces to be the slave faces.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactNXNastran\_1".

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General contact (Sliding contact).
  - 1: Tied contact.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactAlg

- Specify the type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dNormalPenaltyFactor

- Specify the penalty factor for the normal direction. This argument is available to be used if _iContactType=0_.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### dTangentialPenaltyFactor

- Specify the penalty factor for the tangential direction. This argument is available to be used if _iContactType=0_.
- The default value is 1.

### `dForceConvergenceTol`

- A _Double_ designating the Contact Force convergence tolerance. This argument is available to be used if _iContactType=0_.
- The default value is 0.01.

### `dMaxForceIteration`

- A _Double_ designating the maximum number of iterations for a force (inner) loop. This argument is available to be used if _iContactType=0_.
- The default value is 10.

### `dMaxStatusIteration`

- A _Double_ designating the maximum number of iterations for a status (outer) loop. This argument is available to be used if _iContactType=0_.
- The default value is 20.

<!-- @since:5.0.1 @optional -->
### dNumberOfChange

- Specify the allowable number of contact changes. This argument is available to be used if _iContactType=0_.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### dMinContactPercentage

- Specify the minimum contact set percentage. This argument is available to be used if _iContactType=0_.
- The default value is 100.

<!-- @since:5.0.1 @optional -->
### iShellThickness

- Specify whether to include shell thickness for plate elements. The gap between connection regions will be independent of plate element thickness if this option is turned off. This argument is available to be used if _iContactType=0_.
  - 0: Includes half shell thickness as surface offset.
  - 1: Does not include thickness offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactStatus

- Specify the flag to indicate if the contact status for a specific sub-case is to start from the final status of the previous subcase. This argument is available to be used if _iContactType=0_.
  - 0: Starts from previous subcase.
  - 1: Starts from initial state.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitGapOrPenetration

- Specify how Nastran handles initial gap or penetration of the generated contact elements. This setting is particularly useful if some of your elements unintentionally penetrate each other and you do not wish to modify or rebuild your model. This argument is available to be used if _iContactType=0_.
  - 0: Uses the value calculated from the grid coordinates.
  - 1: Sets the penetration to zero for all contact elements.
  - 2: Sets the both penetration and gap to zero for all contact elements.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRegionRefine

- Specify whether or not the source region is refined. This argument is available to be used if _iContactType=0_.
  - 0: Refines the source region based on target surface definition.
  - 1: Does not refine the source region based on target surface definition.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEvaluateOrder

- Specify the number of “Linear Contact Points” for a single element on the source region.
  - 0: Lowest order of points on source region.
  - 1: Medium order of points on source region.
  - 2: Highest order of points on source region.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dMinSearchDist

- Specify the minimum distance for searching the contact elements. This argument is available to be used if _iContactType=0_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxSearchDist

- Specify the maximum distance for searching the contact elements. This argument is available to be used if _iContactType=0_.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef

- Specify the static coefficient of friction for the contact pair. This argument is available to be used if _iContactType=0_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSearchDist

- Specify the search range. This argument is available to be used if _iContactType=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPenaltyFactor

- Specify the penalty proportional coefficient. This argument is available to be used if _iContactType=1_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iShellZOffset

- Specify whether the Z-Offset on shell elements should be included in the contact analysis.
  - 0: Z offset of shells is included as surface offset.
  - 1: Z offset of shells is NOT included as surface offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactColor

- Specify the contact-to-display marker color.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crContactNXNastran

- Specify an existing contact setting (NX Nastran). If this parameter is used, the specified contact setting (NX Nastran) will be modified. When the default value is used, a new contact setting (NX Nastran) will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S", 
                        crlTargets=[Face(24)])

created _contact = Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=Group(1), 
                                                             crFaceSlave=Group(2), 
                                                             dSearchDist=10.0, 
                                                             dPenatlyFactor=1.0, 
                                                             iColor=16711680, 
                                                             iMethod=1)

JPT.Debugger(created _contact)
```
