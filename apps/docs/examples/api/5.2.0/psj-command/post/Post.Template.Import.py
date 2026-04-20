# Title:   Post.Template.Import()
# Desc:    Import the contents of the saved template settings (*.xml) into the template list
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.Import
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create new Template
Post.Template.Create(strName="Template_1", strComment="")
Post.Template.AttachViewPoint(
    strName="Template_1", 
    postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
        dlCenter=[0.016, 0.005, 0.0025], 
        dScaleFactor=0.0349344))
Post.Template.Export(strPath="C:/temp/Template_1.xml")
Post.Template.Delete(strName="Template_1")

# Import template
importTemplate = Post.Template.Import(strPath="C:/temp/Template_1.xml")  # [hl]
JPT.Debugger(importTemplate)
