# ./src/pyremaid/markdown_tools.py

### Imports


---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x1068f1370"]
  node_1["ast.FunctionDef object at 0x1068f13d0"]
  node_2["ast.arguments object at 0x1068f14c0"]
  node_3["ast.arg object at 0x1068f1490"]
  node_4["ast.Name object at 0x1068f17f0"]
  node_5["ast.Load object at 0x1067e70d0"]
  node_6["ast.arg object at 0x1068f17c0"]
  node_7["ast.Subscript object at 0x1068f1790"]
  node_8["ast.Name object at 0x1068f1760"]
  node_9["ast.Load object at 0x1067e70d0"]
  node_10["ast.Name object at 0x1068f1730"]
  node_11["ast.Load object at 0x1067e70d0"]
  node_12["ast.Load object at 0x1067e70d0"]
  node_13["ast.arg object at 0x1068f1820"]
  node_14["ast.Subscript object at 0x1068f1850"]
  node_15["ast.Name object at 0x1068f1880"]
  node_16["ast.Load object at 0x1067e70d0"]
  node_17["ast.Name object at 0x1068f1f40"]
  node_18["ast.Load object at 0x1067e70d0"]
  node_19["ast.Load object at 0x1067e70d0"]
  node_20["ast.arg object at 0x1068f1f70"]
  node_21["ast.Name object at 0x1068f1fa0"]
  node_22["ast.Load object at 0x1067e70d0"]
  node_23["ast.Assign object at 0x1068f1fd0"]
  node_24["ast.Name object at 0x1068f1eb0"]
  node_25["ast.Store object at 0x1067e7070"]
  node_26["ast.Call object at 0x1068f1ee0"]
  node_27["ast.Name object at 0x1068f1e80"]
  node_28["ast.Load object at 0x1067e70d0"]
  node_29["ast.keyword object at 0x1068f1e20"]
  node_30["ast.Name object at 0x1068f1e50"]
  node_31["ast.Load object at 0x1067e70d0"]
  node_32["ast.Assign object at 0x1068f1f10"]
  node_33["ast.Name object at 0x1068f1b20"]
  node_34["ast.Store object at 0x1067e7070"]
  node_35["ast.Call object at 0x1068f1af0"]
  node_36["ast.Name object at 0x1068f1a30"]
  node_37["ast.Load object at 0x1067e70d0"]
  node_38["ast.keyword object at 0x1068f1a60"]
  node_39["ast.Name object at 0x1068f1970"]
  node_40["ast.Load object at 0x1067e70d0"]
  node_41["ast.Assign object at 0x1068f19a0"]
  node_42["ast.Name object at 0x1068f19d0"]
  node_43["ast.Store object at 0x1067e7070"]
  node_44["ast.Call object at 0x1068f1910"]
  node_45["ast.Attribute object at 0x1068f1940"]
  node_46["ast.Constant object at 0x1068f1a00"]
  node_47["ast.Load object at 0x1067e70d0"]
  node_48["ast.Name object at 0x1068f1a90"]
  node_49["ast.Load object at 0x1067e70d0"]
  node_50["ast.Return object at 0x1068f18e0"]
  node_51["ast.JoinedStr object at 0x1068f1ac0"]
  node_52["ast.Constant object at 0x1068f1b50"]
  node_53["ast.FormattedValue object at 0x1068f1dc0"]
  node_54["ast.Name object at 0x1068f1d90"]
  node_55["ast.Load object at 0x1067e70d0"]
  node_56["ast.Constant object at 0x1068f1cd0"]
  node_57["ast.FormattedValue object at 0x1068f1d00"]
  node_58["ast.Name object at 0x1068f1c10"]
  node_59["ast.Load object at 0x1067e70d0"]
  node_60["ast.Constant object at 0x1068f1c40"]
  node_61["ast.FormattedValue object at 0x1068f1c70"]
  node_62["ast.Name object at 0x1068f1bb0"]
  node_63["ast.Load object at 0x1067e70d0"]
  node_64["ast.Constant object at 0x1068f1be0"]
  node_65["ast.FormattedValue object at 0x1068f1ca0"]
  node_66["ast.Name object at 0x1068f1d30"]
  node_67["ast.Load object at 0x1067e70d0"]
  node_68["ast.Constant object at 0x1068f1b80"]
  node_69["ast.Name object at 0x1068f18b0"]
  node_70["ast.Load object at 0x1067e70d0"]
  node_71["ast.FunctionDef object at 0x1068f4fd0"]
  node_72["ast.arguments object at 0x1068f4fa0"]
  node_73["ast.arg object at 0x1068f4f70"]
  node_74["ast.Subscript object at 0x1068f4f40"]
  node_75["ast.Name object at 0x1068f4f10"]
  node_76["ast.Load object at 0x1067e70d0"]
  node_77["ast.Name object at 0x1068f4ee0"]
  node_78["ast.Load object at 0x1067e70d0"]
  node_79["ast.Load object at 0x1067e70d0"]
  node_80["ast.Assign object at 0x1068f4eb0"]
  node_81["ast.Name object at 0x1068f4e80"]
  node_82["ast.Store object at 0x1067e7070"]
  node_83["ast.Constant object at 0x1068f4e50"]
  node_84["ast.For object at 0x1068f4e20"]
  node_85["ast.Name object at 0x1068f4df0"]
  node_86["ast.Store object at 0x1067e7070"]
  node_87["ast.Name object at 0x1068f4dc0"]
  node_88["ast.Load object at 0x1067e70d0"]
  node_89["ast.AugAssign object at 0x1068f4d90"]
  node_90["ast.Name object at 0x1068f4d60"]
  node_91["ast.Store object at 0x1067e7070"]
  node_92["ast.Add object at 0x1067e7760"]
  node_93["ast.JoinedStr object at 0x1068f4d30"]
  node_94["ast.Constant object at 0x1068f4d00"]
  node_95["ast.FormattedValue object at 0x1068f4cd0"]
  node_96["ast.Name object at 0x1068f4ac0"]
  node_97["ast.Load object at 0x1067e70d0"]
  node_98["ast.Constant object at 0x1068f4a90"]
  node_99["ast.Return object at 0x1068f4a30"]
  node_100["ast.Name object at 0x1068f4a00"]
  node_101["ast.Load object at 0x1067e70d0"]
  node_102["ast.Name object at 0x1068f49a0"]
  node_103["ast.Load object at 0x1067e70d0"]
  node_104["ast.FunctionDef object at 0x1068f4970"]
  node_105["ast.arguments object at 0x1068f4940"]
  node_106["ast.arg object at 0x1068f4910"]
  node_107["ast.Name object at 0x1068f48e0"]
  node_108["ast.Load object at 0x1067e70d0"]
  node_109["ast.Return object at 0x1068f48b0"]
  node_110["ast.JoinedStr object at 0x1068f4880"]
  node_111["ast.Constant object at 0x1068f4850"]
  node_112["ast.FormattedValue object at 0x1068f4820"]
  node_113["ast.Name object at 0x1068f47f0"]
  node_114["ast.Load object at 0x1067e70d0"]
  node_115["ast.Constant object at 0x1068f47c0"]
  node_116["ast.Name object at 0x1068f4730"]
  node_117["ast.Load object at 0x1067e70d0"]

  node_0 --> node_1
  node_1 --> node_2
  node_2 --> node_3
  node_3 --> node_4
  node_4 --> node_5
  node_5 --> node_6
  node_6 --> node_7
  node_7 --> node_8
  node_8 --> node_9
  node_9 --> node_10
  node_10 --> node_11
  node_11 --> node_12
  node_12 --> node_13
  node_13 --> node_14
  node_14 --> node_15
  node_15 --> node_16
  node_16 --> node_17
  node_17 --> node_18
  node_18 --> node_19
  node_19 --> node_20
  node_20 --> node_21
  node_21 --> node_22
  node_22 --> node_23
  node_23 --> node_24
  node_24 --> node_25
  node_25 --> node_26
  node_26 --> node_27
  node_27 --> node_28
  node_28 --> node_29
  node_29 --> node_30
  node_30 --> node_31
  node_31 --> node_32
  node_32 --> node_33
  node_33 --> node_34
  node_34 --> node_35
  node_35 --> node_36
  node_36 --> node_37
  node_37 --> node_38
  node_38 --> node_39
  node_39 --> node_40
  node_40 --> node_41
  node_41 --> node_42
  node_42 --> node_43
  node_43 --> node_44
  node_44 --> node_45
  node_45 --> node_46
  node_46 --> node_47
  node_47 --> node_48
  node_48 --> node_49
  node_49 --> node_50
  node_50 --> node_51
  node_51 --> node_52
  node_52 --> node_53
  node_53 --> node_54
  node_54 --> node_55
  node_55 --> node_56
  node_56 --> node_57
  node_57 --> node_58
  node_58 --> node_59
  node_59 --> node_60
  node_60 --> node_61
  node_61 --> node_62
  node_62 --> node_63
  node_63 --> node_64
  node_64 --> node_65
  node_65 --> node_66
  node_66 --> node_67
  node_67 --> node_68
  node_68 --> node_69
  node_69 --> node_70
  node_70 --> node_71
  node_71 --> node_72
  node_72 --> node_73
  node_73 --> node_74
  node_74 --> node_75
  node_75 --> node_76
  node_76 --> node_77
  node_77 --> node_78
  node_78 --> node_79
  node_79 --> node_80
  node_80 --> node_81
  node_81 --> node_82
  node_82 --> node_83
  node_83 --> node_84
  node_84 --> node_85
  node_85 --> node_86
  node_86 --> node_87
  node_87 --> node_88
  node_88 --> node_89
  node_89 --> node_90
  node_90 --> node_91
  node_91 --> node_92
  node_92 --> node_93
  node_93 --> node_94
  node_94 --> node_95
  node_95 --> node_96
  node_96 --> node_97
  node_97 --> node_98
  node_98 --> node_99
  node_99 --> node_100
  node_100 --> node_101
  node_101 --> node_102
  node_102 --> node_103
  node_103 --> node_104
  node_104 --> node_105
  node_105 --> node_106
  node_106 --> node_107
  node_107 --> node_108
  node_108 --> node_109
  node_109 --> node_110
  node_110 --> node_111
  node_111 --> node_112
  node_112 --> node_113
  node_113 --> node_114
  node_114 --> node_115
  node_115 --> node_116
  node_116 --> node_117

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
            arg='mermaid_diagrams',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=5,
                col_offset=22,
                end_lineno=5,
                end_col_offset=26),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=5,
                col_offset=27,
                end_lineno=5,
                end_col_offset=30),
              ctx=Load(),
              lineno=5,
              col_offset=22,
              end_lineno=5,
              end_col_offset=31),
            lineno=5,
            col_offset=4,
            end_lineno=5,
            end_col_offset=31),
          arg(
            arg='debug_dump',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=6,
              col_offset=16,
              end_lineno=6,
              end_col_offset=19),
            lineno=6,
            col_offset=4,
            end_lineno=6,
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
              lineno=8,
              col_offset=4,
              end_lineno=8,
              end_col_offset=15)],
          value=Call(
            func=Name(
              id='create_markdown_debug_dump_block',
              ctx=Load(),
              lineno=8,
              col_offset=18,
              end_lineno=8,
              end_col_offset=50),
            args=[],
            keywords=[
              keyword(
                arg='debug_content',
                value=Name(
                  id='debug_dump',
                  ctx=Load(),
                  lineno=8,
                  col_offset=65,
                  end_lineno=8,
                  end_col_offset=75),
                lineno=8,
                col_offset=51,
                end_lineno=8,
                end_col_offset=75)],
            lineno=8,
            col_offset=18,
            end_lineno=8,
            end_col_offset=76),
          lineno=8,
          col_offset=4,
          end_lineno=8,
          end_col_offset=76),
        Assign(
          targets=[
            Name(
              id='import_block',
              ctx=Store(),
              lineno=9,
              col_offset=4,
              end_lineno=9,
              end_col_offset=16)],
          value=Call(
            func=Name(
              id='turn_out_the_import_list',
              ctx=Load(),
              lineno=9,
              col_offset=19,
              end_lineno=9,
              end_col_offset=43),
            args=[],
            keywords=[
              keyword(
                arg='import_list',
                value=Name(
                  id='import_list',
                  ctx=Load(),
                  lineno=9,
                  col_offset=56,
                  end_lineno=9,
                  end_col_offset=67),
                lineno=9,
                col_offset=44,
                end_lineno=9,
                end_col_offset=67)],
            lineno=9,
            col_offset=19,
            end_lineno=9,
            end_col_offset=68),
          lineno=9,
          col_offset=4,
          end_lineno=9,
          end_col_offset=68),
        Assign(
          targets=[
            Name(
              id='mermaid_blocks',
              ctx=Store(),
              lineno=10,
              col_offset=4,
              end_lineno=10,
              end_col_offset=18)],
          value=Call(
            func=Attribute(
              value=Constant(
                value='\n',
                lineno=10,
                col_offset=21,
                end_lineno=10,
                end_col_offset=25),
              attr='join',
              ctx=Load(),
              lineno=10,
              col_offset=21,
              end_lineno=10,
              end_col_offset=30),
            args=[
              Name(
                id='mermaid_diagrams',
                ctx=Load(),
                lineno=10,
                col_offset=31,
                end_lineno=10,
                end_col_offset=47)],
            keywords=[],
            lineno=10,
            col_offset=21,
            end_lineno=10,
            end_col_offset=48),
          lineno=10,
          col_offset=4,
          end_lineno=10,
          end_col_offset=48),
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='# ',
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='input_file',
                  ctx=Load(),
                  lineno=12,
                  col_offset=13,
                  end_lineno=12,
                  end_col_offset=23),
                conversion=-1,
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              Constant(
                value='\n\n',
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='import_block',
                  ctx=Load(),
                  lineno=13,
                  col_offset=11,
                  end_lineno=13,
                  end_col_offset=23),
                conversion=-1,
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              Constant(
                value='\n---\n',
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='mermaid_blocks',
                  ctx=Load(),
                  lineno=15,
                  col_offset=11,
                  end_lineno=15,
                  end_col_offset=25),
                conversion=-1,
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              Constant(
                value='---\n\n',
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              FormattedValue(
                value=Name(
                  id='debug_block',
                  ctx=Load(),
                  lineno=18,
                  col_offset=11,
                  end_lineno=18,
                  end_col_offset=22),
                conversion=-1,
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26),
              Constant(
                value='\n',
                lineno=12,
                col_offset=8,
                end_lineno=18,
                end_col_offset=26)],
            lineno=12,
            col_offset=8,
            end_lineno=18,
            end_col_offset=26),
          lineno=11,
          col_offset=4,
          end_lineno=19,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=7,
        col_offset=5,
        end_lineno=7,
        end_col_offset=8),
      lineno=2,
      col_offset=0,
      end_lineno=19,
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
                lineno=22,
                col_offset=42,
                end_lineno=22,
                end_col_offset=46),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=22,
                col_offset=47,
                end_lineno=22,
                end_col_offset=50),
              ctx=Load(),
              lineno=22,
              col_offset=42,
              end_lineno=22,
              end_col_offset=51),
            lineno=22,
            col_offset=29,
            end_lineno=22,
            end_col_offset=51)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='list_str',
              ctx=Store(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=12)],
          value=Constant(
            value='### Imports\n\n',
            lineno=23,
            col_offset=15,
            end_lineno=23,
            end_col_offset=32),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=32),
        For(
          target=Name(
            id='import_item',
            ctx=Store(),
            lineno=24,
            col_offset=8,
            end_lineno=24,
            end_col_offset=19),
          iter=Name(
            id='import_list',
            ctx=Load(),
            lineno=24,
            col_offset=23,
            end_lineno=24,
            end_col_offset=34),
          body=[
            AugAssign(
              target=Name(
                id='list_str',
                ctx=Store(),
                lineno=25,
                col_offset=8,
                end_lineno=25,
                end_col_offset=16),
              op=Add(),
              value=JoinedStr(
                values=[
                  Constant(
                    value='  - ',
                    lineno=25,
                    col_offset=20,
                    end_lineno=25,
                    end_col_offset=42),
                  FormattedValue(
                    value=Name(
                      id='import_item',
                      ctx=Load(),
                      lineno=25,
                      col_offset=27,
                      end_lineno=25,
                      end_col_offset=38),
                    conversion=-1,
                    lineno=25,
                    col_offset=20,
                    end_lineno=25,
                    end_col_offset=42),
                  Constant(
                    value='\n',
                    lineno=25,
                    col_offset=20,
                    end_lineno=25,
                    end_col_offset=42)],
                lineno=25,
                col_offset=20,
                end_lineno=25,
                end_col_offset=42),
              lineno=25,
              col_offset=8,
              end_lineno=25,
              end_col_offset=42)],
          orelse=[],
          lineno=24,
          col_offset=4,
          end_lineno=25,
          end_col_offset=42),
        Return(
          value=Name(
            id='list_str',
            ctx=Load(),
            lineno=26,
            col_offset=11,
            end_lineno=26,
            end_col_offset=19),
          lineno=26,
          col_offset=4,
          end_lineno=26,
          end_col_offset=19)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=22,
        col_offset=56,
        end_lineno=22,
        end_col_offset=59),
      lineno=22,
      col_offset=0,
      end_lineno=26,
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
              lineno=30,
              col_offset=52,
              end_lineno=30,
              end_col_offset=55),
            lineno=30,
            col_offset=37,
            end_lineno=30,
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
                lineno=32,
                col_offset=8,
                end_lineno=37,
                end_col_offset=22),
              FormattedValue(
                value=Name(
                  id='debug_content',
                  ctx=Load(),
                  lineno=35,
                  col_offset=11,
                  end_lineno=35,
                  end_col_offset=24),
                conversion=-1,
                lineno=32,
                col_offset=8,
                end_lineno=37,
                end_col_offset=22),
              Constant(
                value='\n```\n</details>\n',
                lineno=32,
                col_offset=8,
                end_lineno=37,
                end_col_offset=22)],
            lineno=32,
            col_offset=8,
            end_lineno=37,
            end_col_offset=22),
          lineno=31,
          col_offset=4,
          end_lineno=38,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=30,
        col_offset=60,
        end_lineno=30,
        end_col_offset=63),
      lineno=30,
      col_offset=0,
      end_lineno=38,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

