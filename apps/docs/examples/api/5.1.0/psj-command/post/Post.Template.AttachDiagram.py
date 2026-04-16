# Title:   Post.Template.AttachDiagram()
# Desc:    Attach the current diagram settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachDiagram
# ---
Post.Template.Create(strName="Diagram_Template", strComment="Attach Diagram Template")
template = Post.Template.AttachDiagram(strName="Diagram_Template",   # [hl:start]
                                    postDataVizOptDiagram=POST_DATA_VIZ_OPT_DIAGRAM(
                                        dRatioModel=0.05, 
                                        dRatioScreen=0.05))  # [hl:end]
JPT.Debugger(template)
