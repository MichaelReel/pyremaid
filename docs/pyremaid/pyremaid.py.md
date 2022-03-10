# ./src/pyremaid/pyremaid.py

### Imports

  - [files.destination.create_cleared_output_folder](/docs/pyremaid/files/destination.py.md)
  - [files.destination.get_output_file_path_for_input_file](/docs/pyremaid/files/destination.py.md)
  - [files.destination.update_output_file](/docs/pyremaid/files/destination.py.md)
  - [files.source.find_all_python_files](/docs/pyremaid/files/source.py.md)
  - [files.source.get_source_code_from_file](/docs/pyremaid/files/source.py.md)
  - [files.source.get_import_name_from_path](/docs/pyremaid/files/source.py.md)
  - [ast_tools.create_mermaid_model_from_ast_model](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_ast_root_node_for_file](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_markdown_dump_for_ast_node](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_used_import_list](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.import_map.get_all_imports_from_files](/docs/pyremaid/ast_tools/import_map.py.md)
  - [markdown_tools.create_markdown_content](/docs/pyremaid/markdown_tools.py.md)
  - [mermaid_tools.create_mermaid_flow_graph_from_links](/docs/pyremaid/mermaid_tools/__init__.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)

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
  _create_mermaid_analysis_from_python_node_28["keyword"]
  _create_mermaid_analysis_from_python_node_29["Name"]
  _create_mermaid_analysis_from_python_node_30["Load"]
  _create_mermaid_analysis_from_python_node_31["For"]
  _create_mermaid_analysis_from_python_node_32["Name"]
  _create_mermaid_analysis_from_python_node_33["Store"]
  _create_mermaid_analysis_from_python_node_34["Name"]
  _create_mermaid_analysis_from_python_node_35["Load"]
  _create_mermaid_analysis_from_python_node_36["Assign"]
  _create_mermaid_analysis_from_python_node_37["Name"]
  _create_mermaid_analysis_from_python_node_38["Store"]
  _create_mermaid_analysis_from_python_node_39["Call"]
  _create_mermaid_analysis_from_python_node_40["Attribute"]
  _create_mermaid_analysis_from_python_node_41["Name"]
  _create_mermaid_analysis_from_python_node_42["Load"]
  _create_mermaid_analysis_from_python_node_43["Load"]
  _create_mermaid_analysis_from_python_node_44["Name"]
  _create_mermaid_analysis_from_python_node_45["Load"]
  _create_mermaid_analysis_from_python_node_46["Constant"]
  _create_mermaid_analysis_from_python_node_47["Assign"]
  _create_mermaid_analysis_from_python_node_48["Name"]
  _create_mermaid_analysis_from_python_node_49["Store"]
  _create_mermaid_analysis_from_python_node_50["Call"]
  _create_mermaid_analysis_from_python_node_51["Name"]
  _create_mermaid_analysis_from_python_node_52["Load"]
  _create_mermaid_analysis_from_python_node_53["keyword"]
  _create_mermaid_analysis_from_python_node_54["Name"]
  _create_mermaid_analysis_from_python_node_55["Load"]
  _create_mermaid_analysis_from_python_node_56["keyword"]
  _create_mermaid_analysis_from_python_node_57["Name"]
  _create_mermaid_analysis_from_python_node_58["Load"]
  _create_mermaid_analysis_from_python_node_59["Assign"]
  _create_mermaid_analysis_from_python_node_60["Name"]
  _create_mermaid_analysis_from_python_node_61["Store"]
  _create_mermaid_analysis_from_python_node_62["Constant"]
  _create_mermaid_analysis_from_python_node_63["Assign"]
  _create_mermaid_analysis_from_python_node_64["Name"]
  _create_mermaid_analysis_from_python_node_65["Store"]
  _create_mermaid_analysis_from_python_node_66["List"]
  _create_mermaid_analysis_from_python_node_67["Load"]
  _create_mermaid_analysis_from_python_node_68["If"]
  _create_mermaid_analysis_from_python_node_69["NamedExpr"]
  _create_mermaid_analysis_from_python_node_70["Name"]
  _create_mermaid_analysis_from_python_node_71["Store"]
  _create_mermaid_analysis_from_python_node_72["Call"]
  _create_mermaid_analysis_from_python_node_73["Name"]
  _create_mermaid_analysis_from_python_node_74["Load"]
  _create_mermaid_analysis_from_python_node_75["keyword"]
  _create_mermaid_analysis_from_python_node_76["Name"]
  _create_mermaid_analysis_from_python_node_77["Load"]
  _create_mermaid_analysis_from_python_node_78["If"]
  _create_mermaid_analysis_from_python_node_79["NamedExpr"]
  _create_mermaid_analysis_from_python_node_80["Name"]
  _create_mermaid_analysis_from_python_node_81["Store"]
  _create_mermaid_analysis_from_python_node_82["Call"]
  _create_mermaid_analysis_from_python_node_83["Name"]
  _create_mermaid_analysis_from_python_node_84["Load"]
  _create_mermaid_analysis_from_python_node_85["keyword"]
  _create_mermaid_analysis_from_python_node_86["Name"]
  _create_mermaid_analysis_from_python_node_87["Load"]
  _create_mermaid_analysis_from_python_node_88["keyword"]
  _create_mermaid_analysis_from_python_node_89["Name"]
  _create_mermaid_analysis_from_python_node_90["Load"]
  _create_mermaid_analysis_from_python_node_91["Assign"]
  _create_mermaid_analysis_from_python_node_92["Name"]
  _create_mermaid_analysis_from_python_node_93["Store"]
  _create_mermaid_analysis_from_python_node_94["Call"]
  _create_mermaid_analysis_from_python_node_95["Name"]
  _create_mermaid_analysis_from_python_node_96["Load"]
  _create_mermaid_analysis_from_python_node_97["keyword"]
  _create_mermaid_analysis_from_python_node_98["Name"]
  _create_mermaid_analysis_from_python_node_99["Load"]
  _create_mermaid_analysis_from_python_node_100["Assign"]
  _create_mermaid_analysis_from_python_node_101["Name"]
  _create_mermaid_analysis_from_python_node_102["Store"]
  _create_mermaid_analysis_from_python_node_103["Call"]
  _create_mermaid_analysis_from_python_node_104["Name"]
  _create_mermaid_analysis_from_python_node_105["Load"]
  _create_mermaid_analysis_from_python_node_106["keyword"]
  _create_mermaid_analysis_from_python_node_107["Name"]
  _create_mermaid_analysis_from_python_node_108["Load"]
  _create_mermaid_analysis_from_python_node_109["AnnAssign"]
  _create_mermaid_analysis_from_python_node_110["Name"]
  _create_mermaid_analysis_from_python_node_111["Store"]
  _create_mermaid_analysis_from_python_node_112["Subscript"]
  _create_mermaid_analysis_from_python_node_113["Name"]
  _create_mermaid_analysis_from_python_node_114["Load"]
  _create_mermaid_analysis_from_python_node_115["Name"]
  _create_mermaid_analysis_from_python_node_116["Load"]
  _create_mermaid_analysis_from_python_node_117["Load"]
  _create_mermaid_analysis_from_python_node_118["Call"]
  _create_mermaid_analysis_from_python_node_119["Name"]
  _create_mermaid_analysis_from_python_node_120["Load"]
  _create_mermaid_analysis_from_python_node_121["keyword"]
  _create_mermaid_analysis_from_python_node_122["Name"]
  _create_mermaid_analysis_from_python_node_123["Load"]
  _create_mermaid_analysis_from_python_node_124["Assign"]
  _create_mermaid_analysis_from_python_node_125["Name"]
  _create_mermaid_analysis_from_python_node_126["Store"]
  _create_mermaid_analysis_from_python_node_127["Call"]
  _create_mermaid_analysis_from_python_node_128["Name"]
  _create_mermaid_analysis_from_python_node_129["Load"]
  _create_mermaid_analysis_from_python_node_130["Name"]
  _create_mermaid_analysis_from_python_node_131["Load"]
  _create_mermaid_analysis_from_python_node_132["Assign"]
  _create_mermaid_analysis_from_python_node_133["Name"]
  _create_mermaid_analysis_from_python_node_134["Store"]
  _create_mermaid_analysis_from_python_node_135["Call"]
  _create_mermaid_analysis_from_python_node_136["Name"]
  _create_mermaid_analysis_from_python_node_137["Load"]
  _create_mermaid_analysis_from_python_node_138["keyword"]
  _create_mermaid_analysis_from_python_node_139["Name"]
  _create_mermaid_analysis_from_python_node_140["Load"]
  _create_mermaid_analysis_from_python_node_141["keyword"]
  _create_mermaid_analysis_from_python_node_142["Name"]
  _create_mermaid_analysis_from_python_node_143["Load"]
  _create_mermaid_analysis_from_python_node_144["keyword"]
  _create_mermaid_analysis_from_python_node_145["Name"]
  _create_mermaid_analysis_from_python_node_146["Load"]
  _create_mermaid_analysis_from_python_node_147["keyword"]
  _create_mermaid_analysis_from_python_node_148["List"]
  _create_mermaid_analysis_from_python_node_149["Name"]
  _create_mermaid_analysis_from_python_node_150["Load"]
  _create_mermaid_analysis_from_python_node_151["Load"]
  _create_mermaid_analysis_from_python_node_152["keyword"]
  _create_mermaid_analysis_from_python_node_153["Name"]
  _create_mermaid_analysis_from_python_node_154["Load"]
  _create_mermaid_analysis_from_python_node_155["Expr"]
  _create_mermaid_analysis_from_python_node_156["Call"]
  _create_mermaid_analysis_from_python_node_157["Name"]
  _create_mermaid_analysis_from_python_node_158["Load"]
  _create_mermaid_analysis_from_python_node_159["keyword"]
  _create_mermaid_analysis_from_python_node_160["Name"]
  _create_mermaid_analysis_from_python_node_161["Load"]
  _create_mermaid_analysis_from_python_node_162["keyword"]
  _create_mermaid_analysis_from_python_node_163["Name"]
  _create_mermaid_analysis_from_python_node_164["Load"]
  _get_global_input_table_node_0["Assign"]
  _get_global_input_table_node_1["Name"]
  _get_global_input_table_node_2["Store"]
  _get_global_input_table_node_3["Call"]
  _get_global_input_table_node_4["Name"]
  _get_global_input_table_node_5["Load"]
  _get_global_input_table_node_6["keyword"]
  _get_global_input_table_node_7["Name"]
  _get_global_input_table_node_8["Load"]
  _get_global_input_table_node_9["keyword"]
  _get_global_input_table_node_10["Name"]
  _get_global_input_table_node_11["Load"]
  _get_global_input_table_node_12["For"]
  _get_global_input_table_node_13["Name"]
  _get_global_input_table_node_14["Store"]
  _get_global_input_table_node_15["Name"]
  _get_global_input_table_node_16["Load"]
  _get_global_input_table_node_17["Assign"]
  _get_global_input_table_node_18["Name"]
  _get_global_input_table_node_19["Store"]
  _get_global_input_table_node_20["Call"]
  _get_global_input_table_node_21["Attribute"]
  _get_global_input_table_node_22["Subscript"]
  _get_global_input_table_node_23["Name"]
  _get_global_input_table_node_24["Load"]
  _get_global_input_table_node_25["Name"]
  _get_global_input_table_node_26["Load"]
  _get_global_input_table_node_27["Load"]
  _get_global_input_table_node_28["Load"]
  _get_global_input_table_node_29["Name"]
  _get_global_input_table_node_30["Load"]
  _get_global_input_table_node_31["Constant"]
  _get_global_input_table_node_32["If"]
  _get_global_input_table_node_33["Name"]
  _get_global_input_table_node_34["Load"]
  _get_global_input_table_node_35["Assign"]
  _get_global_input_table_node_36["Subscript"]
  _get_global_input_table_node_37["Name"]
  _get_global_input_table_node_38["Load"]
  _get_global_input_table_node_39["Name"]
  _get_global_input_table_node_40["Load"]
  _get_global_input_table_node_41["Store"]
  _get_global_input_table_node_42["Call"]
  _get_global_input_table_node_43["Attribute"]
  _get_global_input_table_node_44["Call"]
  _get_global_input_table_node_45["Name"]
  _get_global_input_table_node_46["Load"]
  _get_global_input_table_node_47["keyword"]
  _get_global_input_table_node_48["Name"]
  _get_global_input_table_node_49["Load"]
  _get_global_input_table_node_50["keyword"]
  _get_global_input_table_node_51["Name"]
  _get_global_input_table_node_52["Load"]
  _get_global_input_table_node_53["Load"]
  _get_global_input_table_node_54["Constant"]
  _get_global_input_table_node_55["Expr"]
  _get_global_input_table_node_56["Call"]
  _get_global_input_table_node_57["Name"]
  _get_global_input_table_node_58["Load"]
  _get_global_input_table_node_59["Call"]
  _get_global_input_table_node_60["Attribute"]
  _get_global_input_table_node_61["Constant"]
  _get_global_input_table_node_62["Load"]
  _get_global_input_table_node_63["ListComp"]
  _get_global_input_table_node_64["JoinedStr"]
  _get_global_input_table_node_65["FormattedValue"]
  _get_global_input_table_node_66["Name"]
  _get_global_input_table_node_67["Load"]
  _get_global_input_table_node_68["Constant"]
  _get_global_input_table_node_69["FormattedValue"]
  _get_global_input_table_node_70["Name"]
  _get_global_input_table_node_71["Load"]
  _get_global_input_table_node_72["comprehension"]
  _get_global_input_table_node_73["Tuple"]
  _get_global_input_table_node_74["Name"]
  _get_global_input_table_node_75["Store"]
  _get_global_input_table_node_76["Name"]
  _get_global_input_table_node_77["Store"]
  _get_global_input_table_node_78["Store"]
  _get_global_input_table_node_79["Call"]
  _get_global_input_table_node_80["Attribute"]
  _get_global_input_table_node_81["Name"]
  _get_global_input_table_node_82["Load"]
  _get_global_input_table_node_83["Load"]
  _get_global_input_table_node_84["Return"]
  _get_global_input_table_node_85["Name"]
  _get_global_input_table_node_86["Load"]
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
  end
  subgraph get_global_input_table
    direction TB
    _get_global_input_table_node_0 --> _get_global_input_table_node_1
    _get_global_input_table_node_1 --> _get_global_input_table_node_2
    _get_global_input_table_node_2 --> _get_global_input_table_node_3
    _get_global_input_table_node_3 --> _get_global_input_table_node_4
    _get_global_input_table_node_4 --> _get_global_input_table_node_5
    _get_global_input_table_node_5 --> _get_global_input_table_node_6
    _get_global_input_table_node_6 --> _get_global_input_table_node_7
    _get_global_input_table_node_7 --> _get_global_input_table_node_8
    _get_global_input_table_node_8 --> _get_global_input_table_node_9
    _get_global_input_table_node_9 --> _get_global_input_table_node_10
    _get_global_input_table_node_10 --> _get_global_input_table_node_11
    _get_global_input_table_node_11 --> _get_global_input_table_node_12
    _get_global_input_table_node_12 --> _get_global_input_table_node_13
    _get_global_input_table_node_13 --> _get_global_input_table_node_14
    _get_global_input_table_node_14 --> _get_global_input_table_node_15
    _get_global_input_table_node_15 --> _get_global_input_table_node_16
    _get_global_input_table_node_16 --> _get_global_input_table_node_17
    _get_global_input_table_node_17 --> _get_global_input_table_node_18
    _get_global_input_table_node_18 --> _get_global_input_table_node_19
    _get_global_input_table_node_19 --> _get_global_input_table_node_20
    _get_global_input_table_node_20 --> _get_global_input_table_node_21
    _get_global_input_table_node_21 --> _get_global_input_table_node_22
    _get_global_input_table_node_22 --> _get_global_input_table_node_23
    _get_global_input_table_node_23 --> _get_global_input_table_node_24
    _get_global_input_table_node_24 --> _get_global_input_table_node_25
    _get_global_input_table_node_25 --> _get_global_input_table_node_26
    _get_global_input_table_node_26 --> _get_global_input_table_node_27
    _get_global_input_table_node_27 --> _get_global_input_table_node_28
    _get_global_input_table_node_28 --> _get_global_input_table_node_29
    _get_global_input_table_node_29 --> _get_global_input_table_node_30
    _get_global_input_table_node_30 --> _get_global_input_table_node_31
    _get_global_input_table_node_31 --> _get_global_input_table_node_32
    _get_global_input_table_node_32 --> _get_global_input_table_node_33
    _get_global_input_table_node_33 --> _get_global_input_table_node_34
    _get_global_input_table_node_34 --> _get_global_input_table_node_35
    _get_global_input_table_node_35 --> _get_global_input_table_node_36
    _get_global_input_table_node_36 --> _get_global_input_table_node_37
    _get_global_input_table_node_37 --> _get_global_input_table_node_38
    _get_global_input_table_node_38 --> _get_global_input_table_node_39
    _get_global_input_table_node_39 --> _get_global_input_table_node_40
    _get_global_input_table_node_40 --> _get_global_input_table_node_41
    _get_global_input_table_node_41 --> _get_global_input_table_node_42
    _get_global_input_table_node_42 --> _get_global_input_table_node_43
    _get_global_input_table_node_43 --> _get_global_input_table_node_44
    _get_global_input_table_node_44 --> _get_global_input_table_node_45
    _get_global_input_table_node_45 --> _get_global_input_table_node_46
    _get_global_input_table_node_46 --> _get_global_input_table_node_47
    _get_global_input_table_node_47 --> _get_global_input_table_node_48
    _get_global_input_table_node_48 --> _get_global_input_table_node_49
    _get_global_input_table_node_49 --> _get_global_input_table_node_50
    _get_global_input_table_node_50 --> _get_global_input_table_node_51
    _get_global_input_table_node_51 --> _get_global_input_table_node_52
    _get_global_input_table_node_52 --> _get_global_input_table_node_53
    _get_global_input_table_node_53 --> _get_global_input_table_node_54
    _get_global_input_table_node_54 --> _get_global_input_table_node_55
    _get_global_input_table_node_55 --> _get_global_input_table_node_56
    _get_global_input_table_node_56 --> _get_global_input_table_node_57
    _get_global_input_table_node_57 --> _get_global_input_table_node_58
    _get_global_input_table_node_58 --> _get_global_input_table_node_59
    _get_global_input_table_node_59 --> _get_global_input_table_node_60
    _get_global_input_table_node_60 --> _get_global_input_table_node_61
    _get_global_input_table_node_61 --> _get_global_input_table_node_62
    _get_global_input_table_node_62 --> _get_global_input_table_node_63
    _get_global_input_table_node_63 --> _get_global_input_table_node_64
    _get_global_input_table_node_64 --> _get_global_input_table_node_65
    _get_global_input_table_node_65 --> _get_global_input_table_node_66
    _get_global_input_table_node_66 --> _get_global_input_table_node_67
    _get_global_input_table_node_67 --> _get_global_input_table_node_68
    _get_global_input_table_node_68 --> _get_global_input_table_node_69
    _get_global_input_table_node_69 --> _get_global_input_table_node_70
    _get_global_input_table_node_70 --> _get_global_input_table_node_71
    _get_global_input_table_node_71 --> _get_global_input_table_node_72
    _get_global_input_table_node_72 --> _get_global_input_table_node_73
    _get_global_input_table_node_73 --> _get_global_input_table_node_74
    _get_global_input_table_node_74 --> _get_global_input_table_node_75
    _get_global_input_table_node_75 --> _get_global_input_table_node_76
    _get_global_input_table_node_76 --> _get_global_input_table_node_77
    _get_global_input_table_node_77 --> _get_global_input_table_node_78
    _get_global_input_table_node_78 --> _get_global_input_table_node_79
    _get_global_input_table_node_79 --> _get_global_input_table_node_80
    _get_global_input_table_node_80 --> _get_global_input_table_node_81
    _get_global_input_table_node_81 --> _get_global_input_table_node_82
    _get_global_input_table_node_82 --> _get_global_input_table_node_83
    _get_global_input_table_node_83 --> _get_global_input_table_node_84
    _get_global_input_table_node_84 --> _get_global_input_table_node_85
    _get_global_input_table_node_85 --> _get_global_input_table_node_86
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
              id='global_import_table',
              ctx=Store(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=23)],
          value=Call(
            func=Name(
              id='get_global_input_table',
              ctx=Load(),
              lineno=23,
              col_offset=26,
              end_lineno=23,
              end_col_offset=48),
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
                end_col_offset=56),
              keyword(
                arg='output_root',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=24,
                  col_offset=70,
                  end_lineno=24,
                  end_col_offset=81),
                lineno=24,
                col_offset=58,
                end_lineno=24,
                end_col_offset=81)],
            lineno=23,
            col_offset=26,
            end_lineno=25,
            end_col_offset=5),
          lineno=23,
          col_offset=4,
          end_lineno=25,
          end_col_offset=5),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=27,
            col_offset=8,
            end_lineno=27,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=27,
            col_offset=19,
            end_lineno=27,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=28,
                  col_offset=8,
                  end_lineno=28,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='in_file',
                    ctx=Load(),
                    lineno=28,
                    col_offset=27,
                    end_lineno=28,
                    end_col_offset=34),
                  attr='replace',
                  ctx=Load(),
                  lineno=28,
                  col_offset=27,
                  end_lineno=28,
                  end_col_offset=42),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=28,
                    col_offset=43,
                    end_lineno=28,
                    end_col_offset=53),
                  Constant(
                    value='',
                    lineno=28,
                    col_offset=55,
                    end_lineno=28,
                    end_col_offset=57)],
                keywords=[],
                lineno=28,
                col_offset=27,
                end_lineno=28,
                end_col_offset=58),
              lineno=28,
              col_offset=8,
              end_lineno=28,
              end_col_offset=58),
            Assign(
              targets=[
                Name(
                  id='out_file',
                  ctx=Store(),
                  lineno=29,
                  col_offset=8,
                  end_lineno=29,
                  end_col_offset=16)],
              value=Call(
                func=Name(
                  id='get_output_file_path_for_input_file',
                  ctx=Load(),
                  lineno=29,
                  col_offset=19,
                  end_lineno=29,
                  end_col_offset=54),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='relative_in_file',
                      ctx=Load(),
                      lineno=30,
                      col_offset=23,
                      end_lineno=30,
                      end_col_offset=39),
                    lineno=30,
                    col_offset=12,
                    end_lineno=30,
                    end_col_offset=39),
                  keyword(
                    arg='output_root',
                    value=Name(
                      id='output_path',
                      ctx=Load(),
                      lineno=30,
                      col_offset=53,
                      end_lineno=30,
                      end_col_offset=64),
                    lineno=30,
                    col_offset=41,
                    end_lineno=30,
                    end_col_offset=64)],
                lineno=29,
                col_offset=19,
                end_lineno=31,
                end_col_offset=9),
              lineno=29,
              col_offset=8,
              end_lineno=31,
              end_col_offset=9),
            Assign(
              targets=[
                Name(
                  id='debug_dump',
                  ctx=Store(),
                  lineno=33,
                  col_offset=8,
                  end_lineno=33,
                  end_col_offset=18)],
              value=Constant(
                value='',
                lineno=33,
                col_offset=21,
                end_lineno=33,
                end_col_offset=23),
              lineno=33,
              col_offset=8,
              end_lineno=33,
              end_col_offset=23),
            Assign(
              targets=[
                Name(
                  id='import_list',
                  ctx=Store(),
                  lineno=34,
                  col_offset=8,
                  end_lineno=34,
                  end_col_offset=19)],
              value=List(
                elts=[],
                ctx=Load(),
                lineno=34,
                col_offset=22,
                end_lineno=34,
                end_col_offset=24),
              lineno=34,
              col_offset=8,
              end_lineno=34,
              end_col_offset=24),
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=36,
                  col_offset=11,
                  end_lineno=36,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=36,
                    col_offset=26,
                    end_lineno=36,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=36,
                        col_offset=63,
                        end_lineno=36,
                        end_col_offset=70),
                      lineno=36,
                      col_offset=52,
                      end_lineno=36,
                      end_col_offset=70)],
                  lineno=36,
                  col_offset=26,
                  end_lineno=36,
                  end_col_offset=71),
                lineno=36,
                col_offset=11,
                end_lineno=36,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=37,
                      col_offset=15,
                      end_lineno=37,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=37,
                        col_offset=27,
                        end_lineno=37,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=38,
                            col_offset=28,
                            end_lineno=38,
                            end_col_offset=39),
                          lineno=38,
                          col_offset=16,
                          end_lineno=38,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=39,
                            col_offset=27,
                            end_lineno=39,
                            end_col_offset=34),
                          lineno=39,
                          col_offset=16,
                          end_lineno=39,
                          end_col_offset=34)],
                      lineno=37,
                      col_offset=27,
                      end_lineno=40,
                      end_col_offset=13),
                    lineno=37,
                    col_offset=15,
                    end_lineno=40,
                    end_col_offset=13),
                  body=[
                    Assign(
                      targets=[
                        Name(
                          id='debug_dump',
                          ctx=Store(),
                          lineno=42,
                          col_offset=16,
                          end_lineno=42,
                          end_col_offset=26)],
                      value=Call(
                        func=Name(
                          id='get_markdown_dump_for_ast_node',
                          ctx=Load(),
                          lineno=42,
                          col_offset=29,
                          end_lineno=42,
                          end_col_offset=59),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=42,
                              col_offset=69,
                              end_lineno=42,
                              end_col_offset=77),
                            lineno=42,
                            col_offset=60,
                            end_lineno=42,
                            end_col_offset=77)],
                        lineno=42,
                        col_offset=29,
                        end_lineno=42,
                        end_col_offset=78),
                      lineno=42,
                      col_offset=16,
                      end_lineno=42,
                      end_col_offset=78),
                    Assign(
                      targets=[
                        Name(
                          id='import_list',
                          ctx=Store(),
                          lineno=44,
                          col_offset=16,
                          end_lineno=44,
                          end_col_offset=27)],
                      value=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=44,
                          col_offset=30,
                          end_lineno=44,
                          end_col_offset=50),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=44,
                              col_offset=60,
                              end_lineno=44,
                              end_col_offset=68),
                            lineno=44,
                            col_offset=51,
                            end_lineno=44,
                            end_col_offset=68)],
                        lineno=44,
                        col_offset=30,
                        end_lineno=44,
                        end_col_offset=69),
                      lineno=44,
                      col_offset=16,
                      end_lineno=44,
                      end_col_offset=69),
                    AnnAssign(
                      target=Name(
                        id='link_info',
                        ctx=Store(),
                        lineno=46,
                        col_offset=16,
                        end_lineno=46,
                        end_col_offset=25),
                      annotation=Subscript(
                        value=Name(
                          id='list',
                          ctx=Load(),
                          lineno=46,
                          col_offset=28,
                          end_lineno=46,
                          end_col_offset=32),
                        slice=Name(
                          id='MermaidElement',
                          ctx=Load(),
                          lineno=46,
                          col_offset=33,
                          end_lineno=46,
                          end_col_offset=47),
                        ctx=Load(),
                        lineno=46,
                        col_offset=28,
                        end_lineno=46,
                        end_col_offset=48),
                      value=Call(
                        func=Name(
                          id='create_mermaid_model_from_ast_model',
                          ctx=Load(),
                          lineno=47,
                          col_offset=20,
                          end_lineno=47,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='model',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=47,
                              col_offset=62,
                              end_lineno=47,
                              end_col_offset=70),
                            lineno=47,
                            col_offset=56,
                            end_lineno=47,
                            end_col_offset=70)],
                        lineno=47,
                        col_offset=20,
                        end_lineno=47,
                        end_col_offset=71),
                      simple=1,
                      lineno=46,
                      col_offset=16,
                      end_lineno=48,
                      end_col_offset=17),
                    Assign(
                      targets=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Store(),
                          lineno=50,
                          col_offset=16,
                          end_lineno=50,
                          end_col_offset=31)],
                      value=Call(
                        func=Name(
                          id='create_mermaid_flow_graph_from_links',
                          ctx=Load(),
                          lineno=50,
                          col_offset=34,
                          end_lineno=50,
                          end_col_offset=70),
                        args=[
                          Name(
                            id='link_info',
                            ctx=Load(),
                            lineno=50,
                            col_offset=71,
                            end_lineno=50,
                            end_col_offset=80)],
                        keywords=[],
                        lineno=50,
                        col_offset=34,
                        end_lineno=50,
                        end_col_offset=81),
                      lineno=50,
                      col_offset=16,
                      end_lineno=50,
                      end_col_offset=81)],
                  orelse=[],
                  lineno=37,
                  col_offset=12,
                  end_lineno=50,
                  end_col_offset=81)],
              orelse=[],
              lineno=36,
              col_offset=8,
              end_lineno=50,
              end_col_offset=81),
            Assign(
              targets=[
                Name(
                  id='markdown_content',
                  ctx=Store(),
                  lineno=52,
                  col_offset=8,
                  end_lineno=52,
                  end_col_offset=24)],
              value=Call(
                func=Name(
                  id='create_markdown_content',
                  ctx=Load(),
                  lineno=52,
                  col_offset=27,
                  end_lineno=52,
                  end_col_offset=50),
                args=[],
                keywords=[
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=53,
                      col_offset=23,
                      end_lineno=53,
                      end_col_offset=30),
                    lineno=53,
                    col_offset=12,
                    end_lineno=53,
                    end_col_offset=30),
                  keyword(
                    arg='import_list',
                    value=Name(
                      id='import_list',
                      ctx=Load(),
                      lineno=54,
                      col_offset=24,
                      end_lineno=54,
                      end_col_offset=35),
                    lineno=54,
                    col_offset=12,
                    end_lineno=54,
                    end_col_offset=35),
                  keyword(
                    arg='global_import_table',
                    value=Name(
                      id='global_import_table',
                      ctx=Load(),
                      lineno=55,
                      col_offset=32,
                      end_lineno=55,
                      end_col_offset=51),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=51),
                  keyword(
                    arg='mermaid_diagrams',
                    value=List(
                      elts=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Load(),
                          lineno=56,
                          col_offset=30,
                          end_lineno=56,
                          end_col_offset=45)],
                      ctx=Load(),
                      lineno=56,
                      col_offset=29,
                      end_lineno=56,
                      end_col_offset=46),
                    lineno=56,
                    col_offset=12,
                    end_lineno=56,
                    end_col_offset=46),
                  keyword(
                    arg='debug_dump',
                    value=Name(
                      id='debug_dump',
                      ctx=Load(),
                      lineno=57,
                      col_offset=23,
                      end_lineno=57,
                      end_col_offset=33),
                    lineno=57,
                    col_offset=12,
                    end_lineno=57,
                    end_col_offset=33)],
                lineno=52,
                col_offset=27,
                end_lineno=58,
                end_col_offset=9),
              lineno=52,
              col_offset=8,
              end_lineno=58,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Name(
                  id='update_output_file',
                  ctx=Load(),
                  lineno=60,
                  col_offset=8,
                  end_lineno=60,
                  end_col_offset=26),
                args=[],
                keywords=[
                  keyword(
                    arg='content',
                    value=Name(
                      id='markdown_content',
                      ctx=Load(),
                      lineno=60,
                      col_offset=35,
                      end_lineno=60,
                      end_col_offset=51),
                    lineno=60,
                    col_offset=27,
                    end_lineno=60,
                    end_col_offset=51),
                  keyword(
                    arg='output_file',
                    value=Name(
                      id='out_file',
                      ctx=Load(),
                      lineno=60,
                      col_offset=65,
                      end_lineno=60,
                      end_col_offset=73),
                    lineno=60,
                    col_offset=53,
                    end_lineno=60,
                    end_col_offset=73)],
                lineno=60,
                col_offset=8,
                end_lineno=60,
                end_col_offset=74),
              lineno=60,
              col_offset=8,
              end_lineno=60,
              end_col_offset=74)],
          orelse=[],
          lineno=27,
          col_offset=4,
          end_lineno=60,
          end_col_offset=74)],
      decorator_list=[],
      lineno=20,
      col_offset=0,
      end_lineno=60,
      end_col_offset=74),
    FunctionDef(
      name='get_global_input_table',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=63,
              col_offset=16,
              end_lineno=63,
              end_col_offset=19),
            lineno=63,
            col_offset=4,
            end_lineno=63,
            end_col_offset=19),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=63,
                col_offset=35,
                end_lineno=63,
                end_col_offset=39),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=63,
                col_offset=40,
                end_lineno=63,
                end_col_offset=43),
              ctx=Load(),
              lineno=63,
              col_offset=35,
              end_lineno=63,
              end_col_offset=44),
            lineno=63,
            col_offset=21,
            end_lineno=63,
            end_col_offset=44),
          arg(
            arg='output_root',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=63,
              col_offset=59,
              end_lineno=63,
              end_col_offset=62),
            lineno=63,
            col_offset=46,
            end_lineno=63,
            end_col_offset=62)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='global_import_table',
              ctx=Store(),
              lineno=65,
              col_offset=4,
              end_lineno=65,
              end_col_offset=23)],
          value=Call(
            func=Name(
              id='get_all_imports_from_files',
              ctx=Load(),
              lineno=65,
              col_offset=26,
              end_lineno=65,
              end_col_offset=52),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=66,
                  col_offset=19,
                  end_lineno=66,
                  end_col_offset=29),
                lineno=66,
                col_offset=8,
                end_lineno=66,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=66,
                  col_offset=44,
                  end_lineno=66,
                  end_col_offset=56),
                lineno=66,
                col_offset=31,
                end_lineno=66,
                end_col_offset=56)],
            lineno=65,
            col_offset=26,
            end_lineno=67,
            end_col_offset=5),
          lineno=65,
          col_offset=4,
          end_lineno=67,
          end_col_offset=5),
        For(
          target=Name(
            id='global_import',
            ctx=Store(),
            lineno=68,
            col_offset=8,
            end_lineno=68,
            end_col_offset=21),
          iter=Name(
            id='global_import_table',
            ctx=Load(),
            lineno=68,
            col_offset=25,
            end_lineno=68,
            end_col_offset=44),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=69,
                  col_offset=8,
                  end_lineno=69,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Subscript(
                    value=Name(
                      id='global_import_table',
                      ctx=Load(),
                      lineno=69,
                      col_offset=27,
                      end_lineno=69,
                      end_col_offset=46),
                    slice=Name(
                      id='global_import',
                      ctx=Load(),
                      lineno=69,
                      col_offset=47,
                      end_lineno=69,
                      end_col_offset=60),
                    ctx=Load(),
                    lineno=69,
                    col_offset=27,
                    end_lineno=69,
                    end_col_offset=61),
                  attr='replace',
                  ctx=Load(),
                  lineno=69,
                  col_offset=27,
                  end_lineno=69,
                  end_col_offset=69),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=69,
                    col_offset=70,
                    end_lineno=69,
                    end_col_offset=80),
                  Constant(
                    value='',
                    lineno=69,
                    col_offset=82,
                    end_lineno=69,
                    end_col_offset=84)],
                keywords=[],
                lineno=69,
                col_offset=27,
                end_lineno=69,
                end_col_offset=85),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=85),
            If(
              test=Name(
                id='relative_in_file',
                ctx=Load(),
                lineno=70,
                col_offset=11,
                end_lineno=70,
                end_col_offset=27),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Name(
                        id='global_import_table',
                        ctx=Load(),
                        lineno=71,
                        col_offset=12,
                        end_lineno=71,
                        end_col_offset=31),
                      slice=Name(
                        id='global_import',
                        ctx=Load(),
                        lineno=71,
                        col_offset=32,
                        end_lineno=71,
                        end_col_offset=45),
                      ctx=Store(),
                      lineno=71,
                      col_offset=12,
                      end_lineno=71,
                      end_col_offset=46)],
                  value=Call(
                    func=Attribute(
                      value=Call(
                        func=Name(
                          id='get_output_file_path_for_input_file',
                          ctx=Load(),
                          lineno=71,
                          col_offset=49,
                          end_lineno=71,
                          end_col_offset=84),
                        args=[],
                        keywords=[
                          keyword(
                            arg='input_path',
                            value=Name(
                              id='relative_in_file',
                              ctx=Load(),
                              lineno=72,
                              col_offset=27,
                              end_lineno=72,
                              end_col_offset=43),
                            lineno=72,
                            col_offset=16,
                            end_lineno=72,
                            end_col_offset=43),
                          keyword(
                            arg='output_root',
                            value=Name(
                              id='output_root',
                              ctx=Load(),
                              lineno=72,
                              col_offset=57,
                              end_lineno=72,
                              end_col_offset=68),
                            lineno=72,
                            col_offset=45,
                            end_lineno=72,
                            end_col_offset=68)],
                        lineno=71,
                        col_offset=49,
                        end_lineno=73,
                        end_col_offset=13),
                      attr='lstrip',
                      ctx=Load(),
                      lineno=71,
                      col_offset=49,
                      end_lineno=73,
                      end_col_offset=20),
                    args=[
                      Constant(
                        value='.',
                        lineno=73,
                        col_offset=21,
                        end_lineno=73,
                        end_col_offset=24)],
                    keywords=[],
                    lineno=71,
                    col_offset=49,
                    end_lineno=73,
                    end_col_offset=25),
                  lineno=71,
                  col_offset=12,
                  end_lineno=73,
                  end_col_offset=25)],
              orelse=[],
              lineno=70,
              col_offset=8,
              end_lineno=73,
              end_col_offset=25)],
          orelse=[],
          lineno=68,
          col_offset=4,
          end_lineno=73,
          end_col_offset=25),
        Expr(
          value=Call(
            func=Name(
              id='print',
              ctx=Load(),
              lineno=74,
              col_offset=4,
              end_lineno=74,
              end_col_offset=9),
            args=[
              Call(
                func=Attribute(
                  value=Constant(
                    value='\n',
                    lineno=74,
                    col_offset=10,
                    end_lineno=74,
                    end_col_offset=14),
                  attr='join',
                  ctx=Load(),
                  lineno=74,
                  col_offset=10,
                  end_lineno=74,
                  end_col_offset=19),
                args=[
                  ListComp(
                    elt=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Name(
                            id='k',
                            ctx=Load(),
                            lineno=74,
                            col_offset=24,
                            end_lineno=74,
                            end_col_offset=25),
                          conversion=-1,
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32),
                        Constant(
                          value=': ',
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32),
                        FormattedValue(
                          value=Name(
                            id='v',
                            ctx=Load(),
                            lineno=74,
                            col_offset=29,
                            end_lineno=74,
                            end_col_offset=30),
                          conversion=-1,
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32)],
                      lineno=74,
                      col_offset=21,
                      end_lineno=74,
                      end_col_offset=32),
                    generators=[
                      comprehension(
                        target=Tuple(
                          elts=[
                            Name(
                              id='k',
                              ctx=Store(),
                              lineno=74,
                              col_offset=37,
                              end_lineno=74,
                              end_col_offset=38),
                            Name(
                              id='v',
                              ctx=Store(),
                              lineno=74,
                              col_offset=39,
                              end_lineno=74,
                              end_col_offset=40)],
                          ctx=Store(),
                          lineno=74,
                          col_offset=37,
                          end_lineno=74,
                          end_col_offset=40),
                        iter=Call(
                          func=Attribute(
                            value=Name(
                              id='global_import_table',
                              ctx=Load(),
                              lineno=74,
                              col_offset=44,
                              end_lineno=74,
                              end_col_offset=63),
                            attr='items',
                            ctx=Load(),
                            lineno=74,
                            col_offset=44,
                            end_lineno=74,
                            end_col_offset=69),
                          args=[],
                          keywords=[],
                          lineno=74,
                          col_offset=44,
                          end_lineno=74,
                          end_col_offset=71),
                        ifs=[],
                        is_async=0)],
                    lineno=74,
                    col_offset=20,
                    end_lineno=74,
                    end_col_offset=72)],
                keywords=[],
                lineno=74,
                col_offset=10,
                end_lineno=74,
                end_col_offset=73)],
            keywords=[],
            lineno=74,
            col_offset=4,
            end_lineno=74,
            end_col_offset=74),
          lineno=74,
          col_offset=4,
          end_lineno=74,
          end_col_offset=74),
        Return(
          value=Name(
            id='global_import_table',
            ctx=Load(),
            lineno=75,
            col_offset=11,
            end_lineno=75,
            end_col_offset=30),
          lineno=75,
          col_offset=4,
          end_lineno=75,
          end_col_offset=30)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=64,
          col_offset=5,
          end_lineno=64,
          end_col_offset=9),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=64,
              col_offset=10,
              end_lineno=64,
              end_col_offset=13),
            Name(
              id='str',
              ctx=Load(),
              lineno=64,
              col_offset=14,
              end_lineno=64,
              end_col_offset=17)],
          ctx=Load(),
          lineno=64,
          col_offset=10,
          end_lineno=64,
          end_col_offset=17),
        ctx=Load(),
        lineno=64,
        col_offset=5,
        end_lineno=64,
        end_col_offset=18),
      lineno=62,
      col_offset=0,
      end_lineno=75,
      end_col_offset=30),
    If(
      test=Compare(
        left=Name(
          id='__name__',
          ctx=Load(),
          lineno=78,
          col_offset=3,
          end_lineno=78,
          end_col_offset=11),
        ops=[
          Eq()],
        comparators=[
          Constant(
            value='__main__',
            lineno=78,
            col_offset=15,
            end_lineno=78,
            end_col_offset=25)],
        lineno=78,
        col_offset=3,
        end_lineno=78,
        end_col_offset=25),
      body=[
        Assign(
          targets=[
            Name(
              id='input_path',
              ctx=Store(),
              lineno=81,
              col_offset=4,
              end_lineno=81,
              end_col_offset=14)],
          value=Constant(
            value='./src/pyremaid/',
            lineno=81,
            col_offset=17,
            end_lineno=81,
            end_col_offset=34),
          lineno=81,
          col_offset=4,
          end_lineno=81,
          end_col_offset=34),
        Assign(
          targets=[
            Name(
              id='output_path',
              ctx=Store(),
              lineno=82,
              col_offset=4,
              end_lineno=82,
              end_col_offset=15)],
          value=Constant(
            value='./docs/pyremaid/',
            lineno=82,
            col_offset=18,
            end_lineno=82,
            end_col_offset=36),
          lineno=82,
          col_offset=4,
          end_lineno=82,
          end_col_offset=36),
        Expr(
          value=Call(
            func=Name(
              id='create_mermaid_analysis_from_python',
              ctx=Load(),
              lineno=83,
              col_offset=4,
              end_lineno=83,
              end_col_offset=39),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=83,
                  col_offset=51,
                  end_lineno=83,
                  end_col_offset=61),
                lineno=83,
                col_offset=40,
                end_lineno=83,
                end_col_offset=61),
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=83,
                  col_offset=75,
                  end_lineno=83,
                  end_col_offset=86),
                lineno=83,
                col_offset=63,
                end_lineno=83,
                end_col_offset=86)],
            lineno=83,
            col_offset=4,
            end_lineno=83,
            end_col_offset=87),
          lineno=83,
          col_offset=4,
          end_lineno=83,
          end_col_offset=87)],
      orelse=[],
      lineno=78,
      col_offset=0,
      end_lineno=83,
      end_col_offset=87)],
  type_ignores=[])
```
</details>

