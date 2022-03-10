# ./src/pyremaid/files/destination.py

### Imports

  - os.*

---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x1068e3940"]
  node_1["ast.FunctionDef object at 0x1068e3820"]
  node_2["ast.arguments object at 0x1068e3fa0"]
  node_3["ast.arg object at 0x1068e3a60"]
  node_4["ast.Name object at 0x1068e3fd0"]
  node_5["ast.Load object at 0x1067e70d0"]
  node_6["ast.If object at 0x1068e3b50"]
  node_7["ast.UnaryOp object at 0x1068e3d30"]
  node_8["ast.Not object at 0x1067e7d00"]
  node_9["ast.Call object at 0x1068e3f10"]
  node_10["ast.Attribute object at 0x1068e36d0"]
  node_11["ast.Attribute object at 0x1068e3cd0"]
  node_12["ast.Name object at 0x1068e3580"]
  node_13["ast.Load object at 0x1067e70d0"]
  node_14["ast.Load object at 0x1067e70d0"]
  node_15["ast.Load object at 0x1067e70d0"]
  node_16["ast.Name object at 0x1068e3460"]
  node_17["ast.Load object at 0x1067e70d0"]
  node_18["ast.Expr object at 0x1068e3d00"]
  node_19["ast.Call object at 0x1068e3e80"]
  node_20["ast.Attribute object at 0x1068e36a0"]
  node_21["ast.Name object at 0x1068e3340"]
  node_22["ast.Load object at 0x1067e70d0"]
  node_23["ast.Load object at 0x1067e70d0"]
  node_24["ast.Name object at 0x1068e3700"]
  node_25["ast.Load object at 0x1067e70d0"]
  node_26["ast.Constant object at 0x1068e3370"]
  node_27["ast.FunctionDef object at 0x1068e37c0"]
  node_28["ast.arguments object at 0x1068e33d0"]
  node_29["ast.arg object at 0x1068e3490"]
  node_30["ast.Name object at 0x1068e3a00"]
  node_31["ast.Load object at 0x1067e70d0"]
  node_32["ast.Expr object at 0x1068e3070"]
  node_33["ast.Call object at 0x1068e32e0"]
  node_34["ast.Name object at 0x1068e3430"]
  node_35["ast.Load object at 0x1067e70d0"]
  node_36["ast.keyword object at 0x1068e3a30"]
  node_37["ast.Name object at 0x1068e3c70"]
  node_38["ast.Load object at 0x1067e70d0"]
  node_39["ast.For object at 0x1068e3df0"]
  node_40["ast.Tuple object at 0x1068e39a0"]
  node_41["ast.Name object at 0x1068e37f0"]
  node_42["ast.Store object at 0x1067e7070"]
  node_43["ast.Name object at 0x1068e3ca0"]
  node_44["ast.Store object at 0x1067e7070"]
  node_45["ast.Name object at 0x1068e3a90"]
  node_46["ast.Store object at 0x1067e7070"]
  node_47["ast.Store object at 0x1067e7070"]
  node_48["ast.Call object at 0x1068e3400"]
  node_49["ast.Attribute object at 0x1068e30d0"]
  node_50["ast.Name object at 0x1068e3e20"]
  node_51["ast.Load object at 0x1067e70d0"]
  node_52["ast.Load object at 0x1067e70d0"]
  node_53["ast.Name object at 0x1068e3c10"]
  node_54["ast.Load object at 0x1067e70d0"]
  node_55["ast.keyword object at 0x1068e3dc0"]
  node_56["ast.Constant object at 0x1068e3910"]
  node_57["ast.For object at 0x1068e3af0"]
  node_58["ast.Name object at 0x1068e3220"]
  node_59["ast.Store object at 0x1067e7070"]
  node_60["ast.Name object at 0x1068e3520"]
  node_61["ast.Load object at 0x1067e70d0"]
  node_62["ast.Expr object at 0x1068e3f70"]
  node_63["ast.Call object at 0x1068e38e0"]
  node_64["ast.Attribute object at 0x1068e38b0"]
  node_65["ast.Name object at 0x106933ca0"]
  node_66["ast.Load object at 0x1067e70d0"]
  node_67["ast.Load object at 0x1067e70d0"]
  node_68["ast.Call object at 0x106933640"]
  node_69["ast.Attribute object at 0x106933b20"]
  node_70["ast.Attribute object at 0x1069331c0"]
  node_71["ast.Name object at 0x106933460"]
  node_72["ast.Load object at 0x1067e70d0"]
  node_73["ast.Load object at 0x1067e70d0"]
  node_74["ast.Load object at 0x1067e70d0"]
  node_75["ast.Name object at 0x106933160"]
  node_76["ast.Load object at 0x1067e70d0"]
  node_77["ast.Name object at 0x106933190"]
  node_78["ast.Load object at 0x1067e70d0"]
  node_79["ast.For object at 0x1069331f0"]
  node_80["ast.Name object at 0x106933220"]
  node_81["ast.Store object at 0x1067e7070"]
  node_82["ast.Name object at 0x106933100"]
  node_83["ast.Load object at 0x1067e70d0"]
  node_84["ast.Expr object at 0x106933280"]
  node_85["ast.Call object at 0x106933310"]
  node_86["ast.Attribute object at 0x106933340"]
  node_87["ast.Name object at 0x106933370"]
  node_88["ast.Load object at 0x1067e70d0"]
  node_89["ast.Load object at 0x1067e70d0"]
  node_90["ast.Call object at 0x1069333a0"]
  node_91["ast.Attribute object at 0x106933430"]
  node_92["ast.Attribute object at 0x1069332e0"]
  node_93["ast.Name object at 0x106933490"]
  node_94["ast.Load object at 0x1067e70d0"]
  node_95["ast.Load object at 0x1067e70d0"]
  node_96["ast.Load object at 0x1067e70d0"]
  node_97["ast.Name object at 0x106933400"]
  node_98["ast.Load object at 0x1067e70d0"]
  node_99["ast.Name object at 0x106933880"]
  node_100["ast.Load object at 0x1067e70d0"]
  node_101["ast.Constant object at 0x106933670"]
  node_102["ast.FunctionDef object at 0x1069335b0"]
  node_103["ast.arguments object at 0x1069336a0"]
  node_104["ast.arg object at 0x1069336d0"]
  node_105["ast.Name object at 0x1069335e0"]
  node_106["ast.Load object at 0x1067e70d0"]
  node_107["ast.arg object at 0x106933610"]
  node_108["ast.Name object at 0x106933730"]
  node_109["ast.Load object at 0x1067e70d0"]
  node_110["ast.Return object at 0x106933760"]
  node_111["ast.Call object at 0x106933790"]
  node_112["ast.Attribute object at 0x1069337c0"]
  node_113["ast.Attribute object at 0x106933850"]
  node_114["ast.Name object at 0x106933b80"]
  node_115["ast.Load object at 0x1067e70d0"]
  node_116["ast.Load object at 0x1067e70d0"]
  node_117["ast.Load object at 0x1067e70d0"]
  node_118["ast.Name object at 0x1069338b0"]
  node_119["ast.Load object at 0x1067e70d0"]
  node_120["ast.BinOp object at 0x106933820"]
  node_121["ast.Name object at 0x1069339d0"]
  node_122["ast.Load object at 0x1067e70d0"]
  node_123["ast.Add object at 0x1067e7760"]
  node_124["ast.Constant object at 0x106933ac0"]
  node_125["ast.Name object at 0x106933be0"]
  node_126["ast.Load object at 0x1067e70d0"]
  node_127["ast.FunctionDef object at 0x106933a60"]
  node_128["ast.arguments object at 0x106933cd0"]
  node_129["ast.arg object at 0x106933c40"]
  node_130["ast.Name object at 0x106933dc0"]
  node_131["ast.Load object at 0x1067e70d0"]
  node_132["ast.arg object at 0x106933700"]
  node_133["ast.Name object at 0x106933c70"]
  node_134["ast.Load object at 0x1067e70d0"]
  node_135["ast.If object at 0x106933d90"]
  node_136["ast.UnaryOp object at 0x1069337f0"]
  node_137["ast.Not object at 0x1067e7d00"]
  node_138["ast.Call object at 0x1069338e0"]
  node_139["ast.Attribute object at 0x106933d30"]
  node_140["ast.Attribute object at 0x106933d60"]
  node_141["ast.Name object at 0x106933df0"]
  node_142["ast.Load object at 0x1067e70d0"]
  node_143["ast.Load object at 0x1067e70d0"]
  node_144["ast.Load object at 0x1067e70d0"]
  node_145["ast.Call object at 0x106933fa0"]
  node_146["ast.Attribute object at 0x106933e50"]
  node_147["ast.Attribute object at 0x106933e80"]
  node_148["ast.Name object at 0x106933ee0"]
  node_149["ast.Load object at 0x1067e70d0"]
  node_150["ast.Load object at 0x1067e70d0"]
  node_151["ast.Load object at 0x1067e70d0"]
  node_152["ast.Name object at 0x106933d00"]
  node_153["ast.Load object at 0x1067e70d0"]
  node_154["ast.Expr object at 0x106933e20"]
  node_155["ast.Call object at 0x106933eb0"]
  node_156["ast.Attribute object at 0x106933f70"]
  node_157["ast.Name object at 0x106933f10"]
  node_158["ast.Load object at 0x1067e70d0"]
  node_159["ast.Load object at 0x1067e70d0"]
  node_160["ast.Call object at 0x106933fd0"]
  node_161["ast.Attribute object at 0x106933f40"]
  node_162["ast.Attribute object at 0x106933a00"]
  node_163["ast.Name object at 0x106933a90"]
  node_164["ast.Load object at 0x1067e70d0"]
  node_165["ast.Load object at 0x1067e70d0"]
  node_166["ast.Load object at 0x1067e70d0"]
  node_167["ast.Name object at 0x106933b50"]
  node_168["ast.Load object at 0x1067e70d0"]
  node_169["ast.With object at 0x1069339a0"]
  node_170["ast.withitem object at 0x1069333d0"]
  node_171["ast.Call object at 0x106933940"]
  node_172["ast.Name object at 0x106933910"]
  node_173["ast.Load object at 0x1067e70d0"]
  node_174["ast.Name object at 0x106933550"]
  node_175["ast.Load object at 0x1067e70d0"]
  node_176["ast.Constant object at 0x1069334c0"]
  node_177["ast.Name object at 0x106933580"]
  node_178["ast.Store object at 0x1067e7070"]
  node_179["ast.Expr object at 0x106933040"]
  node_180["ast.Call object at 0x106933520"]
  node_181["ast.Attribute object at 0x1068c7880"]
  node_182["ast.Name object at 0x1068c78e0"]
  node_183["ast.Load object at 0x1067e70d0"]
  node_184["ast.Load object at 0x1067e70d0"]
  node_185["ast.Name object at 0x1068c78b0"]
  node_186["ast.Load object at 0x1067e70d0"]

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
  node_143 --> node_144
  node_144 --> node_145
  node_145 --> node_146
  node_146 --> node_147
  node_147 --> node_148
  node_148 --> node_149
  node_149 --> node_150
  node_150 --> node_151
  node_151 --> node_152
  node_152 --> node_153
  node_153 --> node_154
  node_154 --> node_155
  node_155 --> node_156
  node_156 --> node_157
  node_157 --> node_158
  node_158 --> node_159
  node_159 --> node_160
  node_160 --> node_161
  node_161 --> node_162
  node_162 --> node_163
  node_163 --> node_164
  node_164 --> node_165
  node_165 --> node_166
  node_166 --> node_167
  node_167 --> node_168
  node_168 --> node_169
  node_169 --> node_170
  node_170 --> node_171
  node_171 --> node_172
  node_172 --> node_173
  node_173 --> node_174
  node_174 --> node_175
  node_175 --> node_176
  node_176 --> node_177
  node_177 --> node_178
  node_178 --> node_179
  node_179 --> node_180
  node_180 --> node_181
  node_181 --> node_182
  node_182 --> node_183
  node_183 --> node_184
  node_184 --> node_185
  node_185 --> node_186

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

