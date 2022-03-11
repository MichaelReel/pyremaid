# ./src/pyremaid/markdown_tools.py

### Imports


---
```mermaid
flowchart TB
  _f9_n64["Assign"]
  _f9_n65["Name"]
  _f9_n66["Store"]
  _f9_n67["Call"]
  _f9_n68["Name"]
  _f9_n69["Load"]
  _f9_n70["keyword"]
  _f9_n71["Name"]
  _f9_n72["Load"]
  _f9_n73["Assign"]
  _f9_n74["Name"]
  _f9_n75["Store"]
  _f9_n76["Call"]
  _f9_n77["Name"]
  _f9_n78["Load"]
  _f9_n79["keyword"]
  _f9_n80["Name"]
  _f9_n81["Load"]
  _f9_n82["keyword"]
  _f9_n83["Name"]
  _f9_n84["Load"]
  _f9_n85["Assign"]
  _f9_n86["Name"]
  _f9_n87["Store"]
  _f9_n88["Call"]
  _f9_n89["Attribute"]
  _f9_n90["Constant"]
  _f9_n91["Load"]
  _f9_n92["Name"]
  _f9_n93["Load"]
  _f9_n94["Return"]
  _f9_n95["JoinedStr"]
  _f9_n96["Constant"]
  _f9_n97["FormattedValue"]
  _f9_n98["Name"]
  _f9_n99["Load"]
  _f9_n100["Constant"]
  _f9_n101["FormattedValue"]
  _f9_n102["Name"]
  _f9_n103["Load"]
  _f9_n104["Constant"]
  _f9_n105["FormattedValue"]
  _f9_n106["Name"]
  _f9_n107["Load"]
  _f9_n108["Constant"]
  _f9_n109["FormattedValue"]
  _f9_n110["Name"]
  _f9_n111["Load"]
  _f9_n112["Constant"]
  _f10_n113["Assign"]
  _f10_n114["Name"]
  _f10_n115["Store"]
  _f10_n116["Constant"]
  _f10_l11["import_item"]
  _f10_l11_n117["Assign"]
  _f10_l11_n118["Name"]
  _f10_l11_n119["Store"]
  _f10_l11_n120["Subscript"]
  _f10_l11_n121["Name"]
  _f10_l11_n122["Load"]
  _f10_l11_n123["Name"]
  _f10_l11_n124["Load"]
  _f10_l11_n125["Load"]
  _f10_l11_n126["If"]
  _f10_l11_n127["Name"]
  _f10_l11_n128["Load"]
  _f10_l11_n129["AugAssign"]
  _f10_l11_n130["Name"]
  _f10_l11_n131["Store"]
  _f10_l11_n132["Add"]
  _f10_l11_n133["JoinedStr"]
  _f10_l11_n134["Constant"]
  _f10_l11_n135["FormattedValue"]
  _f10_l11_n136["Name"]
  _f10_l11_n137["Load"]
  _f10_l11_n138["Constant"]
  _f10_l11_n139["FormattedValue"]
  _f10_l11_n140["Name"]
  _f10_l11_n141["Load"]
  _f10_l11_n142["Constant"]
  _f10_l11_n143["AugAssign"]
  _f10_l11_n144["Name"]
  _f10_l11_n145["Store"]
  _f10_l11_n146["Add"]
  _f10_l11_n147["JoinedStr"]
  _f10_l11_n148["Constant"]
  _f10_l11_n149["FormattedValue"]
  _f10_l11_n150["Name"]
  _f10_l11_n151["Load"]
  _f10_l11_n152["Constant"]
  _f10_n153["Return"]
  _f10_n154["Name"]
  _f10_n155["Load"]
  _f12_n156["Return"]
  _f12_n157["JoinedStr"]
  _f12_n158["Constant"]
  _f12_n159["FormattedValue"]
  _f12_n160["Name"]
  _f12_n161["Load"]
  _f12_n162["Constant"]

  subgraph _create_markdown_content
    direction TB
    _f9_n64 --> _f9_n65
    _f9_n65 --> _f9_n66
    _f9_n66 --> _f9_n67
    _f9_n67 --> _f9_n68
    _f9_n68 --> _f9_n69
    _f9_n69 --> _f9_n70
    _f9_n70 --> _f9_n71
    _f9_n71 --> _f9_n72
    _f9_n72 --> _f9_n73
    _f9_n73 --> _f9_n74
    _f9_n74 --> _f9_n75
    _f9_n75 --> _f9_n76
    _f9_n76 --> _f9_n77
    _f9_n77 --> _f9_n78
    _f9_n78 --> _f9_n79
    _f9_n79 --> _f9_n80
    _f9_n80 --> _f9_n81
    _f9_n81 --> _f9_n82
    _f9_n82 --> _f9_n83
    _f9_n83 --> _f9_n84
    _f9_n84 --> _f9_n85
    _f9_n85 --> _f9_n86
    _f9_n86 --> _f9_n87
    _f9_n87 --> _f9_n88
    _f9_n88 --> _f9_n89
    _f9_n89 --> _f9_n90
    _f9_n90 --> _f9_n91
    _f9_n91 --> _f9_n92
    _f9_n92 --> _f9_n93
    _f9_n93 --> _f9_n94
    _f9_n94 --> _f9_n95
    _f9_n95 --> _f9_n96
    _f9_n96 --> _f9_n97
    _f9_n97 --> _f9_n98
    _f9_n98 --> _f9_n99
    _f9_n99 --> _f9_n100
    _f9_n100 --> _f9_n101
    _f9_n101 --> _f9_n102
    _f9_n102 --> _f9_n103
    _f9_n103 --> _f9_n104
    _f9_n104 --> _f9_n105
    _f9_n105 --> _f9_n106
    _f9_n106 --> _f9_n107
    _f9_n107 --> _f9_n108
    _f9_n108 --> _f9_n109
    _f9_n109 --> _f9_n110
    _f9_n110 --> _f9_n111
    _f9_n111 --> _f9_n112
  end
  subgraph _turn_out_the_import_list
    direction TB
    _f10_n113 --> _f10_n114
    _f10_n114 --> _f10_n115
    _f10_n115 --> _f10_n116
    _f10_n116 --> _f10_l11
    %% loop import_item
      _f10_l11_n117 --> _f10_l11_n118
      _f10_l11_n118 --> _f10_l11_n119
      _f10_l11_n119 --> _f10_l11_n120
      _f10_l11_n120 --> _f10_l11_n121
      _f10_l11_n121 --> _f10_l11_n122
      _f10_l11_n122 --> _f10_l11_n123
      _f10_l11_n123 --> _f10_l11_n124
      _f10_l11_n124 --> _f10_l11_n125
      _f10_l11_n125 --> _f10_l11_n126
      _f10_l11_n126 --> _f10_l11_n127
      _f10_l11_n127 --> _f10_l11_n128
      _f10_l11_n128 --> _f10_l11_n129
      _f10_l11_n129 --> _f10_l11_n130
      _f10_l11_n130 --> _f10_l11_n131
      _f10_l11_n131 --> _f10_l11_n132
      _f10_l11_n132 --> _f10_l11_n133
      _f10_l11_n133 --> _f10_l11_n134
      _f10_l11_n134 --> _f10_l11_n135
      _f10_l11_n135 --> _f10_l11_n136
      _f10_l11_n136 --> _f10_l11_n137
      _f10_l11_n137 --> _f10_l11_n138
      _f10_l11_n138 --> _f10_l11_n139
      _f10_l11_n139 --> _f10_l11_n140
      _f10_l11_n140 --> _f10_l11_n141
      _f10_l11_n141 --> _f10_l11_n142
      _f10_l11_n142 --> _f10_l11_n143
      _f10_l11_n143 --> _f10_l11_n144
      _f10_l11_n144 --> _f10_l11_n145
      _f10_l11_n145 --> _f10_l11_n146
      _f10_l11_n146 --> _f10_l11_n147
      _f10_l11_n147 --> _f10_l11_n148
      _f10_l11_n148 --> _f10_l11_n149
      _f10_l11_n149 --> _f10_l11_n150
      _f10_l11_n150 --> _f10_l11_n151
      _f10_l11_n151 --> _f10_l11_n152
    %% end import_item
    _f10_l11_n152 --> _f10_l11_n117
    _f10_l11_n117 --> _f10_n153
    _f10_n153 --> _f10_n154
    _f10_n154 --> _f10_n155
  end
  subgraph _create_markdown_debug_dump_block
    direction TB
    _f12_n156 --> _f12_n157
    _f12_n157 --> _f12_n158
    _f12_n158 --> _f12_n159
    _f12_n159 --> _f12_n160
    _f12_n160 --> _f12_n161
    _f12_n161 --> _f12_n162
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

