import * as path from 'path';
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('psjex extension is now active!');

    const bumpDocsCmd = vscode.commands.registerCommand(
        'psjex.bumpDocs',
        async (uri: vscode.Uri) => {
            if (!uri || !uri.fsPath) return;

            const folderName = path.basename(uri.fsPath);
            const newVersion = await vscode.window.showInputBox({
                prompt: `Enter the new API version to bump from ${folderName}`,
                placeHolder: '5.X.X',
                ignoreFocusOut: true,
            });

            if (!newVersion) return;

            const workspaceFolders = vscode.workspace.workspaceFolders;
            if (!workspaceFolders) return;

            const root = workspaceFolders[0].uri.fsPath;
            const terminal = vscode.window.createTerminal('PSJ Bump Docs');
            terminal.show();
            terminal.sendText(`cd "${path.join(root, 'apps', 'docs')}"`);
            terminal.sendText(`bun run docs:bump ${folderName} ${newVersion}`);
        },
    );

    const initSubmoduleCmd = vscode.commands.registerCommand(
        'psjex.initSubmodule',
        async (uri: vscode.Uri) => {
            if (!uri || !uri.fsPath) return;
            const terminal = vscode.window.createTerminal('PSJ Submodule');
            terminal.show();
            terminal.sendText(`git submodule update --init "${uri.fsPath}"`);
        },
    );

    const syncSubmoduleCmd = vscode.commands.registerCommand(
        'psjex.syncSubmodule',
        async (uri: vscode.Uri) => {
            if (!uri || !uri.fsPath) return;
            const terminal = vscode.window.createTerminal('PSJ Submodule');
            terminal.show();
            terminal.sendText(`git submodule sync "${uri.fsPath}"`);
        },
    );

    const initAllSubmodulesCmd = vscode.commands.registerCommand(
        'psjex.initAllSubmodules',
        async (uri: vscode.Uri) => {
            if (!uri || !uri.fsPath) return;
            const terminal = vscode.window.createTerminal('PSJ Submodule');
            terminal.show();
            terminal.sendText(`git submodule update --init --recursive "${uri.fsPath}"`);
        },
    );

    const syncAllSubmodulesCmd = vscode.commands.registerCommand(
        'psjex.syncAllSubmodules',
        async (uri: vscode.Uri) => {
            if (!uri || !uri.fsPath) return;
            const terminal = vscode.window.createTerminal('PSJ Submodule');
            terminal.show();
            terminal.sendText(`git submodule sync --recursive "${uri.fsPath}"`);
        },
    );

    context.subscriptions.push(
        bumpDocsCmd,
        initSubmoduleCmd,
        syncSubmoduleCmd,
        initAllSubmodulesCmd,
        syncAllSubmodulesCmd,
    );
}

export function deactivate() {}
