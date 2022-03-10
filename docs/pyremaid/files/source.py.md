# ./src/pyremaid/files/source.py

### Imports

  - os.*
  - re.match

---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x106933250"]
  node_1["ast.FunctionDef object at 0x106915610"]
  node_2["ast.arguments object at 0x1069152e0"]
  node_3["ast.arg object at 0x106915af0"]
  node_4["ast.Name object at 0x106915700"]
  node_5["ast.Load object at 0x1067e70d0"]
  node_6["ast.Assign object at 0x106915c40"]
  node_7["ast.Name object at 0x106915c10"]
  node_8["ast.Store object at 0x1067e7070"]
  node_9["ast.List object at 0x106915ca0"]
  node_10["ast.Load object at 0x1067e70d0"]
  node_11["ast.For object at 0x106915c70"]
  node_12["ast.Tuple object at 0x106915b50"]
  node_13["ast.Name object at 0x106915b20"]
  node_14["ast.Store object at 0x1067e7070"]
  node_15["ast.Name object at 0x106915bb0"]
  node_16["ast.Store object at 0x1067e7070"]
  node_17["ast.Name object at 0x106915b80"]
  node_18["ast.Store object at 0x1067e7070"]
  node_19["ast.Store object at 0x1067e7070"]
  node_20["ast.Call object at 0x1069159a0"]
  node_21["ast.Attribute object at 0x1069158b0"]
  node_22["ast.Name object at 0x106915ac0"]
  node_23["ast.Load object at 0x1067e70d0"]
  node_24["ast.Load object at 0x1067e70d0"]
  node_25["ast.Name object at 0x106915a90"]
  node_26["ast.Load object at 0x1067e70d0"]
  node_27["ast.For object at 0x106915a00"]
  node_28["ast.Name object at 0x1069159d0"]
  node_29["ast.Store object at 0x1067e7070"]
  node_30["ast.Name object at 0x106915a60"]
  node_31["ast.Load object at 0x1067e70d0"]
  node_32["ast.If object at 0x106915a30"]
  node_33["ast.Call object at 0x106915910"]
  node_34["ast.Name object at 0x1069158e0"]
  node_35["ast.Load object at 0x1067e70d0"]
  node_36["ast.Constant object at 0x106915970"]
  node_37["ast.Name object at 0x106915940"]
  node_38["ast.Load object at 0x1067e70d0"]
  node_39["ast.Expr object at 0x106915820"]
  node_40["ast.Call object at 0x1069157f0"]
  node_41["ast.Attribute object at 0x106915880"]
  node_42["ast.Name object at 0x106915850"]
  node_43["ast.Load object at 0x1067e70d0"]
  node_44["ast.Load object at 0x1067e70d0"]
  node_45["ast.Call object at 0x106915760"]
  node_46["ast.Attribute object at 0x106915730"]
  node_47["ast.Attribute object at 0x1069157c0"]
  node_48["ast.Name object at 0x106915790"]
  node_49["ast.Load object at 0x1067e70d0"]
  node_50["ast.Load object at 0x1067e70d0"]
  node_51["ast.Load object at 0x1067e70d0"]
  node_52["ast.Name object at 0x106915670"]
  node_53["ast.Load object at 0x1067e70d0"]
  node_54["ast.Name object at 0x106915640"]
  node_55["ast.Load object at 0x1067e70d0"]
  node_56["ast.Return object at 0x1069156a0"]
  node_57["ast.Name object at 0x1069154c0"]
  node_58["ast.Load object at 0x1067e70d0"]
  node_59["ast.Subscript object at 0x1069155e0"]
  node_60["ast.Name object at 0x1069155b0"]
  node_61["ast.Load object at 0x1067e70d0"]
  node_62["ast.Name object at 0x106915520"]
  node_63["ast.Load object at 0x1067e70d0"]
  node_64["ast.Load object at 0x1067e70d0"]
  node_65["ast.FunctionDef object at 0x1069154f0"]
  node_66["ast.arguments object at 0x106915580"]
  node_67["ast.arg object at 0x106915550"]
  node_68["ast.Name object at 0x106915430"]
  node_69["ast.Load object at 0x1067e70d0"]
  node_70["ast.Assign object at 0x106915400"]
  node_71["ast.Name object at 0x106915490"]
  node_72["ast.Store object at 0x1067e7070"]
  node_73["ast.Constant object at 0x106915460"]
  node_74["ast.With object at 0x1069151f0"]
  node_75["ast.withitem object at 0x106915340"]
  node_76["ast.Call object at 0x106915310"]
  node_77["ast.Name object at 0x1069153a0"]
  node_78["ast.Load object at 0x1067e70d0"]
  node_79["ast.Name object at 0x106915370"]
  node_80["ast.Load object at 0x1067e70d0"]
  node_81["ast.Constant object at 0x106915250"]
  node_82["ast.Name object at 0x1069152b0"]
  node_83["ast.Store object at 0x1067e7070"]
  node_84["ast.Assign object at 0x106915280"]
  node_85["ast.Name object at 0x1069150a0"]
  node_86["ast.Store object at 0x1067e7070"]
  node_87["ast.Call object at 0x1069151c0"]
  node_88["ast.Attribute object at 0x106915190"]
  node_89["ast.Name object at 0x106915100"]
  node_90["ast.Load object at 0x1067e70d0"]
  node_91["ast.Load object at 0x1067e70d0"]
  node_92["ast.Return object at 0x1069150d0"]
  node_93["ast.Name object at 0x106915160"]
  node_94["ast.Load object at 0x1067e70d0"]
  node_95["ast.Name object at 0x106915070"]
  node_96["ast.Load object at 0x1067e70d0"]
  node_97["ast.FunctionDef object at 0x106915040"]
  node_98["ast.arguments object at 0x106914cd0"]
  node_99["ast.arg object at 0x106914a60"]
  node_100["ast.Name object at 0x106914dc0"]
  node_101["ast.Load object at 0x1067e70d0"]
  node_102["ast.arg object at 0x106914f70"]
  node_103["ast.Name object at 0x106914fd0"]
  node_104["ast.Load object at 0x1067e70d0"]
  node_105["ast.Return object at 0x106914fa0"]
  node_106["ast.Call object at 0x106914ee0"]
  node_107["ast.Attribute object at 0x106914eb0"]
  node_108["ast.Call object at 0x106914f40"]
  node_109["ast.Attribute object at 0x106914f10"]
  node_110["ast.Call object at 0x106914e20"]
  node_111["ast.Attribute object at 0x106914df0"]
  node_112["ast.Call object at 0x106914e80"]
  node_113["ast.Attribute object at 0x106914e50"]
  node_114["ast.Call object at 0x106914d30"]
  node_115["ast.Attribute object at 0x106914d00"]
  node_116["ast.Call object at 0x106914d90"]
  node_117["ast.Attribute object at 0x106914d60"]
  node_118["ast.Name object at 0x106914b80"]
  node_119["ast.Load object at 0x1067e70d0"]
  node_120["ast.Load object at 0x1067e70d0"]
  node_121["ast.Name object at 0x106914a90"]
  node_122["ast.Load object at 0x1067e70d0"]
  node_123["ast.Constant object at 0x106914ca0"]
  node_124["ast.Load object at 0x1067e70d0"]
  node_125["ast.Constant object at 0x106914c70"]
  node_126["ast.Constant object at 0x106914be0"]
  node_127["ast.Load object at 0x1067e70d0"]
  node_128["ast.Constant object at 0x106914bb0"]
  node_129["ast.Constant object at 0x106914c40"]
  node_130["ast.Load object at 0x1067e70d0"]
  node_131["ast.Attribute object at 0x106914c10"]
  node_132["ast.Name object at 0x106914af0"]
  node_133["ast.Load object at 0x1067e70d0"]
  node_134["ast.Load object at 0x1067e70d0"]
  node_135["ast.Constant object at 0x106914ac0"]
  node_136["ast.Load object at 0x1067e70d0"]
  node_137["ast.Constant object at 0x106914b50"]
  node_138["ast.Constant object at 0x106914b20"]
  node_139["ast.Load object at 0x1067e70d0"]
  node_140["ast.Constant object at 0x1069149d0"]
  node_141["ast.Constant object at 0x1069148e0"]
  node_142["ast.Name object at 0x106914a00"]
  node_143["ast.Load object at 0x1067e70d0"]

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
  node_117 --> node_118
  node_118 --> node_119
  node_119 --> node_120
  node_120 --> node_121
  node_121 --> node_122
  node_122 --> node_123
  node_123 --> node_124
  node_124 --> node_125
  node_125 --> node_126
  node_126 --> node_127
  node_127 --> node_128
  node_128 --> node_129
  node_129 --> node_130
  node_130 --> node_131
  node_131 --> node_132
  node_132 --> node_133
  node_133 --> node_134
  node_134 --> node_135
  node_135 --> node_136
  node_136 --> node_137
  node_137 --> node_138
  node_138 --> node_139
  node_139 --> node_140
  node_140 --> node_141
  node_141 --> node_142
  node_142 --> node_143

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
    ImportFrom(
      module='re',
      names=[
        alias(name='match')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=20),
    FunctionDef(
      name='find_all_python_files',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=5,
              col_offset=38,
              end_lineno=5,
              end_col_offset=41),
            lineno=5,
            col_offset=26,
            end_lineno=5,
            end_col_offset=41)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='python_files',
              ctx=Store(),
              lineno=6,
              col_offset=4,
              end_lineno=6,
              end_col_offset=16)],
          value=List(
            elts=[],
            ctx=Load(),
            lineno=6,
            col_offset=19,
            end_lineno=6,
            end_col_offset=21),
          lineno=6,
          col_offset=4,
          end_lineno=6,
          end_col_offset=21),
        For(
          target=Tuple(
            elts=[
              Name(
                id='dirpath',
                ctx=Store(),
                lineno=7,
                col_offset=8,
                end_lineno=7,
                end_col_offset=15),
              Name(
                id='_dirnames',
                ctx=Store(),
                lineno=7,
                col_offset=17,
                end_lineno=7,
                end_col_offset=26),
              Name(
                id='filenames',
                ctx=Store(),
                lineno=7,
                col_offset=28,
                end_lineno=7,
                end_col_offset=37)],
            ctx=Store(),
            lineno=7,
            col_offset=8,
            end_lineno=7,
            end_col_offset=37),
          iter=Call(
            func=Attribute(
              value=Name(
                id='os',
                ctx=Load(),
                lineno=7,
                col_offset=41,
                end_lineno=7,
                end_col_offset=43),
              attr='walk',
              ctx=Load(),
              lineno=7,
              col_offset=41,
              end_lineno=7,
              end_col_offset=48),
            args=[
              Name(
                id='input_path',
                ctx=Load(),
                lineno=7,
                col_offset=49,
                end_lineno=7,
                end_col_offset=59)],
            keywords=[],
            lineno=7,
            col_offset=41,
            end_lineno=7,
            end_col_offset=60),
          body=[
            For(
              target=Name(
                id='filename',
                ctx=Store(),
                lineno=8,
                col_offset=12,
                end_lineno=8,
                end_col_offset=20),
              iter=Name(
                id='filenames',
                ctx=Load(),
                lineno=8,
                col_offset=24,
                end_lineno=8,
                end_col_offset=33),
              body=[
                If(
                  test=Call(
                    func=Name(
                      id='match',
                      ctx=Load(),
                      lineno=9,
                      col_offset=15,
                      end_lineno=9,
                      end_col_offset=20),
                    args=[
                      Constant(
                        value='.*\\.py$',
                        lineno=9,
                        col_offset=21,
                        end_lineno=9,
                        end_col_offset=31),
                      Name(
                        id='filename',
                        ctx=Load(),
                        lineno=9,
                        col_offset=33,
                        end_lineno=9,
                        end_col_offset=41)],
                    keywords=[],
                    lineno=9,
                    col_offset=15,
                    end_lineno=9,
                    end_col_offset=42),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='python_files',
                            ctx=Load(),
                            lineno=10,
                            col_offset=16,
                            end_lineno=10,
                            end_col_offset=28),
                          attr='append',
                          ctx=Load(),
                          lineno=10,
                          col_offset=16,
                          end_lineno=10,
                          end_col_offset=35),
                        args=[
                          Call(
                            func=Attribute(
                              value=Attribute(
                                value=Name(
                                  id='os',
                                  ctx=Load(),
                                  lineno=10,
                                  col_offset=36,
                                  end_lineno=10,
                                  end_col_offset=38),
                                attr='path',
                                ctx=Load(),
                                lineno=10,
                                col_offset=36,
                                end_lineno=10,
                                end_col_offset=43),
                              attr='join',
                              ctx=Load(),
                              lineno=10,
                              col_offset=36,
                              end_lineno=10,
                              end_col_offset=48),
                            args=[
                              Name(
                                id='dirpath',
                                ctx=Load(),
                                lineno=10,
                                col_offset=49,
                                end_lineno=10,
                                end_col_offset=56),
                              Name(
                                id='filename',
                                ctx=Load(),
                                lineno=10,
                                col_offset=58,
                                end_lineno=10,
                                end_col_offset=66)],
                            keywords=[],
                            lineno=10,
                            col_offset=36,
                            end_lineno=10,
                            end_col_offset=67)],
                        keywords=[],
                        lineno=10,
                        col_offset=16,
                        end_lineno=10,
                        end_col_offset=68),
                      lineno=10,
                      col_offset=16,
                      end_lineno=10,
                      end_col_offset=68)],
                  orelse=[],
                  lineno=9,
                  col_offset=12,
                  end_lineno=10,
                  end_col_offset=68)],
              orelse=[],
              lineno=8,
              col_offset=8,
              end_lineno=10,
              end_col_offset=68)],
          orelse=[],
          lineno=7,
          col_offset=4,
          end_lineno=10,
          end_col_offset=68),
        Return(
          value=Name(
            id='python_files',
            ctx=Load(),
            lineno=12,
            col_offset=11,
            end_lineno=12,
            end_col_offset=23),
          lineno=12,
          col_offset=4,
          end_lineno=12,
          end_col_offset=23)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=5,
          col_offset=46,
          end_lineno=5,
          end_col_offset=50),
        slice=Name(
          id='str',
          ctx=Load(),
          lineno=5,
          col_offset=51,
          end_lineno=5,
          end_col_offset=54),
        ctx=Load(),
        lineno=5,
        col_offset=46,
        end_lineno=5,
        end_col_offset=55),
      lineno=5,
      col_offset=0,
      end_lineno=12,
      end_col_offset=23),
    FunctionDef(
      name='get_source_code_from_file',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=15,
              col_offset=42,
              end_lineno=15,
              end_col_offset=45),
            lineno=15,
            col_offset=30,
            end_lineno=15,
            end_col_offset=45)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='content',
              ctx=Store(),
              lineno=16,
              col_offset=4,
              end_lineno=16,
              end_col_offset=11)],
          value=Constant(
            value='',
            lineno=16,
            col_offset=14,
            end_lineno=16,
            end_col_offset=16),
          lineno=16,
          col_offset=4,
          end_lineno=16,
          end_col_offset=16),
        With(
          items=[
            withitem(
              context_expr=Call(
                func=Name(
                  id='open',
                  ctx=Load(),
                  lineno=17,
                  col_offset=9,
                  end_lineno=17,
                  end_col_offset=13),
                args=[
                  Name(
                    id='input_file',
                    ctx=Load(),
                    lineno=17,
                    col_offset=14,
                    end_lineno=17,
                    end_col_offset=24),
                  Constant(
                    value='r',
                    lineno=17,
                    col_offset=26,
                    end_lineno=17,
                    end_col_offset=29)],
                keywords=[],
                lineno=17,
                col_offset=9,
                end_lineno=17,
                end_col_offset=30),
              optional_vars=Name(
                id='md_file',
                ctx=Store(),
                lineno=17,
                col_offset=34,
                end_lineno=17,
                end_col_offset=41))],
          body=[
            Assign(
              targets=[
                Name(
                  id='content',
                  ctx=Store(),
                  lineno=18,
                  col_offset=8,
                  end_lineno=18,
                  end_col_offset=15)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='md_file',
                    ctx=Load(),
                    lineno=18,
                    col_offset=18,
                    end_lineno=18,
                    end_col_offset=25),
                  attr='read',
                  ctx=Load(),
                  lineno=18,
                  col_offset=18,
                  end_lineno=18,
                  end_col_offset=30),
                args=[],
                keywords=[],
                lineno=18,
                col_offset=18,
                end_lineno=18,
                end_col_offset=32),
              lineno=18,
              col_offset=8,
              end_lineno=18,
              end_col_offset=32)],
          lineno=17,
          col_offset=4,
          end_lineno=18,
          end_col_offset=32),
        Return(
          value=Name(
            id='content',
            ctx=Load(),
            lineno=19,
            col_offset=11,
            end_lineno=19,
            end_col_offset=18),
          lineno=19,
          col_offset=4,
          end_lineno=19,
          end_col_offset=18)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=15,
        col_offset=50,
        end_lineno=15,
        end_col_offset=53),
      lineno=15,
      col_offset=0,
      end_lineno=19,
      end_col_offset=18),
    FunctionDef(
      name='get_import_name_from_path',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=42,
              end_lineno=22,
              end_col_offset=45),
            lineno=22,
            col_offset=30,
            end_lineno=22,
            end_col_offset=45),
          arg(
            arg='input_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=59,
              end_lineno=22,
              end_col_offset=62),
            lineno=22,
            col_offset=47,
            end_lineno=22,
            end_col_offset=62)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Attribute(
              value=Call(
                func=Attribute(
                  value=Call(
                    func=Attribute(
                      value=Call(
                        func=Attribute(
                          value=Call(
                            func=Attribute(
                              value=Call(
                                func=Attribute(
                                  value=Name(
                                    id='input_file',
                                    ctx=Load(),
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=18),
                                  attr='replace',
                                  ctx=Load(),
                                  lineno=24,
                                  col_offset=8,
                                  end_lineno=25,
                                  end_col_offset=16),
                                args=[
                                  Name(
                                    id='input_path',
                                    ctx=Load(),
                                    lineno=25,
                                    col_offset=17,
                                    end_lineno=25,
                                    end_col_offset=27),
                                  Constant(
                                    value='',
                                    lineno=25,
                                    col_offset=29,
                                    end_lineno=25,
                                    end_col_offset=31)],
                                keywords=[],
                                lineno=24,
                                col_offset=8,
                                end_lineno=25,
                                end_col_offset=32),
                              attr='replace',
                              ctx=Load(),
                              lineno=24,
                              col_offset=8,
                              end_lineno=26,
                              end_col_offset=16),
                            args=[
                              Constant(
                                value='.py',
                                lineno=26,
                                col_offset=17,
                                end_lineno=26,
                                end_col_offset=22),
                              Constant(
                                value='',
                                lineno=26,
                                col_offset=24,
                                end_lineno=26,
                                end_col_offset=26)],
                            keywords=[],
                            lineno=24,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=27),
                          attr='replace',
                          ctx=Load(),
                          lineno=24,
                          col_offset=8,
                          end_lineno=27,
                          end_col_offset=16),
                        args=[
                          Constant(
                            value='.',
                            lineno=27,
                            col_offset=17,
                            end_lineno=27,
                            end_col_offset=20),
                          Constant(
                            value='',
                            lineno=27,
                            col_offset=22,
                            end_lineno=27,
                            end_col_offset=24)],
                        keywords=[],
                        lineno=24,
                        col_offset=8,
                        end_lineno=27,
                        end_col_offset=25),
                      attr='replace',
                      ctx=Load(),
                      lineno=24,
                      col_offset=8,
                      end_lineno=28,
                      end_col_offset=16),
                    args=[
                      Attribute(
                        value=Name(
                          id='os',
                          ctx=Load(),
                          lineno=28,
                          col_offset=17,
                          end_lineno=28,
                          end_col_offset=19),
                        attr='sep',
                        ctx=Load(),
                        lineno=28,
                        col_offset=17,
                        end_lineno=28,
                        end_col_offset=23),
                      Constant(
                        value='.',
                        lineno=28,
                        col_offset=25,
                        end_lineno=28,
                        end_col_offset=28)],
                    keywords=[],
                    lineno=24,
                    col_offset=8,
                    end_lineno=28,
                    end_col_offset=29),
                  attr='replace',
                  ctx=Load(),
                  lineno=24,
                  col_offset=8,
                  end_lineno=29,
                  end_col_offset=16),
                args=[
                  Constant(
                    value='.__init__',
                    lineno=29,
                    col_offset=17,
                    end_lineno=29,
                    end_col_offset=28),
                  Constant(
                    value='',
                    lineno=29,
                    col_offset=30,
                    end_lineno=29,
                    end_col_offset=32)],
                keywords=[],
                lineno=24,
                col_offset=8,
                end_lineno=29,
                end_col_offset=33),
              attr='replace',
              ctx=Load(),
              lineno=24,
              col_offset=8,
              end_lineno=30,
              end_col_offset=16),
            args=[
              Constant(
                value='__init__',
                lineno=30,
                col_offset=17,
                end_lineno=30,
                end_col_offset=27),
              Constant(
                value='.',
                lineno=30,
                col_offset=29,
                end_lineno=30,
                end_col_offset=32)],
            keywords=[],
            lineno=24,
            col_offset=8,
            end_lineno=30,
            end_col_offset=33),
          lineno=23,
          col_offset=4,
          end_lineno=31,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=22,
        col_offset=67,
        end_lineno=22,
        end_col_offset=70),
      lineno=22,
      col_offset=0,
      end_lineno=31,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

