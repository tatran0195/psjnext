# Title:   Home.ImportResults.ImportMesh.Nastran()
# Desc:    Import a Nastran mesh file to the Jupiter Database as Post document to add result to the mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ImportResults.ImportMesh.Nastran
# ---
from os import environ

nastran_file_path = environ["Temp"] + "/TechnoStar/Exported_Nastran_File_EXPORT_BDF.bdf"

Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=5000000.0,
                                    crlTargets=[Face(23)])

Properties.Material.Add("Stainless_Steel",
                        [Density([(DENSITY, 7.75e-09)]),
                         Elastic([(YOUNGS_MODULUS, 193000.0),
                                  (POISSONS_RATIO, 0.31)])])
Properties.Solid(crlTargets=[Part(1)],
                 strName="Cube_for_testing",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

Analysis.Nastran.LinearStatic(nastranAnalysis=NASTRAN_ANALYSIS(iSolverType=1,
                                                               iGridFormatType=1,
                                                               bDeleteFloatingNodes=True,
                                                               dEpsilon=DFLT_DBL,
                                                               iMaxNumOfIter=DFLT_INT,
                                                               iMemory=DFLT_INT,
                                                               iNcpu=1,
                                                               iSolNo=101,
                                                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueBcresults=DFLT_INT,
                                                                                                           iValueBgresults=DFLT_INT,
                                                                                                           iTypeStrain=0),
                                                               nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True)),
                              iDummyPropMaterialID=1,
                              strPath=nastran_file_path)

JPT.Exec('New Document()')
import_status = Home.ImportResults.ImportMesh.Nastran(strPath=nastran_file_path)  # [hl]
JPT.Debugger(import_status)
