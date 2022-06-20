# iograft

iograft is a node-based workflow automation tool for Python. 

This repository contains the Python nodes and types that are bundled with iograft by default. It also contains an example Subcore command and some additional resources.

## VSCode Snippets for iograft

These snippets provide a quick way to create nodes by automatically filling in the structure for the Node class as well as InputDefinitions and OutputDefinitions within a Node.

![](https://github.com/iograft/iograft/blob/a035818dc7073a665a8fa6a9abb6530f1c92d60e/resources/iograft_vscode_snippets.gif)

See the [Visual Studio Snippets Docs](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets) for instructions on adding snippets. One possible method is via Preferences > Configure User Snippets, then choose "New Global Snippets file", name the file (i.e. `iograft_node.json.code-snippets`) and paste in the contents from this repository. You can also put the snippets file included in this repository directly in your VSCode snippets directory.

Three snippets are included and can be triggered within Python scopes (via `Ctrl+Space`):
- `iognode` - Create a skeleton iograft Python node.
- `ioginput` - Create an iograft Python node input.
- `iogoutput` - Create an iograft Python node output.
