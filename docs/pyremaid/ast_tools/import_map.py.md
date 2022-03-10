# ./src/pyremaid/ast_tools/import_map.py

### Imports

  - ast_tools.get_ast_root_node_for_file
  - ast_tools.get_used_import_list
  - files.source.get_source_code_from_file
  - files.source.get_import_name_from_path

---
```mermaid
flowchart TB
  ___init___node_0["AnnAssign"]
  ___init___node_1["Attribute"]
  ___init___node_2["Name"]
  ___init___node_3["Load"]
  ___init___node_4["Store"]
  ___init___node_5["Subscript"]
  ___init___node_6["Name"]
  ___init___node_7["Load"]
  ___init___node_8["Tuple"]
  ___init___node_9["Name"]
  ___init___node_10["Load"]
  ___init___node_11["Subscript"]
  ___init___node_12["Name"]
  ___init___node_13["Load"]
  ___init___node_14["Name"]
  ___init___node_15["Load"]
  ___init___node_16["Load"]
  ___init___node_17["Load"]
  ___init___node_18["Load"]
  ___init___node_19["Dict"]
  ___init___node_20["AnnAssign"]
  ___init___node_21["Attribute"]
  ___init___node_22["Name"]
  ___init___node_23["Load"]
  ___init___node_24["Store"]
  ___init___node_25["Subscript"]
  ___init___node_26["Name"]
  ___init___node_27["Load"]
  ___init___node_28["Tuple"]
  ___init___node_29["Name"]
  ___init___node_30["Load"]
  ___init___node_31["Subscript"]
  ___init___node_32["Name"]
  ___init___node_33["Load"]
  ___init___node_34["Name"]
  ___init___node_35["Load"]
  ___init___node_36["Load"]
  ___init___node_37["Load"]
  ___init___node_38["Load"]
  ___init___node_39["Dict"]
  _add_import_node_0["If"]
  _add_import_node_1["Compare"]
  _add_import_node_2["Name"]
  _add_import_node_3["Load"]
  _add_import_node_4["NotIn"]
  _add_import_node_5["Attribute"]
  _add_import_node_6["Name"]
  _add_import_node_7["Load"]
  _add_import_node_8["Load"]
  _add_import_node_9["Assign"]
  _add_import_node_10["Subscript"]
  _add_import_node_11["Attribute"]
  _add_import_node_12["Name"]
  _add_import_node_13["Load"]
  _add_import_node_14["Load"]
  _add_import_node_15["Name"]
  _add_import_node_16["Load"]
  _add_import_node_17["Store"]
  _add_import_node_18["List"]
  _add_import_node_19["Load"]
  _add_import_node_20["Expr"]
  _add_import_node_21["Call"]
  _add_import_node_22["Attribute"]
  _add_import_node_23["Subscript"]
  _add_import_node_24["Attribute"]
  _add_import_node_25["Name"]
  _add_import_node_26["Load"]
  _add_import_node_27["Load"]
  _add_import_node_28["Name"]
  _add_import_node_29["Load"]
  _add_import_node_30["Load"]
  _add_import_node_31["Load"]
  _add_import_node_32["Name"]
  _add_import_node_33["Load"]
  _add_import_node_34["If"]
  _add_import_node_35["Compare"]
  _add_import_node_36["Name"]
  _add_import_node_37["Load"]
  _add_import_node_38["NotIn"]
  _add_import_node_39["Attribute"]
  _add_import_node_40["Name"]
  _add_import_node_41["Load"]
  _add_import_node_42["Load"]
  _add_import_node_43["Assign"]
  _add_import_node_44["Subscript"]
  _add_import_node_45["Attribute"]
  _add_import_node_46["Name"]
  _add_import_node_47["Load"]
  _add_import_node_48["Load"]
  _add_import_node_49["Name"]
  _add_import_node_50["Load"]
  _add_import_node_51["Store"]
  _add_import_node_52["List"]
  _add_import_node_53["Load"]
  _add_import_node_54["Expr"]
  _add_import_node_55["Subscript"]
  _add_import_node_56["Attribute"]
  _add_import_node_57["Subscript"]
  _add_import_node_58["Attribute"]
  _add_import_node_59["Name"]
  _add_import_node_60["Load"]
  _add_import_node_61["Load"]
  _add_import_node_62["Name"]
  _add_import_node_63["Load"]
  _add_import_node_64["Load"]
  _add_import_node_65["Load"]
  _add_import_node_66["Name"]
  _add_import_node_67["Load"]
  _add_import_node_68["Load"]
  __get_import_to_file_map_node_0["Expr"]
  __get_import_to_file_map_node_1["Constant"]
  __get_import_to_file_map_node_2["Assign"]
  __get_import_to_file_map_node_3["Name"]
  __get_import_to_file_map_node_4["Store"]
  __get_import_to_file_map_node_5["Dict"]
  __get_import_to_file_map_node_6["For"]
  __get_import_to_file_map_node_7["Name"]
  __get_import_to_file_map_node_8["Store"]
  __get_import_to_file_map_node_9["Name"]
  __get_import_to_file_map_node_10["Load"]
  __get_import_to_file_map_node_11["Assign"]
  __get_import_to_file_map_node_12["Name"]
  __get_import_to_file_map_node_13["Store"]
  __get_import_to_file_map_node_14["Call"]
  __get_import_to_file_map_node_15["Name"]
  __get_import_to_file_map_node_16["Load"]
  __get_import_to_file_map_node_17["keyword"]
  __get_import_to_file_map_node_18["Name"]
  __get_import_to_file_map_node_19["Load"]
  __get_import_to_file_map_node_20["keyword"]
  __get_import_to_file_map_node_21["Name"]
  __get_import_to_file_map_node_22["Load"]
  __get_import_to_file_map_node_23["Assign"]
  __get_import_to_file_map_node_24["Subscript"]
  __get_import_to_file_map_node_25["Name"]
  __get_import_to_file_map_node_26["Load"]
  __get_import_to_file_map_node_27["Name"]
  __get_import_to_file_map_node_28["Load"]
  __get_import_to_file_map_node_29["Store"]
  __get_import_to_file_map_node_30["Name"]
  __get_import_to_file_map_node_31["Load"]
  __get_import_to_file_map_node_32["Return"]
  __get_import_to_file_map_node_33["Name"]
  __get_import_to_file_map_node_34["Load"]
  __get_parent_import_node_0["Return"]
  __get_parent_import_node_1["Subscript"]
  __get_parent_import_node_2["Name"]
  __get_parent_import_node_3["Load"]
  __get_parent_import_node_4["Slice"]
  __get_parent_import_node_5["Constant"]
  __get_parent_import_node_6["Call"]
  __get_parent_import_node_7["Attribute"]
  __get_parent_import_node_8["Name"]
  __get_parent_import_node_9["Load"]
  __get_parent_import_node_10["Load"]
  __get_parent_import_node_11["Constant"]
  __get_parent_import_node_12["Load"]
  __create_import_table_node_0["Assign"]
  __create_import_table_node_1["Name"]
  __create_import_table_node_2["Store"]
  __create_import_table_node_3["Dict"]
  __create_import_table_node_4["For"]
  __create_import_table_node_5["Name"]
  __create_import_table_node_6["Store"]
  __create_import_table_node_7["Name"]
  __create_import_table_node_8["Load"]
  __create_import_table_node_9["If"]
  __create_import_table_node_10["NamedExpr"]
  __create_import_table_node_11["Name"]
  __create_import_table_node_12["Store"]
  __create_import_table_node_13["Call"]
  __create_import_table_node_14["Name"]
  __create_import_table_node_15["Load"]
  __create_import_table_node_16["keyword"]
  __create_import_table_node_17["Name"]
  __create_import_table_node_18["Load"]
  __create_import_table_node_19["If"]
  __create_import_table_node_20["NamedExpr"]
  __create_import_table_node_21["Name"]
  __create_import_table_node_22["Store"]
  __create_import_table_node_23["Call"]
  __create_import_table_node_24["Name"]
  __create_import_table_node_25["Load"]
  __create_import_table_node_26["keyword"]
  __create_import_table_node_27["Name"]
  __create_import_table_node_28["Load"]
  __create_import_table_node_29["keyword"]
  __create_import_table_node_30["Name"]
  __create_import_table_node_31["Load"]
  __create_import_table_node_32["For"]
  __create_import_table_node_33["Name"]
  __create_import_table_node_34["Store"]
  __create_import_table_node_35["Call"]
  __create_import_table_node_36["Name"]
  __create_import_table_node_37["Load"]
  __create_import_table_node_38["keyword"]
  __create_import_table_node_39["Name"]
  __create_import_table_node_40["Load"]
  __create_import_table_node_41["Assign"]
  __create_import_table_node_42["Name"]
  __create_import_table_node_43["Store"]
  __create_import_table_node_44["Constant"]
  __create_import_table_node_45["Assign"]
  __create_import_table_node_46["Name"]
  __create_import_table_node_47["Store"]
  __create_import_table_node_48["Call"]
  __create_import_table_node_49["Name"]
  __create_import_table_node_50["Load"]
  __create_import_table_node_51["Name"]
  __create_import_table_node_52["Load"]
  __create_import_table_node_53["If"]
  __create_import_table_node_54["Compare"]
  __create_import_table_node_55["Name"]
  __create_import_table_node_56["Load"]
  __create_import_table_node_57["In"]
  __create_import_table_node_58["Name"]
  __create_import_table_node_59["Load"]
  __create_import_table_node_60["Assign"]
  __create_import_table_node_61["Name"]
  __create_import_table_node_62["Store"]
  __create_import_table_node_63["Subscript"]
  __create_import_table_node_64["Name"]
  __create_import_table_node_65["Load"]
  __create_import_table_node_66["Name"]
  __create_import_table_node_67["Load"]
  __create_import_table_node_68["Load"]
  __create_import_table_node_69["Assign"]
  __create_import_table_node_70["Subscript"]
  __create_import_table_node_71["Name"]
  __create_import_table_node_72["Load"]
  __create_import_table_node_73["Name"]
  __create_import_table_node_74["Load"]
  __create_import_table_node_75["Store"]
  __create_import_table_node_76["Name"]
  __create_import_table_node_77["Load"]
  __create_import_table_node_78["Return"]
  __create_import_table_node_79["Name"]
  __create_import_table_node_80["Load"]
  _get_all_imports_from_files_node_0["Expr"]
  _get_all_imports_from_files_node_1["Constant"]
  _get_all_imports_from_files_node_2["Assign"]
  _get_all_imports_from_files_node_3["Name"]
  _get_all_imports_from_files_node_4["Store"]
  _get_all_imports_from_files_node_5["Call"]
  _get_all_imports_from_files_node_6["Name"]
  _get_all_imports_from_files_node_7["Load"]
  _get_all_imports_from_files_node_8["keyword"]
  _get_all_imports_from_files_node_9["Name"]
  _get_all_imports_from_files_node_10["Load"]
  _get_all_imports_from_files_node_11["keyword"]
  _get_all_imports_from_files_node_12["Name"]
  _get_all_imports_from_files_node_13["Load"]
  _get_all_imports_from_files_node_14["Assign"]
  _get_all_imports_from_files_node_15["Name"]
  _get_all_imports_from_files_node_16["Store"]
  _get_all_imports_from_files_node_17["Call"]
  _get_all_imports_from_files_node_18["Name"]
  _get_all_imports_from_files_node_19["Load"]
  _get_all_imports_from_files_node_20["keyword"]
  _get_all_imports_from_files_node_21["Name"]
  _get_all_imports_from_files_node_22["Load"]
  _get_all_imports_from_files_node_23["keyword"]
  _get_all_imports_from_files_node_24["Name"]
  _get_all_imports_from_files_node_25["Load"]
  _get_all_imports_from_files_node_26["Return"]
  _get_all_imports_from_files_node_27["Name"]
  _get_all_imports_from_files_node_28["Load"]

  subgraph __init__
    direction TB
    ___init___node_0 --> ___init___node_1
    ___init___node_1 --> ___init___node_2
    ___init___node_2 --> ___init___node_3
    ___init___node_3 --> ___init___node_4
    ___init___node_4 --> ___init___node_5
    ___init___node_5 --> ___init___node_6
    ___init___node_6 --> ___init___node_7
    ___init___node_7 --> ___init___node_8
    ___init___node_8 --> ___init___node_9
    ___init___node_9 --> ___init___node_10
    ___init___node_10 --> ___init___node_11
    ___init___node_11 --> ___init___node_12
    ___init___node_12 --> ___init___node_13
    ___init___node_13 --> ___init___node_14
    ___init___node_14 --> ___init___node_15
    ___init___node_15 --> ___init___node_16
    ___init___node_16 --> ___init___node_17
    ___init___node_17 --> ___init___node_18
    ___init___node_18 --> ___init___node_19
    ___init___node_19 --> ___init___node_20
    ___init___node_20 --> ___init___node_21
    ___init___node_21 --> ___init___node_22
    ___init___node_22 --> ___init___node_23
    ___init___node_23 --> ___init___node_24
    ___init___node_24 --> ___init___node_25
    ___init___node_25 --> ___init___node_26
    ___init___node_26 --> ___init___node_27
    ___init___node_27 --> ___init___node_28
    ___init___node_28 --> ___init___node_29
    ___init___node_29 --> ___init___node_30
    ___init___node_30 --> ___init___node_31
    ___init___node_31 --> ___init___node_32
    ___init___node_32 --> ___init___node_33
    ___init___node_33 --> ___init___node_34
    ___init___node_34 --> ___init___node_35
    ___init___node_35 --> ___init___node_36
    ___init___node_36 --> ___init___node_37
    ___init___node_37 --> ___init___node_38
    ___init___node_38 --> ___init___node_39
  end
  subgraph add_import
    direction TB
    _add_import_node_0 --> _add_import_node_1
    _add_import_node_1 --> _add_import_node_2
    _add_import_node_2 --> _add_import_node_3
    _add_import_node_3 --> _add_import_node_4
    _add_import_node_4 --> _add_import_node_5
    _add_import_node_5 --> _add_import_node_6
    _add_import_node_6 --> _add_import_node_7
    _add_import_node_7 --> _add_import_node_8
    _add_import_node_8 --> _add_import_node_9
    _add_import_node_9 --> _add_import_node_10
    _add_import_node_10 --> _add_import_node_11
    _add_import_node_11 --> _add_import_node_12
    _add_import_node_12 --> _add_import_node_13
    _add_import_node_13 --> _add_import_node_14
    _add_import_node_14 --> _add_import_node_15
    _add_import_node_15 --> _add_import_node_16
    _add_import_node_16 --> _add_import_node_17
    _add_import_node_17 --> _add_import_node_18
    _add_import_node_18 --> _add_import_node_19
    _add_import_node_19 --> _add_import_node_20
    _add_import_node_20 --> _add_import_node_21
    _add_import_node_21 --> _add_import_node_22
    _add_import_node_22 --> _add_import_node_23
    _add_import_node_23 --> _add_import_node_24
    _add_import_node_24 --> _add_import_node_25
    _add_import_node_25 --> _add_import_node_26
    _add_import_node_26 --> _add_import_node_27
    _add_import_node_27 --> _add_import_node_28
    _add_import_node_28 --> _add_import_node_29
    _add_import_node_29 --> _add_import_node_30
    _add_import_node_30 --> _add_import_node_31
    _add_import_node_31 --> _add_import_node_32
    _add_import_node_32 --> _add_import_node_33
    _add_import_node_33 --> _add_import_node_34
    _add_import_node_34 --> _add_import_node_35
    _add_import_node_35 --> _add_import_node_36
    _add_import_node_36 --> _add_import_node_37
    _add_import_node_37 --> _add_import_node_38
    _add_import_node_38 --> _add_import_node_39
    _add_import_node_39 --> _add_import_node_40
    _add_import_node_40 --> _add_import_node_41
    _add_import_node_41 --> _add_import_node_42
    _add_import_node_42 --> _add_import_node_43
    _add_import_node_43 --> _add_import_node_44
    _add_import_node_44 --> _add_import_node_45
    _add_import_node_45 --> _add_import_node_46
    _add_import_node_46 --> _add_import_node_47
    _add_import_node_47 --> _add_import_node_48
    _add_import_node_48 --> _add_import_node_49
    _add_import_node_49 --> _add_import_node_50
    _add_import_node_50 --> _add_import_node_51
    _add_import_node_51 --> _add_import_node_52
    _add_import_node_52 --> _add_import_node_53
    _add_import_node_53 --> _add_import_node_54
    _add_import_node_54 --> _add_import_node_55
    _add_import_node_55 --> _add_import_node_56
    _add_import_node_56 --> _add_import_node_57
    _add_import_node_57 --> _add_import_node_58
    _add_import_node_58 --> _add_import_node_59
    _add_import_node_59 --> _add_import_node_60
    _add_import_node_60 --> _add_import_node_61
    _add_import_node_61 --> _add_import_node_62
    _add_import_node_62 --> _add_import_node_63
    _add_import_node_63 --> _add_import_node_64
    _add_import_node_64 --> _add_import_node_65
    _add_import_node_65 --> _add_import_node_66
    _add_import_node_66 --> _add_import_node_67
    _add_import_node_67 --> _add_import_node_68
  end
  subgraph _get_import_to_file_map
    direction TB
    __get_import_to_file_map_node_0 --> __get_import_to_file_map_node_1
    __get_import_to_file_map_node_1 --> __get_import_to_file_map_node_2
    __get_import_to_file_map_node_2 --> __get_import_to_file_map_node_3
    __get_import_to_file_map_node_3 --> __get_import_to_file_map_node_4
    __get_import_to_file_map_node_4 --> __get_import_to_file_map_node_5
    __get_import_to_file_map_node_5 --> __get_import_to_file_map_node_6
    __get_import_to_file_map_node_6 --> __get_import_to_file_map_node_7
    __get_import_to_file_map_node_7 --> __get_import_to_file_map_node_8
    __get_import_to_file_map_node_8 --> __get_import_to_file_map_node_9
    __get_import_to_file_map_node_9 --> __get_import_to_file_map_node_10
    __get_import_to_file_map_node_10 --> __get_import_to_file_map_node_11
    __get_import_to_file_map_node_11 --> __get_import_to_file_map_node_12
    __get_import_to_file_map_node_12 --> __get_import_to_file_map_node_13
    __get_import_to_file_map_node_13 --> __get_import_to_file_map_node_14
    __get_import_to_file_map_node_14 --> __get_import_to_file_map_node_15
    __get_import_to_file_map_node_15 --> __get_import_to_file_map_node_16
    __get_import_to_file_map_node_16 --> __get_import_to_file_map_node_17
    __get_import_to_file_map_node_17 --> __get_import_to_file_map_node_18
    __get_import_to_file_map_node_18 --> __get_import_to_file_map_node_19
    __get_import_to_file_map_node_19 --> __get_import_to_file_map_node_20
    __get_import_to_file_map_node_20 --> __get_import_to_file_map_node_21
    __get_import_to_file_map_node_21 --> __get_import_to_file_map_node_22
    __get_import_to_file_map_node_22 --> __get_import_to_file_map_node_23
    __get_import_to_file_map_node_23 --> __get_import_to_file_map_node_24
    __get_import_to_file_map_node_24 --> __get_import_to_file_map_node_25
    __get_import_to_file_map_node_25 --> __get_import_to_file_map_node_26
    __get_import_to_file_map_node_26 --> __get_import_to_file_map_node_27
    __get_import_to_file_map_node_27 --> __get_import_to_file_map_node_28
    __get_import_to_file_map_node_28 --> __get_import_to_file_map_node_29
    __get_import_to_file_map_node_29 --> __get_import_to_file_map_node_30
    __get_import_to_file_map_node_30 --> __get_import_to_file_map_node_31
    __get_import_to_file_map_node_31 --> __get_import_to_file_map_node_32
    __get_import_to_file_map_node_32 --> __get_import_to_file_map_node_33
    __get_import_to_file_map_node_33 --> __get_import_to_file_map_node_34
  end
  subgraph _get_parent_import
    direction TB
    __get_parent_import_node_0 --> __get_parent_import_node_1
    __get_parent_import_node_1 --> __get_parent_import_node_2
    __get_parent_import_node_2 --> __get_parent_import_node_3
    __get_parent_import_node_3 --> __get_parent_import_node_4
    __get_parent_import_node_4 --> __get_parent_import_node_5
    __get_parent_import_node_5 --> __get_parent_import_node_6
    __get_parent_import_node_6 --> __get_parent_import_node_7
    __get_parent_import_node_7 --> __get_parent_import_node_8
    __get_parent_import_node_8 --> __get_parent_import_node_9
    __get_parent_import_node_9 --> __get_parent_import_node_10
    __get_parent_import_node_10 --> __get_parent_import_node_11
    __get_parent_import_node_11 --> __get_parent_import_node_12
  end
  subgraph _create_import_table
    direction TB
    __create_import_table_node_0 --> __create_import_table_node_1
    __create_import_table_node_1 --> __create_import_table_node_2
    __create_import_table_node_2 --> __create_import_table_node_3
    __create_import_table_node_3 --> __create_import_table_node_4
    __create_import_table_node_4 --> __create_import_table_node_5
    __create_import_table_node_5 --> __create_import_table_node_6
    __create_import_table_node_6 --> __create_import_table_node_7
    __create_import_table_node_7 --> __create_import_table_node_8
    __create_import_table_node_8 --> __create_import_table_node_9
    __create_import_table_node_9 --> __create_import_table_node_10
    __create_import_table_node_10 --> __create_import_table_node_11
    __create_import_table_node_11 --> __create_import_table_node_12
    __create_import_table_node_12 --> __create_import_table_node_13
    __create_import_table_node_13 --> __create_import_table_node_14
    __create_import_table_node_14 --> __create_import_table_node_15
    __create_import_table_node_15 --> __create_import_table_node_16
    __create_import_table_node_16 --> __create_import_table_node_17
    __create_import_table_node_17 --> __create_import_table_node_18
    __create_import_table_node_18 --> __create_import_table_node_19
    __create_import_table_node_19 --> __create_import_table_node_20
    __create_import_table_node_20 --> __create_import_table_node_21
    __create_import_table_node_21 --> __create_import_table_node_22
    __create_import_table_node_22 --> __create_import_table_node_23
    __create_import_table_node_23 --> __create_import_table_node_24
    __create_import_table_node_24 --> __create_import_table_node_25
    __create_import_table_node_25 --> __create_import_table_node_26
    __create_import_table_node_26 --> __create_import_table_node_27
    __create_import_table_node_27 --> __create_import_table_node_28
    __create_import_table_node_28 --> __create_import_table_node_29
    __create_import_table_node_29 --> __create_import_table_node_30
    __create_import_table_node_30 --> __create_import_table_node_31
    __create_import_table_node_31 --> __create_import_table_node_32
    __create_import_table_node_32 --> __create_import_table_node_33
    __create_import_table_node_33 --> __create_import_table_node_34
    __create_import_table_node_34 --> __create_import_table_node_35
    __create_import_table_node_35 --> __create_import_table_node_36
    __create_import_table_node_36 --> __create_import_table_node_37
    __create_import_table_node_37 --> __create_import_table_node_38
    __create_import_table_node_38 --> __create_import_table_node_39
    __create_import_table_node_39 --> __create_import_table_node_40
    __create_import_table_node_40 --> __create_import_table_node_41
    __create_import_table_node_41 --> __create_import_table_node_42
    __create_import_table_node_42 --> __create_import_table_node_43
    __create_import_table_node_43 --> __create_import_table_node_44
    __create_import_table_node_44 --> __create_import_table_node_45
    __create_import_table_node_45 --> __create_import_table_node_46
    __create_import_table_node_46 --> __create_import_table_node_47
    __create_import_table_node_47 --> __create_import_table_node_48
    __create_import_table_node_48 --> __create_import_table_node_49
    __create_import_table_node_49 --> __create_import_table_node_50
    __create_import_table_node_50 --> __create_import_table_node_51
    __create_import_table_node_51 --> __create_import_table_node_52
    __create_import_table_node_52 --> __create_import_table_node_53
    __create_import_table_node_53 --> __create_import_table_node_54
    __create_import_table_node_54 --> __create_import_table_node_55
    __create_import_table_node_55 --> __create_import_table_node_56
    __create_import_table_node_56 --> __create_import_table_node_57
    __create_import_table_node_57 --> __create_import_table_node_58
    __create_import_table_node_58 --> __create_import_table_node_59
    __create_import_table_node_59 --> __create_import_table_node_60
    __create_import_table_node_60 --> __create_import_table_node_61
    __create_import_table_node_61 --> __create_import_table_node_62
    __create_import_table_node_62 --> __create_import_table_node_63
    __create_import_table_node_63 --> __create_import_table_node_64
    __create_import_table_node_64 --> __create_import_table_node_65
    __create_import_table_node_65 --> __create_import_table_node_66
    __create_import_table_node_66 --> __create_import_table_node_67
    __create_import_table_node_67 --> __create_import_table_node_68
    __create_import_table_node_68 --> __create_import_table_node_69
    __create_import_table_node_69 --> __create_import_table_node_70
    __create_import_table_node_70 --> __create_import_table_node_71
    __create_import_table_node_71 --> __create_import_table_node_72
    __create_import_table_node_72 --> __create_import_table_node_73
    __create_import_table_node_73 --> __create_import_table_node_74
    __create_import_table_node_74 --> __create_import_table_node_75
    __create_import_table_node_75 --> __create_import_table_node_76
    __create_import_table_node_76 --> __create_import_table_node_77
    __create_import_table_node_77 --> __create_import_table_node_78
    __create_import_table_node_78 --> __create_import_table_node_79
    __create_import_table_node_79 --> __create_import_table_node_80
  end
  subgraph get_all_imports_from_files
    direction TB
    _get_all_imports_from_files_node_0 --> _get_all_imports_from_files_node_1
    _get_all_imports_from_files_node_1 --> _get_all_imports_from_files_node_2
    _get_all_imports_from_files_node_2 --> _get_all_imports_from_files_node_3
    _get_all_imports_from_files_node_3 --> _get_all_imports_from_files_node_4
    _get_all_imports_from_files_node_4 --> _get_all_imports_from_files_node_5
    _get_all_imports_from_files_node_5 --> _get_all_imports_from_files_node_6
    _get_all_imports_from_files_node_6 --> _get_all_imports_from_files_node_7
    _get_all_imports_from_files_node_7 --> _get_all_imports_from_files_node_8
    _get_all_imports_from_files_node_8 --> _get_all_imports_from_files_node_9
    _get_all_imports_from_files_node_9 --> _get_all_imports_from_files_node_10
    _get_all_imports_from_files_node_10 --> _get_all_imports_from_files_node_11
    _get_all_imports_from_files_node_11 --> _get_all_imports_from_files_node_12
    _get_all_imports_from_files_node_12 --> _get_all_imports_from_files_node_13
    _get_all_imports_from_files_node_13 --> _get_all_imports_from_files_node_14
    _get_all_imports_from_files_node_14 --> _get_all_imports_from_files_node_15
    _get_all_imports_from_files_node_15 --> _get_all_imports_from_files_node_16
    _get_all_imports_from_files_node_16 --> _get_all_imports_from_files_node_17
    _get_all_imports_from_files_node_17 --> _get_all_imports_from_files_node_18
    _get_all_imports_from_files_node_18 --> _get_all_imports_from_files_node_19
    _get_all_imports_from_files_node_19 --> _get_all_imports_from_files_node_20
    _get_all_imports_from_files_node_20 --> _get_all_imports_from_files_node_21
    _get_all_imports_from_files_node_21 --> _get_all_imports_from_files_node_22
    _get_all_imports_from_files_node_22 --> _get_all_imports_from_files_node_23
    _get_all_imports_from_files_node_23 --> _get_all_imports_from_files_node_24
    _get_all_imports_from_files_node_24 --> _get_all_imports_from_files_node_25
    _get_all_imports_from_files_node_25 --> _get_all_imports_from_files_node_26
    _get_all_imports_from_files_node_26 --> _get_all_imports_from_files_node_27
    _get_all_imports_from_files_node_27 --> _get_all_imports_from_files_node_28
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='ast_tools',
      names=[
        alias(name='get_ast_root_node_for_file'),
        alias(name='get_used_import_list')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=70),
    ImportFrom(
      module='files.source',
      names=[
        alias(name='get_source_code_from_file'),
        alias(name='get_import_name_from_path')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=77),
    ClassDef(
      name='ImportMap',
      bases=[],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=7,
                col_offset=17,
                end_lineno=7,
                end_col_offset=21)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=8,
                  col_offset=8,
                  end_lineno=8,
                  end_col_offset=12),
                attr='import_to',
                ctx=Store(),
                lineno=8,
                col_offset=8,
                end_lineno=8,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=8,
                  col_offset=25,
                  end_lineno=8,
                  end_col_offset=29),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=8,
                      col_offset=30,
                      end_lineno=8,
                      end_col_offset=33),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=8,
                        col_offset=35,
                        end_lineno=8,
                        end_col_offset=39),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=8,
                        col_offset=40,
                        end_lineno=8,
                        end_col_offset=43),
                      ctx=Load(),
                      lineno=8,
                      col_offset=35,
                      end_lineno=8,
                      end_col_offset=44)],
                  ctx=Load(),
                  lineno=8,
                  col_offset=30,
                  end_lineno=8,
                  end_col_offset=44),
                ctx=Load(),
                lineno=8,
                col_offset=25,
                end_lineno=8,
                end_col_offset=45),
              value=Dict(
                keys=[],
                values=[],
                lineno=8,
                col_offset=48,
                end_lineno=8,
                end_col_offset=50),
              simple=0,
              lineno=8,
              col_offset=8,
              end_lineno=8,
              end_col_offset=50),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=9,
                  col_offset=8,
                  end_lineno=9,
                  end_col_offset=12),
                attr='import_from',
                ctx=Store(),
                lineno=9,
                col_offset=8,
                end_lineno=9,
                end_col_offset=24),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=9,
                  col_offset=27,
                  end_lineno=9,
                  end_col_offset=31),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=9,
                      col_offset=32,
                      end_lineno=9,
                      end_col_offset=35),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=9,
                        col_offset=37,
                        end_lineno=9,
                        end_col_offset=41),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=9,
                        col_offset=42,
                        end_lineno=9,
                        end_col_offset=45),
                      ctx=Load(),
                      lineno=9,
                      col_offset=37,
                      end_lineno=9,
                      end_col_offset=46)],
                  ctx=Load(),
                  lineno=9,
                  col_offset=32,
                  end_lineno=9,
                  end_col_offset=46),
                ctx=Load(),
                lineno=9,
                col_offset=27,
                end_lineno=9,
                end_col_offset=47),
              value=Dict(
                keys=[],
                values=[],
                lineno=9,
                col_offset=50,
                end_lineno=9,
                end_col_offset=52),
              simple=0,
              lineno=9,
              col_offset=8,
              end_lineno=9,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=7,
            col_offset=26,
            end_lineno=7,
            end_col_offset=30),
          lineno=7,
          col_offset=4,
          end_lineno=9,
          end_col_offset=52),
        FunctionDef(
          name='add_import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=12,
                col_offset=19,
                end_lineno=12,
                end_col_offset=23),
              arg(
                arg='from_',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=32,
                  end_lineno=12,
                  end_col_offset=35),
                lineno=12,
                col_offset=25,
                end_lineno=12,
                end_col_offset=35),
              arg(
                arg='to',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=41,
                  end_lineno=12,
                  end_col_offset=44),
                lineno=12,
                col_offset=37,
                end_lineno=12,
                end_col_offset=44)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            If(
              test=Compare(
                left=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=13,
                  col_offset=11,
                  end_lineno=13,
                  end_col_offset=16),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=13,
                      col_offset=24,
                      end_lineno=13,
                      end_col_offset=28),
                    attr='import_to',
                    ctx=Load(),
                    lineno=13,
                    col_offset=24,
                    end_lineno=13,
                    end_col_offset=38)],
                lineno=13,
                col_offset=11,
                end_lineno=13,
                end_col_offset=38),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=14,
                          col_offset=12,
                          end_lineno=14,
                          end_col_offset=16),
                        attr='import_to',
                        ctx=Load(),
                        lineno=14,
                        col_offset=12,
                        end_lineno=14,
                        end_col_offset=26),
                      slice=Name(
                        id='from_',
                        ctx=Load(),
                        lineno=14,
                        col_offset=27,
                        end_lineno=14,
                        end_col_offset=32),
                      ctx=Store(),
                      lineno=14,
                      col_offset=12,
                      end_lineno=14,
                      end_col_offset=33)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=14,
                    col_offset=36,
                    end_lineno=14,
                    end_col_offset=38),
                  lineno=14,
                  col_offset=12,
                  end_lineno=14,
                  end_col_offset=38)],
              orelse=[],
              lineno=13,
              col_offset=8,
              end_lineno=14,
              end_col_offset=38),
            Expr(
              value=Call(
                func=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=15,
                        col_offset=8,
                        end_lineno=15,
                        end_col_offset=12),
                      attr='import_to',
                      ctx=Load(),
                      lineno=15,
                      col_offset=8,
                      end_lineno=15,
                      end_col_offset=22),
                    slice=Name(
                      id='from_',
                      ctx=Load(),
                      lineno=15,
                      col_offset=23,
                      end_lineno=15,
                      end_col_offset=28),
                    ctx=Load(),
                    lineno=15,
                    col_offset=8,
                    end_lineno=15,
                    end_col_offset=29),
                  attr='append',
                  ctx=Load(),
                  lineno=15,
                  col_offset=8,
                  end_lineno=15,
                  end_col_offset=36),
                args=[
                  Name(
                    id='to',
                    ctx=Load(),
                    lineno=15,
                    col_offset=37,
                    end_lineno=15,
                    end_col_offset=39)],
                keywords=[],
                lineno=15,
                col_offset=8,
                end_lineno=15,
                end_col_offset=40),
              lineno=15,
              col_offset=8,
              end_lineno=15,
              end_col_offset=40),
            If(
              test=Compare(
                left=Name(
                  id='to',
                  ctx=Load(),
                  lineno=17,
                  col_offset=11,
                  end_lineno=17,
                  end_col_offset=13),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=17,
                      col_offset=21,
                      end_lineno=17,
                      end_col_offset=25),
                    attr='import_from',
                    ctx=Load(),
                    lineno=17,
                    col_offset=21,
                    end_lineno=17,
                    end_col_offset=37)],
                lineno=17,
                col_offset=11,
                end_lineno=17,
                end_col_offset=37),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=18,
                          col_offset=12,
                          end_lineno=18,
                          end_col_offset=16),
                        attr='import_from',
                        ctx=Load(),
                        lineno=18,
                        col_offset=12,
                        end_lineno=18,
                        end_col_offset=28),
                      slice=Name(
                        id='to',
                        ctx=Load(),
                        lineno=18,
                        col_offset=29,
                        end_lineno=18,
                        end_col_offset=31),
                      ctx=Store(),
                      lineno=18,
                      col_offset=12,
                      end_lineno=18,
                      end_col_offset=32)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=18,
                    col_offset=35,
                    end_lineno=18,
                    end_col_offset=37),
                  lineno=18,
                  col_offset=12,
                  end_lineno=18,
                  end_col_offset=37)],
              orelse=[],
              lineno=17,
              col_offset=8,
              end_lineno=18,
              end_col_offset=37),
            Expr(
              value=Subscript(
                value=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=19,
                        col_offset=8,
                        end_lineno=19,
                        end_col_offset=12),
                      attr='import_from',
                      ctx=Load(),
                      lineno=19,
                      col_offset=8,
                      end_lineno=19,
                      end_col_offset=24),
                    slice=Name(
                      id='to',
                      ctx=Load(),
                      lineno=19,
                      col_offset=25,
                      end_lineno=19,
                      end_col_offset=27),
                    ctx=Load(),
                    lineno=19,
                    col_offset=8,
                    end_lineno=19,
                    end_col_offset=28),
                  attr='append',
                  ctx=Load(),
                  lineno=19,
                  col_offset=8,
                  end_lineno=19,
                  end_col_offset=35),
                slice=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=19,
                  col_offset=36,
                  end_lineno=19,
                  end_col_offset=41),
                ctx=Load(),
                lineno=19,
                col_offset=8,
                end_lineno=19,
                end_col_offset=42),
              lineno=19,
              col_offset=8,
              end_lineno=19,
              end_col_offset=42)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=12,
            col_offset=49,
            end_lineno=12,
            end_col_offset=53),
          lineno=12,
          col_offset=4,
          end_lineno=19,
          end_col_offset=42)],
      decorator_list=[],
      lineno=5,
      col_offset=0,
      end_lineno=19,
      end_col_offset=42),
    FunctionDef(
      name='_get_import_to_file_map',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=40,
              end_lineno=22,
              end_col_offset=43),
            lineno=22,
            col_offset=28,
            end_lineno=22,
            end_col_offset=43),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=22,
                col_offset=59,
                end_lineno=22,
                end_col_offset=63),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=22,
                col_offset=64,
                end_lineno=22,
                end_col_offset=67),
              ctx=Load(),
              lineno=22,
              col_offset=59,
              end_lineno=22,
              end_col_offset=68),
            lineno=22,
            col_offset=45,
            end_lineno=22,
            end_col_offset=68)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value=' Create a mapping of import paths to filenames first ',
            lineno=23,
            col_offset=4,
            end_lineno=23,
            end_col_offset=63),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=63),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=24,
              col_offset=4,
              end_lineno=24,
              end_col_offset=22)],
          value=Dict(
            keys=[],
            values=[],
            lineno=24,
            col_offset=25,
            end_lineno=24,
            end_col_offset=27),
          lineno=24,
          col_offset=4,
          end_lineno=24,
          end_col_offset=27),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=26,
            col_offset=8,
            end_lineno=26,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=26,
            col_offset=19,
            end_lineno=26,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='import_name',
                  ctx=Store(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=19)],
              value=Call(
                func=Name(
                  id='get_import_name_from_path',
                  ctx=Load(),
                  lineno=27,
                  col_offset=22,
                  end_lineno=27,
                  end_col_offset=47),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='input_path',
                      ctx=Load(),
                      lineno=28,
                      col_offset=23,
                      end_lineno=28,
                      end_col_offset=33),
                    lineno=28,
                    col_offset=12,
                    end_lineno=28,
                    end_col_offset=33),
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=28,
                      col_offset=46,
                      end_lineno=28,
                      end_col_offset=53),
                    lineno=28,
                    col_offset=35,
                    end_lineno=28,
                    end_col_offset=53)],
                lineno=27,
                col_offset=22,
                end_lineno=29,
                end_col_offset=9),
              lineno=27,
              col_offset=8,
              end_lineno=29,
              end_col_offset=9),
            Assign(
              targets=[
                Subscript(
                  value=Name(
                    id='import_to_file_map',
                    ctx=Load(),
                    lineno=30,
                    col_offset=8,
                    end_lineno=30,
                    end_col_offset=26),
                  slice=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=30,
                    col_offset=27,
                    end_lineno=30,
                    end_col_offset=38),
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=39)],
              value=Name(
                id='in_file',
                ctx=Load(),
                lineno=30,
                col_offset=42,
                end_lineno=30,
                end_col_offset=49),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=49)],
          orelse=[],
          lineno=26,
          col_offset=4,
          end_lineno=30,
          end_col_offset=49),
        Return(
          value=Name(
            id='import_to_file_map',
            ctx=Load(),
            lineno=32,
            col_offset=11,
            end_lineno=32,
            end_col_offset=29),
          lineno=32,
          col_offset=4,
          end_lineno=32,
          end_col_offset=29)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=22,
          col_offset=73,
          end_lineno=22,
          end_col_offset=77),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=78,
              end_lineno=22,
              end_col_offset=81),
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=83,
              end_lineno=22,
              end_col_offset=86)],
          ctx=Load(),
          lineno=22,
          col_offset=78,
          end_lineno=22,
          end_col_offset=86),
        ctx=Load(),
        lineno=22,
        col_offset=73,
        end_lineno=22,
        end_col_offset=87),
      lineno=22,
      col_offset=0,
      end_lineno=32,
      end_col_offset=29),
    FunctionDef(
      name='_get_parent_import',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='import_name',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=35,
              col_offset=36,
              end_lineno=35,
              end_col_offset=39),
            lineno=35,
            col_offset=23,
            end_lineno=35,
            end_col_offset=39)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Subscript(
            value=Name(
              id='import_name',
              ctx=Load(),
              lineno=36,
              col_offset=11,
              end_lineno=36,
              end_col_offset=22),
            slice=Slice(
              lower=Constant(
                value=0,
                lineno=36,
                col_offset=23,
                end_lineno=36,
                end_col_offset=24),
              upper=Call(
                func=Attribute(
                  value=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=36,
                    col_offset=26,
                    end_lineno=36,
                    end_col_offset=37),
                  attr='rfind',
                  ctx=Load(),
                  lineno=36,
                  col_offset=26,
                  end_lineno=36,
                  end_col_offset=43),
                args=[
                  Constant(
                    value='.',
                    lineno=36,
                    col_offset=44,
                    end_lineno=36,
                    end_col_offset=47)],
                keywords=[],
                lineno=36,
                col_offset=26,
                end_lineno=36,
                end_col_offset=48),
              lineno=36,
              col_offset=23,
              end_lineno=36,
              end_col_offset=48),
            ctx=Load(),
            lineno=36,
            col_offset=11,
            end_lineno=36,
            end_col_offset=49),
          lineno=36,
          col_offset=4,
          end_lineno=36,
          end_col_offset=49)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=35,
        col_offset=44,
        end_lineno=35,
        end_col_offset=47),
      lineno=35,
      col_offset=0,
      end_lineno=36,
      end_col_offset=49),
    FunctionDef(
      name='_create_import_table',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=40,
                col_offset=18,
                end_lineno=40,
                end_col_offset=22),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=40,
                col_offset=23,
                end_lineno=40,
                end_col_offset=26),
              ctx=Load(),
              lineno=40,
              col_offset=18,
              end_lineno=40,
              end_col_offset=27),
            lineno=40,
            col_offset=4,
            end_lineno=40,
            end_col_offset=27),
          arg(
            arg='import_to_file_map',
            annotation=Subscript(
              value=Name(
                id='dict',
                ctx=Load(),
                lineno=41,
                col_offset=24,
                end_lineno=41,
                end_col_offset=28),
              slice=Tuple(
                elts=[
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=29,
                    end_lineno=41,
                    end_col_offset=32),
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=34,
                    end_lineno=41,
                    end_col_offset=37)],
                ctx=Load(),
                lineno=41,
                col_offset=29,
                end_lineno=41,
                end_col_offset=37),
              ctx=Load(),
              lineno=41,
              col_offset=24,
              end_lineno=41,
              end_col_offset=38),
            lineno=41,
            col_offset=4,
            end_lineno=41,
            end_col_offset=38)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=44,
              col_offset=4,
              end_lineno=44,
              end_col_offset=20)],
          value=Dict(
            keys=[],
            values=[],
            lineno=44,
            col_offset=23,
            end_lineno=44,
            end_col_offset=25),
          lineno=44,
          col_offset=4,
          end_lineno=44,
          end_col_offset=25),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=46,
            col_offset=8,
            end_lineno=46,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=46,
            col_offset=19,
            end_lineno=46,
            end_col_offset=31),
          body=[
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=47,
                  col_offset=11,
                  end_lineno=47,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=47,
                    col_offset=26,
                    end_lineno=47,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=47,
                        col_offset=63,
                        end_lineno=47,
                        end_col_offset=70),
                      lineno=47,
                      col_offset=52,
                      end_lineno=47,
                      end_col_offset=70)],
                  lineno=47,
                  col_offset=26,
                  end_lineno=47,
                  end_col_offset=71),
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=48,
                      col_offset=15,
                      end_lineno=48,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=48,
                        col_offset=27,
                        end_lineno=48,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=49,
                            col_offset=28,
                            end_lineno=49,
                            end_col_offset=39),
                          lineno=49,
                          col_offset=16,
                          end_lineno=49,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=50,
                            col_offset=27,
                            end_lineno=50,
                            end_col_offset=34),
                          lineno=50,
                          col_offset=16,
                          end_lineno=50,
                          end_col_offset=34)],
                      lineno=48,
                      col_offset=27,
                      end_lineno=51,
                      end_col_offset=13),
                    lineno=48,
                    col_offset=15,
                    end_lineno=51,
                    end_col_offset=13),
                  body=[
                    For(
                      target=Name(
                        id='used_import',
                        ctx=Store(),
                        lineno=52,
                        col_offset=20,
                        end_lineno=52,
                        end_col_offset=31),
                      iter=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=52,
                          col_offset=35,
                          end_lineno=52,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=52,
                              col_offset=65,
                              end_lineno=52,
                              end_col_offset=73),
                            lineno=52,
                            col_offset=56,
                            end_lineno=52,
                            end_col_offset=73)],
                        lineno=52,
                        col_offset=35,
                        end_lineno=52,
                        end_col_offset=74),
                      body=[
                        Assign(
                          targets=[
                            Name(
                              id='known_file',
                              ctx=Store(),
                              lineno=53,
                              col_offset=20,
                              end_lineno=53,
                              end_col_offset=30)],
                          value=Constant(
                            value='',
                            lineno=53,
                            col_offset=33,
                            end_lineno=53,
                            end_col_offset=35),
                          lineno=53,
                          col_offset=20,
                          end_lineno=53,
                          end_col_offset=35),
                        Assign(
                          targets=[
                            Name(
                              id='parent_import',
                              ctx=Store(),
                              lineno=54,
                              col_offset=20,
                              end_lineno=54,
                              end_col_offset=33)],
                          value=Call(
                            func=Name(
                              id='_get_parent_import',
                              ctx=Load(),
                              lineno=54,
                              col_offset=36,
                              end_lineno=54,
                              end_col_offset=54),
                            args=[
                              Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=54,
                                col_offset=55,
                                end_lineno=54,
                                end_col_offset=66)],
                            keywords=[],
                            lineno=54,
                            col_offset=36,
                            end_lineno=54,
                            end_col_offset=67),
                          lineno=54,
                          col_offset=20,
                          end_lineno=54,
                          end_col_offset=67),
                        If(
                          test=Compare(
                            left=Name(
                              id='parent_import',
                              ctx=Load(),
                              lineno=55,
                              col_offset=23,
                              end_lineno=55,
                              end_col_offset=36),
                            ops=[
                              In()],
                            comparators=[
                              Name(
                                id='import_to_file_map',
                                ctx=Load(),
                                lineno=55,
                                col_offset=40,
                                end_lineno=55,
                                end_col_offset=58)],
                            lineno=55,
                            col_offset=23,
                            end_lineno=55,
                            end_col_offset=58),
                          body=[
                            Assign(
                              targets=[
                                Name(
                                  id='known_file',
                                  ctx=Store(),
                                  lineno=56,
                                  col_offset=24,
                                  end_lineno=56,
                                  end_col_offset=34)],
                              value=Subscript(
                                value=Name(
                                  id='import_to_file_map',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=37,
                                  end_lineno=56,
                                  end_col_offset=55),
                                slice=Name(
                                  id='parent_import',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=56,
                                  end_lineno=56,
                                  end_col_offset=69),
                                ctx=Load(),
                                lineno=56,
                                col_offset=37,
                                end_lineno=56,
                                end_col_offset=70),
                              lineno=56,
                              col_offset=24,
                              end_lineno=56,
                              end_col_offset=70)],
                          orelse=[],
                          lineno=55,
                          col_offset=20,
                          end_lineno=56,
                          end_col_offset=70),
                        Assign(
                          targets=[
                            Subscript(
                              value=Name(
                                id='all_imports_list',
                                ctx=Load(),
                                lineno=57,
                                col_offset=20,
                                end_lineno=57,
                                end_col_offset=36),
                              slice=Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=57,
                                col_offset=37,
                                end_lineno=57,
                                end_col_offset=48),
                              ctx=Store(),
                              lineno=57,
                              col_offset=20,
                              end_lineno=57,
                              end_col_offset=49)],
                          value=Name(
                            id='known_file',
                            ctx=Load(),
                            lineno=57,
                            col_offset=52,
                            end_lineno=57,
                            end_col_offset=62),
                          lineno=57,
                          col_offset=20,
                          end_lineno=57,
                          end_col_offset=62)],
                      orelse=[],
                      lineno=52,
                      col_offset=16,
                      end_lineno=57,
                      end_col_offset=62)],
                  orelse=[],
                  lineno=48,
                  col_offset=12,
                  end_lineno=57,
                  end_col_offset=62)],
              orelse=[],
              lineno=47,
              col_offset=8,
              end_lineno=57,
              end_col_offset=62)],
          orelse=[],
          lineno=46,
          col_offset=4,
          end_lineno=57,
          end_col_offset=62),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=59,
            col_offset=11,
            end_lineno=59,
            end_col_offset=27),
          lineno=59,
          col_offset=4,
          end_lineno=59,
          end_col_offset=27)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=42,
          col_offset=5,
          end_lineno=42,
          end_col_offset=9),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=10,
              end_lineno=42,
              end_col_offset=13),
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=15,
              end_lineno=42,
              end_col_offset=18)],
          ctx=Load(),
          lineno=42,
          col_offset=10,
          end_lineno=42,
          end_col_offset=18),
        ctx=Load(),
        lineno=42,
        col_offset=5,
        end_lineno=42,
        end_col_offset=19),
      lineno=39,
      col_offset=0,
      end_lineno=59,
      end_col_offset=27),
    FunctionDef(
      name='get_all_imports_from_files',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=62,
              col_offset=43,
              end_lineno=62,
              end_col_offset=46),
            lineno=62,
            col_offset=31,
            end_lineno=62,
            end_col_offset=46),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=62,
                col_offset=62,
                end_lineno=62,
                end_col_offset=66),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=62,
                col_offset=67,
                end_lineno=62,
                end_col_offset=70),
              ctx=Load(),
              lineno=62,
              col_offset=62,
              end_lineno=62,
              end_col_offset=71),
            lineno=62,
            col_offset=48,
            end_lineno=62,
            end_col_offset=71)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value="\n    This is kind of expensive for what it does\n    It's tricky not to require multiple passes to achieve what is being done here\n    ",
            lineno=63,
            col_offset=4,
            end_lineno=66,
            end_col_offset=7),
          lineno=63,
          col_offset=4,
          end_lineno=66,
          end_col_offset=7),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=68,
              col_offset=4,
              end_lineno=68,
              end_col_offset=22)],
          value=Call(
            func=Name(
              id='_get_import_to_file_map',
              ctx=Load(),
              lineno=68,
              col_offset=25,
              end_lineno=68,
              end_col_offset=48),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=69,
                  col_offset=19,
                  end_lineno=69,
                  end_col_offset=29),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=69,
                  col_offset=44,
                  end_lineno=69,
                  end_col_offset=56),
                lineno=69,
                col_offset=31,
                end_lineno=69,
                end_col_offset=56)],
            lineno=68,
            col_offset=25,
            end_lineno=70,
            end_col_offset=5),
          lineno=68,
          col_offset=4,
          end_lineno=70,
          end_col_offset=5),
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=72,
              col_offset=4,
              end_lineno=72,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_create_import_table',
              ctx=Load(),
              lineno=72,
              col_offset=23,
              end_lineno=72,
              end_col_offset=43),
            args=[],
            keywords=[
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=73,
                  col_offset=21,
                  end_lineno=73,
                  end_col_offset=33),
                lineno=73,
                col_offset=8,
                end_lineno=73,
                end_col_offset=33),
              keyword(
                arg='import_to_file_map',
                value=Name(
                  id='import_to_file_map',
                  ctx=Load(),
                  lineno=73,
                  col_offset=54,
                  end_lineno=73,
                  end_col_offset=72),
                lineno=73,
                col_offset=35,
                end_lineno=73,
                end_col_offset=72)],
            lineno=72,
            col_offset=23,
            end_lineno=74,
            end_col_offset=5),
          lineno=72,
          col_offset=4,
          end_lineno=74,
          end_col_offset=5),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=76,
            col_offset=11,
            end_lineno=76,
            end_col_offset=27),
          lineno=76,
          col_offset=4,
          end_lineno=76,
          end_col_offset=27)],
      decorator_list=[],
      lineno=62,
      col_offset=0,
      end_lineno=76,
      end_col_offset=27)],
  type_ignores=[])
```
</details>

