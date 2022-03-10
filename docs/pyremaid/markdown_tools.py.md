# ./src/pyremaid/markdown_tools.py

### Imports


---
```mermaid
flowchart TB
  _create_markdown_content_node_0["Assign"]
  _create_markdown_content_node_1["Name"]
  _create_markdown_content_node_2["Store"]
  _create_markdown_content_node_3["Call"]
  _create_markdown_content_node_4["Name"]
  _create_markdown_content_node_5["Load"]
  _create_markdown_content_node_6["keyword"]
  _create_markdown_content_node_7["Name"]
  _create_markdown_content_node_8["Load"]
  _create_markdown_content_node_9["Assign"]
  _create_markdown_content_node_10["Name"]
  _create_markdown_content_node_11["Store"]
  _create_markdown_content_node_12["Call"]
  _create_markdown_content_node_13["Name"]
  _create_markdown_content_node_14["Load"]
  _create_markdown_content_node_15["keyword"]
  _create_markdown_content_node_16["Name"]
  _create_markdown_content_node_17["Load"]
  _create_markdown_content_node_18["keyword"]
  _create_markdown_content_node_19["Name"]
  _create_markdown_content_node_20["Load"]
  _create_markdown_content_node_21["Assign"]
  _create_markdown_content_node_22["Name"]
  _create_markdown_content_node_23["Store"]
  _create_markdown_content_node_24["Call"]
  _create_markdown_content_node_25["Attribute"]
  _create_markdown_content_node_26["Constant"]
  _create_markdown_content_node_27["Load"]
  _create_markdown_content_node_28["Name"]
  _create_markdown_content_node_29["Load"]
  _create_markdown_content_node_30["Return"]
  _create_markdown_content_node_31["JoinedStr"]
  _create_markdown_content_node_32["Constant"]
  _create_markdown_content_node_33["FormattedValue"]
  _create_markdown_content_node_34["Name"]
  _create_markdown_content_node_35["Load"]
  _create_markdown_content_node_36["Constant"]
  _create_markdown_content_node_37["FormattedValue"]
  _create_markdown_content_node_38["Name"]
  _create_markdown_content_node_39["Load"]
  _create_markdown_content_node_40["Constant"]
  _create_markdown_content_node_41["FormattedValue"]
  _create_markdown_content_node_42["Name"]
  _create_markdown_content_node_43["Load"]
  _create_markdown_content_node_44["Constant"]
  _create_markdown_content_node_45["FormattedValue"]
  _create_markdown_content_node_46["Name"]
  _create_markdown_content_node_47["Load"]
  _create_markdown_content_node_48["Constant"]
  _turn_out_the_import_list_node_0["Assign"]
  _turn_out_the_import_list_node_1["Name"]
  _turn_out_the_import_list_node_2["Store"]
  _turn_out_the_import_list_node_3["Constant"]
  _turn_out_the_import_list_node_4["For"]
  _turn_out_the_import_list_node_5["Name"]
  _turn_out_the_import_list_node_6["Store"]
  _turn_out_the_import_list_node_7["Name"]
  _turn_out_the_import_list_node_8["Load"]
  _turn_out_the_import_list_node_9["Assign"]
  _turn_out_the_import_list_node_10["Name"]
  _turn_out_the_import_list_node_11["Store"]
  _turn_out_the_import_list_node_12["Subscript"]
  _turn_out_the_import_list_node_13["Name"]
  _turn_out_the_import_list_node_14["Load"]
  _turn_out_the_import_list_node_15["Name"]
  _turn_out_the_import_list_node_16["Load"]
  _turn_out_the_import_list_node_17["Load"]
  _turn_out_the_import_list_node_18["If"]
  _turn_out_the_import_list_node_19["Name"]
  _turn_out_the_import_list_node_20["Load"]
  _turn_out_the_import_list_node_21["AugAssign"]
  _turn_out_the_import_list_node_22["Name"]
  _turn_out_the_import_list_node_23["Store"]
  _turn_out_the_import_list_node_24["Add"]
  _turn_out_the_import_list_node_25["JoinedStr"]
  _turn_out_the_import_list_node_26["Constant"]
  _turn_out_the_import_list_node_27["FormattedValue"]
  _turn_out_the_import_list_node_28["Name"]
  _turn_out_the_import_list_node_29["Load"]
  _turn_out_the_import_list_node_30["Constant"]
  _turn_out_the_import_list_node_31["FormattedValue"]
  _turn_out_the_import_list_node_32["Name"]
  _turn_out_the_import_list_node_33["Load"]
  _turn_out_the_import_list_node_34["Constant"]
  _turn_out_the_import_list_node_35["AugAssign"]
  _turn_out_the_import_list_node_36["Name"]
  _turn_out_the_import_list_node_37["Store"]
  _turn_out_the_import_list_node_38["Add"]
  _turn_out_the_import_list_node_39["JoinedStr"]
  _turn_out_the_import_list_node_40["Constant"]
  _turn_out_the_import_list_node_41["FormattedValue"]
  _turn_out_the_import_list_node_42["Name"]
  _turn_out_the_import_list_node_43["Load"]
  _turn_out_the_import_list_node_44["Constant"]
  _turn_out_the_import_list_node_45["Return"]
  _turn_out_the_import_list_node_46["Name"]
  _turn_out_the_import_list_node_47["Load"]
  _create_markdown_debug_dump_block_node_0["Return"]
  _create_markdown_debug_dump_block_node_1["JoinedStr"]
  _create_markdown_debug_dump_block_node_2["Constant"]
  _create_markdown_debug_dump_block_node_3["FormattedValue"]
  _create_markdown_debug_dump_block_node_4["Name"]
  _create_markdown_debug_dump_block_node_5["Load"]
  _create_markdown_debug_dump_block_node_6["Constant"]

  subgraph create_markdown_content
    direction TB
    _create_markdown_content_node_0 --> _create_markdown_content_node_1
    _create_markdown_content_node_1 --> _create_markdown_content_node_2
    _create_markdown_content_node_2 --> _create_markdown_content_node_3
    _create_markdown_content_node_3 --> _create_markdown_content_node_4
    _create_markdown_content_node_4 --> _create_markdown_content_node_5
    _create_markdown_content_node_5 --> _create_markdown_content_node_6
    _create_markdown_content_node_6 --> _create_markdown_content_node_7
    _create_markdown_content_node_7 --> _create_markdown_content_node_8
    _create_markdown_content_node_8 --> _create_markdown_content_node_9
    _create_markdown_content_node_9 --> _create_markdown_content_node_10
    _create_markdown_content_node_10 --> _create_markdown_content_node_11
    _create_markdown_content_node_11 --> _create_markdown_content_node_12
    _create_markdown_content_node_12 --> _create_markdown_content_node_13
    _create_markdown_content_node_13 --> _create_markdown_content_node_14
    _create_markdown_content_node_14 --> _create_markdown_content_node_15
    _create_markdown_content_node_15 --> _create_markdown_content_node_16
    _create_markdown_content_node_16 --> _create_markdown_content_node_17
    _create_markdown_content_node_17 --> _create_markdown_content_node_18
    _create_markdown_content_node_18 --> _create_markdown_content_node_19
    _create_markdown_content_node_19 --> _create_markdown_content_node_20
    _create_markdown_content_node_20 --> _create_markdown_content_node_21
    _create_markdown_content_node_21 --> _create_markdown_content_node_22
    _create_markdown_content_node_22 --> _create_markdown_content_node_23
    _create_markdown_content_node_23 --> _create_markdown_content_node_24
    _create_markdown_content_node_24 --> _create_markdown_content_node_25
    _create_markdown_content_node_25 --> _create_markdown_content_node_26
    _create_markdown_content_node_26 --> _create_markdown_content_node_27
    _create_markdown_content_node_27 --> _create_markdown_content_node_28
    _create_markdown_content_node_28 --> _create_markdown_content_node_29
    _create_markdown_content_node_29 --> _create_markdown_content_node_30
    _create_markdown_content_node_30 --> _create_markdown_content_node_31
    _create_markdown_content_node_31 --> _create_markdown_content_node_32
    _create_markdown_content_node_32 --> _create_markdown_content_node_33
    _create_markdown_content_node_33 --> _create_markdown_content_node_34
    _create_markdown_content_node_34 --> _create_markdown_content_node_35
    _create_markdown_content_node_35 --> _create_markdown_content_node_36
    _create_markdown_content_node_36 --> _create_markdown_content_node_37
    _create_markdown_content_node_37 --> _create_markdown_content_node_38
    _create_markdown_content_node_38 --> _create_markdown_content_node_39
    _create_markdown_content_node_39 --> _create_markdown_content_node_40
    _create_markdown_content_node_40 --> _create_markdown_content_node_41
    _create_markdown_content_node_41 --> _create_markdown_content_node_42
    _create_markdown_content_node_42 --> _create_markdown_content_node_43
    _create_markdown_content_node_43 --> _create_markdown_content_node_44
    _create_markdown_content_node_44 --> _create_markdown_content_node_45
    _create_markdown_content_node_45 --> _create_markdown_content_node_46
    _create_markdown_content_node_46 --> _create_markdown_content_node_47
    _create_markdown_content_node_47 --> _create_markdown_content_node_48
  end
  subgraph turn_out_the_import_list
    direction TB
    _turn_out_the_import_list_node_0 --> _turn_out_the_import_list_node_1
    _turn_out_the_import_list_node_1 --> _turn_out_the_import_list_node_2
    _turn_out_the_import_list_node_2 --> _turn_out_the_import_list_node_3
    _turn_out_the_import_list_node_3 --> _turn_out_the_import_list_node_4
    _turn_out_the_import_list_node_4 --> _turn_out_the_import_list_node_5
    _turn_out_the_import_list_node_5 --> _turn_out_the_import_list_node_6
    _turn_out_the_import_list_node_6 --> _turn_out_the_import_list_node_7
    _turn_out_the_import_list_node_7 --> _turn_out_the_import_list_node_8
    _turn_out_the_import_list_node_8 --> _turn_out_the_import_list_node_9
    _turn_out_the_import_list_node_9 --> _turn_out_the_import_list_node_10
    _turn_out_the_import_list_node_10 --> _turn_out_the_import_list_node_11
    _turn_out_the_import_list_node_11 --> _turn_out_the_import_list_node_12
    _turn_out_the_import_list_node_12 --> _turn_out_the_import_list_node_13
    _turn_out_the_import_list_node_13 --> _turn_out_the_import_list_node_14
    _turn_out_the_import_list_node_14 --> _turn_out_the_import_list_node_15
    _turn_out_the_import_list_node_15 --> _turn_out_the_import_list_node_16
    _turn_out_the_import_list_node_16 --> _turn_out_the_import_list_node_17
    _turn_out_the_import_list_node_17 --> _turn_out_the_import_list_node_18
    _turn_out_the_import_list_node_18 --> _turn_out_the_import_list_node_19
    _turn_out_the_import_list_node_19 --> _turn_out_the_import_list_node_20
    _turn_out_the_import_list_node_20 --> _turn_out_the_import_list_node_21
    _turn_out_the_import_list_node_21 --> _turn_out_the_import_list_node_22
    _turn_out_the_import_list_node_22 --> _turn_out_the_import_list_node_23
    _turn_out_the_import_list_node_23 --> _turn_out_the_import_list_node_24
    _turn_out_the_import_list_node_24 --> _turn_out_the_import_list_node_25
    _turn_out_the_import_list_node_25 --> _turn_out_the_import_list_node_26
    _turn_out_the_import_list_node_26 --> _turn_out_the_import_list_node_27
    _turn_out_the_import_list_node_27 --> _turn_out_the_import_list_node_28
    _turn_out_the_import_list_node_28 --> _turn_out_the_import_list_node_29
    _turn_out_the_import_list_node_29 --> _turn_out_the_import_list_node_30
    _turn_out_the_import_list_node_30 --> _turn_out_the_import_list_node_31
    _turn_out_the_import_list_node_31 --> _turn_out_the_import_list_node_32
    _turn_out_the_import_list_node_32 --> _turn_out_the_import_list_node_33
    _turn_out_the_import_list_node_33 --> _turn_out_the_import_list_node_34
    _turn_out_the_import_list_node_34 --> _turn_out_the_import_list_node_35
    _turn_out_the_import_list_node_35 --> _turn_out_the_import_list_node_36
    _turn_out_the_import_list_node_36 --> _turn_out_the_import_list_node_37
    _turn_out_the_import_list_node_37 --> _turn_out_the_import_list_node_38
    _turn_out_the_import_list_node_38 --> _turn_out_the_import_list_node_39
    _turn_out_the_import_list_node_39 --> _turn_out_the_import_list_node_40
    _turn_out_the_import_list_node_40 --> _turn_out_the_import_list_node_41
    _turn_out_the_import_list_node_41 --> _turn_out_the_import_list_node_42
    _turn_out_the_import_list_node_42 --> _turn_out_the_import_list_node_43
    _turn_out_the_import_list_node_43 --> _turn_out_the_import_list_node_44
    _turn_out_the_import_list_node_44 --> _turn_out_the_import_list_node_45
    _turn_out_the_import_list_node_45 --> _turn_out_the_import_list_node_46
    _turn_out_the_import_list_node_46 --> _turn_out_the_import_list_node_47
  end
  subgraph create_markdown_debug_dump_block
    direction TB
    _create_markdown_debug_dump_block_node_0 --> _create_markdown_debug_dump_block_node_1
    _create_markdown_debug_dump_block_node_1 --> _create_markdown_debug_dump_block_node_2
    _create_markdown_debug_dump_block_node_2 --> _create_markdown_debug_dump_block_node_3
    _create_markdown_debug_dump_block_node_3 --> _create_markdown_debug_dump_block_node_4
    _create_markdown_debug_dump_block_node_4 --> _create_markdown_debug_dump_block_node_5
    _create_markdown_debug_dump_block_node_5 --> _create_markdown_debug_dump_block_node_6
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    FunctionDef(
      name='create_markdown_content',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=3,
              col_offset=16,
              end_lineno=3,
              end_col_offset=19),
            lineno=3,
            col_offset=4,
            end_lineno=3,
            end_col_offset=19),
          arg(
            arg='import_list',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=4,
                col_offset=17,
                end_lineno=4,
                end_col_offset=21),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=4,
                col_offset=22,
                end_lineno=4,
                end_col_offset=25),
              ctx=Load(),
              lineno=4,
              col_offset=17,
              end_lineno=4,
              end_col_offset=26),
            lineno=4,
            col_offset=4,
            end_lineno=4,
            end_col_offset=26),
          arg(
            arg='global_import_table',
            annotation=Subscript(
              value=Name(
                id='dict',
                ctx=Load(),
                lineno=5,
                col_offset=25,
                end_lineno=5,
                end_col_offset=29),
              slice=Tuple(
                elts=[
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=5,
                    col_offset=30,
                    end_lineno=5,
                    end_col_offset=33),
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=5,
                    col_offset=34,
                    end_lineno=5,
                    end_col_offset=37)],
                ctx=Load(),
                lineno=5,
                col_offset=30,
                end_lineno=5,
                end_col_offset=37),
              ctx=Load(),
              lineno=5,
              col_offset=25,
              end_lineno=5,
              end_col_offset=38),
            lineno=5,
            col_offset=4,
            end_lineno=5,
            end_col_offset=38),
          arg(
            arg='mermaid_diagrams',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=6,
                col_offset=22,
                end_lineno=6,
                end_col_offset=26),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=6,
                col_offset=27,
                end_lineno=6,
                end_col_offset=30),
              ctx=Load(),
              lineno=6,
              col_offset=22,
              end_lineno=6,
              end_col_offset=31),
            lineno=6,
            col_offset=4,
            end_lineno=6,
            end_col_offset=31),
          arg(
            arg='debug_dump',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=7,
              col_offset=16,
              end_lineno=7,
              end_col_offset=19),
            lineno=7,
            col_offset=4,
            end_lineno=7,
            end_col_offset=19)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='debug_block',
              ctx=Store(),
              lineno=9,
              col_offset=4,
              end_lineno=9,
              end_col_offset=15)],
          value=Call(
            func=Name(
              id='create_markdown_debug_dump_block',
              ctx=Load(),
              lineno=9,
              col_offset=18,
              end_lineno=9,
              end_col_offset=50),
            args=[],
            keywords=[
              keyword(
                arg='debug_content',
                value=Name(
                  id='debug_dump',
                  ctx=Load(),
                  lineno=9,
                  col_offset=65,
                  end_lineno=9,
                  end_col_offset=75),
                lineno=9,
                col_offset=51,
                end_lineno=9,
                end_col_offset=75)],
            lineno=9,
            col_offset=18,
            end_lineno=9,
            end_col_offset=76),
          lineno=9,
          col_offset=4,
          end_lineno=9,
          end_col_offset=76),
        Assign(
          targets=[
            Name(
              id='import_block',
              ctx=Store(),
              lineno=10,
              col_offset=4,
              end_lineno=10,
              end_col_offset=16)],
          value=Call(
            func=Name(
              id='turn_out_the_import_list',
              ctx=Load(),
              lineno=10,
              col_offset=19,
              end_lineno=10,
              end_col_offset=43),
            args=[],
            keywords=[
              keyword(
                arg='import_list',
                value=Name(
                  id='import_list',
                  ctx=Load(),
                  lineno=11,
                  col_offset=20,
                  end_lineno=11,
                  end_col_offset=31),
                lineno=11,
                col_offset=8,
                end_lineno=11,
                end_col_offset=31),
              keyword(
                arg='global_import_table',
                value=Name(
                  id='global_import_table',
                  ctx=Load(),
                  lineno=11,
                  col_offset=53,
                  end_lineno=11,
                  end_col_offset=72),
                lineno=11,
                col_offset=33,
                end_lineno=11,
                end_col_offset=72)],
            lineno=10,
            col_offset=19,
            end_lineno=12,
            end_col_offset=5),
          lineno=10,
          col_offset=4,
          end_lineno=12,
          end_col_offset=5),
        Assign(
          targets=[
            Name(
              id='mermaid_blocks',
              ctx=Store(),
              lineno=13,
              col_offset=4,
              end_lineno=13,
              end_col_offset=18)],
          value=Call(
            func=Attribute(
              value=Constant(
                value='\n',
                lineno=13,
                col_offset=21,
                end_lineno=13,
                end_col_offset=25),
              attr='join',
              ctx=Load(),
              lineno=13,
              col_offset=21,
              end_lineno=13,
              end_col_offset=30),
            args=[
              Name(
                id='mermaid_diagrams',
                ctx=Load(),
                lineno=13,
                col_offset=31,
                end_lineno=13,
                end_col_offset=47)],
            keywords=[],
            lineno=13,
            col_offset=21,
            end_lineno=13,
            end_col_offset=48),
          lineno=13,
          col_offset=4,
          end_lineno=13,
          end_col_offset=48),
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='# ',
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='input_file',
                  ctx=Load(),
                  lineno=15,
                  col_offset=13,
                  end_lineno=15,
                  end_col_offset=23),
                conversion=-1,
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              Constant(
                value='\n\n',
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='import_block',
                  ctx=Load(),
                  lineno=16,
                  col_offset=11,
                  end_lineno=16,
                  end_col_offset=23),
                conversion=-1,
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              Constant(
                value='\n---\n',
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='mermaid_blocks',
                  ctx=Load(),
                  lineno=18,
                  col_offset=11,
                  end_lineno=18,
                  end_col_offset=25),
                conversion=-1,
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              Constant(
                value='---\n\n',
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='debug_block',
                  ctx=Load(),
                  lineno=21,
                  col_offset=11,
                  end_lineno=21,
                  end_col_offset=22),
                conversion=-1,
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26),
              Constant(
                value='\n',
                lineno=15,
                col_offset=8,
                end_lineno=21,
                end_col_offset=26)],
            lineno=15,
            col_offset=8,
            end_lineno=21,
            end_col_offset=26),
          lineno=14,
          col_offset=4,
          end_lineno=22,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=8,
        col_offset=5,
        end_lineno=8,
        end_col_offset=8),
      lineno=2,
      col_offset=0,
      end_lineno=22,
      end_col_offset=5),
    FunctionDef(
      name='turn_out_the_import_list',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='import_list',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=26,
                col_offset=17,
                end_lineno=26,
                end_col_offset=21),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=26,
                col_offset=22,
                end_lineno=26,
                end_col_offset=25),
              ctx=Load(),
              lineno=26,
              col_offset=17,
              end_lineno=26,
              end_col_offset=26),
            lineno=26,
            col_offset=4,
            end_lineno=26,
            end_col_offset=26),
          arg(
            arg='global_import_table',
            annotation=Subscript(
              value=Name(
                id='dict',
                ctx=Load(),
                lineno=26,
                col_offset=49,
                end_lineno=26,
                end_col_offset=53),
              slice=Tuple(
                elts=[
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=26,
                    col_offset=54,
                    end_lineno=26,
                    end_col_offset=57),
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=26,
                    col_offset=58,
                    end_lineno=26,
                    end_col_offset=61)],
                ctx=Load(),
                lineno=26,
                col_offset=54,
                end_lineno=26,
                end_col_offset=61),
              ctx=Load(),
              lineno=26,
              col_offset=49,
              end_lineno=26,
              end_col_offset=62),
            lineno=26,
            col_offset=28,
            end_lineno=26,
            end_col_offset=62)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='list_str',
              ctx=Store(),
              lineno=28,
              col_offset=4,
              end_lineno=28,
              end_col_offset=12)],
          value=Constant(
            value='### Imports\n\n',
            lineno=28,
            col_offset=15,
            end_lineno=28,
            end_col_offset=32),
          lineno=28,
          col_offset=4,
          end_lineno=28,
          end_col_offset=32),
        For(
          target=Name(
            id='import_item',
            ctx=Store(),
            lineno=29,
            col_offset=8,
            end_lineno=29,
            end_col_offset=19),
          iter=Name(
            id='import_list',
            ctx=Load(),
            lineno=29,
            col_offset=23,
            end_lineno=29,
            end_col_offset=34),
          body=[
            Assign(
              targets=[
                Name(
                  id='url',
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=11)],
              value=Subscript(
                value=Name(
                  id='global_import_table',
                  ctx=Load(),
                  lineno=30,
                  col_offset=14,
                  end_lineno=30,
                  end_col_offset=33),
                slice=Name(
                  id='import_item',
                  ctx=Load(),
                  lineno=30,
                  col_offset=34,
                  end_lineno=30,
                  end_col_offset=45),
                ctx=Load(),
                lineno=30,
                col_offset=14,
                end_lineno=30,
                end_col_offset=46),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=46),
            If(
              test=Name(
                id='url',
                ctx=Load(),
                lineno=31,
                col_offset=11,
                end_lineno=31,
                end_col_offset=14),
              body=[
                AugAssign(
                  target=Name(
                    id='list_str',
                    ctx=Store(),
                    lineno=32,
                    col_offset=12,
                    end_lineno=32,
                    end_col_offset=20),
                  op=Add(),
                  value=JoinedStr(
                    values=[
                      Constant(
                        value='  - [',
                        lineno=32,
                        col_offset=24,
                        end_lineno=32,
                        end_col_offset=55),
                      FormattedValue(
                        value=Name(
                          id='import_item',
                          ctx=Load(),
                          lineno=32,
                          col_offset=32,
                          end_lineno=32,
                          end_col_offset=43),
                        conversion=-1,
                        lineno=32,
                        col_offset=24,
                        end_lineno=32,
                        end_col_offset=55),
                      Constant(
                        value='](',
                        lineno=32,
                        col_offset=24,
                        end_lineno=32,
                        end_col_offset=55),
                      FormattedValue(
                        value=Name(
                          id='url',
                          ctx=Load(),
                          lineno=32,
                          col_offset=47,
                          end_lineno=32,
                          end_col_offset=50),
                        conversion=-1,
                        lineno=32,
                        col_offset=24,
                        end_lineno=32,
                        end_col_offset=55),
                      Constant(
                        value=')\n',
                        lineno=32,
                        col_offset=24,
                        end_lineno=32,
                        end_col_offset=55)],
                    lineno=32,
                    col_offset=24,
                    end_lineno=32,
                    end_col_offset=55),
                  lineno=32,
                  col_offset=12,
                  end_lineno=32,
                  end_col_offset=55)],
              orelse=[
                AugAssign(
                  target=Name(
                    id='list_str',
                    ctx=Store(),
                    lineno=34,
                    col_offset=12,
                    end_lineno=34,
                    end_col_offset=20),
                  op=Add(),
                  value=JoinedStr(
                    values=[
                      Constant(
                        value='  - ',
                        lineno=34,
                        col_offset=24,
                        end_lineno=34,
                        end_col_offset=46),
                      FormattedValue(
                        value=Name(
                          id='import_item',
                          ctx=Load(),
                          lineno=34,
                          col_offset=31,
                          end_lineno=34,
                          end_col_offset=42),
                        conversion=-1,
                        lineno=34,
                        col_offset=24,
                        end_lineno=34,
                        end_col_offset=46),
                      Constant(
                        value='\n',
                        lineno=34,
                        col_offset=24,
                        end_lineno=34,
                        end_col_offset=46)],
                    lineno=34,
                    col_offset=24,
                    end_lineno=34,
                    end_col_offset=46),
                  lineno=34,
                  col_offset=12,
                  end_lineno=34,
                  end_col_offset=46)],
              lineno=31,
              col_offset=8,
              end_lineno=34,
              end_col_offset=46)],
          orelse=[],
          lineno=29,
          col_offset=4,
          end_lineno=34,
          end_col_offset=46),
        Return(
          value=Name(
            id='list_str',
            ctx=Load(),
            lineno=35,
            col_offset=11,
            end_lineno=35,
            end_col_offset=19),
          lineno=35,
          col_offset=4,
          end_lineno=35,
          end_col_offset=19)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=27,
        col_offset=5,
        end_lineno=27,
        end_col_offset=8),
      lineno=25,
      col_offset=0,
      end_lineno=35,
      end_col_offset=19),
    FunctionDef(
      name='create_markdown_debug_dump_block',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='debug_content',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=39,
              col_offset=52,
              end_lineno=39,
              end_col_offset=55),
            lineno=39,
            col_offset=37,
            end_lineno=39,
            end_col_offset=55)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='<details>\n<summary>Debug AST model dump</summary>\n\n```\n',
                lineno=41,
                col_offset=8,
                end_lineno=46,
                end_col_offset=22),
              FormattedValue(
                value=Name(
                  id='debug_content',
                  ctx=Load(),
                  lineno=44,
                  col_offset=11,
                  end_lineno=44,
                  end_col_offset=24),
                conversion=-1,
                lineno=41,
                col_offset=8,
                end_lineno=46,
                end_col_offset=22),
              Constant(
                value='\n```\n</details>\n',
                lineno=41,
                col_offset=8,
                end_lineno=46,
                end_col_offset=22)],
            lineno=41,
            col_offset=8,
            end_lineno=46,
            end_col_offset=22),
          lineno=40,
          col_offset=4,
          end_lineno=47,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=39,
        col_offset=60,
        end_lineno=39,
        end_col_offset=63),
      lineno=39,
      col_offset=0,
      end_lineno=47,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

