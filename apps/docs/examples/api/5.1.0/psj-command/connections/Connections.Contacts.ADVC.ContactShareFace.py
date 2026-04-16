# Title:   Connections.Contacts.ADVC.ContactShareFace()
# Desc:    create ADVC Contact Share Face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.ADVC.ContactShareFace
# ---
# Create a model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], 
    strName="Cube_2", 
    iPartColor=14903267
)

# Set shared face between the parts
mating_face=Assemble.FindMatingFaceEx(
    crlTaBodies=[Part(1, 2)], 
    dMatingTol=0.000222222
)
Assemble.AssembleFaceEx(
    ilPairFaceToMakeShareFace=mating_face, 
    dTolerance=0.0002, 
    iTypeConnectPos=0
)

# Set Contact Shared Face
Connections.Contacts.ADVC.ContactShareFace(  # [hl:start]
    crlShareFace=[Face(49)], 
    strName="ContactADVC_1", 
    iContactType=1, 
    iTypeId=1, 
    iColor=65280)  # [hl:end]
