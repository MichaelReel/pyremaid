# ./src/pyremaid/pyremaid.py

### Imports

  - files.destination.create_cleared_output_folder
  - files.destination.get_output_file_path_for_input_file
  - files.destination.update_output_file
  - files.source.find_all_python_files
  - files.source.get_source_code_from_file
  - files.source.get_import_name_from_path
  - ast_tools.create_links_from_ast_model
  - ast_tools.get_ast_root_node_for_file
  - ast_tools.get_markdown_dump_for_ast_node
  - ast_tools.get_used_import_list
  - ast_tools.import_map.get_all_imports_from_files
  - markdown_tools.create_markdown_content
  - mermaid_tools.create_mermaid_flow_graph_from_links
  - models.MermaidLink

---
```mermaid
flowchart TB
    node_37["ast.Expr object at 0x101776b80"]
    node_125["ast.Load object at 0x1016730d0"]
    node_43["ast.Constant object at 0x101776a90"]
    node_50["ast.Constant object at 0x1017769a0"]
    node_101["ast.List object at 0x1017701f0"]
    node_85["ast.Call object at 0x1017702e0"]
    node_15["ast.Load object at 0x1016730d0"]
    node_103["ast.If object at 0x1017701c0"]
    node_146["ast.Store object at 0x101673070"]
    node_144["ast.AnnAssign object at 0x101770ac0"]
    node_211["ast.Expr object at 0x10176c070"]
    node_133["ast.Name object at 0x1017705e0"]
    node_66["ast.For object at 0x101776310"]
    node_107["ast.Call object at 0x101770190"]
    node_68["ast.Store object at 0x101673070"]
    node_181["ast.Name object at 0x10176cc40"]
    node_69["ast.Name object at 0x10176f0a0"]
    node_167["ast.Assign object at 0x10176cb50"]
    node_177["ast.Name object at 0x10176cb20"]
    node_110["ast.keyword object at 0x101770340"]
    node_138["ast.Call object at 0x101770af0"]
    node_145["ast.Name object at 0x101770a60"]
    node_212["ast.Call object at 0x10176c0a0"]
    node_203["ast.Assign object at 0x10176c4c0"]
    node_56["ast.Name object at 0x101776880"]
    node_84["ast.Store object at 0x101673070"]
    node_26["ast.Name object at 0x101776cd0"]
    node_29["ast.Name object at 0x101776c70"]
    node_60["ast.Store object at 0x101673070"]
    node_169["ast.Store object at 0x101673070"]
    node_191["ast.keyword object at 0x10176cbe0"]
    node_71["ast.Assign object at 0x10176f820"]
    node_159["ast.Assign object at 0x10176c910"]
    node_7["ast.Name object at 0x101776fa0"]
    node_62["ast.Attribute object at 0x1017767c0"]
    node_193["ast.Load object at 0x1016730d0"]
    node_51["ast.FormattedValue object at 0x101776970"]
    node_38["ast.Call object at 0x101776b50"]
    node_122["ast.Load object at 0x1016730d0"]
    node_190["ast.Load object at 0x1016730d0"]
    node_100["ast.Store object at 0x101673070"]
    node_105["ast.Name object at 0x101770130"]
    node_89["ast.Name object at 0x1017706d0"]
    node_32["ast.Name object at 0x101776c10"]
    node_188["ast.Call object at 0x10176c220"]
    node_127["ast.Name object at 0x101770220"]
    node_72["ast.Name object at 0x10176f7c0"]
    node_106["ast.Store object at 0x101673070"]
    node_115["ast.Name object at 0x1017704c0"]
    node_174["ast.Name object at 0x10176c520"]
    node_172["ast.Load object at 0x1016730d0"]
    node_1["ast.FunctionDef object at 0x101778910"]
    node_52["ast.Name object at 0x101776940"]
    node_154["ast.Name object at 0x10174a9d0"]
    node_217["ast.Load object at 0x1016730d0"]
    node_207["ast.Assign object at 0x10176c1f0"]
    node_149["ast.Load object at 0x1016730d0"]
    node_112["ast.Load object at 0x1016730d0"]
    node_176["ast.keyword object at 0x10176c760"]
    node_91["ast.keyword object at 0x1017706a0"]
    node_141["ast.keyword object at 0x101770bb0"]
    node_87["ast.Load object at 0x1016730d0"]
    node_118["ast.Name object at 0x101770370"]
    node_117["ast.Call object at 0x101770460"]
    node_0["ast.Module object at 0x101778fd0"]
    node_3["ast.arg object at 0x1017788b0"]
    node_157["ast.Name object at 0x10174a5e0"]
    node_171["ast.Name object at 0x10176caf0"]
    node_104["ast.NamedExpr object at 0x101770430"]
    node_102["ast.Load object at 0x1016730d0"]
    node_113["ast.If object at 0x101770280"]
    node_76["ast.Name object at 0x101770df0"]
    node_57["ast.Store object at 0x101673070"]
    node_55["ast.Tuple object at 0x1017768b0"]
    node_186["ast.Load object at 0x1016730d0"]
    node_150["ast.Name object at 0x10174a130"]
    node_194["ast.keyword object at 0x10176c250"]
    node_61["ast.Call object at 0x1017767f0"]
    node_22["ast.keyword object at 0x101776d60"]
    node_86["ast.Name object at 0x101770e20"]
    node_126["ast.Assign object at 0x101770c10"]
    node_10["ast.Call object at 0x101776f10"]
    node_81["ast.Constant object at 0x101770dc0"]
    node_168["ast.Name object at 0x10176ca90"]
    node_189["ast.Name object at 0x10176c3a0"]
    node_97["ast.Constant object at 0x101770250"]
    node_8["ast.Load object at 0x1016730d0"]
    node_17["ast.Name object at 0x101776df0"]
    node_121["ast.Name object at 0x1017703d0"]
    node_198["ast.Compare object at 0x10176c2b0"]
    node_116["ast.Store object at 0x101673070"]
    node_201["ast.Eq object at 0x101673e50"]
    node_139["ast.Name object at 0x101770be0"]
    node_23["ast.Name object at 0x101776d30"]
    node_82["ast.Assign object at 0x101770c40"]
    node_11["ast.Name object at 0x101776ee0"]
    node_162["ast.Call object at 0x10176c9a0"]
    node_114["ast.NamedExpr object at 0x101770b80"]
    node_33["ast.Load object at 0x1016730d0"]
    node_36["ast.Load object at 0x1016730d0"]
    node_5["ast.Load object at 0x1016730d0"]
    node_58["ast.Name object at 0x101776850"]
    node_64["ast.Load object at 0x1016730d0"]
    node_99["ast.Name object at 0x101770160"]
    node_173["ast.keyword object at 0x10176c6d0"]
    node_213["ast.Name object at 0x10176cee0"]
    node_90["ast.Load object at 0x1016730d0"]
    node_215["ast.keyword object at 0x10176c460"]
    node_134["ast.Load object at 0x1016730d0"]
    node_140["ast.Load object at 0x1016730d0"]
    node_14["ast.Name object at 0x101776e80"]
    node_136["ast.Name object at 0x101770b50"]
    node_54["ast.comprehension object at 0x1017768e0"]
    node_2["ast.arguments object at 0x1017788e0"]
    node_30["ast.Load object at 0x1016730d0"]
    node_199["ast.Name object at 0x10176c490"]
    node_160["ast.Name object at 0x10176cb80"]
    node_70["ast.Load object at 0x1016730d0"]
    node_219["ast.Name object at 0x10176c670"]
    node_119["ast.Load object at 0x1016730d0"]
    node_164["ast.Load object at 0x1016730d0"]
    node_216["ast.Name object at 0x10176c5b0"]
    node_20["ast.Name object at 0x101776d90"]
    node_155["ast.Load object at 0x1016730d0"]
    node_25["ast.Assign object at 0x101776d00"]
    node_42["ast.Attribute object at 0x101776ac0"]
    node_180["ast.List object at 0x10176c700"]
    node_205["ast.Store object at 0x101673070"]
    node_59["ast.Store object at 0x101673070"]
    node_18["ast.Store object at 0x101673070"]
    node_151["ast.Load object at 0x1016730d0"]
    node_80["ast.Load object at 0x1016730d0"]
    node_161["ast.Store object at 0x101673070"]
    node_142["ast.Name object at 0x101770a30"]
    node_200["ast.Load object at 0x1016730d0"]
    node_65["ast.Load object at 0x1016730d0"]
    node_95["ast.Name object at 0x101770100"]
    node_208["ast.Name object at 0x10176c0d0"]
    node_67["ast.Name object at 0x101776220"]
    node_195["ast.Name object at 0x10176c5e0"]
    node_108["ast.Name object at 0x101770310"]
    node_202["ast.Constant object at 0x10176c610"]
    node_129["ast.Call object at 0x101770400"]
    node_4["ast.Name object at 0x101778880"]
    node_96["ast.Store object at 0x101673070"]
    node_34["ast.keyword object at 0x101776be0"]
    node_28["ast.Call object at 0x101776ca0"]
    node_143["ast.Load object at 0x1016730d0"]
    node_16["ast.Assign object at 0x101776e20"]
    node_41["ast.Call object at 0x101776af0"]
    node_94["ast.Assign object at 0x101770cd0"]
    node_179["ast.keyword object at 0x10176c730"]
    node_13["ast.keyword object at 0x101776eb0"]
    node_77["ast.Load object at 0x1016730d0"]
    node_152["ast.Load object at 0x1016730d0"]
    node_184["ast.keyword object at 0x10176cc70"]
    node_158["ast.Load object at 0x1016730d0"]
    node_49["ast.Load object at 0x1016730d0"]
    node_183["ast.Load object at 0x1016730d0"]
    node_73["ast.Store object at 0x101673070"]
    node_45["ast.ListComp object at 0x101776a60"]
    node_156["ast.keyword object at 0x10174aac0"]
    node_46["ast.JoinedStr object at 0x101776a30"]
    node_206["ast.Constant object at 0x10176c340"]
    node_9["ast.Expr object at 0x101776f40"]
    node_137["ast.Store object at 0x101673070"]
    node_214["ast.Load object at 0x1016730d0"]
    node_48["ast.Name object at 0x1017769d0"]
    node_12["ast.Load object at 0x1016730d0"]
    node_79["ast.Name object at 0x101770fa0"]
    node_19["ast.Call object at 0x101776dc0"]
    node_192["ast.Name object at 0x10176cfa0"]
    node_185["ast.Name object at 0x10176cac0"]
    node_131["ast.Load object at 0x1016730d0"]
    node_132["ast.keyword object at 0x101770d00"]
    node_196["ast.Load object at 0x1016730d0"]
    node_165["ast.Name object at 0x10176ca60"]
    node_24["ast.Load object at 0x1016730d0"]
    node_147["ast.Subscript object at 0x10174a490"]
    node_124["ast.Name object at 0x101770610"]
    node_153["ast.Call object at 0x10174af70"]
    node_170["ast.Call object at 0x10176c640"]
    node_218["ast.keyword object at 0x10176ceb0"]
    node_74["ast.Call object at 0x10176f0d0"]
    node_6["ast.arg object at 0x101776fd0"]
    node_35["ast.Name object at 0x101776bb0"]
    node_40["ast.Load object at 0x1016730d0"]
    node_187["ast.Expr object at 0x10176cc10"]
    node_44["ast.Load object at 0x1016730d0"]
    node_39["ast.Name object at 0x101776b20"]
    node_166["ast.Load object at 0x1016730d0"]
    node_197["ast.If object at 0x10176c850"]
    node_135["ast.Assign object at 0x1017705b0"]
    node_63["ast.Name object at 0x101776370"]
    node_88["ast.keyword object at 0x101770c70"]
    node_111["ast.Name object at 0x1017703a0"]
    node_210["ast.Constant object at 0x10176c160"]
    node_93["ast.Load object at 0x1016730d0"]
    node_128["ast.Store object at 0x101673070"]
    node_98["ast.Assign object at 0x101770640"]
    node_78["ast.Load object at 0x1016730d0"]
    node_120["ast.keyword object at 0x1017702b0"]
    node_83["ast.Name object at 0x101770670"]
    node_182["ast.Load object at 0x1016730d0"]
    node_209["ast.Store object at 0x101673070"]
    node_178["ast.Load object at 0x1016730d0"]
    node_220["ast.Load object at 0x1016730d0"]
    node_92["ast.Name object at 0x101770ca0"]
    node_47["ast.FormattedValue object at 0x101776a00"]
    node_123["ast.keyword object at 0x101770490"]
    node_21["ast.Load object at 0x1016730d0"]
    node_27["ast.Store object at 0x101673070"]
    node_130["ast.Name object at 0x101770a90"]
    node_31["ast.keyword object at 0x101776c40"]
    node_53["ast.Load object at 0x1016730d0"]
    node_204["ast.Name object at 0x10176c550"]
    node_175["ast.Load object at 0x1016730d0"]
    node_163["ast.Name object at 0x10176ca30"]
    node_148["ast.Name object at 0x10174adc0"]
    node_75["ast.Attribute object at 0x10176f790"]
    node_109["ast.Load object at 0x1016730d0"]

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
    node_186 --> node_187
    node_187 --> node_188
    node_188 --> node_189
    node_189 --> node_190
    node_190 --> node_191
    node_191 --> node_192
    node_192 --> node_193
    node_193 --> node_194
    node_194 --> node_195
    node_195 --> node_196
    node_196 --> node_197
    node_197 --> node_198
    node_198 --> node_199
    node_199 --> node_200
    node_200 --> node_201
    node_201 --> node_202
    node_202 --> node_203
    node_203 --> node_204
    node_204 --> node_205
    node_205 --> node_206
    node_206 --> node_207
    node_207 --> node_208
    node_208 --> node_209
    node_209 --> node_210
    node_210 --> node_211
    node_211 --> node_212
    node_212 --> node_213
    node_213 --> node_214
    node_214 --> node_215
    node_215 --> node_216
    node_216 --> node_217
    node_217 --> node_218
    node_218 --> node_219
    node_219 --> node_220

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='files.destination',
      names=[
        alias(name='create_cleared_output_folder'),
        alias(name='get_output_file_path_for_input_file'),
        alias(name='update_output_file')],
      level=0,
      lineno=3,
      col_offset=0,
      end_lineno=7,
      end_col_offset=1),
    ImportFrom(
      module='files.source',
      names=[
        alias(name='find_all_python_files'),
        alias(name='get_source_code_from_file'),
        alias(name='get_import_name_from_path')],
      level=0,
      lineno=8,
      col_offset=0,
      end_lineno=8,
      end_col_offset=100),
    ImportFrom(
      module='ast_tools',
      names=[
        alias(name='create_links_from_ast_model'),
        alias(name='get_ast_root_node_for_file'),
        alias(name='get_markdown_dump_for_ast_node'),
        alias(name='get_used_import_list')],
      level=0,
      lineno=9,
      col_offset=0,
      end_lineno=14,
      end_col_offset=1),
    ImportFrom(
      module='ast_tools.import_map',
      names=[
        alias(name='get_all_imports_from_files')],
      level=0,
      lineno=15,
      col_offset=0,
      end_lineno=15,
      end_col_offset=59),
    ImportFrom(
      module='markdown_tools',
      names=[
        alias(name='create_markdown_content')],
      level=0,
      lineno=16,
      col_offset=0,
      end_lineno=16,
      end_col_offset=50),
    ImportFrom(
      module='mermaid_tools',
      names=[
        alias(name='create_mermaid_flow_graph_from_links')],
      level=0,
      lineno=17,
      col_offset=0,
      end_lineno=17,
      end_col_offset=62),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidLink')],
      level=0,
      lineno=18,
      col_offset=0,
      end_lineno=18,
      end_col_offset=30),
    FunctionDef(
      name='create_mermaid_analysis_from_python',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=20,
              col_offset=53,
              end_lineno=20,
              end_col_offset=56),
            lineno=20,
            col_offset=40,
            end_lineno=20,
            end_col_offset=56),
          arg(
            arg='output_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=20,
              col_offset=71,
              end_lineno=20,
              end_col_offset=74),
            lineno=20,
            col_offset=58,
            end_lineno=20,
            end_col_offset=74)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Call(
            func=Name(
              id='create_cleared_output_folder',
              ctx=Load(),
              lineno=21,
              col_offset=4,
              end_lineno=21,
              end_col_offset=32),
            args=[],
            keywords=[
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=21,
                  col_offset=45,
                  end_lineno=21,
                  end_col_offset=56),
                lineno=21,
                col_offset=33,
                end_lineno=21,
                end_col_offset=56)],
            lineno=21,
            col_offset=4,
            end_lineno=21,
            end_col_offset=57),
          lineno=21,
          col_offset=4,
          end_lineno=21,
          end_col_offset=57),
        Assign(
          targets=[
            Name(
              id='python_files',
              ctx=Store(),
              lineno=22,
              col_offset=4,
              end_lineno=22,
              end_col_offset=16)],
          value=Call(
            func=Name(
              id='find_all_python_files',
              ctx=Load(),
              lineno=22,
              col_offset=19,
              end_lineno=22,
              end_col_offset=40),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=22,
                  col_offset=52,
                  end_lineno=22,
                  end_col_offset=62),
                lineno=22,
                col_offset=41,
                end_lineno=22,
                end_col_offset=62)],
            lineno=22,
            col_offset=19,
            end_lineno=22,
            end_col_offset=63),
          lineno=22,
          col_offset=4,
          end_lineno=22,
          end_col_offset=63),
        Assign(
          targets=[
            Name(
              id='global_import_list',
              ctx=Store(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=22)],
          value=Call(
            func=Name(
              id='get_all_imports_from_files',
              ctx=Load(),
              lineno=23,
              col_offset=25,
              end_lineno=23,
              end_col_offset=51),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=24,
                  col_offset=19,
                  end_lineno=24,
                  end_col_offset=29),
                lineno=24,
                col_offset=8,
                end_lineno=24,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=24,
                  col_offset=44,
                  end_lineno=24,
                  end_col_offset=56),
                lineno=24,
                col_offset=31,
                end_lineno=24,
                end_col_offset=56)],
            lineno=23,
            col_offset=25,
            end_lineno=25,
            end_col_offset=5),
          lineno=23,
          col_offset=4,
          end_lineno=25,
          end_col_offset=5),
        Expr(
          value=Call(
            func=Name(
              id='print',
              ctx=Load(),
              lineno=27,
              col_offset=4,
              end_lineno=27,
              end_col_offset=9),
            args=[
              Call(
                func=Attribute(
                  value=Constant(
                    value='\n',
                    lineno=27,
                    col_offset=10,
                    end_lineno=27,
                    end_col_offset=14),
                  attr='join',
                  ctx=Load(),
                  lineno=27,
                  col_offset=10,
                  end_lineno=27,
                  end_col_offset=19),
                args=[
                  ListComp(
                    elt=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Name(
                            id='k',
                            ctx=Load(),
                            lineno=27,
                            col_offset=24,
                            end_lineno=27,
                            end_col_offset=25),
                          conversion=-1,
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32),
                        Constant(
                          value=': ',
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32),
                        FormattedValue(
                          value=Name(
                            id='v',
                            ctx=Load(),
                            lineno=27,
                            col_offset=29,
                            end_lineno=27,
                            end_col_offset=30),
                          conversion=-1,
                          lineno=27,
                          col_offset=21,
                          end_lineno=27,
                          end_col_offset=32)],
                      lineno=27,
                      col_offset=21,
                      end_lineno=27,
                      end_col_offset=32),
                    generators=[
                      comprehension(
                        target=Tuple(
                          elts=[
                            Name(
                              id='k',
                              ctx=Store(),
                              lineno=27,
                              col_offset=37,
                              end_lineno=27,
                              end_col_offset=38),
                            Name(
                              id='v',
                              ctx=Store(),
                              lineno=27,
                              col_offset=39,
                              end_lineno=27,
                              end_col_offset=40)],
                          ctx=Store(),
                          lineno=27,
                          col_offset=37,
                          end_lineno=27,
                          end_col_offset=40),
                        iter=Call(
                          func=Attribute(
                            value=Name(
                              id='global_import_list',
                              ctx=Load(),
                              lineno=27,
                              col_offset=44,
                              end_lineno=27,
                              end_col_offset=62),
                            attr='items',
                            ctx=Load(),
                            lineno=27,
                            col_offset=44,
                            end_lineno=27,
                            end_col_offset=68),
                          args=[],
                          keywords=[],
                          lineno=27,
                          col_offset=44,
                          end_lineno=27,
                          end_col_offset=70),
                        ifs=[],
                        is_async=0)],
                    lineno=27,
                    col_offset=20,
                    end_lineno=27,
                    end_col_offset=71)],
                keywords=[],
                lineno=27,
                col_offset=10,
                end_lineno=27,
                end_col_offset=72)],
            keywords=[],
            lineno=27,
            col_offset=4,
            end_lineno=27,
            end_col_offset=73),
          lineno=27,
          col_offset=4,
          end_lineno=27,
          end_col_offset=73),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=29,
            col_offset=8,
            end_lineno=29,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=29,
            col_offset=19,
            end_lineno=29,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='in_file',
                    ctx=Load(),
                    lineno=30,
                    col_offset=27,
                    end_lineno=30,
                    end_col_offset=34),
                  attr='replace',
                  ctx=Load(),
                  lineno=30,
                  col_offset=27,
                  end_lineno=30,
                  end_col_offset=42),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=30,
                    col_offset=43,
                    end_lineno=30,
                    end_col_offset=53),
                  Constant(
                    value='',
                    lineno=30,
                    col_offset=55,
                    end_lineno=30,
                    end_col_offset=57)],
                keywords=[],
                lineno=30,
                col_offset=27,
                end_lineno=30,
                end_col_offset=58),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=58),
            Assign(
              targets=[
                Name(
                  id='out_file',
                  ctx=Store(),
                  lineno=31,
                  col_offset=8,
                  end_lineno=31,
                  end_col_offset=16)],
              value=Call(
                func=Name(
                  id='get_output_file_path_for_input_file',
                  ctx=Load(),
                  lineno=31,
                  col_offset=19,
                  end_lineno=31,
                  end_col_offset=54),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='relative_in_file',
                      ctx=Load(),
                      lineno=32,
                      col_offset=23,
                      end_lineno=32,
                      end_col_offset=39),
                    lineno=32,
                    col_offset=12,
                    end_lineno=32,
                    end_col_offset=39),
                  keyword(
                    arg='output_root',
                    value=Name(
                      id='output_path',
                      ctx=Load(),
                      lineno=32,
                      col_offset=53,
                      end_lineno=32,
                      end_col_offset=64),
                    lineno=32,
                    col_offset=41,
                    end_lineno=32,
                    end_col_offset=64)],
                lineno=31,
                col_offset=19,
                end_lineno=33,
                end_col_offset=9),
              lineno=31,
              col_offset=8,
              end_lineno=33,
              end_col_offset=9),
            Assign(
              targets=[
                Name(
                  id='debug_dump',
                  ctx=Store(),
                  lineno=35,
                  col_offset=8,
                  end_lineno=35,
                  end_col_offset=18)],
              value=Constant(
                value='',
                lineno=35,
                col_offset=21,
                end_lineno=35,
                end_col_offset=23),
              lineno=35,
              col_offset=8,
              end_lineno=35,
              end_col_offset=23),
            Assign(
              targets=[
                Name(
                  id='import_list',
                  ctx=Store(),
                  lineno=36,
                  col_offset=8,
                  end_lineno=36,
                  end_col_offset=19)],
              value=List(
                elts=[],
                ctx=Load(),
                lineno=36,
                col_offset=22,
                end_lineno=36,
                end_col_offset=24),
              lineno=36,
              col_offset=8,
              end_lineno=36,
              end_col_offset=24),
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=38,
                  col_offset=11,
                  end_lineno=38,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=38,
                    col_offset=26,
                    end_lineno=38,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=38,
                        col_offset=63,
                        end_lineno=38,
                        end_col_offset=70),
                      lineno=38,
                      col_offset=52,
                      end_lineno=38,
                      end_col_offset=70)],
                  lineno=38,
                  col_offset=26,
                  end_lineno=38,
                  end_col_offset=71),
                lineno=38,
                col_offset=11,
                end_lineno=38,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=39,
                      col_offset=15,
                      end_lineno=39,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=39,
                        col_offset=27,
                        end_lineno=39,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=40,
                            col_offset=28,
                            end_lineno=40,
                            end_col_offset=39),
                          lineno=40,
                          col_offset=16,
                          end_lineno=40,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=41,
                            col_offset=27,
                            end_lineno=41,
                            end_col_offset=34),
                          lineno=41,
                          col_offset=16,
                          end_lineno=41,
                          end_col_offset=34)],
                      lineno=39,
                      col_offset=27,
                      end_lineno=42,
                      end_col_offset=13),
                    lineno=39,
                    col_offset=15,
                    end_lineno=42,
                    end_col_offset=13),
                  body=[
                    Assign(
                      targets=[
                        Name(
                          id='debug_dump',
                          ctx=Store(),
                          lineno=44,
                          col_offset=16,
                          end_lineno=44,
                          end_col_offset=26)],
                      value=Call(
                        func=Name(
                          id='get_markdown_dump_for_ast_node',
                          ctx=Load(),
                          lineno=44,
                          col_offset=29,
                          end_lineno=44,
                          end_col_offset=59),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=44,
                              col_offset=69,
                              end_lineno=44,
                              end_col_offset=77),
                            lineno=44,
                            col_offset=60,
                            end_lineno=44,
                            end_col_offset=77)],
                        lineno=44,
                        col_offset=29,
                        end_lineno=44,
                        end_col_offset=78),
                      lineno=44,
                      col_offset=16,
                      end_lineno=44,
                      end_col_offset=78),
                    Assign(
                      targets=[
                        Name(
                          id='import_list',
                          ctx=Store(),
                          lineno=46,
                          col_offset=16,
                          end_lineno=46,
                          end_col_offset=27)],
                      value=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=46,
                          col_offset=30,
                          end_lineno=46,
                          end_col_offset=50),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=46,
                              col_offset=60,
                              end_lineno=46,
                              end_col_offset=68),
                            lineno=46,
                            col_offset=51,
                            end_lineno=46,
                            end_col_offset=68)],
                        lineno=46,
                        col_offset=30,
                        end_lineno=46,
                        end_col_offset=69),
                      lineno=46,
                      col_offset=16,
                      end_lineno=46,
                      end_col_offset=69),
                    AnnAssign(
                      target=Name(
                        id='link_info',
                        ctx=Store(),
                        lineno=48,
                        col_offset=16,
                        end_lineno=48,
                        end_col_offset=25),
                      annotation=Subscript(
                        value=Name(
                          id='list',
                          ctx=Load(),
                          lineno=48,
                          col_offset=28,
                          end_lineno=48,
                          end_col_offset=32),
                        slice=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=48,
                          col_offset=33,
                          end_lineno=48,
                          end_col_offset=44),
                        ctx=Load(),
                        lineno=48,
                        col_offset=28,
                        end_lineno=48,
                        end_col_offset=45),
                      value=Call(
                        func=Name(
                          id='create_links_from_ast_model',
                          ctx=Load(),
                          lineno=48,
                          col_offset=48,
                          end_lineno=48,
                          end_col_offset=75),
                        args=[],
                        keywords=[
                          keyword(
                            arg='model',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=48,
                              col_offset=82,
                              end_lineno=48,
                              end_col_offset=90),
                            lineno=48,
                            col_offset=76,
                            end_lineno=48,
                            end_col_offset=90)],
                        lineno=48,
                        col_offset=48,
                        end_lineno=48,
                        end_col_offset=91),
                      simple=1,
                      lineno=48,
                      col_offset=16,
                      end_lineno=48,
                      end_col_offset=91),
                    Assign(
                      targets=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Store(),
                          lineno=50,
                          col_offset=16,
                          end_lineno=50,
                          end_col_offset=31)],
                      value=Call(
                        func=Name(
                          id='create_mermaid_flow_graph_from_links',
                          ctx=Load(),
                          lineno=50,
                          col_offset=34,
                          end_lineno=50,
                          end_col_offset=70),
                        args=[
                          Name(
                            id='link_info',
                            ctx=Load(),
                            lineno=50,
                            col_offset=71,
                            end_lineno=50,
                            end_col_offset=80)],
                        keywords=[],
                        lineno=50,
                        col_offset=34,
                        end_lineno=50,
                        end_col_offset=81),
                      lineno=50,
                      col_offset=16,
                      end_lineno=50,
                      end_col_offset=81)],
                  orelse=[],
                  lineno=39,
                  col_offset=12,
                  end_lineno=50,
                  end_col_offset=81)],
              orelse=[],
              lineno=38,
              col_offset=8,
              end_lineno=50,
              end_col_offset=81),
            Assign(
              targets=[
                Name(
                  id='markdown_content',
                  ctx=Store(),
                  lineno=52,
                  col_offset=8,
                  end_lineno=52,
                  end_col_offset=24)],
              value=Call(
                func=Name(
                  id='create_markdown_content',
                  ctx=Load(),
                  lineno=52,
                  col_offset=27,
                  end_lineno=52,
                  end_col_offset=50),
                args=[],
                keywords=[
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=53,
                      col_offset=23,
                      end_lineno=53,
                      end_col_offset=30),
                    lineno=53,
                    col_offset=12,
                    end_lineno=53,
                    end_col_offset=30),
                  keyword(
                    arg='import_list',
                    value=Name(
                      id='import_list',
                      ctx=Load(),
                      lineno=54,
                      col_offset=24,
                      end_lineno=54,
                      end_col_offset=35),
                    lineno=54,
                    col_offset=12,
                    end_lineno=54,
                    end_col_offset=35),
                  keyword(
                    arg='mermaid_diagrams',
                    value=List(
                      elts=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Load(),
                          lineno=55,
                          col_offset=30,
                          end_lineno=55,
                          end_col_offset=45)],
                      ctx=Load(),
                      lineno=55,
                      col_offset=29,
                      end_lineno=55,
                      end_col_offset=46),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=46),
                  keyword(
                    arg='debug_dump',
                    value=Name(
                      id='debug_dump',
                      ctx=Load(),
                      lineno=56,
                      col_offset=23,
                      end_lineno=56,
                      end_col_offset=33),
                    lineno=56,
                    col_offset=12,
                    end_lineno=56,
                    end_col_offset=33)],
                lineno=52,
                col_offset=27,
                end_lineno=57,
                end_col_offset=9),
              lineno=52,
              col_offset=8,
              end_lineno=57,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Name(
                  id='update_output_file',
                  ctx=Load(),
                  lineno=59,
                  col_offset=8,
                  end_lineno=59,
                  end_col_offset=26),
                args=[],
                keywords=[
                  keyword(
                    arg='content',
                    value=Name(
                      id='markdown_content',
                      ctx=Load(),
                      lineno=59,
                      col_offset=35,
                      end_lineno=59,
                      end_col_offset=51),
                    lineno=59,
                    col_offset=27,
                    end_lineno=59,
                    end_col_offset=51),
                  keyword(
                    arg='output_file',
                    value=Name(
                      id='out_file',
                      ctx=Load(),
                      lineno=59,
                      col_offset=65,
                      end_lineno=59,
                      end_col_offset=73),
                    lineno=59,
                    col_offset=53,
                    end_lineno=59,
                    end_col_offset=73)],
                lineno=59,
                col_offset=8,
                end_lineno=59,
                end_col_offset=74),
              lineno=59,
              col_offset=8,
              end_lineno=59,
              end_col_offset=74)],
          orelse=[],
          lineno=29,
          col_offset=4,
          end_lineno=59,
          end_col_offset=74)],
      decorator_list=[],
      lineno=20,
      col_offset=0,
      end_lineno=59,
      end_col_offset=74),
    If(
      test=Compare(
        left=Name(
          id='__name__',
          ctx=Load(),
          lineno=62,
          col_offset=3,
          end_lineno=62,
          end_col_offset=11),
        ops=[
          Eq()],
        comparators=[
          Constant(
            value='__main__',
            lineno=62,
            col_offset=15,
            end_lineno=62,
            end_col_offset=25)],
        lineno=62,
        col_offset=3,
        end_lineno=62,
        end_col_offset=25),
      body=[
        Assign(
          targets=[
            Name(
              id='input_path',
              ctx=Store(),
              lineno=65,
              col_offset=4,
              end_lineno=65,
              end_col_offset=14)],
          value=Constant(
            value='./src/pyremaid/',
            lineno=65,
            col_offset=17,
            end_lineno=65,
            end_col_offset=34),
          lineno=65,
          col_offset=4,
          end_lineno=65,
          end_col_offset=34),
        Assign(
          targets=[
            Name(
              id='output_path',
              ctx=Store(),
              lineno=66,
              col_offset=4,
              end_lineno=66,
              end_col_offset=15)],
          value=Constant(
            value='./docs/pyremaid/',
            lineno=66,
            col_offset=18,
            end_lineno=66,
            end_col_offset=36),
          lineno=66,
          col_offset=4,
          end_lineno=66,
          end_col_offset=36),
        Expr(
          value=Call(
            func=Name(
              id='create_mermaid_analysis_from_python',
              ctx=Load(),
              lineno=67,
              col_offset=4,
              end_lineno=67,
              end_col_offset=39),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=67,
                  col_offset=51,
                  end_lineno=67,
                  end_col_offset=61),
                lineno=67,
                col_offset=40,
                end_lineno=67,
                end_col_offset=61),
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=67,
                  col_offset=75,
                  end_lineno=67,
                  end_col_offset=86),
                lineno=67,
                col_offset=63,
                end_lineno=67,
                end_col_offset=86)],
            lineno=67,
            col_offset=4,
            end_lineno=67,
            end_col_offset=87),
          lineno=67,
          col_offset=4,
          end_lineno=67,
          end_col_offset=87)],
      orelse=[],
      lineno=62,
      col_offset=0,
      end_lineno=67,
      end_col_offset=87)],
  type_ignores=[])
```
</details>

