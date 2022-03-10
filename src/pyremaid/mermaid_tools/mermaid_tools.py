from models import MermaidLink, MermaidNode



def _sanitize(markdown: str) -> str:
    return (
        markdown
        .replace("<","")
        .replace(">","")
    )



def _get_unique_nodes(links: list[MermaidLink]) -> list[MermaidNode]:
    # For mainy debug reasons, want to keep this in the input order
    # Change back to a set with `add`s when order isn't important
    node_set = []
    for link in links:
        if link.from_ not in node_set:
            node_set.append(link.from_)
        if link.to not in node_set:
            node_set.append(link.to)
    return node_set


def _get_aliases_for_safe_names(links: list[MermaidLink]) -> str:
    alias_string = ""
    for node in _get_unique_nodes(links=links):
        alias_string += f"    {node.mermaid_safe_name}[\"{node.ast_node}\"]\n"
    return _sanitize(alias_string)


def _get_flow_link_text(link: MermaidLink) -> str:
    from_name = link.from_.mermaid_safe_name
    to_name = link.to.mermaid_safe_name

    return f"    {from_name} --> {to_name}\n"


def _get_flow_connections(links: list[MermaidLink]) -> str:
    connection_text = ""
    for link in links:
        connection_text += _get_flow_link_text(link)

    return connection_text


def create_mermaid_flow_graph_from_links(links: list[MermaidLink]) -> str:
    alaises = _get_aliases_for_safe_names(links=links)
    flow_connections = _get_flow_connections(links=links)
    return (
        "```mermaid\n"
        "flowchart TB\n"
        f"{alaises}\n"
        f"{flow_connections}\n"
        "```\n"
    )

