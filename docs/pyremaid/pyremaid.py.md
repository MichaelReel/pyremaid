# ./src/pyremaid/pyremaid.py

### Imports

  - files.destination.create_cleared_output_folder
  - files.destination.get_output_file_path_for_input_file
  - files.destination.update_output_file
  - files.source.find_all_python_files
  - files.source.get_source_code_from_file
  - files.source.get_import_name_from_path
  - ast_tools.create_mermaid_model_from_ast_model
  - ast_tools.get_ast_root_node_for_file
  - ast_tools.get_markdown_dump_for_ast_node
  - ast_tools.get_used_import_list
  - ast_tools.import_map.get_all_imports_from_files
  - markdown_tools.create_markdown_content
  - mermaid_tools.create_mermaid_flow_graph_from_links
  - models.MermaidElement

---
```mermaid
flowchart TB
  _create_mermaid_analysis_from_python_node_0["Expr"]
  _create_mermaid_analysis_from_python_node_1["Call"]
  _create_mermaid_analysis_from_python_node_2["Name"]
  _create_mermaid_analysis_from_python_node_3["Load"]
  _create_mermaid_analysis_from_python_node_4["keyword"]
  _create_mermaid_analysis_from_python_node_5["Name"]
  _create_mermaid_analysis_from_python_node_6["Load"]
  _create_mermaid_analysis_from_python_node_7["Assign"]
  _create_mermaid_analysis_from_python_node_8["Name"]
  _create_mermaid_analysis_from_python_node_9["Store"]
  _create_mermaid_analysis_from_python_node_10["Call"]
  _create_mermaid_analysis_from_python_node_11["Name"]
  _create_mermaid_analysis_from_python_node_12["Load"]
  _create_mermaid_analysis_from_python_node_13["keyword"]
  _create_mermaid_analysis_from_python_node_14["Name"]
  _create_mermaid_analysis_from_python_node_15["Load"]
  _create_mermaid_analysis_from_python_node_16["Assign"]
  _create_mermaid_analysis_from_python_node_17["Name"]
  _create_mermaid_analysis_from_python_node_18["Store"]
  _create_mermaid_analysis_from_python_node_19["Call"]
  _create_mermaid_analysis_from_python_node_20["Name"]
  _create_mermaid_analysis_from_python_node_21["Load"]
  _create_mermaid_analysis_from_python_node_22["keyword"]
  _create_mermaid_analysis_from_python_node_23["Name"]
  _create_mermaid_analysis_from_python_node_24["Load"]
  _create_mermaid_analysis_from_python_node_25["keyword"]
  _create_mermaid_analysis_from_python_node_26["Name"]
  _create_mermaid_analysis_from_python_node_27["Load"]
  _create_mermaid_analysis_from_python_node_28["Expr"]
  _create_mermaid_analysis_from_python_node_29["Call"]
  _create_mermaid_analysis_from_python_node_30["Name"]
  _create_mermaid_analysis_from_python_node_31["Load"]
  _create_mermaid_analysis_from_python_node_32["Call"]
  _create_mermaid_analysis_from_python_node_33["Attribute"]
  _create_mermaid_analysis_from_python_node_34["Constant"]
  _create_mermaid_analysis_from_python_node_35["Load"]
  _create_mermaid_analysis_from_python_node_36["ListComp"]
  _create_mermaid_analysis_from_python_node_37["JoinedStr"]
  _create_mermaid_analysis_from_python_node_38["FormattedValue"]
  _create_mermaid_analysis_from_python_node_39["Name"]
  _create_mermaid_analysis_from_python_node_40["Load"]
  _create_mermaid_analysis_from_python_node_41["Constant"]
  _create_mermaid_analysis_from_python_node_42["FormattedValue"]
  _create_mermaid_analysis_from_python_node_43["Name"]
  _create_mermaid_analysis_from_python_node_44["Load"]
  _create_mermaid_analysis_from_python_node_45["comprehension"]
  _create_mermaid_analysis_from_python_node_46["Tuple"]
  _create_mermaid_analysis_from_python_node_47["Name"]
  _create_mermaid_analysis_from_python_node_48["Store"]
  _create_mermaid_analysis_from_python_node_49["Name"]
  _create_mermaid_analysis_from_python_node_50["Store"]
  _create_mermaid_analysis_from_python_node_51["Store"]
  _create_mermaid_analysis_from_python_node_52["Call"]
  _create_mermaid_analysis_from_python_node_53["Attribute"]
  _create_mermaid_analysis_from_python_node_54["Name"]
  _create_mermaid_analysis_from_python_node_55["Load"]
  _create_mermaid_analysis_from_python_node_56["Load"]
  _create_mermaid_analysis_from_python_node_57["For"]
  _create_mermaid_analysis_from_python_node_58["Name"]
  _create_mermaid_analysis_from_python_node_59["Store"]
  _create_mermaid_analysis_from_python_node_60["Name"]
  _create_mermaid_analysis_from_python_node_61["Load"]
  _create_mermaid_analysis_from_python_node_62["Assign"]
  _create_mermaid_analysis_from_python_node_63["Name"]
  _create_mermaid_analysis_from_python_node_64["Store"]
  _create_mermaid_analysis_from_python_node_65["Call"]
  _create_mermaid_analysis_from_python_node_66["Attribute"]
  _create_mermaid_analysis_from_python_node_67["Name"]
  _create_mermaid_analysis_from_python_node_68["Load"]
  _create_mermaid_analysis_from_python_node_69["Load"]
  _create_mermaid_analysis_from_python_node_70["Name"]
  _create_mermaid_analysis_from_python_node_71["Load"]
  _create_mermaid_analysis_from_python_node_72["Constant"]
  _create_mermaid_analysis_from_python_node_73["Assign"]
  _create_mermaid_analysis_from_python_node_74["Name"]
  _create_mermaid_analysis_from_python_node_75["Store"]
  _create_mermaid_analysis_from_python_node_76["Call"]
  _create_mermaid_analysis_from_python_node_77["Name"]
  _create_mermaid_analysis_from_python_node_78["Load"]
  _create_mermaid_analysis_from_python_node_79["keyword"]
  _create_mermaid_analysis_from_python_node_80["Name"]
  _create_mermaid_analysis_from_python_node_81["Load"]
  _create_mermaid_analysis_from_python_node_82["keyword"]
  _create_mermaid_analysis_from_python_node_83["Name"]
  _create_mermaid_analysis_from_python_node_84["Load"]
  _create_mermaid_analysis_from_python_node_85["Assign"]
  _create_mermaid_analysis_from_python_node_86["Name"]
  _create_mermaid_analysis_from_python_node_87["Store"]
  _create_mermaid_analysis_from_python_node_88["Constant"]
  _create_mermaid_analysis_from_python_node_89["Assign"]
  _create_mermaid_analysis_from_python_node_90["Name"]
  _create_mermaid_analysis_from_python_node_91["Store"]
  _create_mermaid_analysis_from_python_node_92["List"]
  _create_mermaid_analysis_from_python_node_93["Load"]
  _create_mermaid_analysis_from_python_node_94["If"]
  _create_mermaid_analysis_from_python_node_95["NamedExpr"]
  _create_mermaid_analysis_from_python_node_96["Name"]
  _create_mermaid_analysis_from_python_node_97["Store"]
  _create_mermaid_analysis_from_python_node_98["Call"]
  _create_mermaid_analysis_from_python_node_99["Name"]
  _create_mermaid_analysis_from_python_node_100["Load"]
  _create_mermaid_analysis_from_python_node_101["keyword"]
  _create_mermaid_analysis_from_python_node_102["Name"]
  _create_mermaid_analysis_from_python_node_103["Load"]
  _create_mermaid_analysis_from_python_node_104["If"]
  _create_mermaid_analysis_from_python_node_105["NamedExpr"]
  _create_mermaid_analysis_from_python_node_106["Name"]
  _create_mermaid_analysis_from_python_node_107["Store"]
  _create_mermaid_analysis_from_python_node_108["Call"]
  _create_mermaid_analysis_from_python_node_109["Name"]
  _create_mermaid_analysis_from_python_node_110["Load"]
  _create_mermaid_analysis_from_python_node_111["keyword"]
  _create_mermaid_analysis_from_python_node_112["Name"]
  _create_mermaid_analysis_from_python_node_113["Load"]
  _create_mermaid_analysis_from_python_node_114["keyword"]
  _create_mermaid_analysis_from_python_node_115["Name"]
  _create_mermaid_analysis_from_python_node_116["Load"]
  _create_mermaid_analysis_from_python_node_117["Assign"]
  _create_mermaid_analysis_from_python_node_118["Name"]
  _create_mermaid_analysis_from_python_node_119["Store"]
  _create_mermaid_analysis_from_python_node_120["Call"]
  _create_mermaid_analysis_from_python_node_121["Name"]
  _create_mermaid_analysis_from_python_node_122["Load"]
  _create_mermaid_analysis_from_python_node_123["keyword"]
  _create_mermaid_analysis_from_python_node_124["Name"]
  _create_mermaid_analysis_from_python_node_125["Load"]
  _create_mermaid_analysis_from_python_node_126["Assign"]
  _create_mermaid_analysis_from_python_node_127["Name"]
  _create_mermaid_analysis_from_python_node_128["Store"]
  _create_mermaid_analysis_from_python_node_129["Call"]
  _create_mermaid_analysis_from_python_node_130["Name"]
  _create_mermaid_analysis_from_python_node_131["Load"]
  _create_mermaid_analysis_from_python_node_132["keyword"]
  _create_mermaid_analysis_from_python_node_133["Name"]
  _create_mermaid_analysis_from_python_node_134["Load"]
  _create_mermaid_analysis_from_python_node_135["AnnAssign"]
  _create_mermaid_analysis_from_python_node_136["Name"]
  _create_mermaid_analysis_from_python_node_137["Store"]
  _create_mermaid_analysis_from_python_node_138["Subscript"]
  _create_mermaid_analysis_from_python_node_139["Name"]
  _create_mermaid_analysis_from_python_node_140["Load"]
  _create_mermaid_analysis_from_python_node_141["Name"]
  _create_mermaid_analysis_from_python_node_142["Load"]
  _create_mermaid_analysis_from_python_node_143["Load"]
  _create_mermaid_analysis_from_python_node_144["Call"]
  _create_mermaid_analysis_from_python_node_145["Name"]
  _create_mermaid_analysis_from_python_node_146["Load"]
  _create_mermaid_analysis_from_python_node_147["keyword"]
  _create_mermaid_analysis_from_python_node_148["Name"]
  _create_mermaid_analysis_from_python_node_149["Load"]
  _create_mermaid_analysis_from_python_node_150["Assign"]
  _create_mermaid_analysis_from_python_node_151["Name"]
  _create_mermaid_analysis_from_python_node_152["Store"]
  _create_mermaid_analysis_from_python_node_153["Call"]
  _create_mermaid_analysis_from_python_node_154["Name"]
  _create_mermaid_analysis_from_python_node_155["Load"]
  _create_mermaid_analysis_from_python_node_156["Name"]
  _create_mermaid_analysis_from_python_node_157["Load"]
  _create_mermaid_analysis_from_python_node_158["Assign"]
  _create_mermaid_analysis_from_python_node_159["Name"]
  _create_mermaid_analysis_from_python_node_160["Store"]
  _create_mermaid_analysis_from_python_node_161["Call"]
  _create_mermaid_analysis_from_python_node_162["Name"]
  _create_mermaid_analysis_from_python_node_163["Load"]
  _create_mermaid_analysis_from_python_node_164["keyword"]
  _create_mermaid_analysis_from_python_node_165["Name"]
  _create_mermaid_analysis_from_python_node_166["Load"]
  _create_mermaid_analysis_from_python_node_167["keyword"]
  _create_mermaid_analysis_from_python_node_168["Name"]
  _create_mermaid_analysis_from_python_node_169["Load"]
  _create_mermaid_analysis_from_python_node_170["keyword"]
  _create_mermaid_analysis_from_python_node_171["List"]
  _create_mermaid_analysis_from_python_node_172["Name"]
  _create_mermaid_analysis_from_python_node_173["Load"]
  _create_mermaid_analysis_from_python_node_174["Load"]
  _create_mermaid_analysis_from_python_node_175["keyword"]
  _create_mermaid_analysis_from_python_node_176["Name"]
  _create_mermaid_analysis_from_python_node_177["Load"]
  _create_mermaid_analysis_from_python_node_178["Expr"]
  _create_mermaid_analysis_from_python_node_179["Call"]
  _create_mermaid_analysis_from_python_node_180["Name"]
  _create_mermaid_analysis_from_python_node_181["Load"]
  _create_mermaid_analysis_from_python_node_182["keyword"]
  _create_mermaid_analysis_from_python_node_183["Name"]
  _create_mermaid_analysis_from_python_node_184["Load"]
  _create_mermaid_analysis_from_python_node_185["keyword"]
  _create_mermaid_analysis_from_python_node_186["Name"]
  _create_mermaid_analysis_from_python_node_187["Load"]
  _node_0["If"]
  _node_1["Compare"]
  _node_2["Name"]
  _node_3["Load"]
  _node_4["Eq"]
  _node_5["Constant"]
  _node_6["Assign"]
  _node_7["Name"]
  _node_8["Store"]
  _node_9["Constant"]
  _node_10["Assign"]
  _node_11["Name"]
  _node_12["Store"]
  _node_13["Constant"]
  _node_14["Expr"]
  _node_15["Call"]
  _node_16["Name"]
  _node_17["Load"]
  _node_18["keyword"]
  _node_19["Name"]
  _node_20["Load"]
  _node_21["keyword"]
  _node_22["Name"]
  _node_23["Load"]

  subgraph create_mermaid_analysis_from_python
    direction TB
    _create_mermaid_analysis_from_python_node_0 --> _create_mermaid_analysis_from_python_node_1
    _create_mermaid_analysis_from_python_node_1 --> _create_mermaid_analysis_from_python_node_2
    _create_mermaid_analysis_from_python_node_2 --> _create_mermaid_analysis_from_python_node_3
    _create_mermaid_analysis_from_python_node_3 --> _create_mermaid_analysis_from_python_node_4
    _create_mermaid_analysis_from_python_node_4 --> _create_mermaid_analysis_from_python_node_5
    _create_mermaid_analysis_from_python_node_5 --> _create_mermaid_analysis_from_python_node_6
    _create_mermaid_analysis_from_python_node_6 --> _create_mermaid_analysis_from_python_node_7
    _create_mermaid_analysis_from_python_node_7 --> _create_mermaid_analysis_from_python_node_8
    _create_mermaid_analysis_from_python_node_8 --> _create_mermaid_analysis_from_python_node_9
    _create_mermaid_analysis_from_python_node_9 --> _create_mermaid_analysis_from_python_node_10
    _create_mermaid_analysis_from_python_node_10 --> _create_mermaid_analysis_from_python_node_11
    _create_mermaid_analysis_from_python_node_11 --> _create_mermaid_analysis_from_python_node_12
    _create_mermaid_analysis_from_python_node_12 --> _create_mermaid_analysis_from_python_node_13
    _create_mermaid_analysis_from_python_node_13 --> _create_mermaid_analysis_from_python_node_14
    _create_mermaid_analysis_from_python_node_14 --> _create_mermaid_analysis_from_python_node_15
    _create_mermaid_analysis_from_python_node_15 --> _create_mermaid_analysis_from_python_node_16
    _create_mermaid_analysis_from_python_node_16 --> _create_mermaid_analysis_from_python_node_17
    _create_mermaid_analysis_from_python_node_17 --> _create_mermaid_analysis_from_python_node_18
    _create_mermaid_analysis_from_python_node_18 --> _create_mermaid_analysis_from_python_node_19
    _create_mermaid_analysis_from_python_node_19 --> _create_mermaid_analysis_from_python_node_20
    _create_mermaid_analysis_from_python_node_20 --> _create_mermaid_analysis_from_python_node_21
    _create_mermaid_analysis_from_python_node_21 --> _create_mermaid_analysis_from_python_node_22
    _create_mermaid_analysis_from_python_node_22 --> _create_mermaid_analysis_from_python_node_23
    _create_mermaid_analysis_from_python_node_23 --> _create_mermaid_analysis_from_python_node_24
    _create_mermaid_analysis_from_python_node_24 --> _create_mermaid_analysis_from_python_node_25
    _create_mermaid_analysis_from_python_node_25 --> _create_mermaid_analysis_from_python_node_26
    _create_mermaid_analysis_from_python_node_26 --> _create_mermaid_analysis_from_python_node_27
    _create_mermaid_analysis_from_python_node_27 --> _create_mermaid_analysis_from_python_node_28
    _create_mermaid_analysis_from_python_node_28 --> _create_mermaid_analysis_from_python_node_29
    _create_mermaid_analysis_from_python_node_29 --> _create_mermaid_analysis_from_python_node_30
    _create_mermaid_analysis_from_python_node_30 --> _create_mermaid_analysis_from_python_node_31
    _create_mermaid_analysis_from_python_node_31 --> _create_mermaid_analysis_from_python_node_32
    _create_mermaid_analysis_from_python_node_32 --> _create_mermaid_analysis_from_python_node_33
    _create_mermaid_analysis_from_python_node_33 --> _create_mermaid_analysis_from_python_node_34
    _create_mermaid_analysis_from_python_node_34 --> _create_mermaid_analysis_from_python_node_35
    _create_mermaid_analysis_from_python_node_35 --> _create_mermaid_analysis_from_python_node_36
    _create_mermaid_analysis_from_python_node_36 --> _create_mermaid_analysis_from_python_node_37
    _create_mermaid_analysis_from_python_node_37 --> _create_mermaid_analysis_from_python_node_38
    _create_mermaid_analysis_from_python_node_38 --> _create_mermaid_analysis_from_python_node_39
    _create_mermaid_analysis_from_python_node_39 --> _create_mermaid_analysis_from_python_node_40
    _create_mermaid_analysis_from_python_node_40 --> _create_mermaid_analysis_from_python_node_41
    _create_mermaid_analysis_from_python_node_41 --> _create_mermaid_analysis_from_python_node_42
    _create_mermaid_analysis_from_python_node_42 --> _create_mermaid_analysis_from_python_node_43
    _create_mermaid_analysis_from_python_node_43 --> _create_mermaid_analysis_from_python_node_44
    _create_mermaid_analysis_from_python_node_44 --> _create_mermaid_analysis_from_python_node_45
    _create_mermaid_analysis_from_python_node_45 --> _create_mermaid_analysis_from_python_node_46
    _create_mermaid_analysis_from_python_node_46 --> _create_mermaid_analysis_from_python_node_47
    _create_mermaid_analysis_from_python_node_47 --> _create_mermaid_analysis_from_python_node_48
    _create_mermaid_analysis_from_python_node_48 --> _create_mermaid_analysis_from_python_node_49
    _create_mermaid_analysis_from_python_node_49 --> _create_mermaid_analysis_from_python_node_50
    _create_mermaid_analysis_from_python_node_50 --> _create_mermaid_analysis_from_python_node_51
    _create_mermaid_analysis_from_python_node_51 --> _create_mermaid_analysis_from_python_node_52
    _create_mermaid_analysis_from_python_node_52 --> _create_mermaid_analysis_from_python_node_53
    _create_mermaid_analysis_from_python_node_53 --> _create_mermaid_analysis_from_python_node_54
    _create_mermaid_analysis_from_python_node_54 --> _create_mermaid_analysis_from_python_node_55
    _create_mermaid_analysis_from_python_node_55 --> _create_mermaid_analysis_from_python_node_56
    _create_mermaid_analysis_from_python_node_56 --> _create_mermaid_analysis_from_python_node_57
    _create_mermaid_analysis_from_python_node_57 --> _create_mermaid_analysis_from_python_node_58
    _create_mermaid_analysis_from_python_node_58 --> _create_mermaid_analysis_from_python_node_59
    _create_mermaid_analysis_from_python_node_59 --> _create_mermaid_analysis_from_python_node_60
    _create_mermaid_analysis_from_python_node_60 --> _create_mermaid_analysis_from_python_node_61
    _create_mermaid_analysis_from_python_node_61 --> _create_mermaid_analysis_from_python_node_62
    _create_mermaid_analysis_from_python_node_62 --> _create_mermaid_analysis_from_python_node_63
    _create_mermaid_analysis_from_python_node_63 --> _create_mermaid_analysis_from_python_node_64
    _create_mermaid_analysis_from_python_node_64 --> _create_mermaid_analysis_from_python_node_65
    _create_mermaid_analysis_from_python_node_65 --> _create_mermaid_analysis_from_python_node_66
    _create_mermaid_analysis_from_python_node_66 --> _create_mermaid_analysis_from_python_node_67
    _create_mermaid_analysis_from_python_node_67 --> _create_mermaid_analysis_from_python_node_68
    _create_mermaid_analysis_from_python_node_68 --> _create_mermaid_analysis_from_python_node_69
    _create_mermaid_analysis_from_python_node_69 --> _create_mermaid_analysis_from_python_node_70
    _create_mermaid_analysis_from_python_node_70 --> _create_mermaid_analysis_from_python_node_71
    _create_mermaid_analysis_from_python_node_71 --> _create_mermaid_analysis_from_python_node_72
    _create_mermaid_analysis_from_python_node_72 --> _create_mermaid_analysis_from_python_node_73
    _create_mermaid_analysis_from_python_node_73 --> _create_mermaid_analysis_from_python_node_74
    _create_mermaid_analysis_from_python_node_74 --> _create_mermaid_analysis_from_python_node_75
    _create_mermaid_analysis_from_python_node_75 --> _create_mermaid_analysis_from_python_node_76
    _create_mermaid_analysis_from_python_node_76 --> _create_mermaid_analysis_from_python_node_77
    _create_mermaid_analysis_from_python_node_77 --> _create_mermaid_analysis_from_python_node_78
    _create_mermaid_analysis_from_python_node_78 --> _create_mermaid_analysis_from_python_node_79
    _create_mermaid_analysis_from_python_node_79 --> _create_mermaid_analysis_from_python_node_80
    _create_mermaid_analysis_from_python_node_80 --> _create_mermaid_analysis_from_python_node_81
    _create_mermaid_analysis_from_python_node_81 --> _create_mermaid_analysis_from_python_node_82
    _create_mermaid_analysis_from_python_node_82 --> _create_mermaid_analysis_from_python_node_83
    _create_mermaid_analysis_from_python_node_83 --> _create_mermaid_analysis_from_python_node_84
    _create_mermaid_analysis_from_python_node_84 --> _create_mermaid_analysis_from_python_node_85
    _create_mermaid_analysis_from_python_node_85 --> _create_mermaid_analysis_from_python_node_86
    _create_mermaid_analysis_from_python_node_86 --> _create_mermaid_analysis_from_python_node_87
    _create_mermaid_analysis_from_python_node_87 --> _create_mermaid_analysis_from_python_node_88
    _create_mermaid_analysis_from_python_node_88 --> _create_mermaid_analysis_from_python_node_89
    _create_mermaid_analysis_from_python_node_89 --> _create_mermaid_analysis_from_python_node_90
    _create_mermaid_analysis_from_python_node_90 --> _create_mermaid_analysis_from_python_node_91
    _create_mermaid_analysis_from_python_node_91 --> _create_mermaid_analysis_from_python_node_92
    _create_mermaid_analysis_from_python_node_92 --> _create_mermaid_analysis_from_python_node_93
    _create_mermaid_analysis_from_python_node_93 --> _create_mermaid_analysis_from_python_node_94
    _create_mermaid_analysis_from_python_node_94 --> _create_mermaid_analysis_from_python_node_95
    _create_mermaid_analysis_from_python_node_95 --> _create_mermaid_analysis_from_python_node_96
    _create_mermaid_analysis_from_python_node_96 --> _create_mermaid_analysis_from_python_node_97
    _create_mermaid_analysis_from_python_node_97 --> _create_mermaid_analysis_from_python_node_98
    _create_mermaid_analysis_from_python_node_98 --> _create_mermaid_analysis_from_python_node_99
    _create_mermaid_analysis_from_python_node_99 --> _create_mermaid_analysis_from_python_node_100
    _create_mermaid_analysis_from_python_node_100 --> _create_mermaid_analysis_from_python_node_101
    _create_mermaid_analysis_from_python_node_101 --> _create_mermaid_analysis_from_python_node_102
    _create_mermaid_analysis_from_python_node_102 --> _create_mermaid_analysis_from_python_node_103
    _create_mermaid_analysis_from_python_node_103 --> _create_mermaid_analysis_from_python_node_104
    _create_mermaid_analysis_from_python_node_104 --> _create_mermaid_analysis_from_python_node_105
    _create_mermaid_analysis_from_python_node_105 --> _create_mermaid_analysis_from_python_node_106
    _create_mermaid_analysis_from_python_node_106 --> _create_mermaid_analysis_from_python_node_107
    _create_mermaid_analysis_from_python_node_107 --> _create_mermaid_analysis_from_python_node_108
    _create_mermaid_analysis_from_python_node_108 --> _create_mermaid_analysis_from_python_node_109
    _create_mermaid_analysis_from_python_node_109 --> _create_mermaid_analysis_from_python_node_110
    _create_mermaid_analysis_from_python_node_110 --> _create_mermaid_analysis_from_python_node_111
    _create_mermaid_analysis_from_python_node_111 --> _create_mermaid_analysis_from_python_node_112
    _create_mermaid_analysis_from_python_node_112 --> _create_mermaid_analysis_from_python_node_113
    _create_mermaid_analysis_from_python_node_113 --> _create_mermaid_analysis_from_python_node_114
    _create_mermaid_analysis_from_python_node_114 --> _create_mermaid_analysis_from_python_node_115
    _create_mermaid_analysis_from_python_node_115 --> _create_mermaid_analysis_from_python_node_116
    _create_mermaid_analysis_from_python_node_116 --> _create_mermaid_analysis_from_python_node_117
    _create_mermaid_analysis_from_python_node_117 --> _create_mermaid_analysis_from_python_node_118
    _create_mermaid_analysis_from_python_node_118 --> _create_mermaid_analysis_from_python_node_119
    _create_mermaid_analysis_from_python_node_119 --> _create_mermaid_analysis_from_python_node_120
    _create_mermaid_analysis_from_python_node_120 --> _create_mermaid_analysis_from_python_node_121
    _create_mermaid_analysis_from_python_node_121 --> _create_mermaid_analysis_from_python_node_122
    _create_mermaid_analysis_from_python_node_122 --> _create_mermaid_analysis_from_python_node_123
    _create_mermaid_analysis_from_python_node_123 --> _create_mermaid_analysis_from_python_node_124
    _create_mermaid_analysis_from_python_node_124 --> _create_mermaid_analysis_from_python_node_125
    _create_mermaid_analysis_from_python_node_125 --> _create_mermaid_analysis_from_python_node_126
    _create_mermaid_analysis_from_python_node_126 --> _create_mermaid_analysis_from_python_node_127
    _create_mermaid_analysis_from_python_node_127 --> _create_mermaid_analysis_from_python_node_128
    _create_mermaid_analysis_from_python_node_128 --> _create_mermaid_analysis_from_python_node_129
    _create_mermaid_analysis_from_python_node_129 --> _create_mermaid_analysis_from_python_node_130
    _create_mermaid_analysis_from_python_node_130 --> _create_mermaid_analysis_from_python_node_131
    _create_mermaid_analysis_from_python_node_131 --> _create_mermaid_analysis_from_python_node_132
    _create_mermaid_analysis_from_python_node_132 --> _create_mermaid_analysis_from_python_node_133
    _create_mermaid_analysis_from_python_node_133 --> _create_mermaid_analysis_from_python_node_134
    _create_mermaid_analysis_from_python_node_134 --> _create_mermaid_analysis_from_python_node_135
    _create_mermaid_analysis_from_python_node_135 --> _create_mermaid_analysis_from_python_node_136
    _create_mermaid_analysis_from_python_node_136 --> _create_mermaid_analysis_from_python_node_137
    _create_mermaid_analysis_from_python_node_137 --> _create_mermaid_analysis_from_python_node_138
    _create_mermaid_analysis_from_python_node_138 --> _create_mermaid_analysis_from_python_node_139
    _create_mermaid_analysis_from_python_node_139 --> _create_mermaid_analysis_from_python_node_140
    _create_mermaid_analysis_from_python_node_140 --> _create_mermaid_analysis_from_python_node_141
    _create_mermaid_analysis_from_python_node_141 --> _create_mermaid_analysis_from_python_node_142
    _create_mermaid_analysis_from_python_node_142 --> _create_mermaid_analysis_from_python_node_143
    _create_mermaid_analysis_from_python_node_143 --> _create_mermaid_analysis_from_python_node_144
    _create_mermaid_analysis_from_python_node_144 --> _create_mermaid_analysis_from_python_node_145
    _create_mermaid_analysis_from_python_node_145 --> _create_mermaid_analysis_from_python_node_146
    _create_mermaid_analysis_from_python_node_146 --> _create_mermaid_analysis_from_python_node_147
    _create_mermaid_analysis_from_python_node_147 --> _create_mermaid_analysis_from_python_node_148
    _create_mermaid_analysis_from_python_node_148 --> _create_mermaid_analysis_from_python_node_149
    _create_mermaid_analysis_from_python_node_149 --> _create_mermaid_analysis_from_python_node_150
    _create_mermaid_analysis_from_python_node_150 --> _create_mermaid_analysis_from_python_node_151
    _create_mermaid_analysis_from_python_node_151 --> _create_mermaid_analysis_from_python_node_152
    _create_mermaid_analysis_from_python_node_152 --> _create_mermaid_analysis_from_python_node_153
    _create_mermaid_analysis_from_python_node_153 --> _create_mermaid_analysis_from_python_node_154
    _create_mermaid_analysis_from_python_node_154 --> _create_mermaid_analysis_from_python_node_155
    _create_mermaid_analysis_from_python_node_155 --> _create_mermaid_analysis_from_python_node_156
    _create_mermaid_analysis_from_python_node_156 --> _create_mermaid_analysis_from_python_node_157
    _create_mermaid_analysis_from_python_node_157 --> _create_mermaid_analysis_from_python_node_158
    _create_mermaid_analysis_from_python_node_158 --> _create_mermaid_analysis_from_python_node_159
    _create_mermaid_analysis_from_python_node_159 --> _create_mermaid_analysis_from_python_node_160
    _create_mermaid_analysis_from_python_node_160 --> _create_mermaid_analysis_from_python_node_161
    _create_mermaid_analysis_from_python_node_161 --> _create_mermaid_analysis_from_python_node_162
    _create_mermaid_analysis_from_python_node_162 --> _create_mermaid_analysis_from_python_node_163
    _create_mermaid_analysis_from_python_node_163 --> _create_mermaid_analysis_from_python_node_164
    _create_mermaid_analysis_from_python_node_164 --> _create_mermaid_analysis_from_python_node_165
    _create_mermaid_analysis_from_python_node_165 --> _create_mermaid_analysis_from_python_node_166
    _create_mermaid_analysis_from_python_node_166 --> _create_mermaid_analysis_from_python_node_167
    _create_mermaid_analysis_from_python_node_167 --> _create_mermaid_analysis_from_python_node_168
    _create_mermaid_analysis_from_python_node_168 --> _create_mermaid_analysis_from_python_node_169
    _create_mermaid_analysis_from_python_node_169 --> _create_mermaid_analysis_from_python_node_170
    _create_mermaid_analysis_from_python_node_170 --> _create_mermaid_analysis_from_python_node_171
    _create_mermaid_analysis_from_python_node_171 --> _create_mermaid_analysis_from_python_node_172
    _create_mermaid_analysis_from_python_node_172 --> _create_mermaid_analysis_from_python_node_173
    _create_mermaid_analysis_from_python_node_173 --> _create_mermaid_analysis_from_python_node_174
    _create_mermaid_analysis_from_python_node_174 --> _create_mermaid_analysis_from_python_node_175
    _create_mermaid_analysis_from_python_node_175 --> _create_mermaid_analysis_from_python_node_176
    _create_mermaid_analysis_from_python_node_176 --> _create_mermaid_analysis_from_python_node_177
    _create_mermaid_analysis_from_python_node_177 --> _create_mermaid_analysis_from_python_node_178
    _create_mermaid_analysis_from_python_node_178 --> _create_mermaid_analysis_from_python_node_179
    _create_mermaid_analysis_from_python_node_179 --> _create_mermaid_analysis_from_python_node_180
    _create_mermaid_analysis_from_python_node_180 --> _create_mermaid_analysis_from_python_node_181
    _create_mermaid_analysis_from_python_node_181 --> _create_mermaid_analysis_from_python_node_182
    _create_mermaid_analysis_from_python_node_182 --> _create_mermaid_analysis_from_python_node_183
    _create_mermaid_analysis_from_python_node_183 --> _create_mermaid_analysis_from_python_node_184
    _create_mermaid_analysis_from_python_node_184 --> _create_mermaid_analysis_from_python_node_185
    _create_mermaid_analysis_from_python_node_185 --> _create_mermaid_analysis_from_python_node_186
    _create_mermaid_analysis_from_python_node_186 --> _create_mermaid_analysis_from_python_node_187
  end
  _node_0 --> _node_1
  _node_1 --> _node_2
  _node_2 --> _node_3
  _node_3 --> _node_4
  _node_4 --> _node_5
  _node_5 --> _node_6
  _node_6 --> _node_7
  _node_7 --> _node_8
  _node_8 --> _node_9
  _node_9 --> _node_10
  _node_10 --> _node_11
  _node_11 --> _node_12
  _node_12 --> _node_13
  _node_13 --> _node_14
  _node_14 --> _node_15
  _node_15 --> _node_16
  _node_16 --> _node_17
  _node_17 --> _node_18
  _node_18 --> _node_19
  _node_19 --> _node_20
  _node_20 --> _node_21
  _node_21 --> _node_22
  _node_22 --> _node_23

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='files.destination',
      names=[
        alias(name='create_cleared_output_folder'),
        alias(name='get_output_file_path_for_input_file'),
        alias(name='update_output_file')],
      level=0,
      lineno=3,
      col_offset=0,
      end_lineno=7,
      end_col_offset=1),
    ImportFrom(
      module='files.source',
      names=[
        alias(name='find_all_python_files'),
        alias(name='get_source_code_from_file'),
        alias(name='get_import_name_from_path')],
      level=0,
      lineno=8,
      col_offset=0,
      end_lineno=8,
      end_col_offset=100),
    ImportFrom(
      module='ast_tools',
      names=[
        alias(name='create_mermaid_model_from_ast_model'),
        alias(name='get_ast_root_node_for_file'),
        alias(name='get_markdown_dump_for_ast_node'),
        alias(name='get_used_import_list')],
      level=0,
      lineno=9,
      col_offset=0,
      end_lineno=14,
      end_col_offset=1),
    ImportFrom(
      module='ast_tools.import_map',
      names=[
        alias(name='get_all_imports_from_files')],
      level=0,
      lineno=15,
      col_offset=0,
      end_lineno=15,
      end_col_offset=59),
    ImportFrom(
      module='markdown_tools',
      names=[
        alias(name='create_markdown_content')],
      level=0,
      lineno=16,
      col_offset=0,
      end_lineno=16,
      end_col_offset=50),
    ImportFrom(
      module='mermaid_tools',
      names=[
        alias(name='create_mermaid_flow_graph_from_links')],
      level=0,
      lineno=17,
      col_offset=0,
      end_lineno=17,
      end_col_offset=62),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidElement')],
      level=0,
      lineno=18,
      col_offset=0,
      end_lineno=18,
      end_col_offset=33),
    FunctionDef(
      name='create_mermaid_analysis_from_python',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=20,
              col_offset=53,
              end_lineno=20,
              end_col_offset=56),
            lineno=20,
            col_offset=40,
            end_lineno=20,
            end_col_offset=56),
          arg(
            arg='output_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=20,
              col_offset=71,
              end_lineno=20,
              end_col_offset=74),
            lineno=20,
            col_offset=58,
            end_lineno=20,
            end_col_offset=74)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Call(
            func=Name(
              id='create_cleared_output_folder',
              ctx=Load(),
              lineno=21,
              col_offset=4,
              end_lineno=21,
              end_col_offset=32),
            args=[],
            keywords=[
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=21,
                  col_offset=45,
                  end_lineno=21,
                  end_col_offset=56),
                lineno=21,
                col_offset=33,
                end_lineno=21,
                end_col_offset=56)],
            lineno=21,
            col_offset=4,
            end_lineno=21,
            end_col_offset=57),
          lineno=21,
          col_offset=4,
          end_lineno=21,
          end_col_offset=57),
        Assign(
          targets=[
            Name(
              id='python_files',
              ctx=Store(),
              lineno=22,
              col_offset=4,
              end_lineno=22,
              end_col_offset=16)],
          value=Call(
            func=Name(
              id='find_all_python_files',
              ctx=Load(),
              lineno=22,
              col_offset=19,
              end_lineno=22,
              end_col_offset=40),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=22,
                  col_offset=52,
                  end_lineno=22,
                  end_col_offset=62),
                lineno=22,
                col_offset=41,
                end_lineno=22,
                end_col_offset=62)],
            lineno=22,
            col_offset=19,
            end_lineno=22,
            end_col_offset=63),
          lineno=22,
          col_offset=4,
          end_lineno=22,
          end_col_offset=63),
        Assign(
          targets=[
            Name(
              id='global_import_list',
              ctx=Store(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=22)],
          value=Call(
            func=Name(
              id='get_all_imports_from_files',
              ctx=Load(),
              lineno=23,
              col_offset=25,
              end_lineno=23,
              end_col_offset=51),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=24,
                  col_offset=19,
                  end_lineno=24,
                  end_col_offset=29),
                lineno=24,
                col_offset=8,
                end_lineno=24,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=24,
                  col_offset=44,
                  end_lineno=24,
                  end_col_offset=56),
                lineno=24,
                col_offset=31,
                end_lineno=24,
                end_col_offset=56)],
            lineno=23,
            col_offset=25,
            end_lineno=25,
            end_col_offset=5),
          lineno=23,
          col_offset=4,
          end_lineno=25,
          end_col_offset=5),
        Expr(
          value=Call(
            func=Name(
              id='print',
              ctx=Load(),
              lineno=27,
              col_offset=4,
              end_lineno=27,
              end_col_offset=9),
            args=[
              Call(
                func=Attribute(
                  value=Constant(
                    value='\n',
                    lineno=27,
                    col_offset=10,
                    end_lineno=27,
                    end_col_offset=14),
                  attr='join',
                  ctx=Load(),
                  lineno=27,
                  col_offset=10,
                  end_lineno=27,
                  end_col_offset=19),
                args=[
                  ListComp(
                    elt=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Name(
                            id='k',
                            ctx=Load(),
                            lineno=27,
                            col_offset=24,
                            end_lineno=27,
                            end_col_offset=25),
                          conversion=-1,
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32),
                        Constant(
                          value=': ',
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32),
                        FormattedValue(
                          value=Name(
                            id='v',
                            ctx=Load(),
                            lineno=27,
                            col_offset=29,
                            end_lineno=27,
                            end_col_offset=30),
                          conversion=-1,
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32)],
                      lineno=27,
                      col_offset=21,
                      end_lineno=27,
                      end_col_offset=32),
                    generators=[
                      comprehension(
                        target=Tuple(
                          elts=[
                            Name(
                              id='k',
                              ctx=Store(),
                              lineno=27,
                              col_offset=37,
                              end_lineno=27,
                              end_col_offset=38),
                            Name(
                              id='v',
                              ctx=Store(),
                              lineno=27,
                              col_offset=39,
                              end_lineno=27,
                              end_col_offset=40)],
                          ctx=Store(),
                          lineno=27,
                          col_offset=37,
                          end_lineno=27,
                          end_col_offset=40),
                        iter=Call(
                          func=Attribute(
                            value=Name(
                              id='global_import_list',
                              ctx=Load(),
                              lineno=27,
                              col_offset=44,
                              end_lineno=27,
                              end_col_offset=62),
                            attr='items',
                            ctx=Load(),
                            lineno=27,
                            col_offset=44,
                            end_lineno=27,
                            end_col_offset=68),
                          args=[],
                          keywords=[],
                          lineno=27,
                          col_offset=44,
                          end_lineno=27,
                          end_col_offset=70),
                        ifs=[],
                        is_async=0)],
                    lineno=27,
                    col_offset=20,
                    end_lineno=27,
                    end_col_offset=71)],
                keywords=[],
                lineno=27,
                col_offset=10,
                end_lineno=27,
                end_col_offset=72)],
            keywords=[],
            lineno=27,
            col_offset=4,
            end_lineno=27,
            end_col_offset=73),
          lineno=27,
          col_offset=4,
          end_lineno=27,
          end_col_offset=73),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=29,
            col_offset=8,
            end_lineno=29,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=29,
            col_offset=19,
            end_lineno=29,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='in_file',
                    ctx=Load(),
                    lineno=30,
                    col_offset=27,
                    end_lineno=30,
                    end_col_offset=34),
                  attr='replace',
                  ctx=Load(),
                  lineno=30,
                  col_offset=27,
                  end_lineno=30,
                  end_col_offset=42),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=30,
                    col_offset=43,
                    end_lineno=30,
                    end_col_offset=53),
                  Constant(
                    value='',
                    lineno=30,
                    col_offset=55,
                    end_lineno=30,
                    end_col_offset=57)],
                keywords=[],
                lineno=30,
                col_offset=27,
                end_lineno=30,
                end_col_offset=58),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=58),
            Assign(
              targets=[
                Name(
                  id='out_file',
                  ctx=Store(),
                  lineno=31,
                  col_offset=8,
                  end_lineno=31,
                  end_col_offset=16)],
              value=Call(
                func=Name(
                  id='get_output_file_path_for_input_file',
                  ctx=Load(),
                  lineno=31,
                  col_offset=19,
                  end_lineno=31,
                  end_col_offset=54),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='relative_in_file',
                      ctx=Load(),
                      lineno=32,
                      col_offset=23,
                      end_lineno=32,
                      end_col_offset=39),
                    lineno=32,
                    col_offset=12,
                    end_lineno=32,
                    end_col_offset=39),
                  keyword(
                    arg='output_root',
                    value=Name(
                      id='output_path',
                      ctx=Load(),
                      lineno=32,
                      col_offset=53,
                      end_lineno=32,
                      end_col_offset=64),
                    lineno=32,
                    col_offset=41,
                    end_lineno=32,
                    end_col_offset=64)],
                lineno=31,
                col_offset=19,
                end_lineno=33,
                end_col_offset=9),
              lineno=31,
              col_offset=8,
              end_lineno=33,
              end_col_offset=9),
            Assign(
              targets=[
                Name(
                  id='debug_dump',
                  ctx=Store(),
                  lineno=35,
                  col_offset=8,
                  end_lineno=35,
                  end_col_offset=18)],
              value=Constant(
                value='',
                lineno=35,
                col_offset=21,
                end_lineno=35,
                end_col_offset=23),
              lineno=35,
              col_offset=8,
              end_lineno=35,
              end_col_offset=23),
            Assign(
              targets=[
                Name(
                  id='import_list',
                  ctx=Store(),
                  lineno=36,
                  col_offset=8,
                  end_lineno=36,
                  end_col_offset=19)],
              value=List(
                elts=[],
                ctx=Load(),
                lineno=36,
                col_offset=22,
                end_lineno=36,
                end_col_offset=24),
              lineno=36,
              col_offset=8,
              end_lineno=36,
              end_col_offset=24),
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=38,
                  col_offset=11,
                  end_lineno=38,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=38,
                    col_offset=26,
                    end_lineno=38,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=38,
                        col_offset=63,
                        end_lineno=38,
                        end_col_offset=70),
                      lineno=38,
                      col_offset=52,
                      end_lineno=38,
                      end_col_offset=70)],
                  lineno=38,
                  col_offset=26,
                  end_lineno=38,
                  end_col_offset=71),
                lineno=38,
                col_offset=11,
                end_lineno=38,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=39,
                      col_offset=15,
                      end_lineno=39,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=39,
                        col_offset=27,
                        end_lineno=39,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=40,
                            col_offset=28,
                            end_lineno=40,
                            end_col_offset=39),
                          lineno=40,
                          col_offset=16,
                          end_lineno=40,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=41,
                            col_offset=27,
                            end_lineno=41,
                            end_col_offset=34),
                          lineno=41,
                          col_offset=16,
                          end_lineno=41,
                          end_col_offset=34)],
                      lineno=39,
                      col_offset=27,
                      end_lineno=42,
                      end_col_offset=13),
                    lineno=39,
                    col_offset=15,
                    end_lineno=42,
                    end_col_offset=13),
                  body=[
                    Assign(
                      targets=[
                        Name(
                          id='debug_dump',
                          ctx=Store(),
                          lineno=44,
                          col_offset=16,
                          end_lineno=44,
                          end_col_offset=26)],
                      value=Call(
                        func=Name(
                          id='get_markdown_dump_for_ast_node',
                          ctx=Load(),
                          lineno=44,
                          col_offset=29,
                          end_lineno=44,
                          end_col_offset=59),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=44,
                              col_offset=69,
                              end_lineno=44,
                              end_col_offset=77),
                            lineno=44,
                            col_offset=60,
                            end_lineno=44,
                            end_col_offset=77)],
                        lineno=44,
                        col_offset=29,
                        end_lineno=44,
                        end_col_offset=78),
                      lineno=44,
                      col_offset=16,
                      end_lineno=44,
                      end_col_offset=78),
                    Assign(
                      targets=[
                        Name(
                          id='import_list',
                          ctx=Store(),
                          lineno=46,
                          col_offset=16,
                          end_lineno=46,
                          end_col_offset=27)],
                      value=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=46,
                          col_offset=30,
                          end_lineno=46,
                          end_col_offset=50),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=46,
                              col_offset=60,
                              end_lineno=46,
                              end_col_offset=68),
                            lineno=46,
                            col_offset=51,
                            end_lineno=46,
                            end_col_offset=68)],
                        lineno=46,
                        col_offset=30,
                        end_lineno=46,
                        end_col_offset=69),
                      lineno=46,
                      col_offset=16,
                      end_lineno=46,
                      end_col_offset=69),
                    AnnAssign(
                      target=Name(
                        id='link_info',
                        ctx=Store(),
                        lineno=48,
                        col_offset=16,
                        end_lineno=48,
                        end_col_offset=25),
                      annotation=Subscript(
                        value=Name(
                          id='list',
                          ctx=Load(),
                          lineno=48,
                          col_offset=28,
                          end_lineno=48,
                          end_col_offset=32),
                        slice=Name(
                          id='MermaidElement',
                          ctx=Load(),
                          lineno=48,
                          col_offset=33,
                          end_lineno=48,
                          end_col_offset=47),
                        ctx=Load(),
                        lineno=48,
                        col_offset=28,
                        end_lineno=48,
                        end_col_offset=48),
                      value=Call(
                        func=Name(
                          id='create_mermaid_model_from_ast_model',
                          ctx=Load(),
                          lineno=49,
                          col_offset=20,
                          end_lineno=49,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='model',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=49,
                              col_offset=62,
                              end_lineno=49,
                              end_col_offset=70),
                            lineno=49,
                            col_offset=56,
                            end_lineno=49,
                            end_col_offset=70)],
                        lineno=49,
                        col_offset=20,
                        end_lineno=49,
                        end_col_offset=71),
                      simple=1,
                      lineno=48,
                      col_offset=16,
                      end_lineno=50,
                      end_col_offset=17),
                    Assign(
                      targets=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Store(),
                          lineno=52,
                          col_offset=16,
                          end_lineno=52,
                          end_col_offset=31)],
                      value=Call(
                        func=Name(
                          id='create_mermaid_flow_graph_from_links',
                          ctx=Load(),
                          lineno=52,
                          col_offset=34,
                          end_lineno=52,
                          end_col_offset=70),
                        args=[
                          Name(
                            id='link_info',
                            ctx=Load(),
                            lineno=52,
                            col_offset=71,
                            end_lineno=52,
                            end_col_offset=80)],
                        keywords=[],
                        lineno=52,
                        col_offset=34,
                        end_lineno=52,
                        end_col_offset=81),
                      lineno=52,
                      col_offset=16,
                      end_lineno=52,
                      end_col_offset=81)],
                  orelse=[],
                  lineno=39,
                  col_offset=12,
                  end_lineno=52,
                  end_col_offset=81)],
              orelse=[],
              lineno=38,
              col_offset=8,
              end_lineno=52,
              end_col_offset=81),
            Assign(
              targets=[
                Name(
                  id='markdown_content',
                  ctx=Store(),
                  lineno=54,
                  col_offset=8,
                  end_lineno=54,
                  end_col_offset=24)],
              value=Call(
                func=Name(
                  id='create_markdown_content',
                  ctx=Load(),
                  lineno=54,
                  col_offset=27,
                  end_lineno=54,
                  end_col_offset=50),
                args=[],
                keywords=[
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=55,
                      col_offset=23,
                      end_lineno=55,
                      end_col_offset=30),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=30),
                  keyword(
                    arg='import_list',
                    value=Name(
                      id='import_list',
                      ctx=Load(),
                      lineno=56,
                      col_offset=24,
                      end_lineno=56,
                      end_col_offset=35),
                    lineno=56,
                    col_offset=12,
                    end_lineno=56,
                    end_col_offset=35),
                  keyword(
                    arg='mermaid_diagrams',
                    value=List(
                      elts=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Load(),
                          lineno=57,
                          col_offset=30,
                          end_lineno=57,
                          end_col_offset=45)],
                      ctx=Load(),
                      lineno=57,
                      col_offset=29,
                      end_lineno=57,
                      end_col_offset=46),
                    lineno=57,
                    col_offset=12,
                    end_lineno=57,
                    end_col_offset=46),
                  keyword(
                    arg='debug_dump',
                    value=Name(
                      id='debug_dump',
                      ctx=Load(),
                      lineno=58,
                      col_offset=23,
                      end_lineno=58,
                      end_col_offset=33),
                    lineno=58,
                    col_offset=12,
                    end_lineno=58,
                    end_col_offset=33)],
                lineno=54,
                col_offset=27,
                end_lineno=59,
                end_col_offset=9),
              lineno=54,
              col_offset=8,
              end_lineno=59,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Name(
                  id='update_output_file',
                  ctx=Load(),
                  lineno=61,
                  col_offset=8,
                  end_lineno=61,
                  end_col_offset=26),
                args=[],
                keywords=[
                  keyword(
                    arg='content',
                    value=Name(
                      id='markdown_content',
                      ctx=Load(),
                      lineno=61,
                      col_offset=35,
                      end_lineno=61,
                      end_col_offset=51),
                    lineno=61,
                    col_offset=27,
                    end_lineno=61,
                    end_col_offset=51),
                  keyword(
                    arg='output_file',
                    value=Name(
                      id='out_file',
                      ctx=Load(),
                      lineno=61,
                      col_offset=65,
                      end_lineno=61,
                      end_col_offset=73),
                    lineno=61,
                    col_offset=53,
                    end_lineno=61,
                    end_col_offset=73)],
                lineno=61,
                col_offset=8,
                end_lineno=61,
                end_col_offset=74),
              lineno=61,
              col_offset=8,
              end_lineno=61,
              end_col_offset=74)],
          orelse=[],
          lineno=29,
          col_offset=4,
          end_lineno=61,
          end_col_offset=74)],
      decorator_list=[],
      lineno=20,
      col_offset=0,
      end_lineno=61,
      end_col_offset=74),
    If(
      test=Compare(
        left=Name(
          id='__name__',
          ctx=Load(),
          lineno=64,
          col_offset=3,
          end_lineno=64,
          end_col_offset=11),
        ops=[
          Eq()],
        comparators=[
          Constant(
            value='__main__',
            lineno=64,
            col_offset=15,
            end_lineno=64,
            end_col_offset=25)],
        lineno=64,
        col_offset=3,
        end_lineno=64,
        end_col_offset=25),
      body=[
        Assign(
          targets=[
            Name(
              id='input_path',
              ctx=Store(),
              lineno=67,
              col_offset=4,
              end_lineno=67,
              end_col_offset=14)],
          value=Constant(
            value='./src/pyremaid/',
            lineno=67,
            col_offset=17,
            end_lineno=67,
            end_col_offset=34),
          lineno=67,
          col_offset=4,
          end_lineno=67,
          end_col_offset=34),
        Assign(
          targets=[
            Name(
              id='output_path',
              ctx=Store(),
              lineno=68,
              col_offset=4,
              end_lineno=68,
              end_col_offset=15)],
          value=Constant(
            value='./docs/pyremaid/',
            lineno=68,
            col_offset=18,
            end_lineno=68,
            end_col_offset=36),
          lineno=68,
          col_offset=4,
          end_lineno=68,
          end_col_offset=36),
        Expr(
          value=Call(
            func=Name(
              id='create_mermaid_analysis_from_python',
              ctx=Load(),
              lineno=69,
              col_offset=4,
              end_lineno=69,
              end_col_offset=39),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=69,
                  col_offset=51,
                  end_lineno=69,
                  end_col_offset=61),
                lineno=69,
                col_offset=40,
                end_lineno=69,
                end_col_offset=61),
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=69,
                  col_offset=75,
                  end_lineno=69,
                  end_col_offset=86),
                lineno=69,
                col_offset=63,
                end_lineno=69,
                end_col_offset=86)],
            lineno=69,
            col_offset=4,
            end_lineno=69,
            end_col_offset=87),
          lineno=69,
          col_offset=4,
          end_lineno=69,
          end_col_offset=87)],
      orelse=[],
      lineno=64,
      col_offset=0,
      end_lineno=69,
      end_col_offset=87)],
  type_ignores=[])
```
</details>

