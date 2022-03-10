# ./src/pyremaid/files/__init__.py

### Imports


---
```mermaid
flowchart TB
  _create_output_folder_node_0["If"]
  _create_output_folder_node_1["UnaryOp"]
  _create_output_folder_node_2["Not"]
  _create_output_folder_node_3["Call"]
  _create_output_folder_node_4["Attribute"]
  _create_output_folder_node_5["Attribute"]
  _create_output_folder_node_6["Name"]
  _create_output_folder_node_7["Load"]
  _create_output_folder_node_8["Load"]
  _create_output_folder_node_9["Load"]
  _create_output_folder_node_10["Name"]
  _create_output_folder_node_11["Load"]
  _create_output_folder_node_12["Expr"]
  _create_output_folder_node_13["Call"]
  _create_output_folder_node_14["Attribute"]
  _create_output_folder_node_15["Name"]
  _create_output_folder_node_16["Load"]
  _create_output_folder_node_17["Load"]
  _create_output_folder_node_18["Name"]
  _create_output_folder_node_19["Load"]
  _create_cleared_output_folder_node_0["Expr"]
  _create_cleared_output_folder_node_1["Call"]
  _create_cleared_output_folder_node_2["Name"]
  _create_cleared_output_folder_node_3["Load"]
  _create_cleared_output_folder_node_4["keyword"]
  _create_cleared_output_folder_node_5["Name"]
  _create_cleared_output_folder_node_6["Load"]
  _create_cleared_output_folder_node_7["For"]
  _create_cleared_output_folder_node_8["Tuple"]
  _create_cleared_output_folder_node_9["Name"]
  _create_cleared_output_folder_node_10["Store"]
  _create_cleared_output_folder_node_11["Name"]
  _create_cleared_output_folder_node_12["Store"]
  _create_cleared_output_folder_node_13["Name"]
  _create_cleared_output_folder_node_14["Store"]
  _create_cleared_output_folder_node_15["Store"]
  _create_cleared_output_folder_node_16["Call"]
  _create_cleared_output_folder_node_17["Attribute"]
  _create_cleared_output_folder_node_18["Name"]
  _create_cleared_output_folder_node_19["Load"]
  _create_cleared_output_folder_node_20["Load"]
  _create_cleared_output_folder_node_21["Name"]
  _create_cleared_output_folder_node_22["Load"]
  _create_cleared_output_folder_node_23["keyword"]
  _create_cleared_output_folder_node_24["Constant"]
  _create_cleared_output_folder_node_25["For"]
  _create_cleared_output_folder_node_26["Name"]
  _create_cleared_output_folder_node_27["Store"]
  _create_cleared_output_folder_node_28["Name"]
  _create_cleared_output_folder_node_29["Load"]
  _create_cleared_output_folder_node_30["Expr"]
  _create_cleared_output_folder_node_31["Call"]
  _create_cleared_output_folder_node_32["Attribute"]
  _create_cleared_output_folder_node_33["Name"]
  _create_cleared_output_folder_node_34["Load"]
  _create_cleared_output_folder_node_35["Load"]
  _create_cleared_output_folder_node_36["Call"]
  _create_cleared_output_folder_node_37["Attribute"]
  _create_cleared_output_folder_node_38["Attribute"]
  _create_cleared_output_folder_node_39["Name"]
  _create_cleared_output_folder_node_40["Load"]
  _create_cleared_output_folder_node_41["Load"]
  _create_cleared_output_folder_node_42["Load"]
  _create_cleared_output_folder_node_43["Name"]
  _create_cleared_output_folder_node_44["Load"]
  _create_cleared_output_folder_node_45["Name"]
  _create_cleared_output_folder_node_46["Load"]
  _create_cleared_output_folder_node_47["For"]
  _create_cleared_output_folder_node_48["Name"]
  _create_cleared_output_folder_node_49["Store"]
  _create_cleared_output_folder_node_50["Name"]
  _create_cleared_output_folder_node_51["Load"]
  _create_cleared_output_folder_node_52["Expr"]
  _create_cleared_output_folder_node_53["Call"]
  _create_cleared_output_folder_node_54["Attribute"]
  _create_cleared_output_folder_node_55["Name"]
  _create_cleared_output_folder_node_56["Load"]
  _create_cleared_output_folder_node_57["Load"]
  _create_cleared_output_folder_node_58["Call"]
  _create_cleared_output_folder_node_59["Attribute"]
  _create_cleared_output_folder_node_60["Attribute"]
  _create_cleared_output_folder_node_61["Name"]
  _create_cleared_output_folder_node_62["Load"]
  _create_cleared_output_folder_node_63["Load"]
  _create_cleared_output_folder_node_64["Load"]
  _create_cleared_output_folder_node_65["Name"]
  _create_cleared_output_folder_node_66["Load"]
  _create_cleared_output_folder_node_67["Name"]
  _create_cleared_output_folder_node_68["Load"]
  _get_output_file_path_for_input_file_node_0["Return"]
  _get_output_file_path_for_input_file_node_1["Call"]
  _get_output_file_path_for_input_file_node_2["Attribute"]
  _get_output_file_path_for_input_file_node_3["Attribute"]
  _get_output_file_path_for_input_file_node_4["Name"]
  _get_output_file_path_for_input_file_node_5["Load"]
  _get_output_file_path_for_input_file_node_6["Load"]
  _get_output_file_path_for_input_file_node_7["Load"]
  _get_output_file_path_for_input_file_node_8["Name"]
  _get_output_file_path_for_input_file_node_9["Load"]
  _get_output_file_path_for_input_file_node_10["BinOp"]
  _get_output_file_path_for_input_file_node_11["Name"]
  _get_output_file_path_for_input_file_node_12["Load"]
  _get_output_file_path_for_input_file_node_13["Add"]
  _get_output_file_path_for_input_file_node_14["Constant"]
  _update_output_file_node_0["If"]
  _update_output_file_node_1["UnaryOp"]
  _update_output_file_node_2["Not"]
  _update_output_file_node_3["Call"]
  _update_output_file_node_4["Attribute"]
  _update_output_file_node_5["Attribute"]
  _update_output_file_node_6["Name"]
  _update_output_file_node_7["Load"]
  _update_output_file_node_8["Load"]
  _update_output_file_node_9["Load"]
  _update_output_file_node_10["Call"]
  _update_output_file_node_11["Attribute"]
  _update_output_file_node_12["Attribute"]
  _update_output_file_node_13["Name"]
  _update_output_file_node_14["Load"]
  _update_output_file_node_15["Load"]
  _update_output_file_node_16["Load"]
  _update_output_file_node_17["Name"]
  _update_output_file_node_18["Load"]
  _update_output_file_node_19["Expr"]
  _update_output_file_node_20["Call"]
  _update_output_file_node_21["Attribute"]
  _update_output_file_node_22["Name"]
  _update_output_file_node_23["Load"]
  _update_output_file_node_24["Load"]
  _update_output_file_node_25["Call"]
  _update_output_file_node_26["Attribute"]
  _update_output_file_node_27["Attribute"]
  _update_output_file_node_28["Name"]
  _update_output_file_node_29["Load"]
  _update_output_file_node_30["Load"]
  _update_output_file_node_31["Load"]
  _update_output_file_node_32["Name"]
  _update_output_file_node_33["Load"]
  _update_output_file_node_34["With"]
  _update_output_file_node_35["withitem"]
  _update_output_file_node_36["Call"]
  _update_output_file_node_37["Name"]
  _update_output_file_node_38["Load"]
  _update_output_file_node_39["Name"]
  _update_output_file_node_40["Load"]
  _update_output_file_node_41["Constant"]
  _update_output_file_node_42["Name"]
  _update_output_file_node_43["Store"]
  _update_output_file_node_44["Expr"]
  _update_output_file_node_45["Call"]
  _update_output_file_node_46["Attribute"]
  _update_output_file_node_47["Name"]
  _update_output_file_node_48["Load"]
  _update_output_file_node_49["Load"]
  _update_output_file_node_50["Name"]
  _update_output_file_node_51["Load"]

  subgraph create_output_folder
    direction TB
    _create_output_folder_node_0 --> _create_output_folder_node_1
    _create_output_folder_node_1 --> _create_output_folder_node_2
    _create_output_folder_node_2 --> _create_output_folder_node_3
    _create_output_folder_node_3 --> _create_output_folder_node_4
    _create_output_folder_node_4 --> _create_output_folder_node_5
    _create_output_folder_node_5 --> _create_output_folder_node_6
    _create_output_folder_node_6 --> _create_output_folder_node_7
    _create_output_folder_node_7 --> _create_output_folder_node_8
    _create_output_folder_node_8 --> _create_output_folder_node_9
    _create_output_folder_node_9 --> _create_output_folder_node_10
    _create_output_folder_node_10 --> _create_output_folder_node_11
    _create_output_folder_node_11 --> _create_output_folder_node_12
    _create_output_folder_node_12 --> _create_output_folder_node_13
    _create_output_folder_node_13 --> _create_output_folder_node_14
    _create_output_folder_node_14 --> _create_output_folder_node_15
    _create_output_folder_node_15 --> _create_output_folder_node_16
    _create_output_folder_node_16 --> _create_output_folder_node_17
    _create_output_folder_node_17 --> _create_output_folder_node_18
    _create_output_folder_node_18 --> _create_output_folder_node_19
  end
  subgraph create_cleared_output_folder
    direction TB
    _create_cleared_output_folder_node_0 --> _create_cleared_output_folder_node_1
    _create_cleared_output_folder_node_1 --> _create_cleared_output_folder_node_2
    _create_cleared_output_folder_node_2 --> _create_cleared_output_folder_node_3
    _create_cleared_output_folder_node_3 --> _create_cleared_output_folder_node_4
    _create_cleared_output_folder_node_4 --> _create_cleared_output_folder_node_5
    _create_cleared_output_folder_node_5 --> _create_cleared_output_folder_node_6
    _create_cleared_output_folder_node_6 --> _create_cleared_output_folder_node_7
    _create_cleared_output_folder_node_7 --> _create_cleared_output_folder_node_8
    _create_cleared_output_folder_node_8 --> _create_cleared_output_folder_node_9
    _create_cleared_output_folder_node_9 --> _create_cleared_output_folder_node_10
    _create_cleared_output_folder_node_10 --> _create_cleared_output_folder_node_11
    _create_cleared_output_folder_node_11 --> _create_cleared_output_folder_node_12
    _create_cleared_output_folder_node_12 --> _create_cleared_output_folder_node_13
    _create_cleared_output_folder_node_13 --> _create_cleared_output_folder_node_14
    _create_cleared_output_folder_node_14 --> _create_cleared_output_folder_node_15
    _create_cleared_output_folder_node_15 --> _create_cleared_output_folder_node_16
    _create_cleared_output_folder_node_16 --> _create_cleared_output_folder_node_17
    _create_cleared_output_folder_node_17 --> _create_cleared_output_folder_node_18
    _create_cleared_output_folder_node_18 --> _create_cleared_output_folder_node_19
    _create_cleared_output_folder_node_19 --> _create_cleared_output_folder_node_20
    _create_cleared_output_folder_node_20 --> _create_cleared_output_folder_node_21
    _create_cleared_output_folder_node_21 --> _create_cleared_output_folder_node_22
    _create_cleared_output_folder_node_22 --> _create_cleared_output_folder_node_23
    _create_cleared_output_folder_node_23 --> _create_cleared_output_folder_node_24
    _create_cleared_output_folder_node_24 --> _create_cleared_output_folder_node_25
    _create_cleared_output_folder_node_25 --> _create_cleared_output_folder_node_26
    _create_cleared_output_folder_node_26 --> _create_cleared_output_folder_node_27
    _create_cleared_output_folder_node_27 --> _create_cleared_output_folder_node_28
    _create_cleared_output_folder_node_28 --> _create_cleared_output_folder_node_29
    _create_cleared_output_folder_node_29 --> _create_cleared_output_folder_node_30
    _create_cleared_output_folder_node_30 --> _create_cleared_output_folder_node_31
    _create_cleared_output_folder_node_31 --> _create_cleared_output_folder_node_32
    _create_cleared_output_folder_node_32 --> _create_cleared_output_folder_node_33
    _create_cleared_output_folder_node_33 --> _create_cleared_output_folder_node_34
    _create_cleared_output_folder_node_34 --> _create_cleared_output_folder_node_35
    _create_cleared_output_folder_node_35 --> _create_cleared_output_folder_node_36
    _create_cleared_output_folder_node_36 --> _create_cleared_output_folder_node_37
    _create_cleared_output_folder_node_37 --> _create_cleared_output_folder_node_38
    _create_cleared_output_folder_node_38 --> _create_cleared_output_folder_node_39
    _create_cleared_output_folder_node_39 --> _create_cleared_output_folder_node_40
    _create_cleared_output_folder_node_40 --> _create_cleared_output_folder_node_41
    _create_cleared_output_folder_node_41 --> _create_cleared_output_folder_node_42
    _create_cleared_output_folder_node_42 --> _create_cleared_output_folder_node_43
    _create_cleared_output_folder_node_43 --> _create_cleared_output_folder_node_44
    _create_cleared_output_folder_node_44 --> _create_cleared_output_folder_node_45
    _create_cleared_output_folder_node_45 --> _create_cleared_output_folder_node_46
    _create_cleared_output_folder_node_46 --> _create_cleared_output_folder_node_47
    _create_cleared_output_folder_node_47 --> _create_cleared_output_folder_node_48
    _create_cleared_output_folder_node_48 --> _create_cleared_output_folder_node_49
    _create_cleared_output_folder_node_49 --> _create_cleared_output_folder_node_50
    _create_cleared_output_folder_node_50 --> _create_cleared_output_folder_node_51
    _create_cleared_output_folder_node_51 --> _create_cleared_output_folder_node_52
    _create_cleared_output_folder_node_52 --> _create_cleared_output_folder_node_53
    _create_cleared_output_folder_node_53 --> _create_cleared_output_folder_node_54
    _create_cleared_output_folder_node_54 --> _create_cleared_output_folder_node_55
    _create_cleared_output_folder_node_55 --> _create_cleared_output_folder_node_56
    _create_cleared_output_folder_node_56 --> _create_cleared_output_folder_node_57
    _create_cleared_output_folder_node_57 --> _create_cleared_output_folder_node_58
    _create_cleared_output_folder_node_58 --> _create_cleared_output_folder_node_59
    _create_cleared_output_folder_node_59 --> _create_cleared_output_folder_node_60
    _create_cleared_output_folder_node_60 --> _create_cleared_output_folder_node_61
    _create_cleared_output_folder_node_61 --> _create_cleared_output_folder_node_62
    _create_cleared_output_folder_node_62 --> _create_cleared_output_folder_node_63
    _create_cleared_output_folder_node_63 --> _create_cleared_output_folder_node_64
    _create_cleared_output_folder_node_64 --> _create_cleared_output_folder_node_65
    _create_cleared_output_folder_node_65 --> _create_cleared_output_folder_node_66
    _create_cleared_output_folder_node_66 --> _create_cleared_output_folder_node_67
    _create_cleared_output_folder_node_67 --> _create_cleared_output_folder_node_68
  end
  subgraph get_output_file_path_for_input_file
    direction TB
    _get_output_file_path_for_input_file_node_0 --> _get_output_file_path_for_input_file_node_1
    _get_output_file_path_for_input_file_node_1 --> _get_output_file_path_for_input_file_node_2
    _get_output_file_path_for_input_file_node_2 --> _get_output_file_path_for_input_file_node_3
    _get_output_file_path_for_input_file_node_3 --> _get_output_file_path_for_input_file_node_4
    _get_output_file_path_for_input_file_node_4 --> _get_output_file_path_for_input_file_node_5
    _get_output_file_path_for_input_file_node_5 --> _get_output_file_path_for_input_file_node_6
    _get_output_file_path_for_input_file_node_6 --> _get_output_file_path_for_input_file_node_7
    _get_output_file_path_for_input_file_node_7 --> _get_output_file_path_for_input_file_node_8
    _get_output_file_path_for_input_file_node_8 --> _get_output_file_path_for_input_file_node_9
    _get_output_file_path_for_input_file_node_9 --> _get_output_file_path_for_input_file_node_10
    _get_output_file_path_for_input_file_node_10 --> _get_output_file_path_for_input_file_node_11
    _get_output_file_path_for_input_file_node_11 --> _get_output_file_path_for_input_file_node_12
    _get_output_file_path_for_input_file_node_12 --> _get_output_file_path_for_input_file_node_13
    _get_output_file_path_for_input_file_node_13 --> _get_output_file_path_for_input_file_node_14
  end
  subgraph update_output_file
    direction TB
    _update_output_file_node_0 --> _update_output_file_node_1
    _update_output_file_node_1 --> _update_output_file_node_2
    _update_output_file_node_2 --> _update_output_file_node_3
    _update_output_file_node_3 --> _update_output_file_node_4
    _update_output_file_node_4 --> _update_output_file_node_5
    _update_output_file_node_5 --> _update_output_file_node_6
    _update_output_file_node_6 --> _update_output_file_node_7
    _update_output_file_node_7 --> _update_output_file_node_8
    _update_output_file_node_8 --> _update_output_file_node_9
    _update_output_file_node_9 --> _update_output_file_node_10
    _update_output_file_node_10 --> _update_output_file_node_11
    _update_output_file_node_11 --> _update_output_file_node_12
    _update_output_file_node_12 --> _update_output_file_node_13
    _update_output_file_node_13 --> _update_output_file_node_14
    _update_output_file_node_14 --> _update_output_file_node_15
    _update_output_file_node_15 --> _update_output_file_node_16
    _update_output_file_node_16 --> _update_output_file_node_17
    _update_output_file_node_17 --> _update_output_file_node_18
    _update_output_file_node_18 --> _update_output_file_node_19
    _update_output_file_node_19 --> _update_output_file_node_20
    _update_output_file_node_20 --> _update_output_file_node_21
    _update_output_file_node_21 --> _update_output_file_node_22
    _update_output_file_node_22 --> _update_output_file_node_23
    _update_output_file_node_23 --> _update_output_file_node_24
    _update_output_file_node_24 --> _update_output_file_node_25
    _update_output_file_node_25 --> _update_output_file_node_26
    _update_output_file_node_26 --> _update_output_file_node_27
    _update_output_file_node_27 --> _update_output_file_node_28
    _update_output_file_node_28 --> _update_output_file_node_29
    _update_output_file_node_29 --> _update_output_file_node_30
    _update_output_file_node_30 --> _update_output_file_node_31
    _update_output_file_node_31 --> _update_output_file_node_32
    _update_output_file_node_32 --> _update_output_file_node_33
    _update_output_file_node_33 --> _update_output_file_node_34
    _update_output_file_node_34 --> _update_output_file_node_35
    _update_output_file_node_35 --> _update_output_file_node_36
    _update_output_file_node_36 --> _update_output_file_node_37
    _update_output_file_node_37 --> _update_output_file_node_38
    _update_output_file_node_38 --> _update_output_file_node_39
    _update_output_file_node_39 --> _update_output_file_node_40
    _update_output_file_node_40 --> _update_output_file_node_41
    _update_output_file_node_41 --> _update_output_file_node_42
    _update_output_file_node_42 --> _update_output_file_node_43
    _update_output_file_node_43 --> _update_output_file_node_44
    _update_output_file_node_44 --> _update_output_file_node_45
    _update_output_file_node_45 --> _update_output_file_node_46
    _update_output_file_node_46 --> _update_output_file_node_47
    _update_output_file_node_47 --> _update_output_file_node_48
    _update_output_file_node_48 --> _update_output_file_node_49
    _update_output_file_node_49 --> _update_output_file_node_50
    _update_output_file_node_50 --> _update_output_file_node_51
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```

```
</details>

