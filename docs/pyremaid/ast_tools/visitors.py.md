# ./src/pyremaid/ast_tools/visitors.py

### Imports

  - ast.AST
  - ast.FunctionDef
  - ast.Import
  - ast.ImportFrom
  - ast.Module
  - ast.NodeVisitor
  - [models.MermaidBlock](/docs/pyremaid/models.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)
  - [models.MermaidFunction](/docs/pyremaid/models.py.md)
  - [models.MermaidLink](/docs/pyremaid/models.py.md)
  - [models.MermaidModule](/docs/pyremaid/models.py.md)
  - [models.MermaidNode](/docs/pyremaid/models.py.md)
  - typing.Any
  - typing.Optional

---
```mermaid
flowchart TB
  _node_0["ClassDef"]
  _node_1["Name"]
  _node_2["Load"]
  ___init___node_0["AnnAssign"]
  ___init___node_1["Attribute"]
  ___init___node_2["Name"]
  ___init___node_3["Load"]
  ___init___node_4["Store"]
  ___init___node_5["Subscript"]
  ___init___node_6["Name"]
  ___init___node_7["Load"]
  ___init___node_8["Name"]
  ___init___node_9["Load"]
  ___init___node_10["Load"]
  ___init___node_11["List"]
  ___init___node_12["Load"]
  _visit_Import_node_0["For"]
  _visit_Import_node_1["Name"]
  _visit_Import_node_2["Store"]
  _visit_Import_node_3["Attribute"]
  _visit_Import_node_4["Name"]
  _visit_Import_node_5["Load"]
  _visit_Import_node_6["Load"]
  _visit_Import_node_7["Expr"]
  _visit_Import_node_8["Call"]
  _visit_Import_node_9["Attribute"]
  _visit_Import_node_10["Attribute"]
  _visit_Import_node_11["Name"]
  _visit_Import_node_12["Load"]
  _visit_Import_node_13["Load"]
  _visit_Import_node_14["Load"]
  _visit_Import_node_15["JoinedStr"]
  _visit_Import_node_16["FormattedValue"]
  _visit_Import_node_17["Attribute"]
  _visit_Import_node_18["Name"]
  _visit_Import_node_19["Load"]
  _visit_Import_node_20["Load"]
  _visit_Import_node_21["Constant"]
  _visit_ImportFrom_node_0["Assign"]
  _visit_ImportFrom_node_1["Name"]
  _visit_ImportFrom_node_2["Store"]
  _visit_ImportFrom_node_3["Attribute"]
  _visit_ImportFrom_node_4["Name"]
  _visit_ImportFrom_node_5["Load"]
  _visit_ImportFrom_node_6["Load"]
  _visit_ImportFrom_node_7["For"]
  _visit_ImportFrom_node_8["Name"]
  _visit_ImportFrom_node_9["Store"]
  _visit_ImportFrom_node_10["Attribute"]
  _visit_ImportFrom_node_11["Name"]
  _visit_ImportFrom_node_12["Load"]
  _visit_ImportFrom_node_13["Load"]
  _visit_ImportFrom_node_14["Expr"]
  _visit_ImportFrom_node_15["Call"]
  _visit_ImportFrom_node_16["Attribute"]
  _visit_ImportFrom_node_17["Attribute"]
  _visit_ImportFrom_node_18["Name"]
  _visit_ImportFrom_node_19["Load"]
  _visit_ImportFrom_node_20["Load"]
  _visit_ImportFrom_node_21["Load"]
  _visit_ImportFrom_node_22["JoinedStr"]
  _visit_ImportFrom_node_23["FormattedValue"]
  _visit_ImportFrom_node_24["Name"]
  _visit_ImportFrom_node_25["Load"]
  _visit_ImportFrom_node_26["Constant"]
  _visit_ImportFrom_node_27["FormattedValue"]
  _visit_ImportFrom_node_28["Attribute"]
  _visit_ImportFrom_node_29["Name"]
  _visit_ImportFrom_node_30["Load"]
  _visit_ImportFrom_node_31["Load"]
  _get_found_imports_node_0["Return"]
  _get_found_imports_node_1["Attribute"]
  _get_found_imports_node_2["Name"]
  _get_found_imports_node_3["Load"]
  _get_found_imports_node_4["Load"]
  _node_3["ClassDef"]
  _node_4["Name"]
  _node_5["Load"]
  ___init___node_0["AnnAssign"]
  ___init___node_1["Attribute"]
  ___init___node_2["Name"]
  ___init___node_3["Load"]
  ___init___node_4["Store"]
  ___init___node_5["Subscript"]
  ___init___node_6["Name"]
  ___init___node_7["Load"]
  ___init___node_8["Name"]
  ___init___node_9["Load"]
  ___init___node_10["Load"]
  ___init___node_11["List"]
  ___init___node_12["Load"]
  ___init___node_13["AnnAssign"]
  ___init___node_14["Attribute"]
  ___init___node_15["Name"]
  ___init___node_16["Load"]
  ___init___node_17["Store"]
  ___init___node_18["Subscript"]
  ___init___node_19["Name"]
  ___init___node_20["Load"]
  ___init___node_21["Name"]
  ___init___node_22["Load"]
  ___init___node_23["Load"]
  ___init___node_24["Constant"]
  ___init___node_25["AnnAssign"]
  ___init___node_26["Attribute"]
  ___init___node_27["Name"]
  ___init___node_28["Load"]
  ___init___node_29["Store"]
  ___init___node_30["Name"]
  ___init___node_31["Load"]
  ___init___node_32["Constant"]
  ___init___node_33["Assign"]
  ___init___node_34["Attribute"]
  ___init___node_35["Name"]
  ___init___node_36["Load"]
  ___init___node_37["Store"]
  ___init___node_38["Name"]
  ___init___node_39["Load"]
  _visit_FunctionDef_node_0["Assign"]
  _visit_FunctionDef_node_1["Name"]
  _visit_FunctionDef_node_2["Store"]
  _visit_FunctionDef_node_3["Call"]
  _visit_FunctionDef_node_4["Name"]
  _visit_FunctionDef_node_5["Load"]
  _visit_FunctionDef_node_6["keyword"]
  _visit_FunctionDef_node_7["Attribute"]
  _visit_FunctionDef_node_8["Name"]
  _visit_FunctionDef_node_9["Load"]
  _visit_FunctionDef_node_10["Load"]
  _visit_FunctionDef_node_11["Expr"]
  _visit_FunctionDef_node_12["Call"]
  _visit_FunctionDef_node_13["Attribute"]
  _visit_FunctionDef_node_14["Name"]
  _visit_FunctionDef_node_15["Load"]
  _visit_FunctionDef_node_16["Load"]
  _visit_FunctionDef_node_17["Name"]
  _visit_FunctionDef_node_18["Load"]
  _visit_FunctionDef_node_19["Expr"]
  _visit_FunctionDef_node_20["Call"]
  _visit_FunctionDef_node_21["Attribute"]
  _visit_FunctionDef_node_22["Attribute"]
  _visit_FunctionDef_node_23["Name"]
  _visit_FunctionDef_node_24["Load"]
  _visit_FunctionDef_node_25["Load"]
  _visit_FunctionDef_node_26["Load"]
  _visit_FunctionDef_node_27["Call"]
  _visit_FunctionDef_node_28["Attribute"]
  _visit_FunctionDef_node_29["Name"]
  _visit_FunctionDef_node_30["Load"]
  _visit_FunctionDef_node_31["Load"]
  _generic_visit_node_0["Assign"]
  _generic_visit_node_1["Name"]
  _generic_visit_node_2["Store"]
  _generic_visit_node_3["Call"]
  _generic_visit_node_4["Name"]
  _generic_visit_node_5["Load"]
  _generic_visit_node_6["keyword"]
  _generic_visit_node_7["Name"]
  _generic_visit_node_8["Load"]
  _generic_visit_node_9["keyword"]
  _generic_visit_node_10["JoinedStr"]
  _generic_visit_node_11["FormattedValue"]
  _generic_visit_node_12["Attribute"]
  _generic_visit_node_13["Name"]
  _generic_visit_node_14["Load"]
  _generic_visit_node_15["Load"]
  _generic_visit_node_16["Constant"]
  _generic_visit_node_17["FormattedValue"]
  _generic_visit_node_18["Attribute"]
  _generic_visit_node_19["Name"]
  _generic_visit_node_20["Load"]
  _generic_visit_node_21["Load"]
  _generic_visit_node_22["keyword"]
  _generic_visit_node_23["Attribute"]
  _generic_visit_node_24["Call"]
  _generic_visit_node_25["Name"]
  _generic_visit_node_26["Load"]
  _generic_visit_node_27["Name"]
  _generic_visit_node_28["Load"]
  _generic_visit_node_29["Load"]
  _generic_visit_node_30["AugAssign"]
  _generic_visit_node_31["Attribute"]
  _generic_visit_node_32["Name"]
  _generic_visit_node_33["Load"]
  _generic_visit_node_34["Store"]
  _generic_visit_node_35["Add"]
  _generic_visit_node_36["Constant"]
  _generic_visit_node_37["If"]
  _generic_visit_node_38["Attribute"]
  _generic_visit_node_39["Name"]
  _generic_visit_node_40["Load"]
  _generic_visit_node_41["Load"]
  _generic_visit_node_42["Expr"]
  _generic_visit_node_43["Call"]
  _generic_visit_node_44["Attribute"]
  _generic_visit_node_45["Attribute"]
  _generic_visit_node_46["Name"]
  _generic_visit_node_47["Load"]
  _generic_visit_node_48["Load"]
  _generic_visit_node_49["Load"]
  _generic_visit_node_50["Call"]
  _generic_visit_node_51["Name"]
  _generic_visit_node_52["Load"]
  _generic_visit_node_53["keyword"]
  _generic_visit_node_54["Attribute"]
  _generic_visit_node_55["Name"]
  _generic_visit_node_56["Load"]
  _generic_visit_node_57["Load"]
  _generic_visit_node_58["keyword"]
  _generic_visit_node_59["Name"]
  _generic_visit_node_60["Load"]
  _generic_visit_node_61["Assign"]
  _generic_visit_node_62["Attribute"]
  _generic_visit_node_63["Name"]
  _generic_visit_node_64["Load"]
  _generic_visit_node_65["Store"]
  _generic_visit_node_66["Name"]
  _generic_visit_node_67["Load"]
  _generic_visit_node_68["Return"]
  _generic_visit_node_69["Call"]
  _generic_visit_node_70["Attribute"]
  _generic_visit_node_71["Call"]
  _generic_visit_node_72["Name"]
  _generic_visit_node_73["Load"]
  _generic_visit_node_74["Load"]
  _generic_visit_node_75["Name"]
  _generic_visit_node_76["Load"]
  _get_list_of_elements_node_0["Return"]
  _get_list_of_elements_node_1["Attribute"]
  _get_list_of_elements_node_2["Name"]
  _get_list_of_elements_node_3["Load"]
  _get_list_of_elements_node_4["Load"]
  _node_6["ClassDef"]
  _node_7["Name"]
  _node_8["Load"]
  ___init___node_0["AnnAssign"]
  ___init___node_1["Attribute"]
  ___init___node_2["Name"]
  ___init___node_3["Load"]
  ___init___node_4["Store"]
  ___init___node_5["Subscript"]
  ___init___node_6["Name"]
  ___init___node_7["Load"]
  ___init___node_8["Name"]
  ___init___node_9["Load"]
  ___init___node_10["Load"]
  ___init___node_11["List"]
  ___init___node_12["Load"]
  ___init___node_13["AnnAssign"]
  ___init___node_14["Attribute"]
  ___init___node_15["Name"]
  ___init___node_16["Load"]
  ___init___node_17["Store"]
  ___init___node_18["Name"]
  ___init___node_19["Load"]
  ___init___node_20["Constant"]
  ___init___node_21["Assign"]
  ___init___node_22["Attribute"]
  ___init___node_23["Name"]
  ___init___node_24["Load"]
  ___init___node_25["Store"]
  ___init___node_26["Name"]
  ___init___node_27["Load"]
  __count_node_0["Assign"]
  __count_node_1["Name"]
  __count_node_2["Store"]
  __count_node_3["Attribute"]
  __count_node_4["Name"]
  __count_node_5["Load"]
  __count_node_6["Load"]
  __count_node_7["AugAssign"]
  __count_node_8["Attribute"]
  __count_node_9["Name"]
  __count_node_10["Load"]
  __count_node_11["Store"]
  __count_node_12["Add"]
  __count_node_13["Constant"]
  __count_node_14["Return"]
  __count_node_15["Name"]
  __count_node_16["Load"]
  _visit_Module_node_0["Expr"]
  _visit_Module_node_1["Constant"]
  _visit_Module_node_2["Assign"]
  _visit_Module_node_3["Name"]
  _visit_Module_node_4["Store"]
  _visit_Module_node_5["Call"]
  _visit_Module_node_6["Name"]
  _visit_Module_node_7["Load"]
  _visit_Module_node_8["For"]
  _visit_Module_node_9["Name"]
  _visit_Module_node_10["Store"]
  _visit_Module_node_11["Attribute"]
  _visit_Module_node_12["Name"]
  _visit_Module_node_13["Load"]
  _visit_Module_node_14["Load"]
  _visit_Module_node_15["Expr"]
  _visit_Module_node_16["Call"]
  _visit_Module_node_17["Attribute"]
  _visit_Module_node_18["Name"]
  _visit_Module_node_19["Load"]
  _visit_Module_node_20["Load"]
  _visit_Module_node_21["keyword"]
  _visit_Module_node_22["Name"]
  _visit_Module_node_23["Load"]
  _visit_Module_node_24["Assign"]
  _visit_Module_node_25["Name"]
  _visit_Module_node_26["Store"]
  _visit_Module_node_27["Call"]
  _visit_Module_node_28["Name"]
  _visit_Module_node_29["Load"]
  _visit_Module_node_30["keyword"]
  _visit_Module_node_31["Name"]
  _visit_Module_node_32["Load"]
  _visit_Module_node_33["keyword"]
  _visit_Module_node_34["JoinedStr"]
  _visit_Module_node_35["FormattedValue"]
  _visit_Module_node_36["Attribute"]
  _visit_Module_node_37["Name"]
  _visit_Module_node_38["Load"]
  _visit_Module_node_39["Load"]
  _visit_Module_node_40["Constant"]
  _visit_Module_node_41["FormattedValue"]
  _visit_Module_node_42["Call"]
  _visit_Module_node_43["Attribute"]
  _visit_Module_node_44["Name"]
  _visit_Module_node_45["Load"]
  _visit_Module_node_46["Load"]
  _visit_Module_node_47["keyword"]
  _visit_Module_node_48["Call"]
  _visit_Module_node_49["Attribute"]
  _visit_Module_node_50["Name"]
  _visit_Module_node_51["Load"]
  _visit_Module_node_52["Load"]
  _visit_Module_node_53["keyword"]
  _visit_Module_node_54["Constant"]
  _visit_Module_node_55["Expr"]
  _visit_Module_node_56["Call"]
  _visit_Module_node_57["Attribute"]
  _visit_Module_node_58["Attribute"]
  _visit_Module_node_59["Name"]
  _visit_Module_node_60["Load"]
  _visit_Module_node_61["Load"]
  _visit_Module_node_62["Load"]
  _visit_Module_node_63["Name"]
  _visit_Module_node_64["Load"]
  _visit_FunctionDef_node_0["Expr"]
  _visit_FunctionDef_node_1["Constant"]
  _visit_FunctionDef_node_2["Assign"]
  _visit_FunctionDef_node_3["Name"]
  _visit_FunctionDef_node_4["Store"]
  _visit_FunctionDef_node_5["Call"]
  _visit_FunctionDef_node_6["Name"]
  _visit_FunctionDef_node_7["Load"]
  _visit_FunctionDef_node_8["keyword"]
  _visit_FunctionDef_node_9["JoinedStr"]
  _visit_FunctionDef_node_10["FormattedValue"]
  _visit_FunctionDef_node_11["Attribute"]
  _visit_FunctionDef_node_12["Name"]
  _visit_FunctionDef_node_13["Load"]
  _visit_FunctionDef_node_14["Load"]
  _visit_FunctionDef_node_15["Constant"]
  _visit_FunctionDef_node_16["FormattedValue"]
  _visit_FunctionDef_node_17["Attribute"]
  _visit_FunctionDef_node_18["Name"]
  _visit_FunctionDef_node_19["Load"]
  _visit_FunctionDef_node_20["Load"]
  _visit_FunctionDef_node_21["For"]
  _visit_FunctionDef_node_22["Name"]
  _visit_FunctionDef_node_23["Store"]
  _visit_FunctionDef_node_24["Attribute"]
  _visit_FunctionDef_node_25["Name"]
  _visit_FunctionDef_node_26["Load"]
  _visit_FunctionDef_node_27["Load"]
  _visit_FunctionDef_node_28["Expr"]
  _visit_FunctionDef_node_29["Call"]
  _visit_FunctionDef_node_30["Attribute"]
  _visit_FunctionDef_node_31["Name"]
  _visit_FunctionDef_node_32["Load"]
  _visit_FunctionDef_node_33["Load"]
  _visit_FunctionDef_node_34["keyword"]
  _visit_FunctionDef_node_35["Name"]
  _visit_FunctionDef_node_36["Load"]
  _visit_FunctionDef_node_37["Assign"]
  _visit_FunctionDef_node_38["Name"]
  _visit_FunctionDef_node_39["Store"]
  _visit_FunctionDef_node_40["Call"]
  _visit_FunctionDef_node_41["Name"]
  _visit_FunctionDef_node_42["Load"]
  _visit_FunctionDef_node_43["keyword"]
  _visit_FunctionDef_node_44["Name"]
  _visit_FunctionDef_node_45["Load"]
  _visit_FunctionDef_node_46["keyword"]
  _visit_FunctionDef_node_47["JoinedStr"]
  _visit_FunctionDef_node_48["FormattedValue"]
  _visit_FunctionDef_node_49["Attribute"]
  _visit_FunctionDef_node_50["Name"]
  _visit_FunctionDef_node_51["Load"]
  _visit_FunctionDef_node_52["Load"]
  _visit_FunctionDef_node_53["Constant"]
  _visit_FunctionDef_node_54["FormattedValue"]
  _visit_FunctionDef_node_55["Call"]
  _visit_FunctionDef_node_56["Attribute"]
  _visit_FunctionDef_node_57["Name"]
  _visit_FunctionDef_node_58["Load"]
  _visit_FunctionDef_node_59["Load"]
  _visit_FunctionDef_node_60["keyword"]
  _visit_FunctionDef_node_61["Call"]
  _visit_FunctionDef_node_62["Attribute"]
  _visit_FunctionDef_node_63["Name"]
  _visit_FunctionDef_node_64["Load"]
  _visit_FunctionDef_node_65["Load"]
  _visit_FunctionDef_node_66["keyword"]
  _visit_FunctionDef_node_67["Attribute"]
  _visit_FunctionDef_node_68["Name"]
  _visit_FunctionDef_node_69["Load"]
  _visit_FunctionDef_node_70["Load"]
  _visit_FunctionDef_node_71["Expr"]
  _visit_FunctionDef_node_72["Call"]
  _visit_FunctionDef_node_73["Attribute"]
  _visit_FunctionDef_node_74["Attribute"]
  _visit_FunctionDef_node_75["Name"]
  _visit_FunctionDef_node_76["Load"]
  _visit_FunctionDef_node_77["Load"]
  _visit_FunctionDef_node_78["Load"]
  _visit_FunctionDef_node_79["Name"]
  _visit_FunctionDef_node_80["Load"]
  _generic_visit_node_0["Expr"]
  _generic_visit_node_1["Constant"]
  _generic_visit_node_2["Pass"]
  _get_list_of_elements_node_0["Return"]
  _get_list_of_elements_node_1["Attribute"]
  _get_list_of_elements_node_2["Name"]
  _get_list_of_elements_node_3["Load"]
  _get_list_of_elements_node_4["Load"]

  _node_0 --> _node_1
  _node_1 --> _node_2
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
  end
  subgraph visit_Import
    direction TB
    _visit_Import_node_0 --> _visit_Import_node_1
    _visit_Import_node_1 --> _visit_Import_node_2
    _visit_Import_node_2 --> _visit_Import_node_3
    _visit_Import_node_3 --> _visit_Import_node_4
    _visit_Import_node_4 --> _visit_Import_node_5
    _visit_Import_node_5 --> _visit_Import_node_6
    _visit_Import_node_6 --> _visit_Import_node_7
    _visit_Import_node_7 --> _visit_Import_node_8
    _visit_Import_node_8 --> _visit_Import_node_9
    _visit_Import_node_9 --> _visit_Import_node_10
    _visit_Import_node_10 --> _visit_Import_node_11
    _visit_Import_node_11 --> _visit_Import_node_12
    _visit_Import_node_12 --> _visit_Import_node_13
    _visit_Import_node_13 --> _visit_Import_node_14
    _visit_Import_node_14 --> _visit_Import_node_15
    _visit_Import_node_15 --> _visit_Import_node_16
    _visit_Import_node_16 --> _visit_Import_node_17
    _visit_Import_node_17 --> _visit_Import_node_18
    _visit_Import_node_18 --> _visit_Import_node_19
    _visit_Import_node_19 --> _visit_Import_node_20
    _visit_Import_node_20 --> _visit_Import_node_21
  end
  subgraph visit_ImportFrom
    direction TB
    _visit_ImportFrom_node_0 --> _visit_ImportFrom_node_1
    _visit_ImportFrom_node_1 --> _visit_ImportFrom_node_2
    _visit_ImportFrom_node_2 --> _visit_ImportFrom_node_3
    _visit_ImportFrom_node_3 --> _visit_ImportFrom_node_4
    _visit_ImportFrom_node_4 --> _visit_ImportFrom_node_5
    _visit_ImportFrom_node_5 --> _visit_ImportFrom_node_6
    _visit_ImportFrom_node_6 --> _visit_ImportFrom_node_7
    _visit_ImportFrom_node_7 --> _visit_ImportFrom_node_8
    _visit_ImportFrom_node_8 --> _visit_ImportFrom_node_9
    _visit_ImportFrom_node_9 --> _visit_ImportFrom_node_10
    _visit_ImportFrom_node_10 --> _visit_ImportFrom_node_11
    _visit_ImportFrom_node_11 --> _visit_ImportFrom_node_12
    _visit_ImportFrom_node_12 --> _visit_ImportFrom_node_13
    _visit_ImportFrom_node_13 --> _visit_ImportFrom_node_14
    _visit_ImportFrom_node_14 --> _visit_ImportFrom_node_15
    _visit_ImportFrom_node_15 --> _visit_ImportFrom_node_16
    _visit_ImportFrom_node_16 --> _visit_ImportFrom_node_17
    _visit_ImportFrom_node_17 --> _visit_ImportFrom_node_18
    _visit_ImportFrom_node_18 --> _visit_ImportFrom_node_19
    _visit_ImportFrom_node_19 --> _visit_ImportFrom_node_20
    _visit_ImportFrom_node_20 --> _visit_ImportFrom_node_21
    _visit_ImportFrom_node_21 --> _visit_ImportFrom_node_22
    _visit_ImportFrom_node_22 --> _visit_ImportFrom_node_23
    _visit_ImportFrom_node_23 --> _visit_ImportFrom_node_24
    _visit_ImportFrom_node_24 --> _visit_ImportFrom_node_25
    _visit_ImportFrom_node_25 --> _visit_ImportFrom_node_26
    _visit_ImportFrom_node_26 --> _visit_ImportFrom_node_27
    _visit_ImportFrom_node_27 --> _visit_ImportFrom_node_28
    _visit_ImportFrom_node_28 --> _visit_ImportFrom_node_29
    _visit_ImportFrom_node_29 --> _visit_ImportFrom_node_30
    _visit_ImportFrom_node_30 --> _visit_ImportFrom_node_31
  end
  subgraph get_found_imports
    direction TB
    _get_found_imports_node_0 --> _get_found_imports_node_1
    _get_found_imports_node_1 --> _get_found_imports_node_2
    _get_found_imports_node_2 --> _get_found_imports_node_3
    _get_found_imports_node_3 --> _get_found_imports_node_4
  end
  _node_2 --> _node_3
  _node_3 --> _node_4
  _node_4 --> _node_5
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
  subgraph visit_Import
    direction TB
  end
  subgraph visit_ImportFrom
    direction TB
  end
  subgraph visit_FunctionDef
    direction TB
    _visit_FunctionDef_node_0 --> _visit_FunctionDef_node_1
    _visit_FunctionDef_node_1 --> _visit_FunctionDef_node_2
    _visit_FunctionDef_node_2 --> _visit_FunctionDef_node_3
    _visit_FunctionDef_node_3 --> _visit_FunctionDef_node_4
    _visit_FunctionDef_node_4 --> _visit_FunctionDef_node_5
    _visit_FunctionDef_node_5 --> _visit_FunctionDef_node_6
    _visit_FunctionDef_node_6 --> _visit_FunctionDef_node_7
    _visit_FunctionDef_node_7 --> _visit_FunctionDef_node_8
    _visit_FunctionDef_node_8 --> _visit_FunctionDef_node_9
    _visit_FunctionDef_node_9 --> _visit_FunctionDef_node_10
    _visit_FunctionDef_node_10 --> _visit_FunctionDef_node_11
    _visit_FunctionDef_node_11 --> _visit_FunctionDef_node_12
    _visit_FunctionDef_node_12 --> _visit_FunctionDef_node_13
    _visit_FunctionDef_node_13 --> _visit_FunctionDef_node_14
    _visit_FunctionDef_node_14 --> _visit_FunctionDef_node_15
    _visit_FunctionDef_node_15 --> _visit_FunctionDef_node_16
    _visit_FunctionDef_node_16 --> _visit_FunctionDef_node_17
    _visit_FunctionDef_node_17 --> _visit_FunctionDef_node_18
    _visit_FunctionDef_node_18 --> _visit_FunctionDef_node_19
    _visit_FunctionDef_node_19 --> _visit_FunctionDef_node_20
    _visit_FunctionDef_node_20 --> _visit_FunctionDef_node_21
    _visit_FunctionDef_node_21 --> _visit_FunctionDef_node_22
    _visit_FunctionDef_node_22 --> _visit_FunctionDef_node_23
    _visit_FunctionDef_node_23 --> _visit_FunctionDef_node_24
    _visit_FunctionDef_node_24 --> _visit_FunctionDef_node_25
    _visit_FunctionDef_node_25 --> _visit_FunctionDef_node_26
    _visit_FunctionDef_node_26 --> _visit_FunctionDef_node_27
    _visit_FunctionDef_node_27 --> _visit_FunctionDef_node_28
    _visit_FunctionDef_node_28 --> _visit_FunctionDef_node_29
    _visit_FunctionDef_node_29 --> _visit_FunctionDef_node_30
    _visit_FunctionDef_node_30 --> _visit_FunctionDef_node_31
  end
  subgraph generic_visit
    direction TB
    _generic_visit_node_0 --> _generic_visit_node_1
    _generic_visit_node_1 --> _generic_visit_node_2
    _generic_visit_node_2 --> _generic_visit_node_3
    _generic_visit_node_3 --> _generic_visit_node_4
    _generic_visit_node_4 --> _generic_visit_node_5
    _generic_visit_node_5 --> _generic_visit_node_6
    _generic_visit_node_6 --> _generic_visit_node_7
    _generic_visit_node_7 --> _generic_visit_node_8
    _generic_visit_node_8 --> _generic_visit_node_9
    _generic_visit_node_9 --> _generic_visit_node_10
    _generic_visit_node_10 --> _generic_visit_node_11
    _generic_visit_node_11 --> _generic_visit_node_12
    _generic_visit_node_12 --> _generic_visit_node_13
    _generic_visit_node_13 --> _generic_visit_node_14
    _generic_visit_node_14 --> _generic_visit_node_15
    _generic_visit_node_15 --> _generic_visit_node_16
    _generic_visit_node_16 --> _generic_visit_node_17
    _generic_visit_node_17 --> _generic_visit_node_18
    _generic_visit_node_18 --> _generic_visit_node_19
    _generic_visit_node_19 --> _generic_visit_node_20
    _generic_visit_node_20 --> _generic_visit_node_21
    _generic_visit_node_21 --> _generic_visit_node_22
    _generic_visit_node_22 --> _generic_visit_node_23
    _generic_visit_node_23 --> _generic_visit_node_24
    _generic_visit_node_24 --> _generic_visit_node_25
    _generic_visit_node_25 --> _generic_visit_node_26
    _generic_visit_node_26 --> _generic_visit_node_27
    _generic_visit_node_27 --> _generic_visit_node_28
    _generic_visit_node_28 --> _generic_visit_node_29
    _generic_visit_node_29 --> _generic_visit_node_30
    _generic_visit_node_30 --> _generic_visit_node_31
    _generic_visit_node_31 --> _generic_visit_node_32
    _generic_visit_node_32 --> _generic_visit_node_33
    _generic_visit_node_33 --> _generic_visit_node_34
    _generic_visit_node_34 --> _generic_visit_node_35
    _generic_visit_node_35 --> _generic_visit_node_36
    _generic_visit_node_36 --> _generic_visit_node_37
    _generic_visit_node_37 --> _generic_visit_node_38
    _generic_visit_node_38 --> _generic_visit_node_39
    _generic_visit_node_39 --> _generic_visit_node_40
    _generic_visit_node_40 --> _generic_visit_node_41
    _generic_visit_node_41 --> _generic_visit_node_42
    _generic_visit_node_42 --> _generic_visit_node_43
    _generic_visit_node_43 --> _generic_visit_node_44
    _generic_visit_node_44 --> _generic_visit_node_45
    _generic_visit_node_45 --> _generic_visit_node_46
    _generic_visit_node_46 --> _generic_visit_node_47
    _generic_visit_node_47 --> _generic_visit_node_48
    _generic_visit_node_48 --> _generic_visit_node_49
    _generic_visit_node_49 --> _generic_visit_node_50
    _generic_visit_node_50 --> _generic_visit_node_51
    _generic_visit_node_51 --> _generic_visit_node_52
    _generic_visit_node_52 --> _generic_visit_node_53
    _generic_visit_node_53 --> _generic_visit_node_54
    _generic_visit_node_54 --> _generic_visit_node_55
    _generic_visit_node_55 --> _generic_visit_node_56
    _generic_visit_node_56 --> _generic_visit_node_57
    _generic_visit_node_57 --> _generic_visit_node_58
    _generic_visit_node_58 --> _generic_visit_node_59
    _generic_visit_node_59 --> _generic_visit_node_60
    _generic_visit_node_60 --> _generic_visit_node_61
    _generic_visit_node_61 --> _generic_visit_node_62
    _generic_visit_node_62 --> _generic_visit_node_63
    _generic_visit_node_63 --> _generic_visit_node_64
    _generic_visit_node_64 --> _generic_visit_node_65
    _generic_visit_node_65 --> _generic_visit_node_66
    _generic_visit_node_66 --> _generic_visit_node_67
    _generic_visit_node_67 --> _generic_visit_node_68
    _generic_visit_node_68 --> _generic_visit_node_69
    _generic_visit_node_69 --> _generic_visit_node_70
    _generic_visit_node_70 --> _generic_visit_node_71
    _generic_visit_node_71 --> _generic_visit_node_72
    _generic_visit_node_72 --> _generic_visit_node_73
    _generic_visit_node_73 --> _generic_visit_node_74
    _generic_visit_node_74 --> _generic_visit_node_75
    _generic_visit_node_75 --> _generic_visit_node_76
  end
  subgraph get_list_of_elements
    direction TB
    _get_list_of_elements_node_0 --> _get_list_of_elements_node_1
    _get_list_of_elements_node_1 --> _get_list_of_elements_node_2
    _get_list_of_elements_node_2 --> _get_list_of_elements_node_3
    _get_list_of_elements_node_3 --> _get_list_of_elements_node_4
  end
  _node_5 --> _node_6
  _node_6 --> _node_7
  _node_7 --> _node_8
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
  end
  subgraph _count
    direction TB
    __count_node_0 --> __count_node_1
    __count_node_1 --> __count_node_2
    __count_node_2 --> __count_node_3
    __count_node_3 --> __count_node_4
    __count_node_4 --> __count_node_5
    __count_node_5 --> __count_node_6
    __count_node_6 --> __count_node_7
    __count_node_7 --> __count_node_8
    __count_node_8 --> __count_node_9
    __count_node_9 --> __count_node_10
    __count_node_10 --> __count_node_11
    __count_node_11 --> __count_node_12
    __count_node_12 --> __count_node_13
    __count_node_13 --> __count_node_14
    __count_node_14 --> __count_node_15
    __count_node_15 --> __count_node_16
  end
  subgraph visit_Module
    direction TB
    _visit_Module_node_0 --> _visit_Module_node_1
    _visit_Module_node_1 --> _visit_Module_node_2
    _visit_Module_node_2 --> _visit_Module_node_3
    _visit_Module_node_3 --> _visit_Module_node_4
    _visit_Module_node_4 --> _visit_Module_node_5
    _visit_Module_node_5 --> _visit_Module_node_6
    _visit_Module_node_6 --> _visit_Module_node_7
    _visit_Module_node_7 --> _visit_Module_node_8
    _visit_Module_node_8 --> _visit_Module_node_9
    _visit_Module_node_9 --> _visit_Module_node_10
    _visit_Module_node_10 --> _visit_Module_node_11
    _visit_Module_node_11 --> _visit_Module_node_12
    _visit_Module_node_12 --> _visit_Module_node_13
    _visit_Module_node_13 --> _visit_Module_node_14
    _visit_Module_node_14 --> _visit_Module_node_15
    _visit_Module_node_15 --> _visit_Module_node_16
    _visit_Module_node_16 --> _visit_Module_node_17
    _visit_Module_node_17 --> _visit_Module_node_18
    _visit_Module_node_18 --> _visit_Module_node_19
    _visit_Module_node_19 --> _visit_Module_node_20
    _visit_Module_node_20 --> _visit_Module_node_21
    _visit_Module_node_21 --> _visit_Module_node_22
    _visit_Module_node_22 --> _visit_Module_node_23
    _visit_Module_node_23 --> _visit_Module_node_24
    _visit_Module_node_24 --> _visit_Module_node_25
    _visit_Module_node_25 --> _visit_Module_node_26
    _visit_Module_node_26 --> _visit_Module_node_27
    _visit_Module_node_27 --> _visit_Module_node_28
    _visit_Module_node_28 --> _visit_Module_node_29
    _visit_Module_node_29 --> _visit_Module_node_30
    _visit_Module_node_30 --> _visit_Module_node_31
    _visit_Module_node_31 --> _visit_Module_node_32
    _visit_Module_node_32 --> _visit_Module_node_33
    _visit_Module_node_33 --> _visit_Module_node_34
    _visit_Module_node_34 --> _visit_Module_node_35
    _visit_Module_node_35 --> _visit_Module_node_36
    _visit_Module_node_36 --> _visit_Module_node_37
    _visit_Module_node_37 --> _visit_Module_node_38
    _visit_Module_node_38 --> _visit_Module_node_39
    _visit_Module_node_39 --> _visit_Module_node_40
    _visit_Module_node_40 --> _visit_Module_node_41
    _visit_Module_node_41 --> _visit_Module_node_42
    _visit_Module_node_42 --> _visit_Module_node_43
    _visit_Module_node_43 --> _visit_Module_node_44
    _visit_Module_node_44 --> _visit_Module_node_45
    _visit_Module_node_45 --> _visit_Module_node_46
    _visit_Module_node_46 --> _visit_Module_node_47
    _visit_Module_node_47 --> _visit_Module_node_48
    _visit_Module_node_48 --> _visit_Module_node_49
    _visit_Module_node_49 --> _visit_Module_node_50
    _visit_Module_node_50 --> _visit_Module_node_51
    _visit_Module_node_51 --> _visit_Module_node_52
    _visit_Module_node_52 --> _visit_Module_node_53
    _visit_Module_node_53 --> _visit_Module_node_54
    _visit_Module_node_54 --> _visit_Module_node_55
    _visit_Module_node_55 --> _visit_Module_node_56
    _visit_Module_node_56 --> _visit_Module_node_57
    _visit_Module_node_57 --> _visit_Module_node_58
    _visit_Module_node_58 --> _visit_Module_node_59
    _visit_Module_node_59 --> _visit_Module_node_60
    _visit_Module_node_60 --> _visit_Module_node_61
    _visit_Module_node_61 --> _visit_Module_node_62
    _visit_Module_node_62 --> _visit_Module_node_63
    _visit_Module_node_63 --> _visit_Module_node_64
  end
  subgraph visit_FunctionDef
    direction TB
    _visit_FunctionDef_node_0 --> _visit_FunctionDef_node_1
    _visit_FunctionDef_node_1 --> _visit_FunctionDef_node_2
    _visit_FunctionDef_node_2 --> _visit_FunctionDef_node_3
    _visit_FunctionDef_node_3 --> _visit_FunctionDef_node_4
    _visit_FunctionDef_node_4 --> _visit_FunctionDef_node_5
    _visit_FunctionDef_node_5 --> _visit_FunctionDef_node_6
    _visit_FunctionDef_node_6 --> _visit_FunctionDef_node_7
    _visit_FunctionDef_node_7 --> _visit_FunctionDef_node_8
    _visit_FunctionDef_node_8 --> _visit_FunctionDef_node_9
    _visit_FunctionDef_node_9 --> _visit_FunctionDef_node_10
    _visit_FunctionDef_node_10 --> _visit_FunctionDef_node_11
    _visit_FunctionDef_node_11 --> _visit_FunctionDef_node_12
    _visit_FunctionDef_node_12 --> _visit_FunctionDef_node_13
    _visit_FunctionDef_node_13 --> _visit_FunctionDef_node_14
    _visit_FunctionDef_node_14 --> _visit_FunctionDef_node_15
    _visit_FunctionDef_node_15 --> _visit_FunctionDef_node_16
    _visit_FunctionDef_node_16 --> _visit_FunctionDef_node_17
    _visit_FunctionDef_node_17 --> _visit_FunctionDef_node_18
    _visit_FunctionDef_node_18 --> _visit_FunctionDef_node_19
    _visit_FunctionDef_node_19 --> _visit_FunctionDef_node_20
    _visit_FunctionDef_node_20 --> _visit_FunctionDef_node_21
    _visit_FunctionDef_node_21 --> _visit_FunctionDef_node_22
    _visit_FunctionDef_node_22 --> _visit_FunctionDef_node_23
    _visit_FunctionDef_node_23 --> _visit_FunctionDef_node_24
    _visit_FunctionDef_node_24 --> _visit_FunctionDef_node_25
    _visit_FunctionDef_node_25 --> _visit_FunctionDef_node_26
    _visit_FunctionDef_node_26 --> _visit_FunctionDef_node_27
    _visit_FunctionDef_node_27 --> _visit_FunctionDef_node_28
    _visit_FunctionDef_node_28 --> _visit_FunctionDef_node_29
    _visit_FunctionDef_node_29 --> _visit_FunctionDef_node_30
    _visit_FunctionDef_node_30 --> _visit_FunctionDef_node_31
    _visit_FunctionDef_node_31 --> _visit_FunctionDef_node_32
    _visit_FunctionDef_node_32 --> _visit_FunctionDef_node_33
    _visit_FunctionDef_node_33 --> _visit_FunctionDef_node_34
    _visit_FunctionDef_node_34 --> _visit_FunctionDef_node_35
    _visit_FunctionDef_node_35 --> _visit_FunctionDef_node_36
    _visit_FunctionDef_node_36 --> _visit_FunctionDef_node_37
    _visit_FunctionDef_node_37 --> _visit_FunctionDef_node_38
    _visit_FunctionDef_node_38 --> _visit_FunctionDef_node_39
    _visit_FunctionDef_node_39 --> _visit_FunctionDef_node_40
    _visit_FunctionDef_node_40 --> _visit_FunctionDef_node_41
    _visit_FunctionDef_node_41 --> _visit_FunctionDef_node_42
    _visit_FunctionDef_node_42 --> _visit_FunctionDef_node_43
    _visit_FunctionDef_node_43 --> _visit_FunctionDef_node_44
    _visit_FunctionDef_node_44 --> _visit_FunctionDef_node_45
    _visit_FunctionDef_node_45 --> _visit_FunctionDef_node_46
    _visit_FunctionDef_node_46 --> _visit_FunctionDef_node_47
    _visit_FunctionDef_node_47 --> _visit_FunctionDef_node_48
    _visit_FunctionDef_node_48 --> _visit_FunctionDef_node_49
    _visit_FunctionDef_node_49 --> _visit_FunctionDef_node_50
    _visit_FunctionDef_node_50 --> _visit_FunctionDef_node_51
    _visit_FunctionDef_node_51 --> _visit_FunctionDef_node_52
    _visit_FunctionDef_node_52 --> _visit_FunctionDef_node_53
    _visit_FunctionDef_node_53 --> _visit_FunctionDef_node_54
    _visit_FunctionDef_node_54 --> _visit_FunctionDef_node_55
    _visit_FunctionDef_node_55 --> _visit_FunctionDef_node_56
    _visit_FunctionDef_node_56 --> _visit_FunctionDef_node_57
    _visit_FunctionDef_node_57 --> _visit_FunctionDef_node_58
    _visit_FunctionDef_node_58 --> _visit_FunctionDef_node_59
    _visit_FunctionDef_node_59 --> _visit_FunctionDef_node_60
    _visit_FunctionDef_node_60 --> _visit_FunctionDef_node_61
    _visit_FunctionDef_node_61 --> _visit_FunctionDef_node_62
    _visit_FunctionDef_node_62 --> _visit_FunctionDef_node_63
    _visit_FunctionDef_node_63 --> _visit_FunctionDef_node_64
    _visit_FunctionDef_node_64 --> _visit_FunctionDef_node_65
    _visit_FunctionDef_node_65 --> _visit_FunctionDef_node_66
    _visit_FunctionDef_node_66 --> _visit_FunctionDef_node_67
    _visit_FunctionDef_node_67 --> _visit_FunctionDef_node_68
    _visit_FunctionDef_node_68 --> _visit_FunctionDef_node_69
    _visit_FunctionDef_node_69 --> _visit_FunctionDef_node_70
    _visit_FunctionDef_node_70 --> _visit_FunctionDef_node_71
    _visit_FunctionDef_node_71 --> _visit_FunctionDef_node_72
    _visit_FunctionDef_node_72 --> _visit_FunctionDef_node_73
    _visit_FunctionDef_node_73 --> _visit_FunctionDef_node_74
    _visit_FunctionDef_node_74 --> _visit_FunctionDef_node_75
    _visit_FunctionDef_node_75 --> _visit_FunctionDef_node_76
    _visit_FunctionDef_node_76 --> _visit_FunctionDef_node_77
    _visit_FunctionDef_node_77 --> _visit_FunctionDef_node_78
    _visit_FunctionDef_node_78 --> _visit_FunctionDef_node_79
    _visit_FunctionDef_node_79 --> _visit_FunctionDef_node_80
  end
  subgraph generic_visit
    direction TB
    _generic_visit_node_0 --> _generic_visit_node_1
    _generic_visit_node_1 --> _generic_visit_node_2
  end
  subgraph get_list_of_elements
    direction TB
    _get_list_of_elements_node_0 --> _get_list_of_elements_node_1
    _get_list_of_elements_node_1 --> _get_list_of_elements_node_2
    _get_list_of_elements_node_2 --> _get_list_of_elements_node_3
    _get_list_of_elements_node_3 --> _get_list_of_elements_node_4
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='ast',
      names=[
        alias(name='AST'),
        alias(name='FunctionDef'),
        alias(name='Import'),
        alias(name='ImportFrom'),
        alias(name='Module'),
        alias(name='NodeVisitor')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=73),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidBlock'),
        alias(name='MermaidElement'),
        alias(name='MermaidFunction'),
        alias(name='MermaidLink'),
        alias(name='MermaidModule'),
        alias(name='MermaidNode')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=9,
      end_col_offset=1),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Any'),
        alias(name='Optional')],
      level=0,
      lineno=11,
      col_offset=0,
      end_lineno=11,
      end_col_offset=32),
    ClassDef(
      name='ImportNodeFinder',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=14,
          col_offset=23,
          end_lineno=14,
          end_col_offset=34)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=15,
                col_offset=17,
                end_lineno=15,
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
                  lineno=16,
                  col_offset=8,
                  end_lineno=16,
                  end_col_offset=12),
                attr='found_imports',
                ctx=Store(),
                lineno=16,
                col_offset=8,
                end_lineno=16,
                end_col_offset=26),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=16,
                  col_offset=29,
                  end_lineno=16,
                  end_col_offset=33),
                slice=Name(
                  id='str',
                  ctx=Load(),
                  lineno=16,
                  col_offset=34,
                  end_lineno=16,
                  end_col_offset=37),
                ctx=Load(),
                lineno=16,
                col_offset=29,
                end_lineno=16,
                end_col_offset=38),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=16,
                col_offset=41,
                end_lineno=16,
                end_col_offset=43),
              simple=0,
              lineno=16,
              col_offset=8,
              end_lineno=16,
              end_col_offset=43)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=15,
            col_offset=26,
            end_lineno=15,
            end_col_offset=30),
          lineno=15,
          col_offset=4,
          end_lineno=16,
          end_col_offset=43),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=18,
                col_offset=21,
                end_lineno=18,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=18,
                  col_offset=33,
                  end_lineno=18,
                  end_col_offset=39),
                lineno=18,
                col_offset=27,
                end_lineno=18,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=19,
                col_offset=12,
                end_lineno=19,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=19,
                  col_offset=17,
                  end_lineno=19,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=19,
                col_offset=17,
                end_lineno=19,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=20,
                          col_offset=12,
                          end_lineno=20,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=20,
                        col_offset=12,
                        end_lineno=20,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=20,
                      col_offset=12,
                      end_lineno=20,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=20,
                                col_offset=41,
                                end_lineno=20,
                                end_col_offset=42),
                              attr='name',
                              ctx=Load(),
                              lineno=20,
                              col_offset=41,
                              end_lineno=20,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=20,
                            col_offset=38,
                            end_lineno=20,
                            end_col_offset=51),
                          Constant(
                            value='.*',
                            lineno=20,
                            col_offset=38,
                            end_lineno=20,
                            end_col_offset=51)],
                        lineno=20,
                        col_offset=38,
                        end_lineno=20,
                        end_col_offset=51)],
                    keywords=[],
                    lineno=20,
                    col_offset=12,
                    end_lineno=20,
                    end_col_offset=52),
                  lineno=20,
                  col_offset=12,
                  end_lineno=20,
                  end_col_offset=52)],
              orelse=[],
              lineno=19,
              col_offset=8,
              end_lineno=20,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=18,
            col_offset=44,
            end_lineno=18,
            end_col_offset=48),
          lineno=18,
          col_offset=4,
          end_lineno=20,
          end_col_offset=52),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=22,
                col_offset=25,
                end_lineno=22,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=22,
                  col_offset=37,
                  end_lineno=22,
                  end_col_offset=47),
                lineno=22,
                col_offset=31,
                end_lineno=22,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='module',
                  ctx=Store(),
                  lineno=23,
                  col_offset=8,
                  end_lineno=23,
                  end_col_offset=14)],
              value=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=23,
                  col_offset=17,
                  end_lineno=23,
                  end_col_offset=21),
                attr='module',
                ctx=Load(),
                lineno=23,
                col_offset=17,
                end_lineno=23,
                end_col_offset=28),
              lineno=23,
              col_offset=8,
              end_lineno=23,
              end_col_offset=28),
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=24,
                col_offset=12,
                end_lineno=24,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=24,
                  col_offset=17,
                  end_lineno=24,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=24,
                col_offset=17,
                end_lineno=24,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=25,
                          col_offset=12,
                          end_lineno=25,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=25,
                        col_offset=12,
                        end_lineno=25,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=25,
                      col_offset=12,
                      end_lineno=25,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Name(
                              id='module',
                              ctx=Load(),
                              lineno=25,
                              col_offset=41,
                              end_lineno=25,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58),
                          Constant(
                            value='.',
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58),
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=25,
                                col_offset=50,
                                end_lineno=25,
                                end_col_offset=51),
                              attr='name',
                              ctx=Load(),
                              lineno=25,
                              col_offset=50,
                              end_lineno=25,
                              end_col_offset=56),
                            conversion=-1,
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58)],
                        lineno=25,
                        col_offset=38,
                        end_lineno=25,
                        end_col_offset=58)],
                    keywords=[],
                    lineno=25,
                    col_offset=12,
                    end_lineno=25,
                    end_col_offset=59),
                  lineno=25,
                  col_offset=12,
                  end_lineno=25,
                  end_col_offset=59)],
              orelse=[],
              lineno=24,
              col_offset=8,
              end_lineno=25,
              end_col_offset=59)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=22,
            col_offset=52,
            end_lineno=22,
            end_col_offset=56),
          lineno=22,
          col_offset=4,
          end_lineno=25,
          end_col_offset=59),
        FunctionDef(
          name='get_found_imports',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=27,
                col_offset=26,
                end_lineno=27,
                end_col_offset=30)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=28,
                  col_offset=15,
                  end_lineno=28,
                  end_col_offset=19),
                attr='found_imports',
                ctx=Load(),
                lineno=28,
                col_offset=15,
                end_lineno=28,
                end_col_offset=33),
              lineno=28,
              col_offset=8,
              end_lineno=28,
              end_col_offset=33)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=27,
              col_offset=35,
              end_lineno=27,
              end_col_offset=39),
            slice=Name(
              id='str',
              ctx=Load(),
              lineno=27,
              col_offset=40,
              end_lineno=27,
              end_col_offset=43),
            ctx=Load(),
            lineno=27,
            col_offset=35,
            end_lineno=27,
            end_col_offset=44),
          lineno=27,
          col_offset=4,
          end_lineno=28,
          end_col_offset=33)],
      decorator_list=[],
      lineno=14,
      col_offset=0,
      end_lineno=28,
      end_col_offset=33),
    ClassDef(
      name='LinkGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=31,
          col_offset=20,
          end_lineno=31,
          end_col_offset=31)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=32,
                col_offset=17,
                end_lineno=32,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=32,
                  col_offset=32,
                  end_lineno=32,
                  end_col_offset=35),
                lineno=32,
                col_offset=23,
                end_lineno=32,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=32,
                col_offset=38,
                end_lineno=32,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=33,
                  col_offset=8,
                  end_lineno=33,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=33,
                col_offset=8,
                end_lineno=33,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=33,
                  col_offset=24,
                  end_lineno=33,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=33,
                  col_offset=29,
                  end_lineno=33,
                  end_col_offset=43),
                ctx=Load(),
                lineno=33,
                col_offset=24,
                end_lineno=33,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=33,
                col_offset=47,
                end_lineno=33,
                end_col_offset=49),
              simple=0,
              lineno=33,
              col_offset=8,
              end_lineno=33,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=34,
                  col_offset=8,
                  end_lineno=34,
                  end_col_offset=12),
                attr='prev_node',
                ctx=Store(),
                lineno=34,
                col_offset=8,
                end_lineno=34,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='Optional',
                  ctx=Load(),
                  lineno=34,
                  col_offset=25,
                  end_lineno=34,
                  end_col_offset=33),
                slice=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=34,
                  col_offset=34,
                  end_lineno=34,
                  end_col_offset=37),
                ctx=Load(),
                lineno=34,
                col_offset=25,
                end_lineno=34,
                end_col_offset=38),
              value=Constant(
                value=None,
                lineno=34,
                col_offset=41,
                end_lineno=34,
                end_col_offset=45),
              simple=0,
              lineno=34,
              col_offset=8,
              end_lineno=34,
              end_col_offset=45),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=35,
                  col_offset=8,
                  end_lineno=35,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=35,
                col_offset=8,
                end_lineno=35,
                end_col_offset=18),
              annotation=Name(
                id='int',
                ctx=Load(),
                lineno=35,
                col_offset=21,
                end_lineno=35,
                end_col_offset=24),
              value=Constant(
                value=0,
                lineno=35,
                col_offset=27,
                end_lineno=35,
                end_col_offset=28),
              simple=0,
              lineno=35,
              col_offset=8,
              end_lineno=35,
              end_col_offset=28),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=36,
                    col_offset=8,
                    end_lineno=36,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=36,
                  col_offset=8,
                  end_lineno=36,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=36,
                col_offset=22,
                end_lineno=36,
                end_col_offset=28),
              lineno=36,
              col_offset=8,
              end_lineno=36,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=32,
            col_offset=45,
            end_lineno=32,
            end_col_offset=49),
          lineno=32,
          col_offset=4,
          end_lineno=36,
          end_col_offset=28),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=38,
                col_offset=21,
                end_lineno=38,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=38,
                  col_offset=33,
                  end_lineno=38,
                  end_col_offset=39),
                lineno=38,
                col_offset=27,
                end_lineno=38,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=39,
              col_offset=8,
              end_lineno=39,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=38,
            col_offset=44,
            end_lineno=38,
            end_col_offset=48),
          lineno=38,
          col_offset=4,
          end_lineno=39,
          end_col_offset=12),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=41,
                col_offset=25,
                end_lineno=41,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=41,
                  col_offset=37,
                  end_lineno=41,
                  end_col_offset=47),
                lineno=41,
                col_offset=31,
                end_lineno=41,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=42,
              col_offset=8,
              end_lineno=42,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=41,
            col_offset=52,
            end_lineno=41,
            end_col_offset=56),
          lineno=41,
          col_offset=4,
          end_lineno=42,
          end_col_offset=12),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=44,
                col_offset=26,
                end_lineno=44,
                end_col_offset=30),
              arg(
                arg='node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=44,
                  col_offset=38,
                  end_lineno=44,
                  end_col_offset=49),
                lineno=44,
                col_offset=32,
                end_lineno=44,
                end_col_offset=49)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='block_generator',
                  ctx=Store(),
                  lineno=45,
                  col_offset=8,
                  end_lineno=45,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=45,
                  col_offset=26,
                  end_lineno=45,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=45,
                        col_offset=48,
                        end_lineno=45,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=45,
                      col_offset=48,
                      end_lineno=45,
                      end_col_offset=59),
                    lineno=45,
                    col_offset=41,
                    end_lineno=45,
                    end_col_offset=59)],
                lineno=45,
                col_offset=26,
                end_lineno=45,
                end_col_offset=60),
              lineno=45,
              col_offset=8,
              end_lineno=45,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=46,
                    col_offset=8,
                    end_lineno=46,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=46,
                  col_offset=8,
                  end_lineno=46,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=46,
                    col_offset=30,
                    end_lineno=46,
                    end_col_offset=34)],
                keywords=[],
                lineno=46,
                col_offset=8,
                end_lineno=46,
                end_col_offset=35),
              lineno=46,
              col_offset=8,
              end_lineno=46,
              end_col_offset=35),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=47,
                      col_offset=8,
                      end_lineno=47,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=47,
                    col_offset=8,
                    end_lineno=47,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=47,
                  col_offset=8,
                  end_lineno=47,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Attribute(
                      value=Name(
                        id='block_generator',
                        ctx=Load(),
                        lineno=47,
                        col_offset=29,
                        end_lineno=47,
                        end_col_offset=44),
                      attr='get_list_of_elements',
                      ctx=Load(),
                      lineno=47,
                      col_offset=29,
                      end_lineno=47,
                      end_col_offset=65),
                    args=[],
                    keywords=[],
                    lineno=47,
                    col_offset=29,
                    end_lineno=47,
                    end_col_offset=67)],
                keywords=[],
                lineno=47,
                col_offset=8,
                end_lineno=47,
                end_col_offset=68),
              lineno=47,
              col_offset=8,
              end_lineno=47,
              end_col_offset=68)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=44,
            col_offset=54,
            end_lineno=44,
            end_col_offset=57),
          lineno=44,
          col_offset=4,
          end_lineno=47,
          end_col_offset=68),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=49,
                col_offset=22,
                end_lineno=49,
                end_col_offset=26),
              arg(
                arg='node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=49,
                  col_offset=34,
                  end_lineno=49,
                  end_col_offset=37),
                lineno=49,
                col_offset=28,
                end_lineno=49,
                end_col_offset=37)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='mermaid_data',
                  ctx=Store(),
                  lineno=50,
                  col_offset=8,
                  end_lineno=50,
                  end_col_offset=20)],
              value=Call(
                func=Name(
                  id='MermaidNode',
                  ctx=Load(),
                  lineno=50,
                  col_offset=23,
                  end_lineno=50,
                  end_col_offset=34),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='node',
                      ctx=Load(),
                      lineno=51,
                      col_offset=21,
                      end_lineno=51,
                      end_col_offset=25),
                    lineno=51,
                    col_offset=12,
                    end_lineno=51,
                    end_col_offset=25),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=52,
                              col_offset=33,
                              end_lineno=52,
                              end_col_offset=37),
                            attr='prefix',
                            ctx=Load(),
                            lineno=52,
                            col_offset=33,
                            end_lineno=52,
                            end_col_offset=44),
                          conversion=-1,
                          lineno=52,
                          col_offset=30,
                          end_lineno=52,
                          end_col_offset=64),
                        Constant(
                          value='_node_',
                          lineno=52,
                          col_offset=30,
                          end_lineno=52,
                          end_col_offset=64),
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=52,
                              col_offset=52,
                              end_lineno=52,
                              end_col_offset=56),
                            attr='count',
                            ctx=Load(),
                            lineno=52,
                            col_offset=52,
                            end_lineno=52,
                            end_col_offset=62),
                          conversion=-1,
                          lineno=52,
                          col_offset=30,
                          end_lineno=52,
                          end_col_offset=64)],
                      lineno=52,
                      col_offset=30,
                      end_lineno=52,
                      end_col_offset=64),
                    lineno=52,
                    col_offset=12,
                    end_lineno=52,
                    end_col_offset=64),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Call(
                        func=Name(
                          id='type',
                          ctx=Load(),
                          lineno=53,
                          col_offset=25,
                          end_lineno=53,
                          end_col_offset=29),
                        args=[
                          Name(
                            id='node',
                            ctx=Load(),
                            lineno=53,
                            col_offset=30,
                            end_lineno=53,
                            end_col_offset=34)],
                        keywords=[],
                        lineno=53,
                        col_offset=25,
                        end_lineno=53,
                        end_col_offset=35),
                      attr='__name__',
                      ctx=Load(),
                      lineno=53,
                      col_offset=25,
                      end_lineno=53,
                      end_col_offset=44),
                    lineno=53,
                    col_offset=12,
                    end_lineno=53,
                    end_col_offset=44)],
                lineno=50,
                col_offset=23,
                end_lineno=54,
                end_col_offset=9),
              lineno=50,
              col_offset=8,
              end_lineno=54,
              end_col_offset=9),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=55,
                  col_offset=8,
                  end_lineno=55,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=55,
                col_offset=8,
                end_lineno=55,
                end_col_offset=18),
              op=Add(),
              value=Constant(
                value=1,
                lineno=55,
                col_offset=22,
                end_lineno=55,
                end_col_offset=23),
              lineno=55,
              col_offset=8,
              end_lineno=55,
              end_col_offset=23),
            If(
              test=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=56,
                  col_offset=11,
                  end_lineno=56,
                  end_col_offset=15),
                attr='prev_node',
                ctx=Load(),
                lineno=56,
                col_offset=11,
                end_lineno=56,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=57,
                          col_offset=12,
                          end_lineno=57,
                          end_col_offset=16),
                        attr='elements',
                        ctx=Load(),
                        lineno=57,
                        col_offset=12,
                        end_lineno=57,
                        end_col_offset=25),
                      attr='append',
                      ctx=Load(),
                      lineno=57,
                      col_offset=12,
                      end_lineno=57,
                      end_col_offset=32),
                    args=[
                      Call(
                        func=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=57,
                          col_offset=33,
                          end_lineno=57,
                          end_col_offset=44),
                        args=[],
                        keywords=[
                          keyword(
                            arg='from_',
                            value=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=57,
                                col_offset=51,
                                end_lineno=57,
                                end_col_offset=55),
                              attr='prev_node',
                              ctx=Load(),
                              lineno=57,
                              col_offset=51,
                              end_lineno=57,
                              end_col_offset=65),
                            lineno=57,
                            col_offset=45,
                            end_lineno=57,
                            end_col_offset=65),
                          keyword(
                            arg='to',
                            value=Name(
                              id='mermaid_data',
                              ctx=Load(),
                              lineno=57,
                              col_offset=70,
                              end_lineno=57,
                              end_col_offset=82),
                            lineno=57,
                            col_offset=67,
                            end_lineno=57,
                            end_col_offset=82)],
                        lineno=57,
                        col_offset=33,
                        end_lineno=57,
                        end_col_offset=83)],
                    keywords=[],
                    lineno=57,
                    col_offset=12,
                    end_lineno=57,
                    end_col_offset=84),
                  lineno=57,
                  col_offset=12,
                  end_lineno=57,
                  end_col_offset=84)],
              orelse=[],
              lineno=56,
              col_offset=8,
              end_lineno=57,
              end_col_offset=84),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=58,
                    col_offset=8,
                    end_lineno=58,
                    end_col_offset=12),
                  attr='prev_node',
                  ctx=Store(),
                  lineno=58,
                  col_offset=8,
                  end_lineno=58,
                  end_col_offset=22)],
              value=Name(
                id='mermaid_data',
                ctx=Load(),
                lineno=58,
                col_offset=25,
                end_lineno=58,
                end_col_offset=37),
              lineno=58,
              col_offset=8,
              end_lineno=58,
              end_col_offset=37),
            Return(
              value=Call(
                func=Attribute(
                  value=Call(
                    func=Name(
                      id='super',
                      ctx=Load(),
                      lineno=61,
                      col_offset=15,
                      end_lineno=61,
                      end_col_offset=20),
                    args=[],
                    keywords=[],
                    lineno=61,
                    col_offset=15,
                    end_lineno=61,
                    end_col_offset=22),
                  attr='generic_visit',
                  ctx=Load(),
                  lineno=61,
                  col_offset=15,
                  end_lineno=61,
                  end_col_offset=36),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=61,
                    col_offset=37,
                    end_lineno=61,
                    end_col_offset=41)],
                keywords=[],
                lineno=61,
                col_offset=15,
                end_lineno=61,
                end_col_offset=42),
              lineno=61,
              col_offset=8,
              end_lineno=61,
              end_col_offset=42)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=49,
            col_offset=42,
            end_lineno=49,
            end_col_offset=45),
          lineno=49,
          col_offset=4,
          end_lineno=61,
          end_col_offset=42),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=63,
                col_offset=29,
                end_lineno=63,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=64,
                  col_offset=15,
                  end_lineno=64,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=64,
                col_offset=15,
                end_lineno=64,
                end_col_offset=28),
              lineno=64,
              col_offset=8,
              end_lineno=64,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=63,
              col_offset=38,
              end_lineno=63,
              end_col_offset=42),
            slice=Name(
              id='MermaidLink',
              ctx=Load(),
              lineno=63,
              col_offset=43,
              end_lineno=63,
              end_col_offset=54),
            ctx=Load(),
            lineno=63,
            col_offset=38,
            end_lineno=63,
            end_col_offset=55),
          lineno=63,
          col_offset=4,
          end_lineno=64,
          end_col_offset=28)],
      decorator_list=[],
      lineno=31,
      col_offset=0,
      end_lineno=64,
      end_col_offset=28),
    ClassDef(
      name='BlockGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=67,
          col_offset=21,
          end_lineno=67,
          end_col_offset=32)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=68,
                col_offset=17,
                end_lineno=68,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=68,
                  col_offset=32,
                  end_lineno=68,
                  end_col_offset=35),
                lineno=68,
                col_offset=23,
                end_lineno=68,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=68,
                col_offset=38,
                end_lineno=68,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=69,
                  col_offset=8,
                  end_lineno=69,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=69,
                  col_offset=24,
                  end_lineno=69,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=69,
                  col_offset=29,
                  end_lineno=69,
                  end_col_offset=43),
                ctx=Load(),
                lineno=69,
                col_offset=24,
                end_lineno=69,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=69,
                col_offset=47,
                end_lineno=69,
                end_col_offset=49),
              simple=0,
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=70,
                  col_offset=8,
                  end_lineno=70,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=70,
                col_offset=8,
                end_lineno=70,
                end_col_offset=18),
              annotation=Name(
                id='int',
                ctx=Load(),
                lineno=70,
                col_offset=21,
                end_lineno=70,
                end_col_offset=24),
              value=Constant(
                value=0,
                lineno=70,
                col_offset=27,
                end_lineno=70,
                end_col_offset=28),
              simple=0,
              lineno=70,
              col_offset=8,
              end_lineno=70,
              end_col_offset=28),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=71,
                    col_offset=8,
                    end_lineno=71,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=71,
                  col_offset=8,
                  end_lineno=71,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=71,
                col_offset=22,
                end_lineno=71,
                end_col_offset=28),
              lineno=71,
              col_offset=8,
              end_lineno=71,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=68,
            col_offset=45,
            end_lineno=68,
            end_col_offset=49),
          lineno=68,
          col_offset=4,
          end_lineno=71,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=73,
                col_offset=15,
                end_lineno=73,
                end_col_offset=19)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='value',
                  ctx=Store(),
                  lineno=74,
                  col_offset=8,
                  end_lineno=74,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=74,
                  col_offset=16,
                  end_lineno=74,
                  end_col_offset=20),
                attr='count',
                ctx=Load(),
                lineno=74,
                col_offset=16,
                end_lineno=74,
                end_col_offset=26),
              lineno=74,
              col_offset=8,
              end_lineno=74,
              end_col_offset=26),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=75,
                  col_offset=8,
                  end_lineno=75,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=75,
                col_offset=8,
                end_lineno=75,
                end_col_offset=18),
              op=Add(),
              value=Constant(
                value=1,
                lineno=75,
                col_offset=21,
                end_lineno=75,
                end_col_offset=22),
              lineno=75,
              col_offset=8,
              end_lineno=75,
              end_col_offset=22),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=76,
                col_offset=15,
                end_lineno=76,
                end_col_offset=20),
              lineno=76,
              col_offset=8,
              end_lineno=76,
              end_col_offset=20)],
          decorator_list=[],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=73,
            col_offset=24,
            end_lineno=73,
            end_col_offset=27),
          lineno=73,
          col_offset=4,
          end_lineno=76,
          end_col_offset=20),
        FunctionDef(
          name='visit_Module',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=78,
                col_offset=21,
                end_lineno=78,
                end_col_offset=25),
              arg(
                arg='block_node',
                annotation=Name(
                  id='Module',
                  ctx=Load(),
                  lineno=78,
                  col_offset=39,
                  end_lineno=78,
                  end_col_offset=45),
                lineno=78,
                col_offset=27,
                end_lineno=78,
                end_col_offset=45)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we might want a subgraph, so parse content',
                lineno=79,
                col_offset=8,
                end_lineno=79,
                end_col_offset=73),
              lineno=79,
              col_offset=8,
              end_lineno=79,
              end_col_offset=73),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=80,
                  col_offset=8,
                  end_lineno=80,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=80,
                  col_offset=25,
                  end_lineno=80,
                  end_col_offset=38),
                args=[],
                keywords=[],
                lineno=80,
                col_offset=25,
                end_lineno=80,
                end_col_offset=40),
              lineno=80,
              col_offset=8,
              end_lineno=80,
              end_col_offset=40),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=81,
                col_offset=12,
                end_lineno=81,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=81,
                  col_offset=27,
                  end_lineno=81,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=81,
                col_offset=27,
                end_lineno=81,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=82,
                        col_offset=12,
                        end_lineno=82,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=82,
                      col_offset=12,
                      end_lineno=82,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=82,
                          col_offset=38,
                          end_lineno=82,
                          end_col_offset=49),
                        lineno=82,
                        col_offset=33,
                        end_lineno=82,
                        end_col_offset=49)],
                    lineno=82,
                    col_offset=12,
                    end_lineno=82,
                    end_col_offset=50),
                  lineno=82,
                  col_offset=12,
                  end_lineno=82,
                  end_col_offset=50)],
              orelse=[],
              lineno=81,
              col_offset=8,
              end_lineno=82,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=84,
                  col_offset=8,
                  end_lineno=84,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidModule',
                  ctx=Load(),
                  lineno=84,
                  col_offset=24,
                  end_lineno=84,
                  end_col_offset=37),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=85,
                      col_offset=23,
                      end_lineno=85,
                      end_col_offset=33),
                    lineno=85,
                    col_offset=12,
                    end_lineno=85,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=86,
                              col_offset=35,
                              end_lineno=86,
                              end_col_offset=39),
                            attr='prefix',
                            ctx=Load(),
                            lineno=86,
                            col_offset=35,
                            end_lineno=86,
                            end_col_offset=46),
                          conversion=-1,
                          lineno=86,
                          col_offset=32,
                          end_lineno=86,
                          end_col_offset=71),
                        Constant(
                          value='_module_',
                          lineno=86,
                          col_offset=32,
                          end_lineno=86,
                          end_col_offset=71),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=86,
                                col_offset=56,
                                end_lineno=86,
                                end_col_offset=60),
                              attr='_count',
                              ctx=Load(),
                              lineno=86,
                              col_offset=56,
                              end_lineno=86,
                              end_col_offset=67),
                            args=[],
                            keywords=[],
                            lineno=86,
                            col_offset=56,
                            end_lineno=86,
                            end_col_offset=69),
                          conversion=-1,
                          lineno=86,
                          col_offset=32,
                          end_lineno=86,
                          end_col_offset=71)],
                      lineno=86,
                      col_offset=32,
                      end_lineno=86,
                      end_col_offset=71),
                    lineno=86,
                    col_offset=12,
                    end_lineno=86,
                    end_col_offset=71),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=87,
                          col_offset=29,
                          end_lineno=87,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=87,
                        col_offset=29,
                        end_lineno=87,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=87,
                      col_offset=29,
                      end_lineno=87,
                      end_col_offset=66),
                    lineno=87,
                    col_offset=12,
                    end_lineno=87,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Constant(
                      value='module',
                      lineno=88,
                      col_offset=25,
                      end_lineno=88,
                      end_col_offset=33),
                    lineno=88,
                    col_offset=12,
                    end_lineno=88,
                    end_col_offset=33)],
                lineno=84,
                col_offset=24,
                end_lineno=89,
                end_col_offset=9),
              lineno=84,
              col_offset=8,
              end_lineno=89,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=91,
                      col_offset=8,
                      end_lineno=91,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=91,
                    col_offset=8,
                    end_lineno=91,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=91,
                  col_offset=8,
                  end_lineno=91,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=91,
                    col_offset=29,
                    end_lineno=91,
                    end_col_offset=42)],
                keywords=[],
                lineno=91,
                col_offset=8,
                end_lineno=91,
                end_col_offset=43),
              lineno=91,
              col_offset=8,
              end_lineno=91,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=78,
            col_offset=50,
            end_lineno=78,
            end_col_offset=53),
          lineno=78,
          col_offset=4,
          end_lineno=91,
          end_col_offset=43),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=93,
                col_offset=26,
                end_lineno=93,
                end_col_offset=30),
              arg(
                arg='block_node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=93,
                  col_offset=44,
                  end_lineno=93,
                  end_col_offset=55),
                lineno=93,
                col_offset=32,
                end_lineno=93,
                end_col_offset=55)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=94,
                col_offset=8,
                end_lineno=94,
                end_col_offset=67),
              lineno=94,
              col_offset=8,
              end_lineno=94,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=95,
                  col_offset=8,
                  end_lineno=95,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=95,
                  col_offset=25,
                  end_lineno=95,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=95,
                              col_offset=49,
                              end_lineno=95,
                              end_col_offset=53),
                            attr='prefix',
                            ctx=Load(),
                            lineno=95,
                            col_offset=49,
                            end_lineno=95,
                            end_col_offset=60),
                          conversion=-1,
                          lineno=95,
                          col_offset=46,
                          end_lineno=95,
                          end_col_offset=80),
                        Constant(
                          value='_',
                          lineno=95,
                          col_offset=46,
                          end_lineno=95,
                          end_col_offset=80),
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='block_node',
                              ctx=Load(),
                              lineno=95,
                              col_offset=63,
                              end_lineno=95,
                              end_col_offset=73),
                            attr='name',
                            ctx=Load(),
                            lineno=95,
                            col_offset=63,
                            end_lineno=95,
                            end_col_offset=78),
                          conversion=-1,
                          lineno=95,
                          col_offset=46,
                          end_lineno=95,
                          end_col_offset=80)],
                      lineno=95,
                      col_offset=46,
                      end_lineno=95,
                      end_col_offset=80),
                    lineno=95,
                    col_offset=39,
                    end_lineno=95,
                    end_col_offset=80)],
                lineno=95,
                col_offset=25,
                end_lineno=95,
                end_col_offset=81),
              lineno=95,
              col_offset=8,
              end_lineno=95,
              end_col_offset=81),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=96,
                col_offset=12,
                end_lineno=96,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=96,
                  col_offset=27,
                  end_lineno=96,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=96,
                col_offset=27,
                end_lineno=96,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=97,
                        col_offset=12,
                        end_lineno=97,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=97,
                      col_offset=12,
                      end_lineno=97,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=97,
                          col_offset=38,
                          end_lineno=97,
                          end_col_offset=49),
                        lineno=97,
                        col_offset=33,
                        end_lineno=97,
                        end_col_offset=49)],
                    lineno=97,
                    col_offset=12,
                    end_lineno=97,
                    end_col_offset=50),
                  lineno=97,
                  col_offset=12,
                  end_lineno=97,
                  end_col_offset=50)],
              orelse=[],
              lineno=96,
              col_offset=8,
              end_lineno=97,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=99,
                  col_offset=8,
                  end_lineno=99,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidFunction',
                  ctx=Load(),
                  lineno=99,
                  col_offset=24,
                  end_lineno=99,
                  end_col_offset=39),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=100,
                      col_offset=23,
                      end_lineno=100,
                      end_col_offset=33),
                    lineno=100,
                    col_offset=12,
                    end_lineno=100,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=101,
                              col_offset=35,
                              end_lineno=101,
                              end_col_offset=39),
                            attr='prefix',
                            ctx=Load(),
                            lineno=101,
                            col_offset=35,
                            end_lineno=101,
                            end_col_offset=46),
                          conversion=-1,
                          lineno=101,
                          col_offset=32,
                          end_lineno=101,
                          end_col_offset=73),
                        Constant(
                          value='_function_',
                          lineno=101,
                          col_offset=32,
                          end_lineno=101,
                          end_col_offset=73),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=101,
                                col_offset=58,
                                end_lineno=101,
                                end_col_offset=62),
                              attr='_count',
                              ctx=Load(),
                              lineno=101,
                              col_offset=58,
                              end_lineno=101,
                              end_col_offset=69),
                            args=[],
                            keywords=[],
                            lineno=101,
                            col_offset=58,
                            end_lineno=101,
                            end_col_offset=71),
                          conversion=-1,
                          lineno=101,
                          col_offset=32,
                          end_lineno=101,
                          end_col_offset=73)],
                      lineno=101,
                      col_offset=32,
                      end_lineno=101,
                      end_col_offset=73),
                    lineno=101,
                    col_offset=12,
                    end_lineno=101,
                    end_col_offset=73),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=102,
                          col_offset=29,
                          end_lineno=102,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=102,
                        col_offset=29,
                        end_lineno=102,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=102,
                      col_offset=29,
                      end_lineno=102,
                      end_col_offset=66),
                    lineno=102,
                    col_offset=12,
                    end_lineno=102,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Name(
                        id='block_node',
                        ctx=Load(),
                        lineno=103,
                        col_offset=25,
                        end_lineno=103,
                        end_col_offset=35),
                      attr='name',
                      ctx=Load(),
                      lineno=103,
                      col_offset=25,
                      end_lineno=103,
                      end_col_offset=40),
                    lineno=103,
                    col_offset=12,
                    end_lineno=103,
                    end_col_offset=40)],
                lineno=99,
                col_offset=24,
                end_lineno=104,
                end_col_offset=9),
              lineno=99,
              col_offset=8,
              end_lineno=104,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=108,
                      col_offset=8,
                      end_lineno=108,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=108,
                    col_offset=8,
                    end_lineno=108,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=108,
                  col_offset=8,
                  end_lineno=108,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=108,
                    col_offset=29,
                    end_lineno=108,
                    end_col_offset=42)],
                keywords=[],
                lineno=108,
                col_offset=8,
                end_lineno=108,
                end_col_offset=43),
              lineno=108,
              col_offset=8,
              end_lineno=108,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=93,
            col_offset=60,
            end_lineno=93,
            end_col_offset=63),
          lineno=93,
          col_offset=4,
          end_lineno=108,
          end_col_offset=43),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=110,
                col_offset=22,
                end_lineno=110,
                end_col_offset=26),
              arg(
                arg='_node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=110,
                  col_offset=35,
                  end_lineno=110,
                  end_col_offset=38),
                lineno=110,
                col_offset=28,
                end_lineno=110,
                end_col_offset=38)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='Non block nodes are not interesting here',
                lineno=111,
                col_offset=8,
                end_lineno=111,
                end_col_offset=54),
              lineno=111,
              col_offset=8,
              end_lineno=111,
              end_col_offset=54),
            Pass(
              lineno=112,
              col_offset=8,
              end_lineno=112,
              end_col_offset=12)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=110,
            col_offset=43,
            end_lineno=110,
            end_col_offset=46),
          lineno=110,
          col_offset=4,
          end_lineno=112,
          end_col_offset=12),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=114,
                col_offset=29,
                end_lineno=114,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=115,
                  col_offset=15,
                  end_lineno=115,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=115,
                col_offset=15,
                end_lineno=115,
                end_col_offset=28),
              lineno=115,
              col_offset=8,
              end_lineno=115,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=114,
              col_offset=38,
              end_lineno=114,
              end_col_offset=42),
            slice=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=114,
              col_offset=43,
              end_lineno=114,
              end_col_offset=57),
            ctx=Load(),
            lineno=114,
            col_offset=38,
            end_lineno=114,
            end_col_offset=58),
          lineno=114,
          col_offset=4,
          end_lineno=115,
          end_col_offset=28)],
      decorator_list=[],
      lineno=67,
      col_offset=0,
      end_lineno=115,
      end_col_offset=28)],
  type_ignores=[])
```
</details>

