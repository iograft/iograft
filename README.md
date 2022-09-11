# iograft

iograft is a node-based workflow automation tool for Python. 

This repository contains the Python nodes and types that are bundled with iograft by default. It also contains an example Subcore command and some additional resources.

## VSCode Snippets for iograft

These snippets provide a quick way to create nodes by automatically filling in the structure for the Node class as well as InputDefinitions and OutputDefinitions within a Node.

![](https://github.com/iograft/iograft/blob/a035818dc7073a665a8fa6a9abb6530f1c92d60e/resources/iograft_vscode_snippets.gif)

See the [Visual Studio Snippets Docs](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets) for instructions on adding snippets. One possible method is via Preferences > Configure User Snippets, then choose "New Global Snippets file", name the file (i.e. `iograft_node.json.code-snippets`) and paste in the contents from this repository. You can also put the snippets file included in this repository directly in your VSCode snippets directory.

Three snippets are included in the `iograft_node` snippets file and can be triggered within Python scopes (via `Ctrl+Space`):
- `iognode` - Create a skeleton iograft Python node plugin.
- `ioginput` - Create an iograft Python node input.
- `iogoutput` - Create an iograft Python node output.

One snippet is included in the `iograft_type` snippets file and can be triggered within Python scopes as well:
- `iogtype` - Create a skeleton iograft Python type plugin.

## Node Python Dependencies

Some of the included nodes in this repository require additional Python packages. All of these packages are bundled with the iograft installer and will work out of the box when running iograft's built-in interpreter (Python3.9). 

In custom environments, these packages will need to be added manually in order to use the nodes that depend on them. The required packages can be installed via pip:
- commentjson (https://github.com/vaidik/commentjson) (Nodes: load_json_string.py, load_json_file.py)
- lark-parser (https://github.com/lark-parser/lark) (Nodes: load_json_string.py, load_json_file.py)
