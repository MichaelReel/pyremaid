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
    node_0["ast.Module object at 0x10615efd0"]
    node_1["ast.FunctionDef object at 0x10615e910"]
    node_2["ast.arguments object at 0x10615e8e0"]
    node_3["ast.arg object at 0x10615e8b0"]
    node_4["ast.Name object at 0x10615e880"]
    node_5["ast.Load object at 0x1060500d0"]
    node_6["ast.arg object at 0x10615e850"]
    node_7["ast.Name object at 0x10615e820"]
    node_8["ast.Load object at 0x1060500d0"]
    node_9["ast.Expr object at 0x10615e7c0"]
    node_10["ast.Call object at 0x10615e790"]
    node_11["ast.Name object at 0x10615e760"]
    node_12["ast.Load object at 0x1060500d0"]
    node_13["ast.keyword object at 0x10615e730"]
    node_14["ast.Name object at 0x10615e700"]
    node_15["ast.Load object at 0x1060500d0"]
    node_16["ast.Assign object at 0x10615e6a0"]
    node_17["ast.Name object at 0x10615e670"]
    node_18["ast.Store object at 0x106050070"]
    node_19["ast.Call object at 0x10615e640"]
    node_20["ast.Name object at 0x10615e610"]
    node_21["ast.Load object at 0x1060500d0"]
    node_22["ast.keyword object at 0x10615e5e0"]
    node_23["ast.Name object at 0x10615e5b0"]
    node_24["ast.Load object at 0x1060500d0"]
    node_25["ast.Assign object at 0x10615e580"]
    node_26["ast.Name object at 0x10615e550"]
    node_27["ast.Store object at 0x106050070"]
    node_28["ast.Call object at 0x10615e460"]
    node_29["ast.Name object at 0x10615caf0"]
    node_30["ast.Load object at 0x1060500d0"]
    node_31["ast.keyword object at 0x1061528b0"]
    node_32["ast.Name object at 0x10614f460"]
    node_33["ast.Load object at 0x1060500d0"]
    node_34["ast.keyword object at 0x10614f430"]
    node_35["ast.Name object at 0x10614f310"]
    node_36["ast.Load object at 0x1060500d0"]
    node_37["ast.Expr object at 0x10614f2e0"]
    node_38["ast.Call object at 0x10614f370"]
    node_39["ast.Name object at 0x10614f340"]
    node_40["ast.Load object at 0x1060500d0"]
    node_41["ast.Call object at 0x10614f220"]
    node_42["ast.Attribute object at 0x10614f280"]
    node_43["ast.Constant object at 0x10614f250"]
    node_44["ast.Load object at 0x1060500d0"]
    node_45["ast.ListComp object at 0x10614f190"]
    node_46["ast.JoinedStr object at 0x10614f0a0"]
    node_47["ast.FormattedValue object at 0x10614f1f0"]
    node_48["ast.Name object at 0x10614f1c0"]
    node_49["ast.Load object at 0x1060500d0"]
    node_50["ast.Constant object at 0x10614f100"]
    node_51["ast.FormattedValue object at 0x10614f0d0"]
    node_52["ast.Name object at 0x10614f160"]
    node_53["ast.Load object at 0x1060500d0"]
    node_54["ast.comprehension object at 0x10614f070"]
    node_55["ast.Tuple object at 0x10614f040"]
    node_56["ast.Name object at 0x10613e4f0"]
    node_57["ast.Store object at 0x106050070"]
    node_58["ast.Name object at 0x10613ec10"]
    node_59["ast.Store object at 0x106050070"]
    node_60["ast.Store object at 0x106050070"]
    node_61["ast.Call object at 0x10613e880"]
    node_62["ast.Attribute object at 0x10613ea00"]
    node_63["ast.Name object at 0x10613e040"]
    node_64["ast.Load object at 0x1060500d0"]
    node_65["ast.Load object at 0x1060500d0"]
    node_66["ast.For object at 0x10613e100"]
    node_67["ast.Name object at 0x10613e580"]
    node_68["ast.Store object at 0x106050070"]
    node_69["ast.Name object at 0x10613eb50"]
    node_70["ast.Load object at 0x1060500d0"]
    node_71["ast.Assign object at 0x10613ebb0"]
    node_72["ast.Name object at 0x10613e640"]
    node_73["ast.Store object at 0x106050070"]
    node_74["ast.Call object at 0x10613e490"]
    node_75["ast.Attribute object at 0x10613e790"]
    node_76["ast.Name object at 0x10613e7f0"]
    node_77["ast.Load object at 0x1060500d0"]
    node_78["ast.Load object at 0x1060500d0"]
    node_79["ast.Name object at 0x10613e1c0"]
    node_80["ast.Load object at 0x1060500d0"]
    node_81["ast.Constant object at 0x10613e610"]
    node_82["ast.Assign object at 0x10613e700"]
    node_83["ast.Name object at 0x10613e220"]
    node_84["ast.Store object at 0x106050070"]
    node_85["ast.Call object at 0x10613e190"]
    node_86["ast.Name object at 0x10613efa0"]
    node_87["ast.Load object at 0x1060500d0"]
    node_88["ast.keyword object at 0x10613e070"]
    node_89["ast.Name object at 0x10613e0a0"]
    node_90["ast.Load object at 0x1060500d0"]
    node_91["ast.keyword object at 0x10613eb80"]
    node_92["ast.Name object at 0x10613ec40"]
    node_93["ast.Load object at 0x1060500d0"]
    node_94["ast.Assign object at 0x10613ea60"]
    node_95["ast.Name object at 0x10613ef70"]
    node_96["ast.Store object at 0x106050070"]
    node_97["ast.Constant object at 0x10613e3d0"]
    node_98["ast.Assign object at 0x10613e250"]
    node_99["ast.Name object at 0x10613e1f0"]
    node_100["ast.Store object at 0x106050070"]
    node_101["ast.List object at 0x10613e7c0"]
    node_102["ast.Load object at 0x1060500d0"]
    node_103["ast.If object at 0x10613e370"]
    node_104["ast.NamedExpr object at 0x10613e5e0"]
    node_105["ast.Name object at 0x10613e340"]
    node_106["ast.Store object at 0x106050070"]
    node_107["ast.Call object at 0x10613e6d0"]
    node_108["ast.Name object at 0x10613e430"]
    node_109["ast.Load object at 0x1060500d0"]
    node_110["ast.keyword object at 0x10613e2e0"]
    node_111["ast.Name object at 0x10613e5b0"]
    node_112["ast.Load object at 0x1060500d0"]
    node_113["ast.If object at 0x10613e820"]
    node_114["ast.NamedExpr object at 0x10613e9d0"]
    node_115["ast.Name object at 0x10613ea90"]
    node_116["ast.Store object at 0x106050070"]
    node_117["ast.Call object at 0x10613e520"]
    node_118["ast.Name object at 0x10613ebe0"]
    node_119["ast.Load object at 0x1060500d0"]
    node_120["ast.keyword object at 0x10613e940"]
    node_121["ast.Name object at 0x10613ed00"]
    node_122["ast.Load object at 0x1060500d0"]
    node_123["ast.keyword object at 0x10613e910"]
    node_124["ast.Name object at 0x10613e8e0"]
    node_125["ast.Load object at 0x1060500d0"]
    node_126["ast.Assign object at 0x10613e6a0"]
    node_127["ast.Name object at 0x10613e970"]
    node_128["ast.Store object at 0x106050070"]
    node_129["ast.Call object at 0x10613e4c0"]
    node_130["ast.Name object at 0x10613e9a0"]
    node_131["ast.Load object at 0x1060500d0"]
    node_132["ast.keyword object at 0x10613e130"]
    node_133["ast.Name object at 0x10613e460"]
    node_134["ast.Load object at 0x1060500d0"]
    node_135["ast.Assign object at 0x10613eac0"]
    node_136["ast.Name object at 0x10613efd0"]
    node_137["ast.Store object at 0x106050070"]
    node_138["ast.Call object at 0x10613eaf0"]
    node_139["ast.Name object at 0x10613e850"]
    node_140["ast.Load object at 0x1060500d0"]
    node_141["ast.keyword object at 0x10613e3a0"]
    node_142["ast.Name object at 0x10613e550"]
    node_143["ast.Load object at 0x1060500d0"]
    node_144["ast.AnnAssign object at 0x10613e670"]
    node_145["ast.Name object at 0x10613e2b0"]
    node_146["ast.Store object at 0x106050070"]
    node_147["ast.Subscript object at 0x10613e400"]
    node_148["ast.Name object at 0x10613ea30"]
    node_149["ast.Load object at 0x1060500d0"]
    node_150["ast.Name object at 0x10613e280"]
    node_151["ast.Load object at 0x1060500d0"]
    node_152["ast.Load object at 0x1060500d0"]
    node_153["ast.Call object at 0x10613e730"]
    node_154["ast.Name object at 0x10613eb20"]
    node_155["ast.Load object at 0x1060500d0"]
    node_156["ast.keyword object at 0x1061140a0"]
    node_157["ast.Name object at 0x106114be0"]
    node_158["ast.Load object at 0x1060500d0"]
    node_159["ast.Assign object at 0x106114460"]
    node_160["ast.Name object at 0x106114040"]
    node_161["ast.Store object at 0x106050070"]
    node_162["ast.Call object at 0x106114880"]
    node_163["ast.Name object at 0x106114940"]
    node_164["ast.Load object at 0x1060500d0"]
    node_165["ast.Name object at 0x10604de80"]
    node_166["ast.Load object at 0x1060500d0"]
    node_167["ast.Assign object at 0x10604de20"]
    node_168["ast.Name object at 0x10604dfd0"]
    node_169["ast.Store object at 0x106050070"]
    node_170["ast.Call object at 0x10604df70"]
    node_171["ast.Name object at 0x10604dfa0"]
    node_172["ast.Load object at 0x1060500d0"]
    node_173["ast.keyword object at 0x1061434f0"]
    node_174["ast.Name object at 0x106143880"]
    node_175["ast.Load object at 0x1060500d0"]
    node_176["ast.keyword object at 0x106143580"]
    node_177["ast.Name object at 0x106143640"]
    node_178["ast.Load object at 0x1060500d0"]
    node_179["ast.keyword object at 0x106143c40"]
    node_180["ast.List object at 0x106143400"]
    node_181["ast.Name object at 0x106143e80"]
    node_182["ast.Load object at 0x1060500d0"]
    node_183["ast.Load object at 0x1060500d0"]
    node_184["ast.keyword object at 0x106143730"]
    node_185["ast.Name object at 0x106143790"]
    node_186["ast.Load object at 0x1060500d0"]
    node_187["ast.Expr object at 0x1061434c0"]
    node_188["ast.Call object at 0x106143fd0"]
    node_189["ast.Name object at 0x1061435b0"]
    node_190["ast.Load object at 0x1060500d0"]
    node_191["ast.keyword object at 0x1061437c0"]
    node_192["ast.Name object at 0x106143700"]
    node_193["ast.Load object at 0x1060500d0"]
    node_194["ast.keyword object at 0x1061438b0"]
    node_195["ast.Name object at 0x106143490"]
    node_196["ast.Load object at 0x1060500d0"]
    node_197["ast.If object at 0x106143610"]
    node_198["ast.Compare object at 0x106143f40"]
    node_199["ast.Name object at 0x1061431f0"]
    node_200["ast.Load object at 0x1060500d0"]
    node_201["ast.Eq object at 0x106050e50"]
    node_202["ast.Constant object at 0x106143d00"]
    node_203["ast.Assign object at 0x1061436d0"]
    node_204["ast.Name object at 0x106143e20"]
    node_205["ast.Store object at 0x106050070"]
    node_206["ast.Constant object at 0x106143c70"]
    node_207["ast.Assign object at 0x106143040"]
    node_208["ast.Name object at 0x106143550"]
    node_209["ast.Store object at 0x106050070"]
    node_210["ast.Constant object at 0x106143130"]
    node_211["ast.Expr object at 0x106143af0"]
    node_212["ast.Call object at 0x1061433d0"]
    node_213["ast.Name object at 0x106143bb0"]
    node_214["ast.Load object at 0x1060500d0"]
    node_215["ast.keyword object at 0x106143dc0"]
    node_216["ast.Name object at 0x106143eb0"]
    node_217["ast.Load object at 0x1060500d0"]
    node_218["ast.keyword object at 0x1061430a0"]
    node_219["ast.Name object at 0x106143a90"]
    node_220["ast.Load object at 0x1060500d0"]

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

