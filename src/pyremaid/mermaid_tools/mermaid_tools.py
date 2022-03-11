from models import (
    MermaidBlock,
    MermaidClass,
    MermaidElement,
    MermaidFor,
    MermaidFunction,
    MermaidLink,
    MermaidNode,
)

TAB = "  "


def _sanitize(markdown: str) -> str:
    return (
        markdown
        .replace("<","")
        .replace(">","")
    )


def _get_unique_nodes(elements: list[MermaidElement]) -> list[MermaidNode]:
    # For mainly debug / diffing reasons, want to keep this in the input order
    node_set = []
    for element in elements:
        if isinstance(element, MermaidLink):
            link : MermaidLink = element
            if link.from_ not in node_set:
                node_set.append(link.from_)
            if link.to not in node_set:
                node_set.append(link.to)
        if isinstance(element, MermaidBlock):
            block : MermaidBlock = element
            node_set.extend(_get_unique_nodes(block.block_contents))
    return node_set


def _get_aliases_for_safe_names(elements: list[MermaidElement], indent: int = 1) -> str:
    alias_string = ""
    for node in _get_unique_nodes(elements=elements):
        alias_string += f"{TAB * indent}{node.mermaid_safe_name}[\"{node.display_name}\"]\n"
    return _sanitize(alias_string)


def _get_flow_link_text(link: MermaidElement, indent: int) -> str:
    from_name = link.from_.mermaid_safe_name
    to_name = link.to.mermaid_safe_name

    return f"{TAB*indent}{from_name} --> {to_name}\n"


def _get_flow_connections(elements: list[MermaidElement], indent: int = 1) -> str:
    connection_text = ""
    for element in elements:
        if isinstance(element, MermaidLink):
            link: MermaidLink = element
            connection_text += _get_flow_link_text(link=link, indent=indent)
        elif isinstance(element, MermaidBlock):
            block: MermaidBlock = element
            connection_text += _get_block_text(block=block, indent=indent)

    return connection_text


def _get_block_text(block: MermaidBlock, indent: int) -> str:
    block_text = ""
    if isinstance(block, MermaidFunction):
        function_def : MermaidFunction = block
        block_text += f"{TAB * indent}subgraph {function_def.display_name}\n"
        block_text += f"{TAB * (indent + 1)}direction TB\n"
        block_text += _get_flow_connections(function_def.block_contents, indent + 1)
        block_text += f"{TAB * indent}end\n"
    elif isinstance(block, MermaidClass):
        class_def : MermaidClass = block
        block_text += f"{TAB * indent}subgraph {class_def.display_name}\n"
        block_text += f"{TAB * (indent + 1)}direction TB\n"
        block_text += _get_flow_connections(class_def.block_contents, indent + 1)
        block_text += f"{TAB * indent}end\n"
    elif isinstance(block, MermaidFor):
        for_def : MermaidFor = block
        block_text += f"{TAB * indent}%% loop {for_def.display_name}\n"
        block_text += _get_flow_connections(for_def.block_contents, indent + 1)
        block_text += f"{TAB * indent}%% end {for_def.display_name}\n"
    else:
        block_text += _get_flow_connections(block.block_contents, indent)
    return block_text


def create_mermaid_flow_graph_from_links(elements: list[MermaidElement]) -> str:
    alaises = _get_aliases_for_safe_names(elements=elements)
    flow_connections = _get_flow_connections(elements=elements)
    return (
        "```mermaid\n"
        "flowchart TB\n"
        f"{alaises}\n"
        f"{flow_connections}\n"
        "```\n"
    )

