# Title:   Connections.Contacts.Ansys.ContactShareFace()
# Desc:    Define contact settings for ANSYS by using shared faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.Ansys.ContactShareFace
# ---
Geometry.Part.Cube(iPartColor=13064794)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=13948008)

Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 
                                                   24], 
                        dTolerance=0.000222222,
                        iTypeConnectPos=0)

created_contact = Connections.Contacts.Ansys.ContactShareFace(crlShareFaces=[Face(49)],   # [hl]
                                                              ansysContact=ANSYS_CONTACT(dFricCoef=0.2,   # [hl]
                                                                                         dPenaStiffness=0.1,   # [hl]
                                                                                         dPetrTolerance=0.1))  # [hl]

JPT.Debugger(created_contact)
