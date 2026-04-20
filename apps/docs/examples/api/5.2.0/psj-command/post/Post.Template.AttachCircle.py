# Title:   Post.Template.AttachCircle()
# Desc:    Attach the current result circle settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachCircle
# ---
Post.Template.Create(strName="Circle_Template", strComment="Attach Circle Template")
template = Post.Template.AttachCircle(strName="Circle_Template",   # [hl:start]
                                    postDataVizOptCircle=POST_DATA_VIZ_OPT_CIRCLE(
                                        dRatioModel=0.04, 
                                        dRatioScreen=0.04))  # [hl:end]
JPT.Debugger(template)
