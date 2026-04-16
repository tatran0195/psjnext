# Title:   JPT.GetAllAvailableResultOptions()
# Desc:    Get all available result options of the inputted result type
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAllAvailableResultOptions
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

all_available_result_options_vector = \  # [hl:start]
    JPT.GetAllAvailableResultOptions(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                     1,
                                     1,
                                     "Stress",
                                     "XX",
                                     JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
                                    )  # [hl:end]

JPT.Debugger(all_available_result_options_vector)

for available_PostDataOp in all_available_result_options_vector:
    #Component of AvailablePostDataOp
    print("---------------------------------")
    print("Location: " + str(available_PostDataOp.loc))
    print("Conversion: " + str(available_PostDataOp.cnv))
    print("Continuously: " + str(available_PostDataOp.cont))
    print("Coordinate: " + str(available_PostDataOp.coord))
    print("Load 1D: " + str(available_PostDataOp.load1d))
    print("Load 2D: " + str(available_PostDataOp.load2d))
    print("Complex: " + str(available_PostDataOp.complex))
    print("Phase Angle: " + str(available_PostDataOp.phaseAngle))
    print("User Coordinate ID: " + str(available_PostDataOp.userCoordSysId))
