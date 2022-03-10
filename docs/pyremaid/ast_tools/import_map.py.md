# ./src/pyremaid/ast_tools/import_map.py

### Imports

  - ast_tools.get_ast_root_node_for_file
  - ast_tools.get_used_import_list
  - files.source.get_source_code_from_file
  - files.source.get_import_name_from_path

---
```mermaid
flowchart TB
    node_42["ast.Load object at 0x1016730d0"]
    node_241["ast.If object at 0x101766cd0"]
    node_295["ast.Name object at 0x101766640"]
    node_237["ast.Load object at 0x1016730d0"]
    node_55["ast.If object at 0x101780250"]
    node_139["ast.Assign object at 0x10176af70"]
    node_185["ast.Name object at 0x10176aa60"]
    node_69["ast.Load object at 0x1016730d0"]
    node_322["ast.Name object at 0x101766100"]
    node_155["ast.Name object at 0x10176ae20"]
    node_267["ast.Assign object at 0x101766970"]
    node_249["ast.Name object at 0x101766bb0"]
    node_127["ast.arg object at 0x1016ba040"]
    node_308["ast.Load object at 0x1016730d0"]
    node_269["ast.Store object at 0x101673070"]
    node_13["ast.Tuple object at 0x1017804f0"]
    node_24["ast.Dict object at 0x1017805e0"]
    node_305["ast.Load object at 0x1016730d0"]
    node_346["ast.Name object at 0x101763c10"]
    node_312["ast.Load object at 0x1016730d0"]
    node_19["ast.Name object at 0x101780610"]
    node_177["ast.Load object at 0x1016730d0"]
    node_314["ast.arguments object at 0x101766220"]
    node_152["ast.Name object at 0x10176adc0"]
    node_243["ast.Name object at 0x101766c70"]
    node_260["ast.keyword object at 0x101766a60"]
    node_118["ast.Load object at 0x1016730d0"]
    node_187["ast.Return object at 0x10176aa30"]
    node_228["ast.Store object at 0x101673070"]
    node_265["ast.Store object at 0x101673070"]
    node_60["ast.Attribute object at 0x101780040"]
    node_154["ast.keyword object at 0x10176ae50"]
    node_186["ast.Load object at 0x1016730d0"]
    node_54["ast.Load object at 0x1016730d0"]
    node_120["ast.Load object at 0x1016730d0"]
    node_229["ast.Name object at 0x101766e50"]
    node_286["ast.Name object at 0x101766730"]
    node_350["ast.Load object at 0x1016730d0"]
    node_73["ast.List object at 0x101769ee0"]
    node_150["ast.Store object at 0x101673070"]
    node_104["ast.Name object at 0x101769b50"]
    node_137["ast.Expr object at 0x10176a9a0"]
    node_224["ast.Store object at 0x101673070"]
    node_6["ast.Attribute object at 0x1017806d0"]
    node_18["ast.Load object at 0x1016730d0"]
    node_135["ast.Load object at 0x1016730d0"]
    node_94["ast.Attribute object at 0x101769c70"]
    node_101["ast.Name object at 0x101769b80"]
    node_1["ast.ClassDef object at 0x101780850"]
    node_2["ast.FunctionDef object at 0x101780820"]
    node_3["ast.arguments object at 0x1017807f0"]
    node_242["ast.NamedExpr object at 0x101766ca0"]
    node_167["ast.Name object at 0x10176acd0"]
    node_143["ast.For object at 0x10176afa0"]
    node_337["ast.Name object at 0x101763eb0"]
    node_148["ast.Assign object at 0x10176af40"]
    node_169["ast.Return object at 0x10176aca0"]
    node_327["ast.Assign object at 0x101766040"]
    node_9["ast.Store object at 0x101673070"]
    node_352["ast.Name object at 0x101763b50"]
    node_65["ast.Subscript object at 0x101769fa0"]
    node_141["ast.Store object at 0x101673070"]
    node_210["ast.Load object at 0x1016730d0"]
    node_121["ast.Name object at 0x1017699a0"]
    node_227["ast.Name object at 0x101766e80"]
    node_302["ast.Load object at 0x1016730d0"]
    node_175["ast.Tuple object at 0x10176aaf0"]
    node_179["ast.Load object at 0x1016730d0"]
    node_207["ast.Load object at 0x1016730d0"]
    node_38["ast.Load object at 0x1016730d0"]
    node_256["ast.Store object at 0x101673070"]
    node_36["ast.Subscript object at 0x101780490"]
    node_180["ast.Load object at 0x1016730d0"]
    node_11["ast.Name object at 0x101780700"]
    node_46["ast.FunctionDef object at 0x101780400"]
    node_90["ast.Compare object at 0x101769cd0"]
    node_270["ast.Call object at 0x101766910"]
    node_279["ast.In object at 0x1016a6190"]
    node_231["ast.If object at 0x101766e20"]
    node_72["ast.Store object at 0x101673070"]
    node_292["ast.Subscript object at 0x1017666a0"]
    node_115["ast.Load object at 0x1016730d0"]
    node_328["ast.Name object at 0x101763fd0"]
    node_59["ast.NotIn object at 0x1016a61f0"]
    node_275["ast.If object at 0x101766880"]
    node_40["ast.Load object at 0x1016730d0"]
    node_142["ast.Dict object at 0x10176afd0"]
    node_79["ast.Attribute object at 0x101769df0"]
    node_49["ast.arg object at 0x101780310"]
    node_21["ast.Load object at 0x1016730d0"]
    node_160["ast.Assign object at 0x10176ad60"]
    node_240["ast.Load object at 0x1016730d0"]
    node_261["ast.Name object at 0x101766a30"]
    node_144["ast.Name object at 0x10176aee0"]
    node_31["ast.Name object at 0x101780550"]
    node_70["ast.Name object at 0x101769f10"]
    node_320["ast.Name object at 0x101766130"]
    node_15["ast.Load object at 0x1016730d0"]
    node_134["ast.Name object at 0x101769040"]
    node_319["ast.Subscript object at 0x101766160"]
    node_26["ast.Attribute object at 0x101780520"]
    node_189["ast.Name object at 0x10176a820"]
    node_280["ast.Name object at 0x1017667f0"]
    node_22["ast.Load object at 0x1016730d0"]
    node_251["ast.keyword object at 0x101766b80"]
    node_78["ast.Subscript object at 0x101769e20"]
    node_222["ast.Assign object at 0x101766f40"]
    node_250["ast.Load object at 0x1016730d0"]
    node_200["ast.Name object at 0x10176a400"]
    node_30["ast.Subscript object at 0x1017804c0"]
    node_62["ast.Load object at 0x1016730d0"]
    node_164["ast.Name object at 0x10176ab80"]
    node_199["ast.Load object at 0x1016730d0"]
    node_103["ast.Load object at 0x1016730d0"]
    node_223["ast.Name object at 0x101766f10"]
    node_284["ast.Store object at 0x101673070"]
    node_230["ast.Load object at 0x1016730d0"]
    node_109["ast.Expr object at 0x101769af0"]
    node_33["ast.Tuple object at 0x1017803d0"]
    node_176["ast.Name object at 0x10176aac0"]
    node_258["ast.Name object at 0x101766a90"]
    node_264["ast.Name object at 0x1017669d0"]
    node_278["ast.Load object at 0x1016730d0"]
    node_35["ast.Load object at 0x1016730d0"]
    node_102["ast.Load object at 0x1016730d0"]
    node_61["ast.Name object at 0x101780e20"]
    node_64["ast.Assign object at 0x101769fd0"]
    node_28["ast.Load object at 0x1016730d0"]
    node_247["ast.Load object at 0x1016730d0"]
    node_8["ast.Load object at 0x1016730d0"]
    node_329["ast.Store object at 0x101673070"]
    node_202["ast.FunctionDef object at 0x10176a460"]
    node_147["ast.Load object at 0x1016730d0"]
    node_113["ast.Attribute object at 0x101769a30"]
    node_343["ast.Name object at 0x101763df0"]
    node_257["ast.Call object at 0x101766ac0"]
    node_34["ast.Name object at 0x1017803a0"]
    node_289["ast.Load object at 0x1016730d0"]
    node_98["ast.Assign object at 0x101769c10"]
    node_162["ast.Name object at 0x10176ac70"]
    node_255["ast.Name object at 0x101766af0"]
    node_95["ast.Name object at 0x101769c40"]
    node_188["ast.Subscript object at 0x10176a910"]
    node_126["ast.arguments object at 0x101670fa0"]
    node_291["ast.Assign object at 0x1017666d0"]
    node_239["ast.Name object at 0x101766d00"]
    node_96["ast.Load object at 0x1016730d0"]
    node_77["ast.Attribute object at 0x101769e50"]
    node_313["ast.FunctionDef object at 0x101766250"]
    node_119["ast.Load object at 0x1016730d0"]
    node_145["ast.Store object at 0x101673070"]
    node_348["ast.keyword object at 0x101763be0"]
    node_63["ast.Load object at 0x1016730d0"]
    node_304["ast.Name object at 0x101766310"]
    node_205["ast.Subscript object at 0x10176a6a0"]
    node_332["ast.Load object at 0x1016730d0"]
    node_117["ast.Name object at 0x1017699d0"]
    node_268["ast.Name object at 0x101766940"]
    node_277["ast.Name object at 0x101766820"]
    node_146["ast.Name object at 0x10176aeb0"]
    node_331["ast.Name object at 0x101763f70"]
    node_259["ast.Load object at 0x1016730d0"]
    node_318["ast.arg object at 0x101766190"]
    node_282["ast.Assign object at 0x1017667c0"]
    node_214["ast.Load object at 0x1016730d0"]
    node_87["ast.Name object at 0x101769d60"]
    node_158["ast.Name object at 0x10176aa90"]
    node_32["ast.Load object at 0x1016730d0"]
    node_67["ast.Name object at 0x101769f40"]
    node_351["ast.Return object at 0x101763b80"]
    node_326["ast.Constant object at 0x1017660a0"]
    node_131["ast.Subscript object at 0x101769910"]
    node_68["ast.Load object at 0x1016730d0"]
    node_0["ast.Module object at 0x1017809a0"]
    node_301["ast.Name object at 0x1017663a0"]
    node_263["ast.Assign object at 0x101766a00"]
    node_84["ast.Load object at 0x1016730d0"]
    node_216["ast.Name object at 0x101766fa0"]
    node_336["ast.keyword object at 0x101763ee0"]
    node_16["ast.Subscript object at 0x101780730"]
    node_29["ast.Store object at 0x101673070"]
    node_44["ast.Dict object at 0x1017802b0"]
    node_157["ast.keyword object at 0x10176ad00"]
    node_353["ast.Load object at 0x1016730d0"]
    node_321["ast.Load object at 0x1016730d0"]
    node_287["ast.Load object at 0x1016730d0"]
    node_212["ast.Subscript object at 0x10176a610"]
    node_310["ast.Load object at 0x1016730d0"]
    node_211["ast.arg object at 0x10176a640"]
    node_339["ast.Assign object at 0x101763e80"]
    node_317["ast.Load object at 0x1016730d0"]
    node_37["ast.Name object at 0x101780460"]
    node_106["ast.Store object at 0x101673070"]
    node_217["ast.Load object at 0x1016730d0"]
    node_116["ast.Load object at 0x1016730d0"]
    node_325["ast.Expr object at 0x1017660d0"]
    node_341["ast.Store object at 0x101673070"]
    node_161["ast.Subscript object at 0x10176ad30"]
    node_52["ast.arg object at 0x1017800d0"]
    node_300["ast.Return object at 0x1017663d0"]
    node_276["ast.Compare object at 0x101766850"]
    node_75["ast.Expr object at 0x101769eb0"]
    node_203["ast.arguments object at 0x10176a5b0"]
    node_272["ast.Load object at 0x1016730d0"]
    node_170["ast.Name object at 0x10176abe0"]
    node_195["ast.Name object at 0x10176a8e0"]
    node_17["ast.Name object at 0x101780640"]
    node_93["ast.NotIn object at 0x1016a61f0"]
    node_221["ast.Load object at 0x1016730d0"]
    node_215["ast.Tuple object at 0x101766fd0"]
    node_7["ast.Name object at 0x101780190"]
    node_281["ast.Load object at 0x1016730d0"]
    node_153["ast.Load object at 0x1016730d0"]
    node_45["ast.Constant object at 0x101780430"]
    node_311["ast.Load object at 0x1016730d0"]
    node_50["ast.Name object at 0x1017801f0"]
    node_330["ast.Call object at 0x101763fa0"]
    node_133["ast.Load object at 0x1016730d0"]
    node_294["ast.Load object at 0x1016730d0"]
    node_324["ast.Load object at 0x1016730d0"]
    node_334["ast.Name object at 0x101763f10"]
    node_340["ast.Name object at 0x101763e50"]
    node_309["ast.Name object at 0x101766280"]
    node_105["ast.Load object at 0x1016730d0"]
    node_165["ast.Load object at 0x1016730d0"]
    node_27["ast.Name object at 0x101780370"]
    node_124["ast.Constant object at 0x101769940"]
    node_174["ast.Load object at 0x1016730d0"]
    node_56["ast.Compare object at 0x101780220"]
    node_178["ast.Name object at 0x10176ab50"]
    node_163["ast.Load object at 0x1016730d0"]
    node_296["ast.Load object at 0x1016730d0"]
    node_172["ast.Subscript object at 0x10176ac40"]
    node_232["ast.NamedExpr object at 0x101766df0"]
    node_193["ast.Call object at 0x10176a880"]
    node_248["ast.keyword object at 0x101766be0"]
    node_225["ast.Dict object at 0x101766ee0"]
    node_51["ast.Load object at 0x1016730d0"]
    node_88["ast.Load object at 0x1016730d0"]
    node_159["ast.Load object at 0x1016730d0"]
    node_236["ast.Name object at 0x101766d60"]
    node_97["ast.Load object at 0x1016730d0"]
    node_274["ast.Load object at 0x1016730d0"]
    node_204["ast.arg object at 0x10176a670"]
    node_196["ast.Load object at 0x1016730d0"]
    node_344["ast.Load object at 0x1016730d0"]
    node_76["ast.Call object at 0x101769e80"]
    node_125["ast.FunctionDef object at 0x101670e80"]
    node_100["ast.Attribute object at 0x101769bb0"]
    node_53["ast.Name object at 0x1017800a0"]
    node_82["ast.Load object at 0x1016730d0"]
    node_99["ast.Subscript object at 0x101769be0"]
    node_91["ast.Name object at 0x101769ca0"]
    node_108["ast.Load object at 0x1016730d0"]
    node_219["ast.Load object at 0x1016730d0"]
    node_233["ast.Name object at 0x101766dc0"]
    node_333["ast.keyword object at 0x101763f40"]
    node_201["ast.Load object at 0x1016730d0"]
    node_4["ast.arg object at 0x1017807c0"]
    node_220["ast.Load object at 0x1016730d0"]
    node_266["ast.Constant object at 0x1017669a0"]
    node_85["ast.Load object at 0x1016730d0"]
    node_110["ast.Subscript object at 0x101769ac0"]
    node_136["ast.Load object at 0x1016730d0"]
    node_213["ast.Name object at 0x10176a5e0"]
    node_5["ast.AnnAssign object at 0x101780670"]
    node_244["ast.Store object at 0x101673070"]
    node_288["ast.Name object at 0x101766700"]
    node_253["ast.Load object at 0x1016730d0"]
    node_25["ast.AnnAssign object at 0x1017805b0"]
    node_71["ast.Load object at 0x1016730d0"]
    node_171["ast.Load object at 0x1016730d0"]
    node_39["ast.Name object at 0x1017802e0"]
    node_57["ast.Name object at 0x101780100"]
    node_246["ast.Name object at 0x101766c10"]
    node_262["ast.Load object at 0x1016730d0"]
    node_293["ast.Name object at 0x101766670"]
    node_315["ast.arg object at 0x1017661f0"]
    node_122["ast.Load object at 0x1016730d0"]
    node_190["ast.Load object at 0x1016730d0"]
    node_197["ast.Load object at 0x1016730d0"]
    node_140["ast.Name object at 0x10176ae80"]
    node_58["ast.Load object at 0x1016730d0"]
    node_80["ast.Name object at 0x101769dc0"]
    node_123["ast.Load object at 0x1016730d0"]
    node_192["ast.Constant object at 0x10176a940"]
    node_89["ast.If object at 0x101769d00"]
    node_81["ast.Load object at 0x1016730d0"]
    node_173["ast.Name object at 0x10176ac10"]
    node_342["ast.Call object at 0x101763e20"]
    node_132["ast.Name object at 0x1017698e0"]
    node_290["ast.Load object at 0x1016730d0"]
    node_184["ast.arg object at 0x10176a9d0"]
    node_48["ast.arg object at 0x101780130"]
    node_156["ast.Load object at 0x1016730d0"]
    node_226["ast.For object at 0x101766eb0"]
    node_335["ast.Load object at 0x1016730d0"]
    node_47["ast.arguments object at 0x1017801c0"]
    node_307["ast.Name object at 0x1017662b0"]
    node_107["ast.List object at 0x101769b20"]
    node_112["ast.Subscript object at 0x101769a60"]
    node_218["ast.Name object at 0x101766f70"]
    node_194["ast.Attribute object at 0x10176a850"]
    node_208["ast.Name object at 0x10176a700"]
    node_183["ast.arguments object at 0x10176aa00"]
    node_66["ast.Attribute object at 0x101769f70"]
    node_345["ast.keyword object at 0x101763dc0"]
    node_299["ast.Load object at 0x1016730d0"]
    node_273["ast.Name object at 0x1017668b0"]
    node_92["ast.Load object at 0x1016730d0"]
    node_149["ast.Name object at 0x10176af10"]
    node_20["ast.Load object at 0x1016730d0"]
    node_168["ast.Load object at 0x1016730d0"]
    node_114["ast.Name object at 0x101769a00"]
    node_181["ast.Load object at 0x1016730d0"]
    node_86["ast.Load object at 0x1016730d0"]
    node_338["ast.Load object at 0x1016730d0"]
    node_14["ast.Name object at 0x1017806a0"]
    node_283["ast.Name object at 0x101766790"]
    node_252["ast.Name object at 0x101766b50"]
    node_41["ast.Load object at 0x1016730d0"]
    node_298["ast.Name object at 0x101766610"]
    node_83["ast.Name object at 0x101769d90"]
    node_10["ast.Subscript object at 0x101780760"]
    node_128["ast.Name object at 0x1016ba2b0"]
    node_303["ast.Subscript object at 0x101766340"]
    node_151["ast.Call object at 0x10176adf0"]
    node_323["ast.Load object at 0x1016730d0"]
    node_12["ast.Load object at 0x1016730d0"]
    node_166["ast.Store object at 0x101673070"]
    node_138["ast.Constant object at 0x10176a7f0"]
    node_271["ast.Name object at 0x1017668e0"]
    node_23["ast.Load object at 0x1016730d0"]
    node_209["ast.Load object at 0x1016730d0"]
    node_349["ast.Name object at 0x101763bb0"]
    node_238["ast.keyword object at 0x101766d30"]
    node_234["ast.Store object at 0x101673070"]
    node_111["ast.Attribute object at 0x101769a90"]
    node_306["ast.Tuple object at 0x1017662e0"]
    node_129["ast.Load object at 0x1016730d0"]
    node_198["ast.Constant object at 0x10176a8b0"]
    node_245["ast.Call object at 0x101766c40"]
    node_43["ast.Load object at 0x1016730d0"]
    node_316["ast.Name object at 0x1017661c0"]
    node_254["ast.For object at 0x101766b20"]
    node_130["ast.arg object at 0x1016ba070"]
    node_206["ast.Name object at 0x10176a6d0"]
    node_347["ast.Load object at 0x1016730d0"]
    node_297["ast.Store object at 0x101673070"]
    node_191["ast.Slice object at 0x10176a970"]
    node_182["ast.FunctionDef object at 0x10176ab20"]
    node_285["ast.Subscript object at 0x101766760"]
    node_74["ast.Load object at 0x1016730d0"]
    node_235["ast.Call object at 0x101766d90"]

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
    node_220 --> node_221
    node_221 --> node_222
    node_222 --> node_223
    node_223 --> node_224
    node_224 --> node_225
    node_225 --> node_226
    node_226 --> node_227
    node_227 --> node_228
    node_228 --> node_229
    node_229 --> node_230
    node_230 --> node_231
    node_231 --> node_232
    node_232 --> node_233
    node_233 --> node_234
    node_234 --> node_235
    node_235 --> node_236
    node_236 --> node_237
    node_237 --> node_238
    node_238 --> node_239
    node_239 --> node_240
    node_240 --> node_241
    node_241 --> node_242
    node_242 --> node_243
    node_243 --> node_244
    node_244 --> node_245
    node_245 --> node_246
    node_246 --> node_247
    node_247 --> node_248
    node_248 --> node_249
    node_249 --> node_250
    node_250 --> node_251
    node_251 --> node_252
    node_252 --> node_253
    node_253 --> node_254
    node_254 --> node_255
    node_255 --> node_256
    node_256 --> node_257
    node_257 --> node_258
    node_258 --> node_259
    node_259 --> node_260
    node_260 --> node_261
    node_261 --> node_262
    node_262 --> node_263
    node_263 --> node_264
    node_264 --> node_265
    node_265 --> node_266
    node_266 --> node_267
    node_267 --> node_268
    node_268 --> node_269
    node_269 --> node_270
    node_270 --> node_271
    node_271 --> node_272
    node_272 --> node_273
    node_273 --> node_274
    node_274 --> node_275
    node_275 --> node_276
    node_276 --> node_277
    node_277 --> node_278
    node_278 --> node_279
    node_279 --> node_280
    node_280 --> node_281
    node_281 --> node_282
    node_282 --> node_283
    node_283 --> node_284
    node_284 --> node_285
    node_285 --> node_286
    node_286 --> node_287
    node_287 --> node_288
    node_288 --> node_289
    node_289 --> node_290
    node_290 --> node_291
    node_291 --> node_292
    node_292 --> node_293
    node_293 --> node_294
    node_294 --> node_295
    node_295 --> node_296
    node_296 --> node_297
    node_297 --> node_298
    node_298 --> node_299
    node_299 --> node_300
    node_300 --> node_301
    node_301 --> node_302
    node_302 --> node_303
    node_303 --> node_304
    node_304 --> node_305
    node_305 --> node_306
    node_306 --> node_307
    node_307 --> node_308
    node_308 --> node_309
    node_309 --> node_310
    node_310 --> node_311
    node_311 --> node_312
    node_312 --> node_313
    node_313 --> node_314
    node_314 --> node_315
    node_315 --> node_316
    node_316 --> node_317
    node_317 --> node_318
    node_318 --> node_319
    node_319 --> node_320
    node_320 --> node_321
    node_321 --> node_322
    node_322 --> node_323
    node_323 --> node_324
    node_324 --> node_325
    node_325 --> node_326
    node_326 --> node_327
    node_327 --> node_328
    node_328 --> node_329
    node_329 --> node_330
    node_330 --> node_331
    node_331 --> node_332
    node_332 --> node_333
    node_333 --> node_334
    node_334 --> node_335
    node_335 --> node_336
    node_336 --> node_337
    node_337 --> node_338
    node_338 --> node_339
    node_339 --> node_340
    node_340 --> node_341
    node_341 --> node_342
    node_342 --> node_343
    node_343 --> node_344
    node_344 --> node_345
    node_345 --> node_346
    node_346 --> node_347
    node_347 --> node_348
    node_348 --> node_349
    node_349 --> node_350
    node_350 --> node_351
    node_351 --> node_352
    node_352 --> node_353

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='ast_tools',
      names=[
        alias(name='get_ast_root_node_for_file'),
        alias(name='get_used_import_list')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=70),
    ImportFrom(
      module='files.source',
      names=[
        alias(name='get_source_code_from_file'),
        alias(name='get_import_name_from_path')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=77),
    ClassDef(
      name='ImportMap',
      bases=[],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=7,
                col_offset=17,
                end_lineno=7,
                end_col_offset=21)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=8,
                  col_offset=8,
                  end_lineno=8,
                  end_col_offset=12),
                attr='import_to',
                ctx=Store(),
                lineno=8,
                col_offset=8,
                end_lineno=8,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=8,
                  col_offset=25,
                  end_lineno=8,
                  end_col_offset=29),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=8,
                      col_offset=30,
                      end_lineno=8,
                      end_col_offset=33),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=8,
                        col_offset=35,
                        end_lineno=8,
                        end_col_offset=39),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=8,
                        col_offset=40,
                        end_lineno=8,
                        end_col_offset=43),
                      ctx=Load(),
                      lineno=8,
                      col_offset=35,
                      end_lineno=8,
                      end_col_offset=44)],
                  ctx=Load(),
                  lineno=8,
                  col_offset=30,
                  end_lineno=8,
                  end_col_offset=44),
                ctx=Load(),
                lineno=8,
                col_offset=25,
                end_lineno=8,
                end_col_offset=45),
              value=Dict(
                keys=[],
                values=[],
                lineno=8,
                col_offset=48,
                end_lineno=8,
                end_col_offset=50),
              simple=0,
              lineno=8,
              col_offset=8,
              end_lineno=8,
              end_col_offset=50),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=9,
                  col_offset=8,
                  end_lineno=9,
                  end_col_offset=12),
                attr='import_from',
                ctx=Store(),
                lineno=9,
                col_offset=8,
                end_lineno=9,
                end_col_offset=24),
              annotation=Subscript(
                value=Name(
                  id='dict',
                  ctx=Load(),
                  lineno=9,
                  col_offset=27,
                  end_lineno=9,
                  end_col_offset=31),
                slice=Tuple(
                  elts=[
                    Name(
                      id='str',
                      ctx=Load(),
                      lineno=9,
                      col_offset=32,
                      end_lineno=9,
                      end_col_offset=35),
                    Subscript(
                      value=Name(
                        id='list',
                        ctx=Load(),
                        lineno=9,
                        col_offset=37,
                        end_lineno=9,
                        end_col_offset=41),
                      slice=Name(
                        id='str',
                        ctx=Load(),
                        lineno=9,
                        col_offset=42,
                        end_lineno=9,
                        end_col_offset=45),
                      ctx=Load(),
                      lineno=9,
                      col_offset=37,
                      end_lineno=9,
                      end_col_offset=46)],
                  ctx=Load(),
                  lineno=9,
                  col_offset=32,
                  end_lineno=9,
                  end_col_offset=46),
                ctx=Load(),
                lineno=9,
                col_offset=27,
                end_lineno=9,
                end_col_offset=47),
              value=Dict(
                keys=[],
                values=[],
                lineno=9,
                col_offset=50,
                end_lineno=9,
                end_col_offset=52),
              simple=0,
              lineno=9,
              col_offset=8,
              end_lineno=9,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=7,
            col_offset=26,
            end_lineno=7,
            end_col_offset=30),
          lineno=7,
          col_offset=4,
          end_lineno=9,
          end_col_offset=52),
        FunctionDef(
          name='add_import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=12,
                col_offset=19,
                end_lineno=12,
                end_col_offset=23),
              arg(
                arg='from_',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=32,
                  end_lineno=12,
                  end_col_offset=35),
                lineno=12,
                col_offset=25,
                end_lineno=12,
                end_col_offset=35),
              arg(
                arg='to',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=12,
                  col_offset=41,
                  end_lineno=12,
                  end_col_offset=44),
                lineno=12,
                col_offset=37,
                end_lineno=12,
                end_col_offset=44)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            If(
              test=Compare(
                left=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=13,
                  col_offset=11,
                  end_lineno=13,
                  end_col_offset=16),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=13,
                      col_offset=24,
                      end_lineno=13,
                      end_col_offset=28),
                    attr='import_to',
                    ctx=Load(),
                    lineno=13,
                    col_offset=24,
                    end_lineno=13,
                    end_col_offset=38)],
                lineno=13,
                col_offset=11,
                end_lineno=13,
                end_col_offset=38),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=14,
                          col_offset=12,
                          end_lineno=14,
                          end_col_offset=16),
                        attr='import_to',
                        ctx=Load(),
                        lineno=14,
                        col_offset=12,
                        end_lineno=14,
                        end_col_offset=26),
                      slice=Name(
                        id='from_',
                        ctx=Load(),
                        lineno=14,
                        col_offset=27,
                        end_lineno=14,
                        end_col_offset=32),
                      ctx=Store(),
                      lineno=14,
                      col_offset=12,
                      end_lineno=14,
                      end_col_offset=33)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=14,
                    col_offset=36,
                    end_lineno=14,
                    end_col_offset=38),
                  lineno=14,
                  col_offset=12,
                  end_lineno=14,
                  end_col_offset=38)],
              orelse=[],
              lineno=13,
              col_offset=8,
              end_lineno=14,
              end_col_offset=38),
            Expr(
              value=Call(
                func=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=15,
                        col_offset=8,
                        end_lineno=15,
                        end_col_offset=12),
                      attr='import_to',
                      ctx=Load(),
                      lineno=15,
                      col_offset=8,
                      end_lineno=15,
                      end_col_offset=22),
                    slice=Name(
                      id='from_',
                      ctx=Load(),
                      lineno=15,
                      col_offset=23,
                      end_lineno=15,
                      end_col_offset=28),
                    ctx=Load(),
                    lineno=15,
                    col_offset=8,
                    end_lineno=15,
                    end_col_offset=29),
                  attr='append',
                  ctx=Load(),
                  lineno=15,
                  col_offset=8,
                  end_lineno=15,
                  end_col_offset=36),
                args=[
                  Name(
                    id='to',
                    ctx=Load(),
                    lineno=15,
                    col_offset=37,
                    end_lineno=15,
                    end_col_offset=39)],
                keywords=[],
                lineno=15,
                col_offset=8,
                end_lineno=15,
                end_col_offset=40),
              lineno=15,
              col_offset=8,
              end_lineno=15,
              end_col_offset=40),
            If(
              test=Compare(
                left=Name(
                  id='to',
                  ctx=Load(),
                  lineno=17,
                  col_offset=11,
                  end_lineno=17,
                  end_col_offset=13),
                ops=[
                  NotIn()],
                comparators=[
                  Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=17,
                      col_offset=21,
                      end_lineno=17,
                      end_col_offset=25),
                    attr='import_from',
                    ctx=Load(),
                    lineno=17,
                    col_offset=21,
                    end_lineno=17,
                    end_col_offset=37)],
                lineno=17,
                col_offset=11,
                end_lineno=17,
                end_col_offset=37),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=18,
                          col_offset=12,
                          end_lineno=18,
                          end_col_offset=16),
                        attr='import_from',
                        ctx=Load(),
                        lineno=18,
                        col_offset=12,
                        end_lineno=18,
                        end_col_offset=28),
                      slice=Name(
                        id='to',
                        ctx=Load(),
                        lineno=18,
                        col_offset=29,
                        end_lineno=18,
                        end_col_offset=31),
                      ctx=Store(),
                      lineno=18,
                      col_offset=12,
                      end_lineno=18,
                      end_col_offset=32)],
                  value=List(
                    elts=[],
                    ctx=Load(),
                    lineno=18,
                    col_offset=35,
                    end_lineno=18,
                    end_col_offset=37),
                  lineno=18,
                  col_offset=12,
                  end_lineno=18,
                  end_col_offset=37)],
              orelse=[],
              lineno=17,
              col_offset=8,
              end_lineno=18,
              end_col_offset=37),
            Expr(
              value=Subscript(
                value=Attribute(
                  value=Subscript(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=19,
                        col_offset=8,
                        end_lineno=19,
                        end_col_offset=12),
                      attr='import_from',
                      ctx=Load(),
                      lineno=19,
                      col_offset=8,
                      end_lineno=19,
                      end_col_offset=24),
                    slice=Name(
                      id='to',
                      ctx=Load(),
                      lineno=19,
                      col_offset=25,
                      end_lineno=19,
                      end_col_offset=27),
                    ctx=Load(),
                    lineno=19,
                    col_offset=8,
                    end_lineno=19,
                    end_col_offset=28),
                  attr='append',
                  ctx=Load(),
                  lineno=19,
                  col_offset=8,
                  end_lineno=19,
                  end_col_offset=35),
                slice=Name(
                  id='from_',
                  ctx=Load(),
                  lineno=19,
                  col_offset=36,
                  end_lineno=19,
                  end_col_offset=41),
                ctx=Load(),
                lineno=19,
                col_offset=8,
                end_lineno=19,
                end_col_offset=42),
              lineno=19,
              col_offset=8,
              end_lineno=19,
              end_col_offset=42)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=12,
            col_offset=49,
            end_lineno=12,
            end_col_offset=53),
          lineno=12,
          col_offset=4,
          end_lineno=19,
          end_col_offset=42)],
      decorator_list=[],
      lineno=5,
      col_offset=0,
      end_lineno=19,
      end_col_offset=42),
    FunctionDef(
      name='_get_import_to_file_map',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=40,
              end_lineno=22,
              end_col_offset=43),
            lineno=22,
            col_offset=28,
            end_lineno=22,
            end_col_offset=43),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=22,
                col_offset=59,
                end_lineno=22,
                end_col_offset=63),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=22,
                col_offset=64,
                end_lineno=22,
                end_col_offset=67),
              ctx=Load(),
              lineno=22,
              col_offset=59,
              end_lineno=22,
              end_col_offset=68),
            lineno=22,
            col_offset=45,
            end_lineno=22,
            end_col_offset=68)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value=' Create a mapping of import paths to filenames first ',
            lineno=23,
            col_offset=4,
            end_lineno=23,
            end_col_offset=63),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=63),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=24,
              col_offset=4,
              end_lineno=24,
              end_col_offset=22)],
          value=Dict(
            keys=[],
            values=[],
            lineno=24,
            col_offset=25,
            end_lineno=24,
            end_col_offset=27),
          lineno=24,
          col_offset=4,
          end_lineno=24,
          end_col_offset=27),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=26,
            col_offset=8,
            end_lineno=26,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=26,
            col_offset=19,
            end_lineno=26,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='import_name',
                  ctx=Store(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=19)],
              value=Call(
                func=Name(
                  id='get_import_name_from_path',
                  ctx=Load(),
                  lineno=27,
                  col_offset=22,
                  end_lineno=27,
                  end_col_offset=47),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='input_path',
                      ctx=Load(),
                      lineno=28,
                      col_offset=23,
                      end_lineno=28,
                      end_col_offset=33),
                    lineno=28,
                    col_offset=12,
                    end_lineno=28,
                    end_col_offset=33),
                  keyword(
                    arg='input_file',
                    value=Name(
                      id='in_file',
                      ctx=Load(),
                      lineno=28,
                      col_offset=46,
                      end_lineno=28,
                      end_col_offset=53),
                    lineno=28,
                    col_offset=35,
                    end_lineno=28,
                    end_col_offset=53)],
                lineno=27,
                col_offset=22,
                end_lineno=29,
                end_col_offset=9),
              lineno=27,
              col_offset=8,
              end_lineno=29,
              end_col_offset=9),
            Assign(
              targets=[
                Subscript(
                  value=Name(
                    id='import_to_file_map',
                    ctx=Load(),
                    lineno=30,
                    col_offset=8,
                    end_lineno=30,
                    end_col_offset=26),
                  slice=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=30,
                    col_offset=27,
                    end_lineno=30,
                    end_col_offset=38),
                  ctx=Store(),
                  lineno=30,
                  col_offset=8,
                  end_lineno=30,
                  end_col_offset=39)],
              value=Name(
                id='in_file',
                ctx=Load(),
                lineno=30,
                col_offset=42,
                end_lineno=30,
                end_col_offset=49),
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=49)],
          orelse=[],
          lineno=26,
          col_offset=4,
          end_lineno=30,
          end_col_offset=49),
        Return(
          value=Name(
            id='import_to_file_map',
            ctx=Load(),
            lineno=32,
            col_offset=11,
            end_lineno=32,
            end_col_offset=29),
          lineno=32,
          col_offset=4,
          end_lineno=32,
          end_col_offset=29)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=22,
          col_offset=73,
          end_lineno=22,
          end_col_offset=77),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=78,
              end_lineno=22,
              end_col_offset=81),
            Name(
              id='str',
              ctx=Load(),
              lineno=22,
              col_offset=83,
              end_lineno=22,
              end_col_offset=86)],
          ctx=Load(),
          lineno=22,
          col_offset=78,
          end_lineno=22,
          end_col_offset=86),
        ctx=Load(),
        lineno=22,
        col_offset=73,
        end_lineno=22,
        end_col_offset=87),
      lineno=22,
      col_offset=0,
      end_lineno=32,
      end_col_offset=29),
    FunctionDef(
      name='_get_parent_import',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='import_name',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=35,
              col_offset=36,
              end_lineno=35,
              end_col_offset=39),
            lineno=35,
            col_offset=23,
            end_lineno=35,
            end_col_offset=39)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Subscript(
            value=Name(
              id='import_name',
              ctx=Load(),
              lineno=36,
              col_offset=11,
              end_lineno=36,
              end_col_offset=22),
            slice=Slice(
              lower=Constant(
                value=0,
                lineno=36,
                col_offset=23,
                end_lineno=36,
                end_col_offset=24),
              upper=Call(
                func=Attribute(
                  value=Name(
                    id='import_name',
                    ctx=Load(),
                    lineno=36,
                    col_offset=26,
                    end_lineno=36,
                    end_col_offset=37),
                  attr='rfind',
                  ctx=Load(),
                  lineno=36,
                  col_offset=26,
                  end_lineno=36,
                  end_col_offset=43),
                args=[
                  Constant(
                    value='.',
                    lineno=36,
                    col_offset=44,
                    end_lineno=36,
                    end_col_offset=47)],
                keywords=[],
                lineno=36,
                col_offset=26,
                end_lineno=36,
                end_col_offset=48),
              lineno=36,
              col_offset=23,
              end_lineno=36,
              end_col_offset=48),
            ctx=Load(),
            lineno=36,
            col_offset=11,
            end_lineno=36,
            end_col_offset=49),
          lineno=36,
          col_offset=4,
          end_lineno=36,
          end_col_offset=49)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=35,
        col_offset=44,
        end_lineno=35,
        end_col_offset=47),
      lineno=35,
      col_offset=0,
      end_lineno=36,
      end_col_offset=49),
    FunctionDef(
      name='_create_import_table',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=40,
                col_offset=18,
                end_lineno=40,
                end_col_offset=22),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=40,
                col_offset=23,
                end_lineno=40,
                end_col_offset=26),
              ctx=Load(),
              lineno=40,
              col_offset=18,
              end_lineno=40,
              end_col_offset=27),
            lineno=40,
            col_offset=4,
            end_lineno=40,
            end_col_offset=27),
          arg(
            arg='import_to_file_map',
            annotation=Subscript(
              value=Name(
                id='dict',
                ctx=Load(),
                lineno=41,
                col_offset=24,
                end_lineno=41,
                end_col_offset=28),
              slice=Tuple(
                elts=[
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=29,
                    end_lineno=41,
                    end_col_offset=32),
                  Name(
                    id='str',
                    ctx=Load(),
                    lineno=41,
                    col_offset=34,
                    end_lineno=41,
                    end_col_offset=37)],
                ctx=Load(),
                lineno=41,
                col_offset=29,
                end_lineno=41,
                end_col_offset=37),
              ctx=Load(),
              lineno=41,
              col_offset=24,
              end_lineno=41,
              end_col_offset=38),
            lineno=41,
            col_offset=4,
            end_lineno=41,
            end_col_offset=38)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=44,
              col_offset=4,
              end_lineno=44,
              end_col_offset=20)],
          value=Dict(
            keys=[],
            values=[],
            lineno=44,
            col_offset=23,
            end_lineno=44,
            end_col_offset=25),
          lineno=44,
          col_offset=4,
          end_lineno=44,
          end_col_offset=25),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=46,
            col_offset=8,
            end_lineno=46,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=46,
            col_offset=19,
            end_lineno=46,
            end_col_offset=31),
          body=[
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=47,
                  col_offset=11,
                  end_lineno=47,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=47,
                    col_offset=26,
                    end_lineno=47,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=47,
                        col_offset=63,
                        end_lineno=47,
                        end_col_offset=70),
                      lineno=47,
                      col_offset=52,
                      end_lineno=47,
                      end_col_offset=70)],
                  lineno=47,
                  col_offset=26,
                  end_lineno=47,
                  end_col_offset=71),
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=48,
                      col_offset=15,
                      end_lineno=48,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=48,
                        col_offset=27,
                        end_lineno=48,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=49,
                            col_offset=28,
                            end_lineno=49,
                            end_col_offset=39),
                          lineno=49,
                          col_offset=16,
                          end_lineno=49,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=50,
                            col_offset=27,
                            end_lineno=50,
                            end_col_offset=34),
                          lineno=50,
                          col_offset=16,
                          end_lineno=50,
                          end_col_offset=34)],
                      lineno=48,
                      col_offset=27,
                      end_lineno=51,
                      end_col_offset=13),
                    lineno=48,
                    col_offset=15,
                    end_lineno=51,
                    end_col_offset=13),
                  body=[
                    For(
                      target=Name(
                        id='used_import',
                        ctx=Store(),
                        lineno=52,
                        col_offset=20,
                        end_lineno=52,
                        end_col_offset=31),
                      iter=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=52,
                          col_offset=35,
                          end_lineno=52,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=52,
                              col_offset=65,
                              end_lineno=52,
                              end_col_offset=73),
                            lineno=52,
                            col_offset=56,
                            end_lineno=52,
                            end_col_offset=73)],
                        lineno=52,
                        col_offset=35,
                        end_lineno=52,
                        end_col_offset=74),
                      body=[
                        Assign(
                          targets=[
                            Name(
                              id='known_file',
                              ctx=Store(),
                              lineno=53,
                              col_offset=20,
                              end_lineno=53,
                              end_col_offset=30)],
                          value=Constant(
                            value='',
                            lineno=53,
                            col_offset=33,
                            end_lineno=53,
                            end_col_offset=35),
                          lineno=53,
                          col_offset=20,
                          end_lineno=53,
                          end_col_offset=35),
                        Assign(
                          targets=[
                            Name(
                              id='parent_import',
                              ctx=Store(),
                              lineno=54,
                              col_offset=20,
                              end_lineno=54,
                              end_col_offset=33)],
                          value=Call(
                            func=Name(
                              id='_get_parent_import',
                              ctx=Load(),
                              lineno=54,
                              col_offset=36,
                              end_lineno=54,
                              end_col_offset=54),
                            args=[
                              Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=54,
                                col_offset=55,
                                end_lineno=54,
                                end_col_offset=66)],
                            keywords=[],
                            lineno=54,
                            col_offset=36,
                            end_lineno=54,
                            end_col_offset=67),
                          lineno=54,
                          col_offset=20,
                          end_lineno=54,
                          end_col_offset=67),
                        If(
                          test=Compare(
                            left=Name(
                              id='parent_import',
                              ctx=Load(),
                              lineno=55,
                              col_offset=23,
                              end_lineno=55,
                              end_col_offset=36),
                            ops=[
                              In()],
                            comparators=[
                              Name(
                                id='import_to_file_map',
                                ctx=Load(),
                                lineno=55,
                                col_offset=40,
                                end_lineno=55,
                                end_col_offset=58)],
                            lineno=55,
                            col_offset=23,
                            end_lineno=55,
                            end_col_offset=58),
                          body=[
                            Assign(
                              targets=[
                                Name(
                                  id='known_file',
                                  ctx=Store(),
                                  lineno=56,
                                  col_offset=24,
                                  end_lineno=56,
                                  end_col_offset=34)],
                              value=Subscript(
                                value=Name(
                                  id='import_to_file_map',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=37,
                                  end_lineno=56,
                                  end_col_offset=55),
                                slice=Name(
                                  id='parent_import',
                                  ctx=Load(),
                                  lineno=56,
                                  col_offset=56,
                                  end_lineno=56,
                                  end_col_offset=69),
                                ctx=Load(),
                                lineno=56,
                                col_offset=37,
                                end_lineno=56,
                                end_col_offset=70),
                              lineno=56,
                              col_offset=24,
                              end_lineno=56,
                              end_col_offset=70)],
                          orelse=[],
                          lineno=55,
                          col_offset=20,
                          end_lineno=56,
                          end_col_offset=70),
                        Assign(
                          targets=[
                            Subscript(
                              value=Name(
                                id='all_imports_list',
                                ctx=Load(),
                                lineno=57,
                                col_offset=20,
                                end_lineno=57,
                                end_col_offset=36),
                              slice=Name(
                                id='used_import',
                                ctx=Load(),
                                lineno=57,
                                col_offset=37,
                                end_lineno=57,
                                end_col_offset=48),
                              ctx=Store(),
                              lineno=57,
                              col_offset=20,
                              end_lineno=57,
                              end_col_offset=49)],
                          value=Name(
                            id='known_file',
                            ctx=Load(),
                            lineno=57,
                            col_offset=52,
                            end_lineno=57,
                            end_col_offset=62),
                          lineno=57,
                          col_offset=20,
                          end_lineno=57,
                          end_col_offset=62)],
                      orelse=[],
                      lineno=52,
                      col_offset=16,
                      end_lineno=57,
                      end_col_offset=62)],
                  orelse=[],
                  lineno=48,
                  col_offset=12,
                  end_lineno=57,
                  end_col_offset=62)],
              orelse=[],
              lineno=47,
              col_offset=8,
              end_lineno=57,
              end_col_offset=62)],
          orelse=[],
          lineno=46,
          col_offset=4,
          end_lineno=57,
          end_col_offset=62),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=59,
            col_offset=11,
            end_lineno=59,
            end_col_offset=27),
          lineno=59,
          col_offset=4,
          end_lineno=59,
          end_col_offset=27)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=42,
          col_offset=5,
          end_lineno=42,
          end_col_offset=9),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=10,
              end_lineno=42,
              end_col_offset=13),
            Name(
              id='str',
              ctx=Load(),
              lineno=42,
              col_offset=15,
              end_lineno=42,
              end_col_offset=18)],
          ctx=Load(),
          lineno=42,
          col_offset=10,
          end_lineno=42,
          end_col_offset=18),
        ctx=Load(),
        lineno=42,
        col_offset=5,
        end_lineno=42,
        end_col_offset=19),
      lineno=39,
      col_offset=0,
      end_lineno=59,
      end_col_offset=27),
    FunctionDef(
      name='get_all_imports_from_files',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=62,
              col_offset=43,
              end_lineno=62,
              end_col_offset=46),
            lineno=62,
            col_offset=31,
            end_lineno=62,
            end_col_offset=46),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=62,
                col_offset=62,
                end_lineno=62,
                end_col_offset=66),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=62,
                col_offset=67,
                end_lineno=62,
                end_col_offset=70),
              ctx=Load(),
              lineno=62,
              col_offset=62,
              end_lineno=62,
              end_col_offset=71),
            lineno=62,
            col_offset=48,
            end_lineno=62,
            end_col_offset=71)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Constant(
            value="\n    This is kind of expensive for what it does\n    It's tricky not to require multiple passes to achieve what is being done here\n    ",
            lineno=63,
            col_offset=4,
            end_lineno=66,
            end_col_offset=7),
          lineno=63,
          col_offset=4,
          end_lineno=66,
          end_col_offset=7),
        Assign(
          targets=[
            Name(
              id='import_to_file_map',
              ctx=Store(),
              lineno=68,
              col_offset=4,
              end_lineno=68,
              end_col_offset=22)],
          value=Call(
            func=Name(
              id='_get_import_to_file_map',
              ctx=Load(),
              lineno=68,
              col_offset=25,
              end_lineno=68,
              end_col_offset=48),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=69,
                  col_offset=19,
                  end_lineno=69,
                  end_col_offset=29),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=69,
                  col_offset=44,
                  end_lineno=69,
                  end_col_offset=56),
                lineno=69,
                col_offset=31,
                end_lineno=69,
                end_col_offset=56)],
            lineno=68,
            col_offset=25,
            end_lineno=70,
            end_col_offset=5),
          lineno=68,
          col_offset=4,
          end_lineno=70,
          end_col_offset=5),
        Assign(
          targets=[
            Name(
              id='all_imports_list',
              ctx=Store(),
              lineno=72,
              col_offset=4,
              end_lineno=72,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_create_import_table',
              ctx=Load(),
              lineno=72,
              col_offset=23,
              end_lineno=72,
              end_col_offset=43),
            args=[],
            keywords=[
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=73,
                  col_offset=21,
                  end_lineno=73,
                  end_col_offset=33),
                lineno=73,
                col_offset=8,
                end_lineno=73,
                end_col_offset=33),
              keyword(
                arg='import_to_file_map',
                value=Name(
                  id='import_to_file_map',
                  ctx=Load(),
                  lineno=73,
                  col_offset=54,
                  end_lineno=73,
                  end_col_offset=72),
                lineno=73,
                col_offset=35,
                end_lineno=73,
                end_col_offset=72)],
            lineno=72,
            col_offset=23,
            end_lineno=74,
            end_col_offset=5),
          lineno=72,
          col_offset=4,
          end_lineno=74,
          end_col_offset=5),
        Return(
          value=Name(
            id='all_imports_list',
            ctx=Load(),
            lineno=76,
            col_offset=11,
            end_lineno=76,
            end_col_offset=27),
          lineno=76,
          col_offset=4,
          end_lineno=76,
          end_col_offset=27)],
      decorator_list=[],
      lineno=62,
      col_offset=0,
      end_lineno=76,
      end_col_offset=27)],
  type_ignores=[])
```
</details>

