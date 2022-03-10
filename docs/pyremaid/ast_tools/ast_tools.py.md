# ./src/pyremaid/ast_tools/ast_tools.py

### Imports

  - ast.AST
  - ast.dump
  - ast.parse
  - typing.Optional
  - ast_tools.visitors.BlockGenerator
  - ast_tools.visitors.ImportNodeFinder
  - models.MermaidElement

---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x1068cf310"]
  node_1["ast.FunctionDef object at 0x1068cf6d0"]
  node_2["ast.arguments object at 0x1068cf8b0"]
  node_3["ast.arg object at 0x1068cfa00"]
  node_4["ast.Name object at 0x1068cf130"]
  node_5["ast.Load object at 0x1067e70d0"]
  node_6["ast.arg object at 0x1068cf0d0"]
  node_7["ast.Name object at 0x1068cf0a0"]
  node_8["ast.Load object at 0x1067e70d0"]
  node_9["ast.Return object at 0x1068cff70"]
  node_10["ast.Call object at 0x1068cfd00"]
  node_11["ast.Name object at 0x1068cf760"]
  node_12["ast.Load object at 0x1067e70d0"]
  node_13["ast.keyword object at 0x1068cffa0"]
  node_14["ast.Name object at 0x1068cfb80"]
  node_15["ast.Load object at 0x1067e70d0"]
  node_16["ast.keyword object at 0x1068cfbb0"]
  node_17["ast.Name object at 0x1068cfe80"]
  node_18["ast.Load object at 0x1067e70d0"]
  node_19["ast.keyword object at 0x1068cf8e0"]
  node_20["ast.Constant object at 0x1068cffd0"]
  node_21["ast.keyword object at 0x1068cf5e0"]
  node_22["ast.Constant object at 0x1068cf5b0"]
  node_23["ast.Subscript object at 0x1068cf790"]
  node_24["ast.Name object at 0x1068cf340"]
  node_25["ast.Load object at 0x1067e70d0"]
  node_26["ast.Name object at 0x1068cf640"]
  node_27["ast.Load object at 0x1067e70d0"]
  node_28["ast.Load object at 0x1067e70d0"]
  node_29["ast.FunctionDef object at 0x1068cfd60"]
  node_30["ast.arguments object at 0x1068cf2e0"]
  node_31["ast.arg object at 0x1068cf850"]
  node_32["ast.Name object at 0x1068cfc70"]
  node_33["ast.Load object at 0x1067e70d0"]
  node_34["ast.Return object at 0x1068cff40"]
  node_35["ast.Call object at 0x1068cfbe0"]
  node_36["ast.Name object at 0x1068cfcd0"]
  node_37["ast.Load object at 0x1067e70d0"]
  node_38["ast.Name object at 0x1068ab160"]
  node_39["ast.Load object at 0x1067e70d0"]
  node_40["ast.keyword object at 0x1068ab9a0"]
  node_41["ast.Constant object at 0x1068abcd0"]
  node_42["ast.keyword object at 0x1068abb80"]
  node_43["ast.Constant object at 0x1068abaf0"]
  node_44["ast.keyword object at 0x1068abfd0"]
  node_45["ast.Constant object at 0x1068ab460"]
  node_46["ast.Name object at 0x1068ab3a0"]
  node_47["ast.Load object at 0x1067e70d0"]
  node_48["ast.FunctionDef object at 0x1068abca0"]
  node_49["ast.arguments object at 0x1068ab820"]
  node_50["ast.arg object at 0x1068abbb0"]
  node_51["ast.Name object at 0x1068abfa0"]
  node_52["ast.Load object at 0x1067e70d0"]
  node_53["ast.Assign object at 0x1068ab340"]
  node_54["ast.Name object at 0x1067e4e80"]
  node_55["ast.Store object at 0x1067e7070"]
  node_56["ast.Call object at 0x1067e4f70"]
  node_57["ast.Name object at 0x1067e4fd0"]
  node_58["ast.Load object at 0x1067e70d0"]
  node_59["ast.Expr object at 0x1067e4fa0"]
  node_60["ast.Call object at 0x1068c7f10"]
  node_61["ast.Attribute object at 0x1068c7250"]
  node_62["ast.Name object at 0x1068c7160"]
  node_63["ast.Load object at 0x1067e70d0"]
  node_64["ast.Load object at 0x1067e70d0"]
  node_65["ast.Name object at 0x1068c7eb0"]
  node_66["ast.Load object at 0x1067e70d0"]
  node_67["ast.Return object at 0x1068c7940"]
  node_68["ast.Call object at 0x1068c70a0"]
  node_69["ast.Attribute object at 0x1068c7bb0"]
  node_70["ast.Name object at 0x1068c7610"]
  node_71["ast.Load object at 0x1067e70d0"]
  node_72["ast.Load object at 0x1067e70d0"]
  node_73["ast.Subscript object at 0x1068c7850"]
  node_74["ast.Name object at 0x1068c7130"]
  node_75["ast.Load object at 0x1067e70d0"]
  node_76["ast.Name object at 0x1068c7970"]
  node_77["ast.Load object at 0x1067e70d0"]
  node_78["ast.Load object at 0x1067e70d0"]
  node_79["ast.FunctionDef object at 0x1068c7550"]
  node_80["ast.arguments object at 0x1068c7c40"]
  node_81["ast.arg object at 0x1068c7af0"]
  node_82["ast.Name object at 0x1068c7280"]
  node_83["ast.Load object at 0x1067e70d0"]
  node_84["ast.Assign object at 0x1068c71f0"]
  node_85["ast.Name object at 0x1068c78e0"]
  node_86["ast.Store object at 0x1067e7070"]
  node_87["ast.Call object at 0x1068c76d0"]
  node_88["ast.Name object at 0x1068c78b0"]
  node_89["ast.Load object at 0x1067e70d0"]
  node_90["ast.Expr object at 0x1068c7880"]
  node_91["ast.Call object at 0x1068c7df0"]
  node_92["ast.Attribute object at 0x1068c76a0"]
  node_93["ast.Name object at 0x1068c75e0"]
  node_94["ast.Load object at 0x1067e70d0"]
  node_95["ast.Load object at 0x1067e70d0"]
  node_96["ast.keyword object at 0x1068c7d90"]
  node_97["ast.Name object at 0x1068c7e20"]
  node_98["ast.Load object at 0x1067e70d0"]
  node_99["ast.Return object at 0x1068c7cd0"]
  node_100["ast.Call object at 0x1068c7dc0"]
  node_101["ast.Attribute object at 0x1068c73d0"]
  node_102["ast.Name object at 0x1068c7ca0"]
  node_103["ast.Load object at 0x1067e70d0"]
  node_104["ast.Load object at 0x1067e70d0"]
  node_105["ast.Subscript object at 0x1068c7c10"]
  node_106["ast.Name object at 0x1068c7070"]
  node_107["ast.Load object at 0x1067e70d0"]
  node_108["ast.Name object at 0x1068e8d90"]
  node_109["ast.Load object at 0x1067e70d0"]
  node_110["ast.Load object at 0x1067e70d0"]

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
        alias(name='dump'),
        alias(name='parse')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=32),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Optional')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=27),
    ImportFrom(
      module='ast_tools.visitors',
      names=[
        alias(name='BlockGenerator'),
        alias(name='ImportNodeFinder')],
      level=0,
      lineno=4,
      col_offset=0,
      end_lineno=4,
      end_col_offset=63),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidElement')],
      level=0,
      lineno=5,
      col_offset=0,
      end_lineno=5,
      end_col_offset=33),
    FunctionDef(
      name='get_ast_root_node_for_file',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='source_code',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=8,
              col_offset=44,
              end_lineno=8,
              end_col_offset=47),
            lineno=8,
            col_offset=31,
            end_lineno=8,
            end_col_offset=47),
          arg(
            arg='input_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=8,
              col_offset=61,
              end_lineno=8,
              end_col_offset=64),
            lineno=8,
            col_offset=49,
            end_lineno=8,
            end_col_offset=64)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Name(
              id='parse',
              ctx=Load(),
              lineno=9,
              col_offset=11,
              end_lineno=9,
              end_col_offset=16),
            args=[],
            keywords=[
              keyword(
                arg='source',
                value=Name(
                  id='source_code',
                  ctx=Load(),
                  lineno=10,
                  col_offset=15,
                  end_lineno=10,
                  end_col_offset=26),
                lineno=10,
                col_offset=8,
                end_lineno=10,
                end_col_offset=26),
              keyword(
                arg='filename',
                value=Name(
                  id='input_file',
                  ctx=Load(),
                  lineno=11,
                  col_offset=17,
                  end_lineno=11,
                  end_col_offset=27),
                lineno=11,
                col_offset=8,
                end_lineno=11,
                end_col_offset=27),
              keyword(
                arg='mode',
                value=Constant(
                  value='exec',
                  lineno=12,
                  col_offset=13,
                  end_lineno=12,
                  end_col_offset=19),
                lineno=12,
                col_offset=8,
                end_lineno=12,
                end_col_offset=19),
              keyword(
                arg='type_comments',
                value=Constant(
                  value=True,
                  lineno=13,
                  col_offset=22,
                  end_lineno=13,
                  end_col_offset=26),
                lineno=13,
                col_offset=8,
                end_lineno=13,
                end_col_offset=26)],
            lineno=9,
            col_offset=11,
            end_lineno=14,
            end_col_offset=5),
          lineno=9,
          col_offset=4,
          end_lineno=14,
          end_col_offset=5)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='Optional',
          ctx=Load(),
          lineno=8,
          col_offset=69,
          end_lineno=8,
          end_col_offset=77),
        slice=Name(
          id='AST',
          ctx=Load(),
          lineno=8,
          col_offset=78,
          end_lineno=8,
          end_col_offset=81),
        ctx=Load(),
        lineno=8,
        col_offset=69,
        end_lineno=8,
        end_col_offset=82),
      lineno=8,
      col_offset=0,
      end_lineno=14,
      end_col_offset=5),
    FunctionDef(
      name='get_markdown_dump_for_ast_node',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='ast_node',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=17,
              col_offset=45,
              end_lineno=17,
              end_col_offset=48),
            lineno=17,
            col_offset=35,
            end_lineno=17,
            end_col_offset=48)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Name(
              id='dump',
              ctx=Load(),
              lineno=18,
              col_offset=11,
              end_lineno=18,
              end_col_offset=15),
            args=[
              Name(
                id='ast_node',
                ctx=Load(),
                lineno=18,
                col_offset=16,
                end_lineno=18,
                end_col_offset=24)],
            keywords=[
              keyword(
                arg='annotate_fields',
                value=Constant(
                  value=True,
                  lineno=18,
                  col_offset=42,
                  end_lineno=18,
                  end_col_offset=46),
                lineno=18,
                col_offset=26,
                end_lineno=18,
                end_col_offset=46),
              keyword(
                arg='include_attributes',
                value=Constant(
                  value=True,
                  lineno=18,
                  col_offset=67,
                  end_lineno=18,
                  end_col_offset=71),
                lineno=18,
                col_offset=48,
                end_lineno=18,
                end_col_offset=71),
              keyword(
                arg='indent',
                value=Constant(
                  value=2,
                  lineno=18,
                  col_offset=80,
                  end_lineno=18,
                  end_col_offset=81),
                lineno=18,
                col_offset=73,
                end_lineno=18,
                end_col_offset=81)],
            lineno=18,
            col_offset=11,
            end_lineno=18,
            end_col_offset=82),
          lineno=18,
          col_offset=4,
          end_lineno=18,
          end_col_offset=82)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=17,
        col_offset=53,
        end_lineno=17,
        end_col_offset=56),
      lineno=17,
      col_offset=0,
      end_lineno=18,
      end_col_offset=82),
    FunctionDef(
      name='get_used_import_list',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='ast_node',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=21,
              col_offset=35,
              end_lineno=21,
              end_col_offset=38),
            lineno=21,
            col_offset=25,
            end_lineno=21,
            end_col_offset=38)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='finder',
              ctx=Store(),
              lineno=22,
              col_offset=4,
              end_lineno=22,
              end_col_offset=10)],
          value=Call(
            func=Name(
              id='ImportNodeFinder',
              ctx=Load(),
              lineno=22,
              col_offset=13,
              end_lineno=22,
              end_col_offset=29),
            args=[],
            keywords=[],
            lineno=22,
            col_offset=13,
            end_lineno=22,
            end_col_offset=31),
          lineno=22,
          col_offset=4,
          end_lineno=22,
          end_col_offset=31),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(
                id='finder',
                ctx=Load(),
                lineno=23,
                col_offset=4,
                end_lineno=23,
                end_col_offset=10),
              attr='visit',
              ctx=Load(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=16),
            args=[
              Name(
                id='ast_node',
                ctx=Load(),
                lineno=23,
                col_offset=17,
                end_lineno=23,
                end_col_offset=25)],
            keywords=[],
            lineno=23,
            col_offset=4,
            end_lineno=23,
            end_col_offset=26),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=26),
        Return(
          value=Call(
            func=Attribute(
              value=Name(
                id='finder',
                ctx=Load(),
                lineno=24,
                col_offset=11,
                end_lineno=24,
                end_col_offset=17),
              attr='get_found_imports',
              ctx=Load(),
              lineno=24,
              col_offset=11,
              end_lineno=24,
              end_col_offset=35),
            args=[],
            keywords=[],
            lineno=24,
            col_offset=11,
            end_lineno=24,
            end_col_offset=37),
          lineno=24,
          col_offset=4,
          end_lineno=24,
          end_col_offset=37)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=21,
          col_offset=43,
          end_lineno=21,
          end_col_offset=47),
        slice=Name(
          id='str',
          ctx=Load(),
          lineno=21,
          col_offset=48,
          end_lineno=21,
          end_col_offset=51),
        ctx=Load(),
        lineno=21,
        col_offset=43,
        end_lineno=21,
        end_col_offset=52),
      lineno=21,
      col_offset=0,
      end_lineno=24,
      end_col_offset=37),
    FunctionDef(
      name='create_mermaid_model_from_ast_model',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='model',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=27,
              col_offset=47,
              end_lineno=27,
              end_col_offset=50),
            lineno=27,
            col_offset=40,
            end_lineno=27,
            end_col_offset=50)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='generator',
              ctx=Store(),
              lineno=28,
              col_offset=4,
              end_lineno=28,
              end_col_offset=13)],
          value=Call(
            func=Name(
              id='BlockGenerator',
              ctx=Load(),
              lineno=28,
              col_offset=16,
              end_lineno=28,
              end_col_offset=30),
            args=[],
            keywords=[],
            lineno=28,
            col_offset=16,
            end_lineno=28,
            end_col_offset=32),
          lineno=28,
          col_offset=4,
          end_lineno=28,
          end_col_offset=32),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(
                id='generator',
                ctx=Load(),
                lineno=29,
                col_offset=4,
                end_lineno=29,
                end_col_offset=13),
              attr='visit',
              ctx=Load(),
              lineno=29,
              col_offset=4,
              end_lineno=29,
              end_col_offset=19),
            args=[],
            keywords=[
              keyword(
                arg='node',
                value=Name(
                  id='model',
                  ctx=Load(),
                  lineno=29,
                  col_offset=25,
                  end_lineno=29,
                  end_col_offset=30),
                lineno=29,
                col_offset=20,
                end_lineno=29,
                end_col_offset=30)],
            lineno=29,
            col_offset=4,
            end_lineno=29,
            end_col_offset=31),
          lineno=29,
          col_offset=4,
          end_lineno=29,
          end_col_offset=31),
        Return(
          value=Call(
            func=Attribute(
              value=Name(
                id='generator',
                ctx=Load(),
                lineno=30,
                col_offset=11,
                end_lineno=30,
                end_col_offset=20),
              attr='get_list_of_elements',
              ctx=Load(),
              lineno=30,
              col_offset=11,
              end_lineno=30,
              end_col_offset=41),
            args=[],
            keywords=[],
            lineno=30,
            col_offset=11,
            end_lineno=30,
            end_col_offset=43),
          lineno=30,
          col_offset=4,
          end_lineno=30,
          end_col_offset=43)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=27,
          col_offset=55,
          end_lineno=27,
          end_col_offset=59),
        slice=Name(
          id='MermaidElement',
          ctx=Load(),
          lineno=27,
          col_offset=60,
          end_lineno=27,
          end_col_offset=74),
        ctx=Load(),
        lineno=27,
        col_offset=55,
        end_lineno=27,
        end_col_offset=75),
      lineno=27,
      col_offset=0,
      end_lineno=30,
      end_col_offset=43)],
  type_ignores=[])
```
</details>

