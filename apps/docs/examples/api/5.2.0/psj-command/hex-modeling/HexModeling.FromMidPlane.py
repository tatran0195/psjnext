# Title:   HexModeling.FromMidPlane()
# Desc:    Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/hex-modeling/HexModeling.FromMidPlane
# ---
import os

#Check license of midplane to use midplane function
MidplaneLicense="JPT_MIDP"
JPT.EnableLicenseFeature(MidplaneLicense, 1)
check=JPT.CheckLicense(MidplaneLicense)

if check == False:
    JPT.MessageBoxPSJ(f"{MidplaneLicense} license is needed to create midplane.\n (This sample needs midplane to execute.)", JPT.MsgBoxType.MB_WARNING_OK)
else:
    cadFile=os.path.join(JPT.GetProgramPath(),'SampleData/bracket.x_t')

    Home.ImportCAD.Parasolid(strlPaths=[cadFile], dScale=0.001)

    MidPlane.PressShell(crlPart=[Part(1)], dTinyHollowDepth=0.0002)

    Meshing.SetMeshAttribute(
        crlParts=[Part(1)], 
        surfaceMesh=SURFACE_MESH(
            dAvgElemSize=0.01, 
            dMaxElemSize=0.02, 
            dGeomAngle=0.7853981634, 
            iPerformanceMode=1, 
            dAutoMergeTinyFacesAngle=0.5235987756, 
            bOutputQuadMesh=True, 
            bGeomApprox=True, 
            iNextEntityOffsetId=0))

    Meshing.SurfaceMeshing(
        crlParts=[Part(1)], 
        surfaceMesh=SURFACE_MESH(dAvgElemSize=0.01, 
        dMaxElemSize=0.02, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

    HexModeling.FromMidPlane(crlParts=[Part(1)])  # [hl]
