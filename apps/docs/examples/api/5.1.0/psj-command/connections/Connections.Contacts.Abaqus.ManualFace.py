# Title:   Connections.Contacts.Abaqus.ManualFace()
# Desc:    Define contact settings between specified faces for the Abaqus solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.Abaqus.ManualFace
# ---
Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                   strName="Cube_2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube_3",
                   iPartColor=5395146)
Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(48)])
Assembly.RightClick.Rename(strNewName="Master",
                           crItem=Group(1))
Assembly.RightClick.Rename(strNewName="Slave",
                           crItem=Group(2))
Meshing.SolidMeshing(crlParts=[Part(1, 2, 3)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M",
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S",
                        crlTargets=[Face(49)])

# Create face contact (Abaqus)
creating_status = Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus_1",  # [hl]
                                                         dAdjustWidth=0.01,  # [hl]
                                                         dExtensionZone=DFLT_DBL,  # [hl]
                                                         dMaxPenetration=DFLT_DBL,  # [hl]
                                                         iSmallSliding=1,  # [hl]
                                                         dSmoothAngle=DFLT_DBL,  # [hl]
                                                         iFrictionType=1,  # [hl]
                                                         dFrictionCoeff1=0.015,  # [hl]
                                                         dFrictionCoeff2=DFLT_DBL,  # [hl]
                                                         dShearStressLimit=DFLT_DBL,  # [hl]
                                                         dSlipTolerance=DFLT_DBL,  # [hl]
                                                         dStaticFrictionCoeff=DFLT_DBL,  # [hl]
                                                         dKineticFrictionCoeff=DFLT_DBL,  # [hl]
                                                         dDecayCoeff=DFLT_DBL,  # [hl]
                                                         bAdjustPosition=True,  # [hl]
                                                         dPositionTolerance=DFLT_DBL,  # [hl]
                                                         dContactStiffness=DFLT_DBL,  # [hl]
                                                         tshPressureOverclosure=[0, 0],  # [hl]
                                                         tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],  # [hl]
                                                         tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL],  # [hl]
                                                         crplTargets=[CursorPair(Group(3), Group(4))],  # [hl]
                                                         iContactColor=16711680)  # [hl]

JPT.Debugger(creating_status)
