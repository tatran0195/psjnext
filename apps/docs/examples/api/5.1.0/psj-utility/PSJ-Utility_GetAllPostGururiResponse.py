# Title:   JPT.GetAllPostGururiResponses()
# Desc:    Get all the information of all existing Grururi responses
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllPostGururiResponse
# ---
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                dAmplitude=10.0, crlTargets=[Node(501)])

# Create a load case
loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])

# Response calculation
response = Calculation.Gururi.Response(crTargetAnalysis=PostFreqAnalysis(1), dInputFrequency=180.0, 
                                        iStepNumber=30)
# Get all Post Gururi Response
listResponses = JPT.GetAllPostFreqResponsesSolver()  # [hl]
JPT.Debugger(listResponses)
for response in listResponses:
    print(response.name)
    print(response.type)
    print(response.id)
    JPT.Debugger(response.targetAnalysis)
