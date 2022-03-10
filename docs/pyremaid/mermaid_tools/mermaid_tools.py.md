# ./src/pyremaid/mermaid_tools/mermaid_tools.py

### Imports

  - models.MermaidBlock
  - models.MermaidElement
  - models.MermaidFunction
  - models.MermaidLink
  - models.MermaidNode

---
```mermaid
flowchart TB
  _node_0["Assign"]
  _node_1["Name"]
  _node_2["Store"]
  _node_3["Constant"]
  __sanitize_node_0["Return"]
  __sanitize_node_1["Call"]
  __sanitize_node_2["Attribute"]
  __sanitize_node_3["Call"]
  __sanitize_node_4["Attribute"]
  __sanitize_node_5["Name"]
  __sanitize_node_6["Load"]
  __sanitize_node_7["Load"]
  __sanitize_node_8["Constant"]
  __sanitize_node_9["Constant"]
  __sanitize_node_10["Load"]
  __sanitize_node_11["Constant"]
  __sanitize_node_12["Constant"]
  __get_unique_nodes_node_0["Assign"]
  __get_unique_nodes_node_1["Name"]
  __get_unique_nodes_node_2["Store"]
  __get_unique_nodes_node_3["List"]
  __get_unique_nodes_node_4["Load"]
  __get_unique_nodes_node_5["For"]
  __get_unique_nodes_node_6["Name"]
  __get_unique_nodes_node_7["Store"]
  __get_unique_nodes_node_8["Name"]
  __get_unique_nodes_node_9["Load"]
  __get_unique_nodes_node_10["If"]
  __get_unique_nodes_node_11["Call"]
  __get_unique_nodes_node_12["Name"]
  __get_unique_nodes_node_13["Load"]
  __get_unique_nodes_node_14["Name"]
  __get_unique_nodes_node_15["Load"]
  __get_unique_nodes_node_16["Name"]
  __get_unique_nodes_node_17["Load"]
  __get_unique_nodes_node_18["AnnAssign"]
  __get_unique_nodes_node_19["Name"]
  __get_unique_nodes_node_20["Store"]
  __get_unique_nodes_node_21["Name"]
  __get_unique_nodes_node_22["Load"]
  __get_unique_nodes_node_23["Name"]
  __get_unique_nodes_node_24["Load"]
  __get_unique_nodes_node_25["If"]
  __get_unique_nodes_node_26["Compare"]
  __get_unique_nodes_node_27["Attribute"]
  __get_unique_nodes_node_28["Name"]
  __get_unique_nodes_node_29["Load"]
  __get_unique_nodes_node_30["Load"]
  __get_unique_nodes_node_31["NotIn"]
  __get_unique_nodes_node_32["Name"]
  __get_unique_nodes_node_33["Load"]
  __get_unique_nodes_node_34["Expr"]
  __get_unique_nodes_node_35["Call"]
  __get_unique_nodes_node_36["Attribute"]
  __get_unique_nodes_node_37["Name"]
  __get_unique_nodes_node_38["Load"]
  __get_unique_nodes_node_39["Load"]
  __get_unique_nodes_node_40["Attribute"]
  __get_unique_nodes_node_41["Name"]
  __get_unique_nodes_node_42["Load"]
  __get_unique_nodes_node_43["Load"]
  __get_unique_nodes_node_44["If"]
  __get_unique_nodes_node_45["Compare"]
  __get_unique_nodes_node_46["Attribute"]
  __get_unique_nodes_node_47["Name"]
  __get_unique_nodes_node_48["Load"]
  __get_unique_nodes_node_49["Load"]
  __get_unique_nodes_node_50["NotIn"]
  __get_unique_nodes_node_51["Name"]
  __get_unique_nodes_node_52["Load"]
  __get_unique_nodes_node_53["Expr"]
  __get_unique_nodes_node_54["Call"]
  __get_unique_nodes_node_55["Attribute"]
  __get_unique_nodes_node_56["Name"]
  __get_unique_nodes_node_57["Load"]
  __get_unique_nodes_node_58["Load"]
  __get_unique_nodes_node_59["Attribute"]
  __get_unique_nodes_node_60["Name"]
  __get_unique_nodes_node_61["Load"]
  __get_unique_nodes_node_62["Load"]
  __get_unique_nodes_node_63["If"]
  __get_unique_nodes_node_64["Call"]
  __get_unique_nodes_node_65["Name"]
  __get_unique_nodes_node_66["Load"]
  __get_unique_nodes_node_67["Name"]
  __get_unique_nodes_node_68["Load"]
  __get_unique_nodes_node_69["Name"]
  __get_unique_nodes_node_70["Load"]
  __get_unique_nodes_node_71["AnnAssign"]
  __get_unique_nodes_node_72["Name"]
  __get_unique_nodes_node_73["Store"]
  __get_unique_nodes_node_74["Name"]
  __get_unique_nodes_node_75["Load"]
  __get_unique_nodes_node_76["Name"]
  __get_unique_nodes_node_77["Load"]
  __get_unique_nodes_node_78["Expr"]
  __get_unique_nodes_node_79["Call"]
  __get_unique_nodes_node_80["Attribute"]
  __get_unique_nodes_node_81["Name"]
  __get_unique_nodes_node_82["Load"]
  __get_unique_nodes_node_83["Load"]
  __get_unique_nodes_node_84["Call"]
  __get_unique_nodes_node_85["Name"]
  __get_unique_nodes_node_86["Load"]
  __get_unique_nodes_node_87["Attribute"]
  __get_unique_nodes_node_88["Name"]
  __get_unique_nodes_node_89["Load"]
  __get_unique_nodes_node_90["Load"]
  __get_unique_nodes_node_91["Return"]
  __get_unique_nodes_node_92["Name"]
  __get_unique_nodes_node_93["Load"]
  __get_aliases_for_safe_names_node_0["Assign"]
  __get_aliases_for_safe_names_node_1["Name"]
  __get_aliases_for_safe_names_node_2["Store"]
  __get_aliases_for_safe_names_node_3["Constant"]
  __get_aliases_for_safe_names_node_4["For"]
  __get_aliases_for_safe_names_node_5["Name"]
  __get_aliases_for_safe_names_node_6["Store"]
  __get_aliases_for_safe_names_node_7["Call"]
  __get_aliases_for_safe_names_node_8["Name"]
  __get_aliases_for_safe_names_node_9["Load"]
  __get_aliases_for_safe_names_node_10["keyword"]
  __get_aliases_for_safe_names_node_11["Name"]
  __get_aliases_for_safe_names_node_12["Load"]
  __get_aliases_for_safe_names_node_13["AugAssign"]
  __get_aliases_for_safe_names_node_14["Name"]
  __get_aliases_for_safe_names_node_15["Store"]
  __get_aliases_for_safe_names_node_16["Add"]
  __get_aliases_for_safe_names_node_17["JoinedStr"]
  __get_aliases_for_safe_names_node_18["FormattedValue"]
  __get_aliases_for_safe_names_node_19["BinOp"]
  __get_aliases_for_safe_names_node_20["Name"]
  __get_aliases_for_safe_names_node_21["Load"]
  __get_aliases_for_safe_names_node_22["Mult"]
  __get_aliases_for_safe_names_node_23["Name"]
  __get_aliases_for_safe_names_node_24["Load"]
  __get_aliases_for_safe_names_node_25["FormattedValue"]
  __get_aliases_for_safe_names_node_26["Attribute"]
  __get_aliases_for_safe_names_node_27["Name"]
  __get_aliases_for_safe_names_node_28["Load"]
  __get_aliases_for_safe_names_node_29["Load"]
  __get_aliases_for_safe_names_node_30["Constant"]
  __get_aliases_for_safe_names_node_31["FormattedValue"]
  __get_aliases_for_safe_names_node_32["Attribute"]
  __get_aliases_for_safe_names_node_33["Name"]
  __get_aliases_for_safe_names_node_34["Load"]
  __get_aliases_for_safe_names_node_35["Load"]
  __get_aliases_for_safe_names_node_36["Constant"]
  __get_aliases_for_safe_names_node_37["Return"]
  __get_aliases_for_safe_names_node_38["Call"]
  __get_aliases_for_safe_names_node_39["Name"]
  __get_aliases_for_safe_names_node_40["Load"]
  __get_aliases_for_safe_names_node_41["Name"]
  __get_aliases_for_safe_names_node_42["Load"]
  __get_flow_link_text_node_0["Assign"]
  __get_flow_link_text_node_1["Name"]
  __get_flow_link_text_node_2["Store"]
  __get_flow_link_text_node_3["Attribute"]
  __get_flow_link_text_node_4["Attribute"]
  __get_flow_link_text_node_5["Name"]
  __get_flow_link_text_node_6["Load"]
  __get_flow_link_text_node_7["Load"]
  __get_flow_link_text_node_8["Load"]
  __get_flow_link_text_node_9["Assign"]
  __get_flow_link_text_node_10["Name"]
  __get_flow_link_text_node_11["Store"]
  __get_flow_link_text_node_12["Attribute"]
  __get_flow_link_text_node_13["Attribute"]
  __get_flow_link_text_node_14["Name"]
  __get_flow_link_text_node_15["Load"]
  __get_flow_link_text_node_16["Load"]
  __get_flow_link_text_node_17["Load"]
  __get_flow_link_text_node_18["Return"]
  __get_flow_link_text_node_19["JoinedStr"]
  __get_flow_link_text_node_20["FormattedValue"]
  __get_flow_link_text_node_21["BinOp"]
  __get_flow_link_text_node_22["Name"]
  __get_flow_link_text_node_23["Load"]
  __get_flow_link_text_node_24["Mult"]
  __get_flow_link_text_node_25["Name"]
  __get_flow_link_text_node_26["Load"]
  __get_flow_link_text_node_27["FormattedValue"]
  __get_flow_link_text_node_28["Name"]
  __get_flow_link_text_node_29["Load"]
  __get_flow_link_text_node_30["Constant"]
  __get_flow_link_text_node_31["FormattedValue"]
  __get_flow_link_text_node_32["Name"]
  __get_flow_link_text_node_33["Load"]
  __get_flow_link_text_node_34["Constant"]
  __get_flow_connections_node_0["Assign"]
  __get_flow_connections_node_1["Name"]
  __get_flow_connections_node_2["Store"]
  __get_flow_connections_node_3["Constant"]
  __get_flow_connections_node_4["For"]
  __get_flow_connections_node_5["Name"]
  __get_flow_connections_node_6["Store"]
  __get_flow_connections_node_7["Name"]
  __get_flow_connections_node_8["Load"]
  __get_flow_connections_node_9["If"]
  __get_flow_connections_node_10["Call"]
  __get_flow_connections_node_11["Name"]
  __get_flow_connections_node_12["Load"]
  __get_flow_connections_node_13["Name"]
  __get_flow_connections_node_14["Load"]
  __get_flow_connections_node_15["Name"]
  __get_flow_connections_node_16["Load"]
  __get_flow_connections_node_17["AnnAssign"]
  __get_flow_connections_node_18["Name"]
  __get_flow_connections_node_19["Store"]
  __get_flow_connections_node_20["Name"]
  __get_flow_connections_node_21["Load"]
  __get_flow_connections_node_22["Name"]
  __get_flow_connections_node_23["Load"]
  __get_flow_connections_node_24["AugAssign"]
  __get_flow_connections_node_25["Name"]
  __get_flow_connections_node_26["Store"]
  __get_flow_connections_node_27["Add"]
  __get_flow_connections_node_28["Call"]
  __get_flow_connections_node_29["Name"]
  __get_flow_connections_node_30["Load"]
  __get_flow_connections_node_31["keyword"]
  __get_flow_connections_node_32["Name"]
  __get_flow_connections_node_33["Load"]
  __get_flow_connections_node_34["keyword"]
  __get_flow_connections_node_35["Name"]
  __get_flow_connections_node_36["Load"]
  __get_flow_connections_node_37["If"]
  __get_flow_connections_node_38["Call"]
  __get_flow_connections_node_39["Name"]
  __get_flow_connections_node_40["Load"]
  __get_flow_connections_node_41["Name"]
  __get_flow_connections_node_42["Load"]
  __get_flow_connections_node_43["Name"]
  __get_flow_connections_node_44["Load"]
  __get_flow_connections_node_45["AnnAssign"]
  __get_flow_connections_node_46["Name"]
  __get_flow_connections_node_47["Store"]
  __get_flow_connections_node_48["Name"]
  __get_flow_connections_node_49["Load"]
  __get_flow_connections_node_50["Name"]
  __get_flow_connections_node_51["Load"]
  __get_flow_connections_node_52["AugAssign"]
  __get_flow_connections_node_53["Name"]
  __get_flow_connections_node_54["Store"]
  __get_flow_connections_node_55["Add"]
  __get_flow_connections_node_56["Call"]
  __get_flow_connections_node_57["Name"]
  __get_flow_connections_node_58["Load"]
  __get_flow_connections_node_59["keyword"]
  __get_flow_connections_node_60["Name"]
  __get_flow_connections_node_61["Load"]
  __get_flow_connections_node_62["keyword"]
  __get_flow_connections_node_63["Name"]
  __get_flow_connections_node_64["Load"]
  __get_flow_connections_node_65["Return"]
  __get_flow_connections_node_66["Name"]
  __get_flow_connections_node_67["Load"]
  __get_block_text_node_0["Assign"]
  __get_block_text_node_1["Name"]
  __get_block_text_node_2["Store"]
  __get_block_text_node_3["Constant"]
  __get_block_text_node_4["If"]
  __get_block_text_node_5["Call"]
  __get_block_text_node_6["Name"]
  __get_block_text_node_7["Load"]
  __get_block_text_node_8["Name"]
  __get_block_text_node_9["Load"]
  __get_block_text_node_10["Name"]
  __get_block_text_node_11["Load"]
  __get_block_text_node_12["AnnAssign"]
  __get_block_text_node_13["Name"]
  __get_block_text_node_14["Store"]
  __get_block_text_node_15["Name"]
  __get_block_text_node_16["Load"]
  __get_block_text_node_17["Name"]
  __get_block_text_node_18["Load"]
  __get_block_text_node_19["AugAssign"]
  __get_block_text_node_20["Name"]
  __get_block_text_node_21["Store"]
  __get_block_text_node_22["Add"]
  __get_block_text_node_23["JoinedStr"]
  __get_block_text_node_24["FormattedValue"]
  __get_block_text_node_25["BinOp"]
  __get_block_text_node_26["Name"]
  __get_block_text_node_27["Load"]
  __get_block_text_node_28["Mult"]
  __get_block_text_node_29["Name"]
  __get_block_text_node_30["Load"]
  __get_block_text_node_31["Constant"]
  __get_block_text_node_32["FormattedValue"]
  __get_block_text_node_33["Attribute"]
  __get_block_text_node_34["Name"]
  __get_block_text_node_35["Load"]
  __get_block_text_node_36["Load"]
  __get_block_text_node_37["Constant"]
  __get_block_text_node_38["AugAssign"]
  __get_block_text_node_39["Name"]
  __get_block_text_node_40["Store"]
  __get_block_text_node_41["Add"]
  __get_block_text_node_42["JoinedStr"]
  __get_block_text_node_43["FormattedValue"]
  __get_block_text_node_44["BinOp"]
  __get_block_text_node_45["Name"]
  __get_block_text_node_46["Load"]
  __get_block_text_node_47["Mult"]
  __get_block_text_node_48["BinOp"]
  __get_block_text_node_49["Name"]
  __get_block_text_node_50["Load"]
  __get_block_text_node_51["Add"]
  __get_block_text_node_52["Constant"]
  __get_block_text_node_53["Constant"]
  __get_block_text_node_54["AugAssign"]
  __get_block_text_node_55["Name"]
  __get_block_text_node_56["Store"]
  __get_block_text_node_57["Add"]
  __get_block_text_node_58["Call"]
  __get_block_text_node_59["Name"]
  __get_block_text_node_60["Load"]
  __get_block_text_node_61["Attribute"]
  __get_block_text_node_62["Name"]
  __get_block_text_node_63["Load"]
  __get_block_text_node_64["Load"]
  __get_block_text_node_65["BinOp"]
  __get_block_text_node_66["Name"]
  __get_block_text_node_67["Load"]
  __get_block_text_node_68["Add"]
  __get_block_text_node_69["Constant"]
  __get_block_text_node_70["AugAssign"]
  __get_block_text_node_71["Name"]
  __get_block_text_node_72["Store"]
  __get_block_text_node_73["Add"]
  __get_block_text_node_74["JoinedStr"]
  __get_block_text_node_75["FormattedValue"]
  __get_block_text_node_76["BinOp"]
  __get_block_text_node_77["Name"]
  __get_block_text_node_78["Load"]
  __get_block_text_node_79["Mult"]
  __get_block_text_node_80["Name"]
  __get_block_text_node_81["Load"]
  __get_block_text_node_82["Constant"]
  __get_block_text_node_83["AugAssign"]
  __get_block_text_node_84["Name"]
  __get_block_text_node_85["Store"]
  __get_block_text_node_86["Add"]
  __get_block_text_node_87["Call"]
  __get_block_text_node_88["Name"]
  __get_block_text_node_89["Load"]
  __get_block_text_node_90["Attribute"]
  __get_block_text_node_91["Name"]
  __get_block_text_node_92["Load"]
  __get_block_text_node_93["Load"]
  __get_block_text_node_94["Name"]
  __get_block_text_node_95["Load"]
  __get_block_text_node_96["Return"]
  __get_block_text_node_97["Name"]
  __get_block_text_node_98["Load"]
  _create_mermaid_flow_graph_from_links_node_0["Assign"]
  _create_mermaid_flow_graph_from_links_node_1["Name"]
  _create_mermaid_flow_graph_from_links_node_2["Store"]
  _create_mermaid_flow_graph_from_links_node_3["Call"]
  _create_mermaid_flow_graph_from_links_node_4["Name"]
  _create_mermaid_flow_graph_from_links_node_5["Load"]
  _create_mermaid_flow_graph_from_links_node_6["keyword"]
  _create_mermaid_flow_graph_from_links_node_7["Name"]
  _create_mermaid_flow_graph_from_links_node_8["Load"]
  _create_mermaid_flow_graph_from_links_node_9["Assign"]
  _create_mermaid_flow_graph_from_links_node_10["Name"]
  _create_mermaid_flow_graph_from_links_node_11["Store"]
  _create_mermaid_flow_graph_from_links_node_12["Call"]
  _create_mermaid_flow_graph_from_links_node_13["Name"]
  _create_mermaid_flow_graph_from_links_node_14["Load"]
  _create_mermaid_flow_graph_from_links_node_15["keyword"]
  _create_mermaid_flow_graph_from_links_node_16["Name"]
  _create_mermaid_flow_graph_from_links_node_17["Load"]
  _create_mermaid_flow_graph_from_links_node_18["Return"]
  _create_mermaid_flow_graph_from_links_node_19["JoinedStr"]
  _create_mermaid_flow_graph_from_links_node_20["Constant"]
  _create_mermaid_flow_graph_from_links_node_21["FormattedValue"]
  _create_mermaid_flow_graph_from_links_node_22["Name"]
  _create_mermaid_flow_graph_from_links_node_23["Load"]
  _create_mermaid_flow_graph_from_links_node_24["Constant"]
  _create_mermaid_flow_graph_from_links_node_25["FormattedValue"]
  _create_mermaid_flow_graph_from_links_node_26["Name"]
  _create_mermaid_flow_graph_from_links_node_27["Load"]
  _create_mermaid_flow_graph_from_links_node_28["Constant"]

  _node_0 --> _node_1
  _node_1 --> _node_2
  _node_2 --> _node_3
  subgraph _sanitize
    direction TB
    __sanitize_node_0 --> __sanitize_node_1
    __sanitize_node_1 --> __sanitize_node_2
    __sanitize_node_2 --> __sanitize_node_3
    __sanitize_node_3 --> __sanitize_node_4
    __sanitize_node_4 --> __sanitize_node_5
    __sanitize_node_5 --> __sanitize_node_6
    __sanitize_node_6 --> __sanitize_node_7
    __sanitize_node_7 --> __sanitize_node_8
    __sanitize_node_8 --> __sanitize_node_9
    __sanitize_node_9 --> __sanitize_node_10
    __sanitize_node_10 --> __sanitize_node_11
    __sanitize_node_11 --> __sanitize_node_12
  end
  subgraph _get_unique_nodes
    direction TB
    __get_unique_nodes_node_0 --> __get_unique_nodes_node_1
    __get_unique_nodes_node_1 --> __get_unique_nodes_node_2
    __get_unique_nodes_node_2 --> __get_unique_nodes_node_3
    __get_unique_nodes_node_3 --> __get_unique_nodes_node_4
    __get_unique_nodes_node_4 --> __get_unique_nodes_node_5
    __get_unique_nodes_node_5 --> __get_unique_nodes_node_6
    __get_unique_nodes_node_6 --> __get_unique_nodes_node_7
    __get_unique_nodes_node_7 --> __get_unique_nodes_node_8
    __get_unique_nodes_node_8 --> __get_unique_nodes_node_9
    __get_unique_nodes_node_9 --> __get_unique_nodes_node_10
    __get_unique_nodes_node_10 --> __get_unique_nodes_node_11
    __get_unique_nodes_node_11 --> __get_unique_nodes_node_12
    __get_unique_nodes_node_12 --> __get_unique_nodes_node_13
    __get_unique_nodes_node_13 --> __get_unique_nodes_node_14
    __get_unique_nodes_node_14 --> __get_unique_nodes_node_15
    __get_unique_nodes_node_15 --> __get_unique_nodes_node_16
    __get_unique_nodes_node_16 --> __get_unique_nodes_node_17
    __get_unique_nodes_node_17 --> __get_unique_nodes_node_18
    __get_unique_nodes_node_18 --> __get_unique_nodes_node_19
    __get_unique_nodes_node_19 --> __get_unique_nodes_node_20
    __get_unique_nodes_node_20 --> __get_unique_nodes_node_21
    __get_unique_nodes_node_21 --> __get_unique_nodes_node_22
    __get_unique_nodes_node_22 --> __get_unique_nodes_node_23
    __get_unique_nodes_node_23 --> __get_unique_nodes_node_24
    __get_unique_nodes_node_24 --> __get_unique_nodes_node_25
    __get_unique_nodes_node_25 --> __get_unique_nodes_node_26
    __get_unique_nodes_node_26 --> __get_unique_nodes_node_27
    __get_unique_nodes_node_27 --> __get_unique_nodes_node_28
    __get_unique_nodes_node_28 --> __get_unique_nodes_node_29
    __get_unique_nodes_node_29 --> __get_unique_nodes_node_30
    __get_unique_nodes_node_30 --> __get_unique_nodes_node_31
    __get_unique_nodes_node_31 --> __get_unique_nodes_node_32
    __get_unique_nodes_node_32 --> __get_unique_nodes_node_33
    __get_unique_nodes_node_33 --> __get_unique_nodes_node_34
    __get_unique_nodes_node_34 --> __get_unique_nodes_node_35
    __get_unique_nodes_node_35 --> __get_unique_nodes_node_36
    __get_unique_nodes_node_36 --> __get_unique_nodes_node_37
    __get_unique_nodes_node_37 --> __get_unique_nodes_node_38
    __get_unique_nodes_node_38 --> __get_unique_nodes_node_39
    __get_unique_nodes_node_39 --> __get_unique_nodes_node_40
    __get_unique_nodes_node_40 --> __get_unique_nodes_node_41
    __get_unique_nodes_node_41 --> __get_unique_nodes_node_42
    __get_unique_nodes_node_42 --> __get_unique_nodes_node_43
    __get_unique_nodes_node_43 --> __get_unique_nodes_node_44
    __get_unique_nodes_node_44 --> __get_unique_nodes_node_45
    __get_unique_nodes_node_45 --> __get_unique_nodes_node_46
    __get_unique_nodes_node_46 --> __get_unique_nodes_node_47
    __get_unique_nodes_node_47 --> __get_unique_nodes_node_48
    __get_unique_nodes_node_48 --> __get_unique_nodes_node_49
    __get_unique_nodes_node_49 --> __get_unique_nodes_node_50
    __get_unique_nodes_node_50 --> __get_unique_nodes_node_51
    __get_unique_nodes_node_51 --> __get_unique_nodes_node_52
    __get_unique_nodes_node_52 --> __get_unique_nodes_node_53
    __get_unique_nodes_node_53 --> __get_unique_nodes_node_54
    __get_unique_nodes_node_54 --> __get_unique_nodes_node_55
    __get_unique_nodes_node_55 --> __get_unique_nodes_node_56
    __get_unique_nodes_node_56 --> __get_unique_nodes_node_57
    __get_unique_nodes_node_57 --> __get_unique_nodes_node_58
    __get_unique_nodes_node_58 --> __get_unique_nodes_node_59
    __get_unique_nodes_node_59 --> __get_unique_nodes_node_60
    __get_unique_nodes_node_60 --> __get_unique_nodes_node_61
    __get_unique_nodes_node_61 --> __get_unique_nodes_node_62
    __get_unique_nodes_node_62 --> __get_unique_nodes_node_63
    __get_unique_nodes_node_63 --> __get_unique_nodes_node_64
    __get_unique_nodes_node_64 --> __get_unique_nodes_node_65
    __get_unique_nodes_node_65 --> __get_unique_nodes_node_66
    __get_unique_nodes_node_66 --> __get_unique_nodes_node_67
    __get_unique_nodes_node_67 --> __get_unique_nodes_node_68
    __get_unique_nodes_node_68 --> __get_unique_nodes_node_69
    __get_unique_nodes_node_69 --> __get_unique_nodes_node_70
    __get_unique_nodes_node_70 --> __get_unique_nodes_node_71
    __get_unique_nodes_node_71 --> __get_unique_nodes_node_72
    __get_unique_nodes_node_72 --> __get_unique_nodes_node_73
    __get_unique_nodes_node_73 --> __get_unique_nodes_node_74
    __get_unique_nodes_node_74 --> __get_unique_nodes_node_75
    __get_unique_nodes_node_75 --> __get_unique_nodes_node_76
    __get_unique_nodes_node_76 --> __get_unique_nodes_node_77
    __get_unique_nodes_node_77 --> __get_unique_nodes_node_78
    __get_unique_nodes_node_78 --> __get_unique_nodes_node_79
    __get_unique_nodes_node_79 --> __get_unique_nodes_node_80
    __get_unique_nodes_node_80 --> __get_unique_nodes_node_81
    __get_unique_nodes_node_81 --> __get_unique_nodes_node_82
    __get_unique_nodes_node_82 --> __get_unique_nodes_node_83
    __get_unique_nodes_node_83 --> __get_unique_nodes_node_84
    __get_unique_nodes_node_84 --> __get_unique_nodes_node_85
    __get_unique_nodes_node_85 --> __get_unique_nodes_node_86
    __get_unique_nodes_node_86 --> __get_unique_nodes_node_87
    __get_unique_nodes_node_87 --> __get_unique_nodes_node_88
    __get_unique_nodes_node_88 --> __get_unique_nodes_node_89
    __get_unique_nodes_node_89 --> __get_unique_nodes_node_90
    __get_unique_nodes_node_90 --> __get_unique_nodes_node_91
    __get_unique_nodes_node_91 --> __get_unique_nodes_node_92
    __get_unique_nodes_node_92 --> __get_unique_nodes_node_93
  end
  subgraph _get_aliases_for_safe_names
    direction TB
    __get_aliases_for_safe_names_node_0 --> __get_aliases_for_safe_names_node_1
    __get_aliases_for_safe_names_node_1 --> __get_aliases_for_safe_names_node_2
    __get_aliases_for_safe_names_node_2 --> __get_aliases_for_safe_names_node_3
    __get_aliases_for_safe_names_node_3 --> __get_aliases_for_safe_names_node_4
    __get_aliases_for_safe_names_node_4 --> __get_aliases_for_safe_names_node_5
    __get_aliases_for_safe_names_node_5 --> __get_aliases_for_safe_names_node_6
    __get_aliases_for_safe_names_node_6 --> __get_aliases_for_safe_names_node_7
    __get_aliases_for_safe_names_node_7 --> __get_aliases_for_safe_names_node_8
    __get_aliases_for_safe_names_node_8 --> __get_aliases_for_safe_names_node_9
    __get_aliases_for_safe_names_node_9 --> __get_aliases_for_safe_names_node_10
    __get_aliases_for_safe_names_node_10 --> __get_aliases_for_safe_names_node_11
    __get_aliases_for_safe_names_node_11 --> __get_aliases_for_safe_names_node_12
    __get_aliases_for_safe_names_node_12 --> __get_aliases_for_safe_names_node_13
    __get_aliases_for_safe_names_node_13 --> __get_aliases_for_safe_names_node_14
    __get_aliases_for_safe_names_node_14 --> __get_aliases_for_safe_names_node_15
    __get_aliases_for_safe_names_node_15 --> __get_aliases_for_safe_names_node_16
    __get_aliases_for_safe_names_node_16 --> __get_aliases_for_safe_names_node_17
    __get_aliases_for_safe_names_node_17 --> __get_aliases_for_safe_names_node_18
    __get_aliases_for_safe_names_node_18 --> __get_aliases_for_safe_names_node_19
    __get_aliases_for_safe_names_node_19 --> __get_aliases_for_safe_names_node_20
    __get_aliases_for_safe_names_node_20 --> __get_aliases_for_safe_names_node_21
    __get_aliases_for_safe_names_node_21 --> __get_aliases_for_safe_names_node_22
    __get_aliases_for_safe_names_node_22 --> __get_aliases_for_safe_names_node_23
    __get_aliases_for_safe_names_node_23 --> __get_aliases_for_safe_names_node_24
    __get_aliases_for_safe_names_node_24 --> __get_aliases_for_safe_names_node_25
    __get_aliases_for_safe_names_node_25 --> __get_aliases_for_safe_names_node_26
    __get_aliases_for_safe_names_node_26 --> __get_aliases_for_safe_names_node_27
    __get_aliases_for_safe_names_node_27 --> __get_aliases_for_safe_names_node_28
    __get_aliases_for_safe_names_node_28 --> __get_aliases_for_safe_names_node_29
    __get_aliases_for_safe_names_node_29 --> __get_aliases_for_safe_names_node_30
    __get_aliases_for_safe_names_node_30 --> __get_aliases_for_safe_names_node_31
    __get_aliases_for_safe_names_node_31 --> __get_aliases_for_safe_names_node_32
    __get_aliases_for_safe_names_node_32 --> __get_aliases_for_safe_names_node_33
    __get_aliases_for_safe_names_node_33 --> __get_aliases_for_safe_names_node_34
    __get_aliases_for_safe_names_node_34 --> __get_aliases_for_safe_names_node_35
    __get_aliases_for_safe_names_node_35 --> __get_aliases_for_safe_names_node_36
    __get_aliases_for_safe_names_node_36 --> __get_aliases_for_safe_names_node_37
    __get_aliases_for_safe_names_node_37 --> __get_aliases_for_safe_names_node_38
    __get_aliases_for_safe_names_node_38 --> __get_aliases_for_safe_names_node_39
    __get_aliases_for_safe_names_node_39 --> __get_aliases_for_safe_names_node_40
    __get_aliases_for_safe_names_node_40 --> __get_aliases_for_safe_names_node_41
    __get_aliases_for_safe_names_node_41 --> __get_aliases_for_safe_names_node_42
  end
  subgraph _get_flow_link_text
    direction TB
    __get_flow_link_text_node_0 --> __get_flow_link_text_node_1
    __get_flow_link_text_node_1 --> __get_flow_link_text_node_2
    __get_flow_link_text_node_2 --> __get_flow_link_text_node_3
    __get_flow_link_text_node_3 --> __get_flow_link_text_node_4
    __get_flow_link_text_node_4 --> __get_flow_link_text_node_5
    __get_flow_link_text_node_5 --> __get_flow_link_text_node_6
    __get_flow_link_text_node_6 --> __get_flow_link_text_node_7
    __get_flow_link_text_node_7 --> __get_flow_link_text_node_8
    __get_flow_link_text_node_8 --> __get_flow_link_text_node_9
    __get_flow_link_text_node_9 --> __get_flow_link_text_node_10
    __get_flow_link_text_node_10 --> __get_flow_link_text_node_11
    __get_flow_link_text_node_11 --> __get_flow_link_text_node_12
    __get_flow_link_text_node_12 --> __get_flow_link_text_node_13
    __get_flow_link_text_node_13 --> __get_flow_link_text_node_14
    __get_flow_link_text_node_14 --> __get_flow_link_text_node_15
    __get_flow_link_text_node_15 --> __get_flow_link_text_node_16
    __get_flow_link_text_node_16 --> __get_flow_link_text_node_17
    __get_flow_link_text_node_17 --> __get_flow_link_text_node_18
    __get_flow_link_text_node_18 --> __get_flow_link_text_node_19
    __get_flow_link_text_node_19 --> __get_flow_link_text_node_20
    __get_flow_link_text_node_20 --> __get_flow_link_text_node_21
    __get_flow_link_text_node_21 --> __get_flow_link_text_node_22
    __get_flow_link_text_node_22 --> __get_flow_link_text_node_23
    __get_flow_link_text_node_23 --> __get_flow_link_text_node_24
    __get_flow_link_text_node_24 --> __get_flow_link_text_node_25
    __get_flow_link_text_node_25 --> __get_flow_link_text_node_26
    __get_flow_link_text_node_26 --> __get_flow_link_text_node_27
    __get_flow_link_text_node_27 --> __get_flow_link_text_node_28
    __get_flow_link_text_node_28 --> __get_flow_link_text_node_29
    __get_flow_link_text_node_29 --> __get_flow_link_text_node_30
    __get_flow_link_text_node_30 --> __get_flow_link_text_node_31
    __get_flow_link_text_node_31 --> __get_flow_link_text_node_32
    __get_flow_link_text_node_32 --> __get_flow_link_text_node_33
    __get_flow_link_text_node_33 --> __get_flow_link_text_node_34
  end
  subgraph _get_flow_connections
    direction TB
    __get_flow_connections_node_0 --> __get_flow_connections_node_1
    __get_flow_connections_node_1 --> __get_flow_connections_node_2
    __get_flow_connections_node_2 --> __get_flow_connections_node_3
    __get_flow_connections_node_3 --> __get_flow_connections_node_4
    __get_flow_connections_node_4 --> __get_flow_connections_node_5
    __get_flow_connections_node_5 --> __get_flow_connections_node_6
    __get_flow_connections_node_6 --> __get_flow_connections_node_7
    __get_flow_connections_node_7 --> __get_flow_connections_node_8
    __get_flow_connections_node_8 --> __get_flow_connections_node_9
    __get_flow_connections_node_9 --> __get_flow_connections_node_10
    __get_flow_connections_node_10 --> __get_flow_connections_node_11
    __get_flow_connections_node_11 --> __get_flow_connections_node_12
    __get_flow_connections_node_12 --> __get_flow_connections_node_13
    __get_flow_connections_node_13 --> __get_flow_connections_node_14
    __get_flow_connections_node_14 --> __get_flow_connections_node_15
    __get_flow_connections_node_15 --> __get_flow_connections_node_16
    __get_flow_connections_node_16 --> __get_flow_connections_node_17
    __get_flow_connections_node_17 --> __get_flow_connections_node_18
    __get_flow_connections_node_18 --> __get_flow_connections_node_19
    __get_flow_connections_node_19 --> __get_flow_connections_node_20
    __get_flow_connections_node_20 --> __get_flow_connections_node_21
    __get_flow_connections_node_21 --> __get_flow_connections_node_22
    __get_flow_connections_node_22 --> __get_flow_connections_node_23
    __get_flow_connections_node_23 --> __get_flow_connections_node_24
    __get_flow_connections_node_24 --> __get_flow_connections_node_25
    __get_flow_connections_node_25 --> __get_flow_connections_node_26
    __get_flow_connections_node_26 --> __get_flow_connections_node_27
    __get_flow_connections_node_27 --> __get_flow_connections_node_28
    __get_flow_connections_node_28 --> __get_flow_connections_node_29
    __get_flow_connections_node_29 --> __get_flow_connections_node_30
    __get_flow_connections_node_30 --> __get_flow_connections_node_31
    __get_flow_connections_node_31 --> __get_flow_connections_node_32
    __get_flow_connections_node_32 --> __get_flow_connections_node_33
    __get_flow_connections_node_33 --> __get_flow_connections_node_34
    __get_flow_connections_node_34 --> __get_flow_connections_node_35
    __get_flow_connections_node_35 --> __get_flow_connections_node_36
    __get_flow_connections_node_36 --> __get_flow_connections_node_37
    __get_flow_connections_node_37 --> __get_flow_connections_node_38
    __get_flow_connections_node_38 --> __get_flow_connections_node_39
    __get_flow_connections_node_39 --> __get_flow_connections_node_40
    __get_flow_connections_node_40 --> __get_flow_connections_node_41
    __get_flow_connections_node_41 --> __get_flow_connections_node_42
    __get_flow_connections_node_42 --> __get_flow_connections_node_43
    __get_flow_connections_node_43 --> __get_flow_connections_node_44
    __get_flow_connections_node_44 --> __get_flow_connections_node_45
    __get_flow_connections_node_45 --> __get_flow_connections_node_46
    __get_flow_connections_node_46 --> __get_flow_connections_node_47
    __get_flow_connections_node_47 --> __get_flow_connections_node_48
    __get_flow_connections_node_48 --> __get_flow_connections_node_49
    __get_flow_connections_node_49 --> __get_flow_connections_node_50
    __get_flow_connections_node_50 --> __get_flow_connections_node_51
    __get_flow_connections_node_51 --> __get_flow_connections_node_52
    __get_flow_connections_node_52 --> __get_flow_connections_node_53
    __get_flow_connections_node_53 --> __get_flow_connections_node_54
    __get_flow_connections_node_54 --> __get_flow_connections_node_55
    __get_flow_connections_node_55 --> __get_flow_connections_node_56
    __get_flow_connections_node_56 --> __get_flow_connections_node_57
    __get_flow_connections_node_57 --> __get_flow_connections_node_58
    __get_flow_connections_node_58 --> __get_flow_connections_node_59
    __get_flow_connections_node_59 --> __get_flow_connections_node_60
    __get_flow_connections_node_60 --> __get_flow_connections_node_61
    __get_flow_connections_node_61 --> __get_flow_connections_node_62
    __get_flow_connections_node_62 --> __get_flow_connections_node_63
    __get_flow_connections_node_63 --> __get_flow_connections_node_64
    __get_flow_connections_node_64 --> __get_flow_connections_node_65
    __get_flow_connections_node_65 --> __get_flow_connections_node_66
    __get_flow_connections_node_66 --> __get_flow_connections_node_67
  end
  subgraph _get_block_text
    direction TB
    __get_block_text_node_0 --> __get_block_text_node_1
    __get_block_text_node_1 --> __get_block_text_node_2
    __get_block_text_node_2 --> __get_block_text_node_3
    __get_block_text_node_3 --> __get_block_text_node_4
    __get_block_text_node_4 --> __get_block_text_node_5
    __get_block_text_node_5 --> __get_block_text_node_6
    __get_block_text_node_6 --> __get_block_text_node_7
    __get_block_text_node_7 --> __get_block_text_node_8
    __get_block_text_node_8 --> __get_block_text_node_9
    __get_block_text_node_9 --> __get_block_text_node_10
    __get_block_text_node_10 --> __get_block_text_node_11
    __get_block_text_node_11 --> __get_block_text_node_12
    __get_block_text_node_12 --> __get_block_text_node_13
    __get_block_text_node_13 --> __get_block_text_node_14
    __get_block_text_node_14 --> __get_block_text_node_15
    __get_block_text_node_15 --> __get_block_text_node_16
    __get_block_text_node_16 --> __get_block_text_node_17
    __get_block_text_node_17 --> __get_block_text_node_18
    __get_block_text_node_18 --> __get_block_text_node_19
    __get_block_text_node_19 --> __get_block_text_node_20
    __get_block_text_node_20 --> __get_block_text_node_21
    __get_block_text_node_21 --> __get_block_text_node_22
    __get_block_text_node_22 --> __get_block_text_node_23
    __get_block_text_node_23 --> __get_block_text_node_24
    __get_block_text_node_24 --> __get_block_text_node_25
    __get_block_text_node_25 --> __get_block_text_node_26
    __get_block_text_node_26 --> __get_block_text_node_27
    __get_block_text_node_27 --> __get_block_text_node_28
    __get_block_text_node_28 --> __get_block_text_node_29
    __get_block_text_node_29 --> __get_block_text_node_30
    __get_block_text_node_30 --> __get_block_text_node_31
    __get_block_text_node_31 --> __get_block_text_node_32
    __get_block_text_node_32 --> __get_block_text_node_33
    __get_block_text_node_33 --> __get_block_text_node_34
    __get_block_text_node_34 --> __get_block_text_node_35
    __get_block_text_node_35 --> __get_block_text_node_36
    __get_block_text_node_36 --> __get_block_text_node_37
    __get_block_text_node_37 --> __get_block_text_node_38
    __get_block_text_node_38 --> __get_block_text_node_39
    __get_block_text_node_39 --> __get_block_text_node_40
    __get_block_text_node_40 --> __get_block_text_node_41
    __get_block_text_node_41 --> __get_block_text_node_42
    __get_block_text_node_42 --> __get_block_text_node_43
    __get_block_text_node_43 --> __get_block_text_node_44
    __get_block_text_node_44 --> __get_block_text_node_45
    __get_block_text_node_45 --> __get_block_text_node_46
    __get_block_text_node_46 --> __get_block_text_node_47
    __get_block_text_node_47 --> __get_block_text_node_48
    __get_block_text_node_48 --> __get_block_text_node_49
    __get_block_text_node_49 --> __get_block_text_node_50
    __get_block_text_node_50 --> __get_block_text_node_51
    __get_block_text_node_51 --> __get_block_text_node_52
    __get_block_text_node_52 --> __get_block_text_node_53
    __get_block_text_node_53 --> __get_block_text_node_54
    __get_block_text_node_54 --> __get_block_text_node_55
    __get_block_text_node_55 --> __get_block_text_node_56
    __get_block_text_node_56 --> __get_block_text_node_57
    __get_block_text_node_57 --> __get_block_text_node_58
    __get_block_text_node_58 --> __get_block_text_node_59
    __get_block_text_node_59 --> __get_block_text_node_60
    __get_block_text_node_60 --> __get_block_text_node_61
    __get_block_text_node_61 --> __get_block_text_node_62
    __get_block_text_node_62 --> __get_block_text_node_63
    __get_block_text_node_63 --> __get_block_text_node_64
    __get_block_text_node_64 --> __get_block_text_node_65
    __get_block_text_node_65 --> __get_block_text_node_66
    __get_block_text_node_66 --> __get_block_text_node_67
    __get_block_text_node_67 --> __get_block_text_node_68
    __get_block_text_node_68 --> __get_block_text_node_69
    __get_block_text_node_69 --> __get_block_text_node_70
    __get_block_text_node_70 --> __get_block_text_node_71
    __get_block_text_node_71 --> __get_block_text_node_72
    __get_block_text_node_72 --> __get_block_text_node_73
    __get_block_text_node_73 --> __get_block_text_node_74
    __get_block_text_node_74 --> __get_block_text_node_75
    __get_block_text_node_75 --> __get_block_text_node_76
    __get_block_text_node_76 --> __get_block_text_node_77
    __get_block_text_node_77 --> __get_block_text_node_78
    __get_block_text_node_78 --> __get_block_text_node_79
    __get_block_text_node_79 --> __get_block_text_node_80
    __get_block_text_node_80 --> __get_block_text_node_81
    __get_block_text_node_81 --> __get_block_text_node_82
    __get_block_text_node_82 --> __get_block_text_node_83
    __get_block_text_node_83 --> __get_block_text_node_84
    __get_block_text_node_84 --> __get_block_text_node_85
    __get_block_text_node_85 --> __get_block_text_node_86
    __get_block_text_node_86 --> __get_block_text_node_87
    __get_block_text_node_87 --> __get_block_text_node_88
    __get_block_text_node_88 --> __get_block_text_node_89
    __get_block_text_node_89 --> __get_block_text_node_90
    __get_block_text_node_90 --> __get_block_text_node_91
    __get_block_text_node_91 --> __get_block_text_node_92
    __get_block_text_node_92 --> __get_block_text_node_93
    __get_block_text_node_93 --> __get_block_text_node_94
    __get_block_text_node_94 --> __get_block_text_node_95
    __get_block_text_node_95 --> __get_block_text_node_96
    __get_block_text_node_96 --> __get_block_text_node_97
    __get_block_text_node_97 --> __get_block_text_node_98
  end
  subgraph create_mermaid_flow_graph_from_links
    direction TB
    _create_mermaid_flow_graph_from_links_node_0 --> _create_mermaid_flow_graph_from_links_node_1
    _create_mermaid_flow_graph_from_links_node_1 --> _create_mermaid_flow_graph_from_links_node_2
    _create_mermaid_flow_graph_from_links_node_2 --> _create_mermaid_flow_graph_from_links_node_3
    _create_mermaid_flow_graph_from_links_node_3 --> _create_mermaid_flow_graph_from_links_node_4
    _create_mermaid_flow_graph_from_links_node_4 --> _create_mermaid_flow_graph_from_links_node_5
    _create_mermaid_flow_graph_from_links_node_5 --> _create_mermaid_flow_graph_from_links_node_6
    _create_mermaid_flow_graph_from_links_node_6 --> _create_mermaid_flow_graph_from_links_node_7
    _create_mermaid_flow_graph_from_links_node_7 --> _create_mermaid_flow_graph_from_links_node_8
    _create_mermaid_flow_graph_from_links_node_8 --> _create_mermaid_flow_graph_from_links_node_9
    _create_mermaid_flow_graph_from_links_node_9 --> _create_mermaid_flow_graph_from_links_node_10
    _create_mermaid_flow_graph_from_links_node_10 --> _create_mermaid_flow_graph_from_links_node_11
    _create_mermaid_flow_graph_from_links_node_11 --> _create_mermaid_flow_graph_from_links_node_12
    _create_mermaid_flow_graph_from_links_node_12 --> _create_mermaid_flow_graph_from_links_node_13
    _create_mermaid_flow_graph_from_links_node_13 --> _create_mermaid_flow_graph_from_links_node_14
    _create_mermaid_flow_graph_from_links_node_14 --> _create_mermaid_flow_graph_from_links_node_15
    _create_mermaid_flow_graph_from_links_node_15 --> _create_mermaid_flow_graph_from_links_node_16
    _create_mermaid_flow_graph_from_links_node_16 --> _create_mermaid_flow_graph_from_links_node_17
    _create_mermaid_flow_graph_from_links_node_17 --> _create_mermaid_flow_graph_from_links_node_18
    _create_mermaid_flow_graph_from_links_node_18 --> _create_mermaid_flow_graph_from_links_node_19
    _create_mermaid_flow_graph_from_links_node_19 --> _create_mermaid_flow_graph_from_links_node_20
    _create_mermaid_flow_graph_from_links_node_20 --> _create_mermaid_flow_graph_from_links_node_21
    _create_mermaid_flow_graph_from_links_node_21 --> _create_mermaid_flow_graph_from_links_node_22
    _create_mermaid_flow_graph_from_links_node_22 --> _create_mermaid_flow_graph_from_links_node_23
    _create_mermaid_flow_graph_from_links_node_23 --> _create_mermaid_flow_graph_from_links_node_24
    _create_mermaid_flow_graph_from_links_node_24 --> _create_mermaid_flow_graph_from_links_node_25
    _create_mermaid_flow_graph_from_links_node_25 --> _create_mermaid_flow_graph_from_links_node_26
    _create_mermaid_flow_graph_from_links_node_26 --> _create_mermaid_flow_graph_from_links_node_27
    _create_mermaid_flow_graph_from_links_node_27 --> _create_mermaid_flow_graph_from_links_node_28
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidBlock'),
        alias(name='MermaidElement'),
        alias(name='MermaidFunction'),
        alias(name='MermaidLink'),
        alias(name='MermaidNode')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=7,
      end_col_offset=1),
    Assign(
      targets=[
        Name(
          id='TAB',
          ctx=Store(),
          lineno=9,
          col_offset=0,
          end_lineno=9,
          end_col_offset=3)],
      value=Constant(
        value='  ',
        lineno=9,
        col_offset=6,
        end_lineno=9,
        end_col_offset=10),
      lineno=9,
      col_offset=0,
      end_lineno=9,
      end_col_offset=10),
    FunctionDef(
      name='_sanitize',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='markdown',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=12,
              col_offset=24,
              end_lineno=12,
              end_col_offset=27),
            lineno=12,
            col_offset=14,
            end_lineno=12,
            end_col_offset=27)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Attribute(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='markdown',
                    ctx=Load(),
                    lineno=14,
                    col_offset=8,
                    end_lineno=14,
                    end_col_offset=16),
                  attr='replace',
                  ctx=Load(),
                  lineno=14,
                  col_offset=8,
                  end_lineno=15,
                  end_col_offset=16),
                args=[
                  Constant(
                    value='<',
                    lineno=15,
                    col_offset=17,
                    end_lineno=15,
                    end_col_offset=20),
                  Constant(
                    value='',
                    lineno=15,
                    col_offset=21,
                    end_lineno=15,
                    end_col_offset=23)],
                keywords=[],
                lineno=14,
                col_offset=8,
                end_lineno=15,
                end_col_offset=24),
              attr='replace',
              ctx=Load(),
              lineno=14,
              col_offset=8,
              end_lineno=16,
              end_col_offset=16),
            args=[
              Constant(
                value='>',
                lineno=16,
                col_offset=17,
                end_lineno=16,
                end_col_offset=20),
              Constant(
                value='',
                lineno=16,
                col_offset=21,
                end_lineno=16,
                end_col_offset=23)],
            keywords=[],
            lineno=14,
            col_offset=8,
            end_lineno=16,
            end_col_offset=24),
          lineno=13,
          col_offset=4,
          end_lineno=17,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=12,
        col_offset=32,
        end_lineno=12,
        end_col_offset=35),
      lineno=12,
      col_offset=0,
      end_lineno=17,
      end_col_offset=5),
    FunctionDef(
      name='_get_unique_nodes',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=20,
                col_offset=32,
                end_lineno=20,
                end_col_offset=36),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=20,
                col_offset=37,
                end_lineno=20,
                end_col_offset=51),
              ctx=Load(),
              lineno=20,
              col_offset=32,
              end_lineno=20,
              end_col_offset=52),
            lineno=20,
            col_offset=22,
            end_lineno=20,
            end_col_offset=52)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='node_set',
              ctx=Store(),
              lineno=22,
              col_offset=4,
              end_lineno=22,
              end_col_offset=12)],
          value=List(
            elts=[],
            ctx=Load(),
            lineno=22,
            col_offset=15,
            end_lineno=22,
            end_col_offset=17),
          lineno=22,
          col_offset=4,
          end_lineno=22,
          end_col_offset=17),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=23,
            col_offset=8,
            end_lineno=23,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=23,
            col_offset=19,
            end_lineno=23,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=24,
                  col_offset=11,
                  end_lineno=24,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=24,
                    col_offset=22,
                    end_lineno=24,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=24,
                    col_offset=31,
                    end_lineno=24,
                    end_col_offset=42)],
                keywords=[],
                lineno=24,
                col_offset=11,
                end_lineno=24,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=25,
                    col_offset=12,
                    end_lineno=25,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=25,
                    col_offset=19,
                    end_lineno=25,
                    end_col_offset=30),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=25,
                    col_offset=33,
                    end_lineno=25,
                    end_col_offset=40),
                  simple=1,
                  lineno=25,
                  col_offset=12,
                  end_lineno=25,
                  end_col_offset=40),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=26,
                        col_offset=15,
                        end_lineno=26,
                        end_col_offset=19),
                      attr='from_',
                      ctx=Load(),
                      lineno=26,
                      col_offset=15,
                      end_lineno=26,
                      end_col_offset=25),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=26,
                        col_offset=33,
                        end_lineno=26,
                        end_col_offset=41)],
                    lineno=26,
                    col_offset=15,
                    end_lineno=26,
                    end_col_offset=41),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=27,
                            col_offset=16,
                            end_lineno=27,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=27,
                          col_offset=16,
                          end_lineno=27,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=27,
                              col_offset=32,
                              end_lineno=27,
                              end_col_offset=36),
                            attr='from_',
                            ctx=Load(),
                            lineno=27,
                            col_offset=32,
                            end_lineno=27,
                            end_col_offset=42)],
                        keywords=[],
                        lineno=27,
                        col_offset=16,
                        end_lineno=27,
                        end_col_offset=43),
                      lineno=27,
                      col_offset=16,
                      end_lineno=27,
                      end_col_offset=43)],
                  orelse=[],
                  lineno=26,
                  col_offset=12,
                  end_lineno=27,
                  end_col_offset=43),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=28,
                        col_offset=15,
                        end_lineno=28,
                        end_col_offset=19),
                      attr='to',
                      ctx=Load(),
                      lineno=28,
                      col_offset=15,
                      end_lineno=28,
                      end_col_offset=22),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=28,
                        col_offset=30,
                        end_lineno=28,
                        end_col_offset=38)],
                    lineno=28,
                    col_offset=15,
                    end_lineno=28,
                    end_col_offset=38),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=29,
                            col_offset=16,
                            end_lineno=29,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=29,
                          col_offset=16,
                          end_lineno=29,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=29,
                              col_offset=32,
                              end_lineno=29,
                              end_col_offset=36),
                            attr='to',
                            ctx=Load(),
                            lineno=29,
                            col_offset=32,
                            end_lineno=29,
                            end_col_offset=39)],
                        keywords=[],
                        lineno=29,
                        col_offset=16,
                        end_lineno=29,
                        end_col_offset=40),
                      lineno=29,
                      col_offset=16,
                      end_lineno=29,
                      end_col_offset=40)],
                  orelse=[],
                  lineno=28,
                  col_offset=12,
                  end_lineno=29,
                  end_col_offset=40)],
              orelse=[],
              lineno=24,
              col_offset=8,
              end_lineno=29,
              end_col_offset=40),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=30,
                  col_offset=11,
                  end_lineno=30,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=30,
                    col_offset=22,
                    end_lineno=30,
                    end_col_offset=29),
                  Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=30,
                    col_offset=31,
                    end_lineno=30,
                    end_col_offset=43)],
                keywords=[],
                lineno=30,
                col_offset=11,
                end_lineno=30,
                end_col_offset=44),
              body=[
                AnnAssign(
                  target=Name(
                    id='block',
                    ctx=Store(),
                    lineno=31,
                    col_offset=12,
                    end_lineno=31,
                    end_col_offset=17),
                  annotation=Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=31,
                    col_offset=20,
                    end_lineno=31,
                    end_col_offset=32),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=31,
                    col_offset=35,
                    end_lineno=31,
                    end_col_offset=42),
                  simple=1,
                  lineno=31,
                  col_offset=12,
                  end_lineno=31,
                  end_col_offset=42),
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=32,
                        col_offset=12,
                        end_lineno=32,
                        end_col_offset=20),
                      attr='extend',
                      ctx=Load(),
                      lineno=32,
                      col_offset=12,
                      end_lineno=32,
                      end_col_offset=27),
                    args=[
                      Call(
                        func=Name(
                          id='_get_unique_nodes',
                          ctx=Load(),
                          lineno=32,
                          col_offset=28,
                          end_lineno=32,
                          end_col_offset=45),
                        args=[
                          Attribute(
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=32,
                              col_offset=46,
                              end_lineno=32,
                              end_col_offset=51),
                            attr='block_contents',
                            ctx=Load(),
                            lineno=32,
                            col_offset=46,
                            end_lineno=32,
                            end_col_offset=66)],
                        keywords=[],
                        lineno=32,
                        col_offset=28,
                        end_lineno=32,
                        end_col_offset=67)],
                    keywords=[],
                    lineno=32,
                    col_offset=12,
                    end_lineno=32,
                    end_col_offset=68),
                  lineno=32,
                  col_offset=12,
                  end_lineno=32,
                  end_col_offset=68)],
              orelse=[],
              lineno=30,
              col_offset=8,
              end_lineno=32,
              end_col_offset=68)],
          orelse=[],
          lineno=23,
          col_offset=4,
          end_lineno=32,
          end_col_offset=68),
        Return(
          value=Name(
            id='node_set',
            ctx=Load(),
            lineno=33,
            col_offset=11,
            end_lineno=33,
            end_col_offset=19),
          lineno=33,
          col_offset=4,
          end_lineno=33,
          end_col_offset=19)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=20,
          col_offset=57,
          end_lineno=20,
          end_col_offset=61),
        slice=Name(
          id='MermaidNode',
          ctx=Load(),
          lineno=20,
          col_offset=62,
          end_lineno=20,
          end_col_offset=73),
        ctx=Load(),
        lineno=20,
        col_offset=57,
        end_lineno=20,
        end_col_offset=74),
      lineno=20,
      col_offset=0,
      end_lineno=33,
      end_col_offset=19),
    FunctionDef(
      name='_get_aliases_for_safe_names',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=36,
                col_offset=42,
                end_lineno=36,
                end_col_offset=46),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=36,
                col_offset=47,
                end_lineno=36,
                end_col_offset=61),
              ctx=Load(),
              lineno=36,
              col_offset=42,
              end_lineno=36,
              end_col_offset=62),
            lineno=36,
            col_offset=32,
            end_lineno=36,
            end_col_offset=62),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=36,
              col_offset=72,
              end_lineno=36,
              end_col_offset=75),
            lineno=36,
            col_offset=64,
            end_lineno=36,
            end_col_offset=75)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=36,
            col_offset=78,
            end_lineno=36,
            end_col_offset=79)]),
      body=[
        Assign(
          targets=[
            Name(
              id='alias_string',
              ctx=Store(),
              lineno=37,
              col_offset=4,
              end_lineno=37,
              end_col_offset=16)],
          value=Constant(
            value='',
            lineno=37,
            col_offset=19,
            end_lineno=37,
            end_col_offset=21),
          lineno=37,
          col_offset=4,
          end_lineno=37,
          end_col_offset=21),
        For(
          target=Name(
            id='node',
            ctx=Store(),
            lineno=38,
            col_offset=8,
            end_lineno=38,
            end_col_offset=12),
          iter=Call(
            func=Name(
              id='_get_unique_nodes',
              ctx=Load(),
              lineno=38,
              col_offset=16,
              end_lineno=38,
              end_col_offset=33),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=38,
                  col_offset=43,
                  end_lineno=38,
                  end_col_offset=51),
                lineno=38,
                col_offset=34,
                end_lineno=38,
                end_col_offset=51)],
            lineno=38,
            col_offset=16,
            end_lineno=38,
            end_col_offset=52),
          body=[
            AugAssign(
              target=Name(
                id='alias_string',
                ctx=Store(),
                lineno=39,
                col_offset=8,
                end_lineno=39,
                end_col_offset=20),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=39,
                        col_offset=27,
                        end_lineno=39,
                        end_col_offset=30),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=39,
                        col_offset=33,
                        end_lineno=39,
                        end_col_offset=39),
                      lineno=39,
                      col_offset=27,
                      end_lineno=39,
                      end_col_offset=39),
                    conversion=-1,
                    lineno=39,
                    col_offset=24,
                    end_lineno=39,
                    end_col_offset=92),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=39,
                        col_offset=41,
                        end_lineno=39,
                        end_col_offset=45),
                      attr='mermaid_safe_name',
                      ctx=Load(),
                      lineno=39,
                      col_offset=41,
                      end_lineno=39,
                      end_col_offset=63),
                    conversion=-1,
                    lineno=39,
                    col_offset=24,
                    end_lineno=39,
                    end_col_offset=92),
                  Constant(
                    value='["',
                    lineno=39,
                    col_offset=24,
                    end_lineno=39,
                    end_col_offset=92),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=39,
                        col_offset=68,
                        end_lineno=39,
                        end_col_offset=72),
                      attr='display_name',
                      ctx=Load(),
                      lineno=39,
                      col_offset=68,
                      end_lineno=39,
                      end_col_offset=85),
                    conversion=-1,
                    lineno=39,
                    col_offset=24,
                    end_lineno=39,
                    end_col_offset=92),
                  Constant(
                    value='"]\n',
                    lineno=39,
                    col_offset=24,
                    end_lineno=39,
                    end_col_offset=92)],
                lineno=39,
                col_offset=24,
                end_lineno=39,
                end_col_offset=92),
              lineno=39,
              col_offset=8,
              end_lineno=39,
              end_col_offset=92)],
          orelse=[],
          lineno=38,
          col_offset=4,
          end_lineno=39,
          end_col_offset=92),
        Return(
          value=Call(
            func=Name(
              id='_sanitize',
              ctx=Load(),
              lineno=40,
              col_offset=11,
              end_lineno=40,
              end_col_offset=20),
            args=[
              Name(
                id='alias_string',
                ctx=Load(),
                lineno=40,
                col_offset=21,
                end_lineno=40,
                end_col_offset=33)],
            keywords=[],
            lineno=40,
            col_offset=11,
            end_lineno=40,
            end_col_offset=34),
          lineno=40,
          col_offset=4,
          end_lineno=40,
          end_col_offset=34)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=36,
        col_offset=84,
        end_lineno=36,
        end_col_offset=87),
      lineno=36,
      col_offset=0,
      end_lineno=40,
      end_col_offset=34),
    FunctionDef(
      name='_get_flow_link_text',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='link',
            annotation=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=43,
              col_offset=30,
              end_lineno=43,
              end_col_offset=44),
            lineno=43,
            col_offset=24,
            end_lineno=43,
            end_col_offset=44),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=43,
              col_offset=54,
              end_lineno=43,
              end_col_offset=57),
            lineno=43,
            col_offset=46,
            end_lineno=43,
            end_col_offset=57)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='from_name',
              ctx=Store(),
              lineno=44,
              col_offset=4,
              end_lineno=44,
              end_col_offset=13)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=44,
                col_offset=16,
                end_lineno=44,
                end_col_offset=20),
              attr='from_',
              ctx=Load(),
              lineno=44,
              col_offset=16,
              end_lineno=44,
              end_col_offset=26),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=44,
            col_offset=16,
            end_lineno=44,
            end_col_offset=44),
          lineno=44,
          col_offset=4,
          end_lineno=44,
          end_col_offset=44),
        Assign(
          targets=[
            Name(
              id='to_name',
              ctx=Store(),
              lineno=45,
              col_offset=4,
              end_lineno=45,
              end_col_offset=11)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=45,
                col_offset=14,
                end_lineno=45,
                end_col_offset=18),
              attr='to',
              ctx=Load(),
              lineno=45,
              col_offset=14,
              end_lineno=45,
              end_col_offset=21),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=45,
            col_offset=14,
            end_lineno=45,
            end_col_offset=39),
          lineno=45,
          col_offset=4,
          end_lineno=45,
          end_col_offset=39),
        Return(
          value=JoinedStr(
            values=[
              FormattedValue(
                value=BinOp(
                  left=Name(
                    id='TAB',
                    ctx=Load(),
                    lineno=47,
                    col_offset=14,
                    end_lineno=47,
                    end_col_offset=17),
                  op=Mult(),
                  right=Name(
                    id='indent',
                    ctx=Load(),
                    lineno=47,
                    col_offset=18,
                    end_lineno=47,
                    end_col_offset=24),
                  lineno=47,
                  col_offset=14,
                  end_lineno=47,
                  end_col_offset=24),
                conversion=-1,
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='from_name',
                  ctx=Load(),
                  lineno=47,
                  col_offset=26,
                  end_lineno=47,
                  end_col_offset=35),
                conversion=-1,
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=53),
              Constant(
                value=' --> ',
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='to_name',
                  ctx=Load(),
                  lineno=47,
                  col_offset=42,
                  end_lineno=47,
                  end_col_offset=49),
                conversion=-1,
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=53),
              Constant(
                value='\n',
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=53)],
            lineno=47,
            col_offset=11,
            end_lineno=47,
            end_col_offset=53),
          lineno=47,
          col_offset=4,
          end_lineno=47,
          end_col_offset=53)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=43,
        col_offset=62,
        end_lineno=43,
        end_col_offset=65),
      lineno=43,
      col_offset=0,
      end_lineno=47,
      end_col_offset=53),
    FunctionDef(
      name='_get_flow_connections',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=50,
                col_offset=36,
                end_lineno=50,
                end_col_offset=40),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=50,
                col_offset=41,
                end_lineno=50,
                end_col_offset=55),
              ctx=Load(),
              lineno=50,
              col_offset=36,
              end_lineno=50,
              end_col_offset=56),
            lineno=50,
            col_offset=26,
            end_lineno=50,
            end_col_offset=56),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=50,
              col_offset=66,
              end_lineno=50,
              end_col_offset=69),
            lineno=50,
            col_offset=58,
            end_lineno=50,
            end_col_offset=69)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=50,
            col_offset=72,
            end_lineno=50,
            end_col_offset=73)]),
      body=[
        Assign(
          targets=[
            Name(
              id='connection_text',
              ctx=Store(),
              lineno=51,
              col_offset=4,
              end_lineno=51,
              end_col_offset=19)],
          value=Constant(
            value='',
            lineno=51,
            col_offset=22,
            end_lineno=51,
            end_col_offset=24),
          lineno=51,
          col_offset=4,
          end_lineno=51,
          end_col_offset=24),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=52,
            col_offset=8,
            end_lineno=52,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=52,
            col_offset=19,
            end_lineno=52,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=53,
                  col_offset=11,
                  end_lineno=53,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=53,
                    col_offset=22,
                    end_lineno=53,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=53,
                    col_offset=31,
                    end_lineno=53,
                    end_col_offset=42)],
                keywords=[],
                lineno=53,
                col_offset=11,
                end_lineno=53,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=54,
                    col_offset=12,
                    end_lineno=54,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=54,
                    col_offset=18,
                    end_lineno=54,
                    end_col_offset=29),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=54,
                    col_offset=32,
                    end_lineno=54,
                    end_col_offset=39),
                  simple=1,
                  lineno=54,
                  col_offset=12,
                  end_lineno=54,
                  end_col_offset=39),
                AugAssign(
                  target=Name(
                    id='connection_text',
                    ctx=Store(),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=27),
                  op=Add(),
                  value=Call(
                    func=Name(
                      id='_get_flow_link_text',
                      ctx=Load(),
                      lineno=55,
                      col_offset=31,
                      end_lineno=55,
                      end_col_offset=50),
                    args=[],
                    keywords=[
                      keyword(
                        arg='link',
                        value=Name(
                          id='link',
                          ctx=Load(),
                          lineno=55,
                          col_offset=56,
                          end_lineno=55,
                          end_col_offset=60),
                        lineno=55,
                        col_offset=51,
                        end_lineno=55,
                        end_col_offset=60),
                      keyword(
                        arg='indent',
                        value=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=55,
                          col_offset=69,
                          end_lineno=55,
                          end_col_offset=75),
                        lineno=55,
                        col_offset=62,
                        end_lineno=55,
                        end_col_offset=75)],
                    lineno=55,
                    col_offset=31,
                    end_lineno=55,
                    end_col_offset=76),
                  lineno=55,
                  col_offset=12,
                  end_lineno=55,
                  end_col_offset=76)],
              orelse=[
                If(
                  test=Call(
                    func=Name(
                      id='isinstance',
                      ctx=Load(),
                      lineno=56,
                      col_offset=13,
                      end_lineno=56,
                      end_col_offset=23),
                    args=[
                      Name(
                        id='element',
                        ctx=Load(),
                        lineno=56,
                        col_offset=24,
                        end_lineno=56,
                        end_col_offset=31),
                      Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=56,
                        col_offset=33,
                        end_lineno=56,
                        end_col_offset=45)],
                    keywords=[],
                    lineno=56,
                    col_offset=13,
                    end_lineno=56,
                    end_col_offset=46),
                  body=[
                    AnnAssign(
                      target=Name(
                        id='block',
                        ctx=Store(),
                        lineno=57,
                        col_offset=12,
                        end_lineno=57,
                        end_col_offset=17),
                      annotation=Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=57,
                        col_offset=19,
                        end_lineno=57,
                        end_col_offset=31),
                      value=Name(
                        id='element',
                        ctx=Load(),
                        lineno=57,
                        col_offset=34,
                        end_lineno=57,
                        end_col_offset=41),
                      simple=1,
                      lineno=57,
                      col_offset=12,
                      end_lineno=57,
                      end_col_offset=41),
                    AugAssign(
                      target=Name(
                        id='connection_text',
                        ctx=Store(),
                        lineno=58,
                        col_offset=12,
                        end_lineno=58,
                        end_col_offset=27),
                      op=Add(),
                      value=Call(
                        func=Name(
                          id='_get_block_text',
                          ctx=Load(),
                          lineno=58,
                          col_offset=31,
                          end_lineno=58,
                          end_col_offset=46),
                        args=[],
                        keywords=[
                          keyword(
                            arg='block',
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=58,
                              col_offset=53,
                              end_lineno=58,
                              end_col_offset=58),
                            lineno=58,
                            col_offset=47,
                            end_lineno=58,
                            end_col_offset=58),
                          keyword(
                            arg='indent',
                            value=Name(
                              id='indent',
                              ctx=Load(),
                              lineno=58,
                              col_offset=67,
                              end_lineno=58,
                              end_col_offset=73),
                            lineno=58,
                            col_offset=60,
                            end_lineno=58,
                            end_col_offset=73)],
                        lineno=58,
                        col_offset=31,
                        end_lineno=58,
                        end_col_offset=74),
                      lineno=58,
                      col_offset=12,
                      end_lineno=58,
                      end_col_offset=74)],
                  orelse=[],
                  lineno=56,
                  col_offset=8,
                  end_lineno=58,
                  end_col_offset=74)],
              lineno=53,
              col_offset=8,
              end_lineno=58,
              end_col_offset=74)],
          orelse=[],
          lineno=52,
          col_offset=4,
          end_lineno=58,
          end_col_offset=74),
        Return(
          value=Name(
            id='connection_text',
            ctx=Load(),
            lineno=60,
            col_offset=11,
            end_lineno=60,
            end_col_offset=26),
          lineno=60,
          col_offset=4,
          end_lineno=60,
          end_col_offset=26)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=50,
        col_offset=78,
        end_lineno=50,
        end_col_offset=81),
      lineno=50,
      col_offset=0,
      end_lineno=60,
      end_col_offset=26),
    FunctionDef(
      name='_get_block_text',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='block',
            annotation=Name(
              id='MermaidBlock',
              ctx=Load(),
              lineno=63,
              col_offset=27,
              end_lineno=63,
              end_col_offset=39),
            lineno=63,
            col_offset=20,
            end_lineno=63,
            end_col_offset=39),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=63,
              col_offset=49,
              end_lineno=63,
              end_col_offset=52),
            lineno=63,
            col_offset=41,
            end_lineno=63,
            end_col_offset=52)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='block_text',
              ctx=Store(),
              lineno=64,
              col_offset=4,
              end_lineno=64,
              end_col_offset=14)],
          value=Constant(
            value='',
            lineno=64,
            col_offset=17,
            end_lineno=64,
            end_col_offset=19),
          lineno=64,
          col_offset=4,
          end_lineno=64,
          end_col_offset=19),
        If(
          test=Call(
            func=Name(
              id='isinstance',
              ctx=Load(),
              lineno=65,
              col_offset=7,
              end_lineno=65,
              end_col_offset=17),
            args=[
              Name(
                id='block',
                ctx=Load(),
                lineno=65,
                col_offset=18,
                end_lineno=65,
                end_col_offset=23),
              Name(
                id='MermaidFunction',
                ctx=Load(),
                lineno=65,
                col_offset=25,
                end_lineno=65,
                end_col_offset=40)],
            keywords=[],
            lineno=65,
            col_offset=7,
            end_lineno=65,
            end_col_offset=41),
          body=[
            AnnAssign(
              target=Name(
                id='function_def',
                ctx=Store(),
                lineno=66,
                col_offset=8,
                end_lineno=66,
                end_col_offset=20),
              annotation=Name(
                id='MermaidFunction',
                ctx=Load(),
                lineno=66,
                col_offset=23,
                end_lineno=66,
                end_col_offset=38),
              value=Name(
                id='block',
                ctx=Load(),
                lineno=66,
                col_offset=41,
                end_lineno=66,
                end_col_offset=46),
              simple=1,
              lineno=66,
              col_offset=8,
              end_lineno=66,
              end_col_offset=46),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=67,
                col_offset=8,
                end_lineno=67,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=67,
                        col_offset=25,
                        end_lineno=67,
                        end_col_offset=28),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=67,
                        col_offset=31,
                        end_lineno=67,
                        end_col_offset=37),
                      lineno=67,
                      col_offset=25,
                      end_lineno=67,
                      end_col_offset=37),
                    conversion=-1,
                    lineno=67,
                    col_offset=22,
                    end_lineno=67,
                    end_col_offset=77),
                  Constant(
                    value='subgraph ',
                    lineno=67,
                    col_offset=22,
                    end_lineno=67,
                    end_col_offset=77),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='function_def',
                        ctx=Load(),
                        lineno=67,
                        col_offset=48,
                        end_lineno=67,
                        end_col_offset=60),
                      attr='display_name',
                      ctx=Load(),
                      lineno=67,
                      col_offset=48,
                      end_lineno=67,
                      end_col_offset=73),
                    conversion=-1,
                    lineno=67,
                    col_offset=22,
                    end_lineno=67,
                    end_col_offset=77),
                  Constant(
                    value='\n',
                    lineno=67,
                    col_offset=22,
                    end_lineno=67,
                    end_col_offset=77)],
                lineno=67,
                col_offset=22,
                end_lineno=67,
                end_col_offset=77),
              lineno=67,
              col_offset=8,
              end_lineno=67,
              end_col_offset=77),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=68,
                col_offset=8,
                end_lineno=68,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=68,
                        col_offset=25,
                        end_lineno=68,
                        end_col_offset=28),
                      op=Mult(),
                      right=BinOp(
                        left=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=68,
                          col_offset=32,
                          end_lineno=68,
                          end_col_offset=38),
                        op=Add(),
                        right=Constant(
                          value=1,
                          lineno=68,
                          col_offset=41,
                          end_lineno=68,
                          end_col_offset=42),
                        lineno=68,
                        col_offset=32,
                        end_lineno=68,
                        end_col_offset=42),
                      lineno=68,
                      col_offset=25,
                      end_lineno=68,
                      end_col_offset=43),
                    conversion=-1,
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=59),
                  Constant(
                    value='direction TB\n',
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=59)],
                lineno=68,
                col_offset=22,
                end_lineno=68,
                end_col_offset=59),
              lineno=68,
              col_offset=8,
              end_lineno=68,
              end_col_offset=59),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=18),
              op=Add(),
              value=Call(
                func=Name(
                  id='_get_flow_connections',
                  ctx=Load(),
                  lineno=69,
                  col_offset=22,
                  end_lineno=69,
                  end_col_offset=43),
                args=[
                  Attribute(
                    value=Name(
                      id='function_def',
                      ctx=Load(),
                      lineno=69,
                      col_offset=44,
                      end_lineno=69,
                      end_col_offset=56),
                    attr='block_contents',
                    ctx=Load(),
                    lineno=69,
                    col_offset=44,
                    end_lineno=69,
                    end_col_offset=71),
                  BinOp(
                    left=Name(
                      id='indent',
                      ctx=Load(),
                      lineno=69,
                      col_offset=73,
                      end_lineno=69,
                      end_col_offset=79),
                    op=Add(),
                    right=Constant(
                      value=1,
                      lineno=69,
                      col_offset=82,
                      end_lineno=69,
                      end_col_offset=83),
                    lineno=69,
                    col_offset=73,
                    end_lineno=69,
                    end_col_offset=83)],
                keywords=[],
                lineno=69,
                col_offset=22,
                end_lineno=69,
                end_col_offset=84),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=84),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=70,
                col_offset=8,
                end_lineno=70,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=70,
                        col_offset=25,
                        end_lineno=70,
                        end_col_offset=28),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=70,
                        col_offset=31,
                        end_lineno=70,
                        end_col_offset=37),
                      lineno=70,
                      col_offset=25,
                      end_lineno=70,
                      end_col_offset=37),
                    conversion=-1,
                    lineno=70,
                    col_offset=22,
                    end_lineno=70,
                    end_col_offset=44),
                  Constant(
                    value='end\n',
                    lineno=70,
                    col_offset=22,
                    end_lineno=70,
                    end_col_offset=44)],
                lineno=70,
                col_offset=22,
                end_lineno=70,
                end_col_offset=44),
              lineno=70,
              col_offset=8,
              end_lineno=70,
              end_col_offset=44)],
          orelse=[
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=72,
                col_offset=8,
                end_lineno=72,
                end_col_offset=18),
              op=Add(),
              value=Call(
                func=Name(
                  id='_get_flow_connections',
                  ctx=Load(),
                  lineno=72,
                  col_offset=22,
                  end_lineno=72,
                  end_col_offset=43),
                args=[
                  Attribute(
                    value=Name(
                      id='block',
                      ctx=Load(),
                      lineno=72,
                      col_offset=44,
                      end_lineno=72,
                      end_col_offset=49),
                    attr='block_contents',
                    ctx=Load(),
                    lineno=72,
                    col_offset=44,
                    end_lineno=72,
                    end_col_offset=64),
                  Name(
                    id='indent',
                    ctx=Load(),
                    lineno=72,
                    col_offset=66,
                    end_lineno=72,
                    end_col_offset=72)],
                keywords=[],
                lineno=72,
                col_offset=22,
                end_lineno=72,
                end_col_offset=73),
              lineno=72,
              col_offset=8,
              end_lineno=72,
              end_col_offset=73)],
          lineno=65,
          col_offset=4,
          end_lineno=72,
          end_col_offset=73),
        Return(
          value=Name(
            id='block_text',
            ctx=Load(),
            lineno=73,
            col_offset=11,
            end_lineno=73,
            end_col_offset=21),
          lineno=73,
          col_offset=4,
          end_lineno=73,
          end_col_offset=21)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=63,
        col_offset=57,
        end_lineno=63,
        end_col_offset=60),
      lineno=63,
      col_offset=0,
      end_lineno=73,
      end_col_offset=21),
    FunctionDef(
      name='create_mermaid_flow_graph_from_links',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=76,
                col_offset=51,
                end_lineno=76,
                end_col_offset=55),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=76,
                col_offset=56,
                end_lineno=76,
                end_col_offset=70),
              ctx=Load(),
              lineno=76,
              col_offset=51,
              end_lineno=76,
              end_col_offset=71),
            lineno=76,
            col_offset=41,
            end_lineno=76,
            end_col_offset=71)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='alaises',
              ctx=Store(),
              lineno=77,
              col_offset=4,
              end_lineno=77,
              end_col_offset=11)],
          value=Call(
            func=Name(
              id='_get_aliases_for_safe_names',
              ctx=Load(),
              lineno=77,
              col_offset=14,
              end_lineno=77,
              end_col_offset=41),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=77,
                  col_offset=51,
                  end_lineno=77,
                  end_col_offset=59),
                lineno=77,
                col_offset=42,
                end_lineno=77,
                end_col_offset=59)],
            lineno=77,
            col_offset=14,
            end_lineno=77,
            end_col_offset=60),
          lineno=77,
          col_offset=4,
          end_lineno=77,
          end_col_offset=60),
        Assign(
          targets=[
            Name(
              id='flow_connections',
              ctx=Store(),
              lineno=78,
              col_offset=4,
              end_lineno=78,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_get_flow_connections',
              ctx=Load(),
              lineno=78,
              col_offset=23,
              end_lineno=78,
              end_col_offset=44),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=78,
                  col_offset=54,
                  end_lineno=78,
                  end_col_offset=62),
                lineno=78,
                col_offset=45,
                end_lineno=78,
                end_col_offset=62)],
            lineno=78,
            col_offset=23,
            end_lineno=78,
            end_col_offset=63),
          lineno=78,
          col_offset=4,
          end_lineno=78,
          end_col_offset=63),
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='```mermaid\nflowchart TB\n',
                lineno=80,
                col_offset=8,
                end_lineno=84,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='alaises',
                  ctx=Load(),
                  lineno=82,
                  col_offset=11,
                  end_lineno=82,
                  end_col_offset=18),
                conversion=-1,
                lineno=80,
                col_offset=8,
                end_lineno=84,
                end_col_offset=15),
              Constant(
                value='\n',
                lineno=80,
                col_offset=8,
                end_lineno=84,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='flow_connections',
                  ctx=Load(),
                  lineno=83,
                  col_offset=11,
                  end_lineno=83,
                  end_col_offset=27),
                conversion=-1,
                lineno=80,
                col_offset=8,
                end_lineno=84,
                end_col_offset=15),
              Constant(
                value='\n```\n',
                lineno=80,
                col_offset=8,
                end_lineno=84,
                end_col_offset=15)],
            lineno=80,
            col_offset=8,
            end_lineno=84,
            end_col_offset=15),
          lineno=79,
          col_offset=4,
          end_lineno=85,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=76,
        col_offset=76,
        end_lineno=76,
        end_col_offset=79),
      lineno=76,
      col_offset=0,
      end_lineno=85,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

