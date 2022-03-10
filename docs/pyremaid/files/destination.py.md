# ./src/pyremaid/files/destination.py

### Imports

  - os.*

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
Module(
  body=[
    Import(
      names=[
        alias(name='os')],
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=9),
    FunctionDef(
      name='create_output_folder',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='output_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=4,
              col_offset=39,
              end_lineno=4,
              end_col_offset=42),
            lineno=4,
            col_offset=25,
            end_lineno=4,
            end_col_offset=42)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        If(
          test=UnaryOp(
            op=Not(),
            operand=Call(
              func=Attribute(
                value=Attribute(
                  value=Name(
                    id='os',
                    ctx=Load(),
                    lineno=5,
                    col_offset=11,
                    end_lineno=5,
                    end_col_offset=13),
                  attr='path',
                  ctx=Load(),
                  lineno=5,
                  col_offset=11,
                  end_lineno=5,
                  end_col_offset=18),
                attr='isdir',
                ctx=Load(),
                lineno=5,
                col_offset=11,
                end_lineno=5,
                end_col_offset=24),
              args=[
                Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=5,
                  col_offset=25,
                  end_lineno=5,
                  end_col_offset=36)],
              keywords=[],
              lineno=5,
              col_offset=11,
              end_lineno=5,
              end_col_offset=37),
            lineno=5,
            col_offset=7,
            end_lineno=5,
            end_col_offset=37),
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='os',
                    ctx=Load(),
                    lineno=6,
                    col_offset=8,
                    end_lineno=6,
                    end_col_offset=10),
                  attr='makedirs',
                  ctx=Load(),
                  lineno=6,
                  col_offset=8,
                  end_lineno=6,
                  end_col_offset=19),
                args=[
                  Name(
                    id='output_path',
                    ctx=Load(),
                    lineno=6,
                    col_offset=20,
                    end_lineno=6,
                    end_col_offset=31)],
                keywords=[],
                lineno=6,
                col_offset=8,
                end_lineno=6,
                end_col_offset=32),
              lineno=6,
              col_offset=8,
              end_lineno=6,
              end_col_offset=32)],
          orelse=[],
          lineno=5,
          col_offset=4,
          end_lineno=6,
          end_col_offset=32)],
      decorator_list=[],
      returns=Constant(
        value=None,
        lineno=4,
        col_offset=47,
        end_lineno=4,
        end_col_offset=51),
      lineno=4,
      col_offset=0,
      end_lineno=6,
      end_col_offset=32),
    FunctionDef(
      name='create_cleared_output_folder',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='output_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=9,
              col_offset=46,
              end_lineno=9,
              end_col_offset=49),
            lineno=9,
            col_offset=33,
            end_lineno=9,
            end_col_offset=49)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Call(
            func=Name(
              id='create_output_folder',
              ctx=Load(),
              lineno=10,
              col_offset=4,
              end_lineno=10,
              end_col_offset=24),
            args=[],
            keywords=[
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=10,
                  col_offset=37,
                  end_lineno=10,
                  end_col_offset=48),
                lineno=10,
                col_offset=25,
                end_lineno=10,
                end_col_offset=48)],
            lineno=10,
            col_offset=4,
            end_lineno=10,
            end_col_offset=49),
          lineno=10,
          col_offset=4,
          end_lineno=10,
          end_col_offset=49),
        For(
          target=Tuple(
            elts=[
              Name(
                id='root',
                ctx=Store(),
                lineno=11,
                col_offset=8,
                end_lineno=11,
                end_col_offset=12),
              Name(
                id='dirs',
                ctx=Store(),
                lineno=11,
                col_offset=14,
                end_lineno=11,
                end_col_offset=18),
              Name(
                id='files',
                ctx=Store(),
                lineno=11,
                col_offset=20,
                end_lineno=11,
                end_col_offset=25)],
            ctx=Store(),
            lineno=11,
            col_offset=8,
            end_lineno=11,
            end_col_offset=25),
          iter=Call(
            func=Attribute(
              value=Name(
                id='os',
                ctx=Load(),
                lineno=11,
                col_offset=29,
                end_lineno=11,
                end_col_offset=31),
              attr='walk',
              ctx=Load(),
              lineno=11,
              col_offset=29,
              end_lineno=11,
              end_col_offset=36),
            args=[
              Name(
                id='output_path',
                ctx=Load(),
                lineno=11,
                col_offset=37,
                end_lineno=11,
                end_col_offset=48)],
            keywords=[
              keyword(
                arg='topdown',
                value=Constant(
                  value=False,
                  lineno=11,
                  col_offset=58,
                  end_lineno=11,
                  end_col_offset=63),
                lineno=11,
                col_offset=50,
                end_lineno=11,
                end_col_offset=63)],
            lineno=11,
            col_offset=29,
            end_lineno=11,
            end_col_offset=64),
          body=[
            For(
              target=Name(
                id='name',
                ctx=Store(),
                lineno=12,
                col_offset=12,
                end_lineno=12,
                end_col_offset=16),
              iter=Name(
                id='files',
                ctx=Load(),
                lineno=12,
                col_offset=20,
                end_lineno=12,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='os',
                        ctx=Load(),
                        lineno=13,
                        col_offset=12,
                        end_lineno=13,
                        end_col_offset=14),
                      attr='remove',
                      ctx=Load(),
                      lineno=13,
                      col_offset=12,
                      end_lineno=13,
                      end_col_offset=21),
                    args=[
                      Call(
                        func=Attribute(
                          value=Attribute(
                            value=Name(
                              id='os',
                              ctx=Load(),
                              lineno=13,
                              col_offset=22,
                              end_lineno=13,
                              end_col_offset=24),
                            attr='path',
                            ctx=Load(),
                            lineno=13,
                            col_offset=22,
                            end_lineno=13,
                            end_col_offset=29),
                          attr='join',
                          ctx=Load(),
                          lineno=13,
                          col_offset=22,
                          end_lineno=13,
                          end_col_offset=34),
                        args=[
                          Name(
                            id='root',
                            ctx=Load(),
                            lineno=13,
                            col_offset=35,
                            end_lineno=13,
                            end_col_offset=39),
                          Name(
                            id='name',
                            ctx=Load(),
                            lineno=13,
                            col_offset=41,
                            end_lineno=13,
                            end_col_offset=45)],
                        keywords=[],
                        lineno=13,
                        col_offset=22,
                        end_lineno=13,
                        end_col_offset=46)],
                    keywords=[],
                    lineno=13,
                    col_offset=12,
                    end_lineno=13,
                    end_col_offset=47),
                  lineno=13,
                  col_offset=12,
                  end_lineno=13,
                  end_col_offset=47)],
              orelse=[],
              lineno=12,
              col_offset=8,
              end_lineno=13,
              end_col_offset=47),
            For(
              target=Name(
                id='name',
                ctx=Store(),
                lineno=14,
                col_offset=12,
                end_lineno=14,
                end_col_offset=16),
              iter=Name(
                id='dirs',
                ctx=Load(),
                lineno=14,
                col_offset=20,
                end_lineno=14,
                end_col_offset=24),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='os',
                        ctx=Load(),
                        lineno=15,
                        col_offset=12,
                        end_lineno=15,
                        end_col_offset=14),
                      attr='rmdir',
                      ctx=Load(),
                      lineno=15,
                      col_offset=12,
                      end_lineno=15,
                      end_col_offset=20),
                    args=[
                      Call(
                        func=Attribute(
                          value=Attribute(
                            value=Name(
                              id='os',
                              ctx=Load(),
                              lineno=15,
                              col_offset=21,
                              end_lineno=15,
                              end_col_offset=23),
                            attr='path',
                            ctx=Load(),
                            lineno=15,
                            col_offset=21,
                            end_lineno=15,
                            end_col_offset=28),
                          attr='join',
                          ctx=Load(),
                          lineno=15,
                          col_offset=21,
                          end_lineno=15,
                          end_col_offset=33),
                        args=[
                          Name(
                            id='root',
                            ctx=Load(),
                            lineno=15,
                            col_offset=34,
                            end_lineno=15,
                            end_col_offset=38),
                          Name(
                            id='name',
                            ctx=Load(),
                            lineno=15,
                            col_offset=40,
                            end_lineno=15,
                            end_col_offset=44)],
                        keywords=[],
                        lineno=15,
                        col_offset=21,
                        end_lineno=15,
                        end_col_offset=45)],
                    keywords=[],
                    lineno=15,
                    col_offset=12,
                    end_lineno=15,
                    end_col_offset=46),
                  lineno=15,
                  col_offset=12,
                  end_lineno=15,
                  end_col_offset=46)],
              orelse=[],
              lineno=14,
              col_offset=8,
              end_lineno=15,
              end_col_offset=46)],
          orelse=[],
          lineno=11,
          col_offset=4,
          end_lineno=15,
          end_col_offset=46)],
      decorator_list=[],
      returns=Constant(
        value=None,
        lineno=9,
        col_offset=54,
        end_lineno=9,
        end_col_offset=58),
      lineno=9,
      col_offset=0,
      end_lineno=15,
      end_col_offset=46),
    FunctionDef(
      name='get_output_file_path_for_input_file',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=18,
              col_offset=52,
              end_lineno=18,
              end_col_offset=55),
            lineno=18,
            col_offset=40,
            end_lineno=18,
            end_col_offset=55),
          arg(
            arg='output_root',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=18,
              col_offset=70,
              end_lineno=18,
              end_col_offset=73),
            lineno=18,
            col_offset=57,
            end_lineno=18,
            end_col_offset=73)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Attribute(
              value=Attribute(
                value=Name(
                  id='os',
                  ctx=Load(),
                  lineno=19,
                  col_offset=11,
                  end_lineno=19,
                  end_col_offset=13),
                attr='path',
                ctx=Load(),
                lineno=19,
                col_offset=11,
                end_lineno=19,
                end_col_offset=18),
              attr='join',
              ctx=Load(),
              lineno=19,
              col_offset=11,
              end_lineno=19,
              end_col_offset=23),
            args=[
              Name(
                id='output_root',
                ctx=Load(),
                lineno=19,
                col_offset=24,
                end_lineno=19,
                end_col_offset=35),
              BinOp(
                left=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=19,
                  col_offset=37,
                  end_lineno=19,
                  end_col_offset=47),
                op=Add(),
                right=Constant(
                  value='.md',
                  lineno=19,
                  col_offset=50,
                  end_lineno=19,
                  end_col_offset=55),
                lineno=19,
                col_offset=37,
                end_lineno=19,
                end_col_offset=55)],
            keywords=[],
            lineno=19,
            col_offset=11,
            end_lineno=19,
            end_col_offset=56),
          lineno=19,
          col_offset=4,
          end_lineno=19,
          end_col_offset=56)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=18,
        col_offset=78,
        end_lineno=18,
        end_col_offset=81),
      lineno=18,
      col_offset=0,
      end_lineno=19,
      end_col_offset=56),
    FunctionDef(
      name='update_output_file',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='content',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=32,
              end_lineno=22,
              end_col_offset=35),
            lineno=22,
            col_offset=23,
            end_lineno=22,
            end_col_offset=35),
          arg(
            arg='output_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=50,
              end_lineno=22,
              end_col_offset=53),
            lineno=22,
            col_offset=37,
            end_lineno=22,
            end_col_offset=53)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        If(
          test=UnaryOp(
            op=Not(),
            operand=Call(
              func=Attribute(
                value=Attribute(
                  value=Name(
                    id='os',
                    ctx=Load(),
                    lineno=23,
                    col_offset=11,
                    end_lineno=23,
                    end_col_offset=13),
                  attr='path',
                  ctx=Load(),
                  lineno=23,
                  col_offset=11,
                  end_lineno=23,
                  end_col_offset=18),
                attr='isdir',
                ctx=Load(),
                lineno=23,
                col_offset=11,
                end_lineno=23,
                end_col_offset=24),
              args=[
                Call(
                  func=Attribute(
                    value=Attribute(
                      value=Name(
                        id='os',
                        ctx=Load(),
                        lineno=23,
                        col_offset=25,
                        end_lineno=23,
                        end_col_offset=27),
                      attr='path',
                      ctx=Load(),
                      lineno=23,
                      col_offset=25,
                      end_lineno=23,
                      end_col_offset=32),
                    attr='dirname',
                    ctx=Load(),
                    lineno=23,
                    col_offset=25,
                    end_lineno=23,
                    end_col_offset=40),
                  args=[
                    Name(
                      id='output_file',
                      ctx=Load(),
                      lineno=23,
                      col_offset=41,
                      end_lineno=23,
                      end_col_offset=52)],
                  keywords=[],
                  lineno=23,
                  col_offset=25,
                  end_lineno=23,
                  end_col_offset=53)],
              keywords=[],
              lineno=23,
              col_offset=11,
              end_lineno=23,
              end_col_offset=54),
            lineno=23,
            col_offset=7,
            end_lineno=23,
            end_col_offset=54),
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='os',
                    ctx=Load(),
                    lineno=24,
                    col_offset=8,
                    end_lineno=24,
                    end_col_offset=10),
                  attr='makedirs',
                  ctx=Load(),
                  lineno=24,
                  col_offset=8,
                  end_lineno=24,
                  end_col_offset=19),
                args=[
                  Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='os',
                          ctx=Load(),
                          lineno=24,
                          col_offset=20,
                          end_lineno=24,
                          end_col_offset=22),
                        attr='path',
                        ctx=Load(),
                        lineno=24,
                        col_offset=20,
                        end_lineno=24,
                        end_col_offset=27),
                      attr='dirname',
                      ctx=Load(),
                      lineno=24,
                      col_offset=20,
                      end_lineno=24,
                      end_col_offset=35),
                    args=[
                      Name(
                        id='output_file',
                        ctx=Load(),
                        lineno=24,
                        col_offset=36,
                        end_lineno=24,
                        end_col_offset=47)],
                    keywords=[],
                    lineno=24,
                    col_offset=20,
                    end_lineno=24,
                    end_col_offset=48)],
                keywords=[],
                lineno=24,
                col_offset=8,
                end_lineno=24,
                end_col_offset=49),
              lineno=24,
              col_offset=8,
              end_lineno=24,
              end_col_offset=49)],
          orelse=[],
          lineno=23,
          col_offset=4,
          end_lineno=24,
          end_col_offset=49),
        With(
          items=[
            withitem(
              context_expr=Call(
                func=Name(
                  id='open',
                  ctx=Load(),
                  lineno=26,
                  col_offset=9,
                  end_lineno=26,
                  end_col_offset=13),
                args=[
                  Name(
                    id='output_file',
                    ctx=Load(),
                    lineno=26,
                    col_offset=14,
                    end_lineno=26,
                    end_col_offset=25),
                  Constant(
                    value='w',
                    lineno=26,
                    col_offset=27,
                    end_lineno=26,
                    end_col_offset=30)],
                keywords=[],
                lineno=26,
                col_offset=9,
                end_lineno=26,
                end_col_offset=31),
              optional_vars=Name(
                id='md_file',
                ctx=Store(),
                lineno=26,
                col_offset=35,
                end_lineno=26,
                end_col_offset=42))],
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='md_file',
                    ctx=Load(),
                    lineno=27,
                    col_offset=8,
                    end_lineno=27,
                    end_col_offset=15),
                  attr='write',
                  ctx=Load(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=21),
                args=[
                  Name(
                    id='content',
                    ctx=Load(),
                    lineno=27,
                    col_offset=22,
                    end_lineno=27,
                    end_col_offset=29)],
                keywords=[],
                lineno=27,
                col_offset=8,
                end_lineno=27,
                end_col_offset=30),
              lineno=27,
              col_offset=8,
              end_lineno=27,
              end_col_offset=30)],
          lineno=26,
          col_offset=4,
          end_lineno=27,
          end_col_offset=30)],
      decorator_list=[],
      lineno=22,
      col_offset=0,
      end_lineno=27,
      end_col_offset=30)],
  type_ignores=[])
```
</details>

