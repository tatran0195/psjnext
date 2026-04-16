# Title:   Connections.Contacts.Abaqus.ManualGroup()
# Desc:    Define the contact set between the specified group for Abaqus. Create a group with master and slave surfaces beforehand to define the contact in the contact settings
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.Abaqus.ManualGroup
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.Abaqus.ManualGroup(strName="ContactAbaqus_1",   # [hl]
                                                          dAdjustWidth=DFLT_DBL,  # [hl]
                                                          dExtensionZone=DFLT_DBL,   # [hl]
                                                          dMaxPenetration=DFLT_DBL,   # [hl]
                                                          iSmallSliding=1,  # [hl]
                                                          dSmoothAngle=DFLT_DBL,  # [hl]
                                                          iFrictionType=1,   # [hl]
                                                          dFrictionCoeff1=DFLT_DBL,   # [hl]
                                                          dFrictionCoeff2=DFLT_DBL,   # [hl]
                                                          dShearStressLimit=DFLT_DBL,  # [hl]
                                                          dSlipTolerance=DFLT_DBL,   # [hl]
                                                          dStaticFrictionCoeff=DFLT_DBL,   # [hl]
                                                          dKineticFrictionCoeff=DFLT_DBL,  # [hl]
                                                          dDecayCoeff=DFLT_DBL,   # [hl]
                                                          bAdjustPosition=1,   # [hl]
                                                          dPositionTolerance=DFLT_DBL,   # [hl]
                                                          iFormulationType=1,   # [hl]
                                                          iTied=1,  # [hl]
                                                          iPressureOverclosureType=1,   # [hl]
                                                          dContactStiffness=DFLT_DBL,   # [hl]
                                                          tshPressureOverclosure=[0,   # [hl]
                                                                                  0],  # [hl]
                                                          iThermalConductanceDef=3,   # [hl]
                                                          tshClearanceData=[1,   # [hl]
                                                                            2,   # [hl]
                                                                            DFLT_DBL,   # [hl]
                                                                            DFLT_DBL],  # [hl]
                                                          tshPressureData=[1,   # [hl]
                                                                          2,   # [hl]
                                                                          DFLT_DBL,   # [hl]
                                                                          DFLT_DBL],   # [hl]
                                                          crplTargets=[CursorPair(Group(1),   # [hl]
                                                                                  Group(2))],  # [hl]
                                                          iContactColor=16711680)  # [hl]

JPT.Debugger(created_contact)
