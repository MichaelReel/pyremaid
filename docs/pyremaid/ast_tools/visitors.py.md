# ./src/pyremaid/ast_tools/visitors.py

### Imports

  - ast.AST
  - ast.Import
  - ast.ImportFrom
  - ast.Module
  - ast.NodeVisitor
  - models.MermaidBlock
  - models.MermaidElement
  - models.MermaidLink
  - models.MermaidNode
  - typing.Any
  - typing.Optional

---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x106916a30"]
  node_1["ast.ClassDef object at 0x1069164f0"]
  node_2["ast.Name object at 0x1069164c0"]
  node_3["ast.Load object at 0x1067e70d0"]
  node_4["ast.FunctionDef object at 0x106916490"]
  node_5["ast.arguments object at 0x106916460"]
  node_6["ast.arg object at 0x106916430"]
  node_7["ast.AnnAssign object at 0x106916400"]
  node_8["ast.Attribute object at 0x1069163d0"]
  node_9["ast.Name object at 0x1069163a0"]
  node_10["ast.Load object at 0x1067e70d0"]
  node_11["ast.Store object at 0x1067e7070"]
  node_12["ast.Subscript object at 0x106916370"]
  node_13["ast.Name object at 0x106916340"]
  node_14["ast.Load object at 0x1067e70d0"]
  node_15["ast.Name object at 0x106916310"]
  node_16["ast.Load object at 0x1067e70d0"]
  node_17["ast.Load object at 0x1067e70d0"]
  node_18["ast.List object at 0x1069162e0"]
  node_19["ast.Load object at 0x1067e70d0"]
  node_20["ast.Constant object at 0x1069162b0"]
  node_21["ast.FunctionDef object at 0x106916280"]
  node_22["ast.arguments object at 0x106916250"]
  node_23["ast.arg object at 0x106916220"]
  node_24["ast.arg object at 0x1069161f0"]
  node_25["ast.Name object at 0x1069161c0"]
  node_26["ast.Load object at 0x1067e70d0"]
  node_27["ast.For object at 0x106916190"]
  node_28["ast.Name object at 0x106916160"]
  node_29["ast.Store object at 0x1067e7070"]
  node_30["ast.Attribute object at 0x106916130"]
  node_31["ast.Name object at 0x106916100"]
  node_32["ast.Load object at 0x1067e70d0"]
  node_33["ast.Load object at 0x1067e70d0"]
  node_34["ast.Expr object at 0x1069160d0"]
  node_35["ast.Call object at 0x1069160a0"]
  node_36["ast.Attribute object at 0x106916070"]
  node_37["ast.Attribute object at 0x106916040"]
  node_38["ast.Name object at 0x106913fd0"]
  node_39["ast.Load object at 0x1067e70d0"]
  node_40["ast.Load object at 0x1067e70d0"]
  node_41["ast.Load object at 0x1067e70d0"]
  node_42["ast.JoinedStr object at 0x106913fa0"]
  node_43["ast.FormattedValue object at 0x106913f70"]
  node_44["ast.Attribute object at 0x106913f40"]
  node_45["ast.Name object at 0x106913f10"]
  node_46["ast.Load object at 0x1067e70d0"]
  node_47["ast.Load object at 0x1067e70d0"]
  node_48["ast.Constant object at 0x106913ee0"]
  node_49["ast.Constant object at 0x106913e50"]
  node_50["ast.FunctionDef object at 0x106913e20"]
  node_51["ast.arguments object at 0x106913df0"]
  node_52["ast.arg object at 0x106913dc0"]
  node_53["ast.arg object at 0x106913d90"]
  node_54["ast.Name object at 0x106913d60"]
  node_55["ast.Load object at 0x1067e70d0"]
  node_56["ast.Assign object at 0x106913d30"]
  node_57["ast.Name object at 0x106913d00"]
  node_58["ast.Store object at 0x1067e7070"]
  node_59["ast.Attribute object at 0x106913cd0"]
  node_60["ast.Name object at 0x106913ca0"]
  node_61["ast.Load object at 0x1067e70d0"]
  node_62["ast.Load object at 0x1067e70d0"]
  node_63["ast.For object at 0x106913c70"]
  node_64["ast.Name object at 0x106913c40"]
  node_65["ast.Store object at 0x1067e7070"]
  node_66["ast.Attribute object at 0x106913c10"]
  node_67["ast.Name object at 0x106913be0"]
  node_68["ast.Load object at 0x1067e70d0"]
  node_69["ast.Load object at 0x1067e70d0"]
  node_70["ast.Expr object at 0x106913bb0"]
  node_71["ast.Call object at 0x106913b80"]
  node_72["ast.Attribute object at 0x106913b50"]
  node_73["ast.Attribute object at 0x106913b20"]
  node_74["ast.Name object at 0x106913af0"]
  node_75["ast.Load object at 0x1067e70d0"]
  node_76["ast.Load object at 0x1067e70d0"]
  node_77["ast.Load object at 0x1067e70d0"]
  node_78["ast.JoinedStr object at 0x106913ac0"]
  node_79["ast.FormattedValue object at 0x106913a90"]
  node_80["ast.Name object at 0x106913a60"]
  node_81["ast.Load object at 0x1067e70d0"]
  node_82["ast.Constant object at 0x106913a30"]
  node_83["ast.FormattedValue object at 0x106913a00"]
  node_84["ast.Attribute object at 0x1069139d0"]
  node_85["ast.Name object at 0x1069139a0"]
  node_86["ast.Load object at 0x1067e70d0"]
  node_87["ast.Load object at 0x1067e70d0"]
  node_88["ast.Constant object at 0x106912eb0"]
  node_89["ast.FunctionDef object at 0x106912e80"]
  node_90["ast.arguments object at 0x106912e50"]
  node_91["ast.arg object at 0x106912e20"]
  node_92["ast.Return object at 0x106912df0"]
  node_93["ast.Attribute object at 0x106912dc0"]
  node_94["ast.Name object at 0x106912d90"]
  node_95["ast.Load object at 0x1067e70d0"]
  node_96["ast.Load object at 0x1067e70d0"]
  node_97["ast.Subscript object at 0x106912d30"]
  node_98["ast.Name object at 0x106912d00"]
  node_99["ast.Load object at 0x1067e70d0"]
  node_100["ast.Name object at 0x106912cd0"]
  node_101["ast.Load object at 0x1067e70d0"]
  node_102["ast.Load object at 0x1067e70d0"]
  node_103["ast.ClassDef object at 0x106912ca0"]
  node_104["ast.Name object at 0x106912c70"]
  node_105["ast.Load object at 0x1067e70d0"]
  node_106["ast.FunctionDef object at 0x106912c10"]
  node_107["ast.arguments object at 0x106912be0"]
  node_108["ast.arg object at 0x106912bb0"]
  node_109["ast.AnnAssign object at 0x106912b80"]
  node_110["ast.Attribute object at 0x106912b50"]
  node_111["ast.Name object at 0x106912b20"]
  node_112["ast.Load object at 0x1067e70d0"]
  node_113["ast.Store object at 0x1067e7070"]
  node_114["ast.Subscript object at 0x106912af0"]
  node_115["ast.Name object at 0x106912ac0"]
  node_116["ast.Load object at 0x1067e70d0"]
  node_117["ast.Name object at 0x106912a90"]
  node_118["ast.Load object at 0x1067e70d0"]
  node_119["ast.Load object at 0x1067e70d0"]
  node_120["ast.List object at 0x106912a60"]
  node_121["ast.Load object at 0x1067e70d0"]
  node_122["ast.AnnAssign object at 0x106912a30"]
  node_123["ast.Attribute object at 0x106912a00"]
  node_124["ast.Name object at 0x1069129d0"]
  node_125["ast.Load object at 0x1067e70d0"]
  node_126["ast.Store object at 0x1067e7070"]
  node_127["ast.Subscript object at 0x1069129a0"]
  node_128["ast.Name object at 0x106912970"]
  node_129["ast.Load object at 0x1067e70d0"]
  node_130["ast.Name object at 0x106912940"]
  node_131["ast.Load object at 0x1067e70d0"]
  node_132["ast.Load object at 0x1067e70d0"]
  node_133["ast.Constant object at 0x106912910"]
  node_134["ast.AnnAssign object at 0x1069128e0"]
  node_135["ast.Attribute object at 0x1069128b0"]
  node_136["ast.Name object at 0x106912880"]
  node_137["ast.Load object at 0x1067e70d0"]
  node_138["ast.Store object at 0x1067e7070"]
  node_139["ast.Name object at 0x106912850"]
  node_140["ast.Load object at 0x1067e70d0"]
  node_141["ast.Constant object at 0x106912820"]
  node_142["ast.Constant object at 0x1069127f0"]
  node_143["ast.FunctionDef object at 0x1069127c0"]
  node_144["ast.arguments object at 0x106912790"]
  node_145["ast.arg object at 0x106912760"]
  node_146["ast.arg object at 0x106912730"]
  node_147["ast.Name object at 0x106912700"]
  node_148["ast.Load object at 0x1067e70d0"]
  node_149["ast.Pass object at 0x1069126d0"]
  node_150["ast.Constant object at 0x106912670"]
  node_151["ast.FunctionDef object at 0x106912640"]
  node_152["ast.arguments object at 0x106912610"]
  node_153["ast.arg object at 0x1069125e0"]
  node_154["ast.arg object at 0x1069125b0"]
  node_155["ast.Name object at 0x106912580"]
  node_156["ast.Load object at 0x1067e70d0"]
  node_157["ast.Pass object at 0x106912550"]
  node_158["ast.Constant object at 0x1069124f0"]
  node_159["ast.FunctionDef object at 0x1069124c0"]
  node_160["ast.arguments object at 0x106912490"]
  node_161["ast.arg object at 0x106912460"]
  node_162["ast.arg object at 0x106912430"]
  node_163["ast.Name object at 0x106912400"]
  node_164["ast.Load object at 0x1067e70d0"]
  node_165["ast.Assign object at 0x1069123a0"]
  node_166["ast.Name object at 0x106912370"]
  node_167["ast.Store object at 0x1067e7070"]
  node_168["ast.Call object at 0x106912340"]
  node_169["ast.Name object at 0x106912310"]
  node_170["ast.Load object at 0x1067e70d0"]
  node_171["ast.keyword object at 0x1069122e0"]
  node_172["ast.Name object at 0x1069122b0"]
  node_173["ast.Load object at 0x1067e70d0"]
  node_174["ast.keyword object at 0x106912280"]
  node_175["ast.JoinedStr object at 0x106912250"]
  node_176["ast.Constant object at 0x106912220"]
  node_177["ast.FormattedValue object at 0x1069121f0"]
  node_178["ast.Attribute object at 0x1069121c0"]
  node_179["ast.Name object at 0x106912190"]
  node_180["ast.Load object at 0x1067e70d0"]
  node_181["ast.Load object at 0x1067e70d0"]
  node_182["ast.AugAssign object at 0x106912130"]
  node_183["ast.Attribute object at 0x106912100"]
  node_184["ast.Name object at 0x1069120d0"]
  node_185["ast.Load object at 0x1067e70d0"]
  node_186["ast.Store object at 0x1067e7070"]
  node_187["ast.Add object at 0x1067e7760"]
  node_188["ast.Constant object at 0x1069120a0"]
  node_189["ast.If object at 0x106912070"]
  node_190["ast.Attribute object at 0x106912040"]
  node_191["ast.Name object at 0x106911fd0"]
  node_192["ast.Load object at 0x1067e70d0"]
  node_193["ast.Load object at 0x1067e70d0"]
  node_194["ast.Expr object at 0x106911fa0"]
  node_195["ast.Call object at 0x106911f70"]
  node_196["ast.Attribute object at 0x106911f40"]
  node_197["ast.Attribute object at 0x106911f10"]
  node_198["ast.Name object at 0x106911ee0"]
  node_199["ast.Load object at 0x1067e70d0"]
  node_200["ast.Load object at 0x1067e70d0"]
  node_201["ast.Load object at 0x1067e70d0"]
  node_202["ast.Call object at 0x106911eb0"]
  node_203["ast.Name object at 0x106911e80"]
  node_204["ast.Load object at 0x1067e70d0"]
  node_205["ast.keyword object at 0x106911e50"]
  node_206["ast.Attribute object at 0x106911e20"]
  node_207["ast.Name object at 0x106911df0"]
  node_208["ast.Load object at 0x1067e70d0"]
  node_209["ast.Load object at 0x1067e70d0"]
  node_210["ast.keyword object at 0x106911dc0"]
  node_211["ast.Name object at 0x106911d90"]
  node_212["ast.Load object at 0x1067e70d0"]
  node_213["ast.Assign object at 0x106911d30"]
  node_214["ast.Attribute object at 0x106911d00"]
  node_215["ast.Name object at 0x106911cd0"]
  node_216["ast.Load object at 0x1067e70d0"]
  node_217["ast.Store object at 0x1067e7070"]
  node_218["ast.Name object at 0x106911ca0"]
  node_219["ast.Load object at 0x1067e70d0"]
  node_220["ast.Return object at 0x106911c70"]
  node_221["ast.Call object at 0x106911c40"]
  node_222["ast.Attribute object at 0x106911c10"]
  node_223["ast.Call object at 0x106911be0"]
  node_224["ast.Name object at 0x106911bb0"]
  node_225["ast.Load object at 0x1067e70d0"]
  node_226["ast.Load object at 0x1067e70d0"]
  node_227["ast.Name object at 0x106911b80"]
  node_228["ast.Load object at 0x1067e70d0"]
  node_229["ast.Name object at 0x106911b20"]
  node_230["ast.Load object at 0x1067e70d0"]
  node_231["ast.FunctionDef object at 0x106911af0"]
  node_232["ast.arguments object at 0x106911ac0"]
  node_233["ast.arg object at 0x106911a90"]
  node_234["ast.Return object at 0x106911a60"]
  node_235["ast.Attribute object at 0x106911a30"]
  node_236["ast.Name object at 0x106911a00"]
  node_237["ast.Load object at 0x1067e70d0"]
  node_238["ast.Load object at 0x1067e70d0"]
  node_239["ast.Subscript object at 0x1069119a0"]
  node_240["ast.Name object at 0x106911970"]
  node_241["ast.Load object at 0x1067e70d0"]
  node_242["ast.Name object at 0x106911940"]
  node_243["ast.Load object at 0x1067e70d0"]
  node_244["ast.Load object at 0x1067e70d0"]
  node_245["ast.ClassDef object at 0x106911910"]
  node_246["ast.Name object at 0x1069118e0"]
  node_247["ast.Load object at 0x1067e70d0"]
  node_248["ast.FunctionDef object at 0x106911880"]
  node_249["ast.arguments object at 0x106911850"]
  node_250["ast.arg object at 0x106911820"]
  node_251["ast.AnnAssign object at 0x1069117f0"]
  node_252["ast.Attribute object at 0x1069117c0"]
  node_253["ast.Name object at 0x106911790"]
  node_254["ast.Load object at 0x1067e70d0"]
  node_255["ast.Store object at 0x1067e7070"]
  node_256["ast.Subscript object at 0x106911760"]
  node_257["ast.Name object at 0x106911730"]
  node_258["ast.Load object at 0x1067e70d0"]
  node_259["ast.Name object at 0x106911700"]
  node_260["ast.Load object at 0x1067e70d0"]
  node_261["ast.Load object at 0x1067e70d0"]
  node_262["ast.List object at 0x106911160"]
  node_263["ast.Load object at 0x1067e70d0"]
  node_264["ast.AnnAssign object at 0x106911130"]
  node_265["ast.Attribute object at 0x106911100"]
  node_266["ast.Name object at 0x1069110d0"]
  node_267["ast.Load object at 0x1067e70d0"]
  node_268["ast.Store object at 0x1067e7070"]
  node_269["ast.Name object at 0x1069110a0"]
  node_270["ast.Load object at 0x1067e70d0"]
  node_271["ast.Constant object at 0x106911070"]
  node_272["ast.Constant object at 0x106911040"]
  node_273["ast.FunctionDef object at 0x106910fd0"]
  node_274["ast.arguments object at 0x106910fa0"]
  node_275["ast.arg object at 0x106910f70"]
  node_276["ast.Assign object at 0x106910f40"]
  node_277["ast.Name object at 0x106910f10"]
  node_278["ast.Store object at 0x1067e7070"]
  node_279["ast.Attribute object at 0x106910ee0"]
  node_280["ast.Name object at 0x106910eb0"]
  node_281["ast.Load object at 0x1067e70d0"]
  node_282["ast.Load object at 0x1067e70d0"]
  node_283["ast.AugAssign object at 0x106910e80"]
  node_284["ast.Attribute object at 0x106910e50"]
  node_285["ast.Name object at 0x106910e20"]
  node_286["ast.Load object at 0x1067e70d0"]
  node_287["ast.Store object at 0x1067e7070"]
  node_288["ast.Add object at 0x1067e7760"]
  node_289["ast.Constant object at 0x106910df0"]
  node_290["ast.Return object at 0x106910dc0"]
  node_291["ast.Name object at 0x106910d90"]
  node_292["ast.Load object at 0x1067e70d0"]
  node_293["ast.Name object at 0x106910d30"]
  node_294["ast.Load object at 0x1067e70d0"]
  node_295["ast.FunctionDef object at 0x106910d00"]
  node_296["ast.arguments object at 0x106910cd0"]
  node_297["ast.arg object at 0x106910ca0"]
  node_298["ast.arg object at 0x106910c70"]
  node_299["ast.Name object at 0x106910c40"]
  node_300["ast.Load object at 0x1067e70d0"]
  node_301["ast.Expr object at 0x106910be0"]
  node_302["ast.Constant object at 0x106910bb0"]
  node_303["ast.Assign object at 0x106910b50"]
  node_304["ast.Name object at 0x106910b20"]
  node_305["ast.Store object at 0x1067e7070"]
  node_306["ast.Call object at 0x106910af0"]
  node_307["ast.Name object at 0x106910ac0"]
  node_308["ast.Load object at 0x1067e70d0"]
  node_309["ast.Expr object at 0x106910a90"]
  node_310["ast.Call object at 0x106910a60"]
  node_311["ast.Attribute object at 0x106910a30"]
  node_312["ast.Name object at 0x106910a00"]
  node_313["ast.Load object at 0x1067e70d0"]
  node_314["ast.Load object at 0x1067e70d0"]
  node_315["ast.keyword object at 0x1069109d0"]
  node_316["ast.Name object at 0x1069109a0"]
  node_317["ast.Load object at 0x1067e70d0"]
  node_318["ast.Assign object at 0x106910940"]
  node_319["ast.Name object at 0x106910910"]
  node_320["ast.Store object at 0x1067e7070"]
  node_321["ast.Call object at 0x1069108e0"]
  node_322["ast.Name object at 0x1069108b0"]
  node_323["ast.Load object at 0x1067e70d0"]
  node_324["ast.keyword object at 0x106910880"]
  node_325["ast.Name object at 0x106910850"]
  node_326["ast.Load object at 0x1067e70d0"]
  node_327["ast.keyword object at 0x106910820"]
  node_328["ast.JoinedStr object at 0x1069107f0"]
  node_329["ast.Constant object at 0x1069107c0"]
  node_330["ast.FormattedValue object at 0x106910790"]
  node_331["ast.Call object at 0x106910760"]
  node_332["ast.Attribute object at 0x106910730"]
  node_333["ast.Name object at 0x106910700"]
  node_334["ast.Load object at 0x1067e70d0"]
  node_335["ast.Load object at 0x1067e70d0"]
  node_336["ast.keyword object at 0x1069106a0"]
  node_337["ast.Call object at 0x106910670"]
  node_338["ast.Attribute object at 0x106910640"]
  node_339["ast.Name object at 0x106910610"]
  node_340["ast.Load object at 0x1067e70d0"]
  node_341["ast.Load object at 0x1067e70d0"]
  node_342["ast.Expr object at 0x1069105e0"]
  node_343["ast.Call object at 0x1069105b0"]
  node_344["ast.Attribute object at 0x106910580"]
  node_345["ast.Attribute object at 0x106910550"]
  node_346["ast.Name object at 0x1069102e0"]
  node_347["ast.Load object at 0x1067e70d0"]
  node_348["ast.Load object at 0x1067e70d0"]
  node_349["ast.Load object at 0x1067e70d0"]
  node_350["ast.Name object at 0x1069102b0"]
  node_351["ast.Load object at 0x1067e70d0"]
  node_352["ast.Name object at 0x106910250"]
  node_353["ast.Load object at 0x1067e70d0"]
  node_354["ast.FunctionDef object at 0x106910220"]
  node_355["ast.arguments object at 0x1069101f0"]
  node_356["ast.arg object at 0x1069101c0"]
  node_357["ast.arg object at 0x106910190"]
  node_358["ast.Name object at 0x106910160"]
  node_359["ast.Load object at 0x1067e70d0"]
  node_360["ast.Expr object at 0x106910130"]
  node_361["ast.Constant object at 0x106910100"]
  node_362["ast.Pass object at 0x1069100a0"]
  node_363["ast.Name object at 0x106910040"]
  node_364["ast.Load object at 0x1067e70d0"]
  node_365["ast.FunctionDef object at 0x10690ffd0"]
  node_366["ast.arguments object at 0x10690ffa0"]
  node_367["ast.arg object at 0x10690ff70"]
  node_368["ast.Return object at 0x10690ff40"]
  node_369["ast.Attribute object at 0x10690ff10"]
  node_370["ast.Name object at 0x10690fee0"]
  node_371["ast.Load object at 0x1067e70d0"]
  node_372["ast.Load object at 0x1067e70d0"]
  node_373["ast.Subscript object at 0x10690fe80"]
  node_374["ast.Name object at 0x10690fe50"]
  node_375["ast.Load object at 0x1067e70d0"]
  node_376["ast.Name object at 0x10690fe20"]
  node_377["ast.Load object at 0x1067e70d0"]
  node_378["ast.Load object at 0x1067e70d0"]

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
  node_353 --> node_354
  node_354 --> node_355
  node_355 --> node_356
  node_356 --> node_357
  node_357 --> node_358
  node_358 --> node_359
  node_359 --> node_360
  node_360 --> node_361
  node_361 --> node_362
  node_362 --> node_363
  node_363 --> node_364
  node_364 --> node_365
  node_365 --> node_366
  node_366 --> node_367
  node_367 --> node_368
  node_368 --> node_369
  node_369 --> node_370
  node_370 --> node_371
  node_371 --> node_372
  node_372 --> node_373
  node_373 --> node_374
  node_374 --> node_375
  node_375 --> node_376
  node_376 --> node_377
  node_377 --> node_378

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
        alias(name='Import'),
        alias(name='ImportFrom'),
        alias(name='Module'),
        alias(name='NodeVisitor')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=60),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidBlock'),
        alias(name='MermaidElement'),
        alias(name='MermaidLink'),
        alias(name='MermaidNode')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=73),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Any'),
        alias(name='Optional')],
      level=0,
      lineno=3,
      col_offset=0,
      end_lineno=3,
      end_col_offset=32),
    ClassDef(
      name='ImportNodeFinder',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=6,
          col_offset=23,
          end_lineno=6,
          end_col_offset=34)],
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
                attr='found_imports',
                ctx=Store(),
                lineno=8,
                col_offset=8,
                end_lineno=8,
                end_col_offset=26),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=8,
                  col_offset=29,
                  end_lineno=8,
                  end_col_offset=33),
                slice=Name(
                  id='str',
                  ctx=Load(),
                  lineno=8,
                  col_offset=34,
                  end_lineno=8,
                  end_col_offset=37),
                ctx=Load(),
                lineno=8,
                col_offset=29,
                end_lineno=8,
                end_col_offset=38),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=8,
                col_offset=41,
                end_lineno=8,
                end_col_offset=43),
              simple=0,
              lineno=8,
              col_offset=8,
              end_lineno=8,
              end_col_offset=43)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=7,
            col_offset=26,
            end_lineno=7,
            end_col_offset=30),
          lineno=7,
          col_offset=4,
          end_lineno=8,
          end_col_offset=43),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=10,
                col_offset=21,
                end_lineno=10,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=10,
                  col_offset=33,
                  end_lineno=10,
                  end_col_offset=39),
                lineno=10,
                col_offset=27,
                end_lineno=10,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=11,
                col_offset=12,
                end_lineno=11,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=11,
                  col_offset=17,
                  end_lineno=11,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=11,
                col_offset=17,
                end_lineno=11,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=12,
                          col_offset=12,
                          end_lineno=12,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=12,
                        col_offset=12,
                        end_lineno=12,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=12,
                      col_offset=12,
                      end_lineno=12,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=12,
                                col_offset=41,
                                end_lineno=12,
                                end_col_offset=42),
                              attr='name',
                              ctx=Load(),
                              lineno=12,
                              col_offset=41,
                              end_lineno=12,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=12,
                            col_offset=38,
                            end_lineno=12,
                            end_col_offset=51),
                          Constant(
                            value='.*',
                            lineno=12,
                            col_offset=38,
                            end_lineno=12,
                            end_col_offset=51)],
                        lineno=12,
                        col_offset=38,
                        end_lineno=12,
                        end_col_offset=51)],
                    keywords=[],
                    lineno=12,
                    col_offset=12,
                    end_lineno=12,
                    end_col_offset=52),
                  lineno=12,
                  col_offset=12,
                  end_lineno=12,
                  end_col_offset=52)],
              orelse=[],
              lineno=11,
              col_offset=8,
              end_lineno=12,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=10,
            col_offset=44,
            end_lineno=10,
            end_col_offset=48),
          lineno=10,
          col_offset=4,
          end_lineno=12,
          end_col_offset=52),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=14,
                col_offset=25,
                end_lineno=14,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=14,
                  col_offset=37,
                  end_lineno=14,
                  end_col_offset=47),
                lineno=14,
                col_offset=31,
                end_lineno=14,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='module',
                  ctx=Store(),
                  lineno=15,
                  col_offset=8,
                  end_lineno=15,
                  end_col_offset=14)],
              value=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=15,
                  col_offset=17,
                  end_lineno=15,
                  end_col_offset=21),
                attr='module',
                ctx=Load(),
                lineno=15,
                col_offset=17,
                end_lineno=15,
                end_col_offset=28),
              lineno=15,
              col_offset=8,
              end_lineno=15,
              end_col_offset=28),
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=16,
                col_offset=12,
                end_lineno=16,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=16,
                  col_offset=17,
                  end_lineno=16,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=16,
                col_offset=17,
                end_lineno=16,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=17,
                          col_offset=12,
                          end_lineno=17,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=17,
                        col_offset=12,
                        end_lineno=17,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=17,
                      col_offset=12,
                      end_lineno=17,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Name(
                              id='module',
                              ctx=Load(),
                              lineno=17,
                              col_offset=41,
                              end_lineno=17,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=17,
                            col_offset=38,
                            end_lineno=17,
                            end_col_offset=58),
                          Constant(
                            value='.',
                            lineno=17,
                            col_offset=38,
                            end_lineno=17,
                            end_col_offset=58),
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=17,
                                col_offset=50,
                                end_lineno=17,
                                end_col_offset=51),
                              attr='name',
                              ctx=Load(),
                              lineno=17,
                              col_offset=50,
                              end_lineno=17,
                              end_col_offset=56),
                            conversion=-1,
                            lineno=17,
                            col_offset=38,
                            end_lineno=17,
                            end_col_offset=58)],
                        lineno=17,
                        col_offset=38,
                        end_lineno=17,
                        end_col_offset=58)],
                    keywords=[],
                    lineno=17,
                    col_offset=12,
                    end_lineno=17,
                    end_col_offset=59),
                  lineno=17,
                  col_offset=12,
                  end_lineno=17,
                  end_col_offset=59)],
              orelse=[],
              lineno=16,
              col_offset=8,
              end_lineno=17,
              end_col_offset=59)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=14,
            col_offset=52,
            end_lineno=14,
            end_col_offset=56),
          lineno=14,
          col_offset=4,
          end_lineno=17,
          end_col_offset=59),
        FunctionDef(
          name='get_found_imports',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=19,
                col_offset=26,
                end_lineno=19,
                end_col_offset=30)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=20,
                  col_offset=15,
                  end_lineno=20,
                  end_col_offset=19),
                attr='found_imports',
                ctx=Load(),
                lineno=20,
                col_offset=15,
                end_lineno=20,
                end_col_offset=33),
              lineno=20,
              col_offset=8,
              end_lineno=20,
              end_col_offset=33)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=19,
              col_offset=35,
              end_lineno=19,
              end_col_offset=39),
            slice=Name(
              id='str',
              ctx=Load(),
              lineno=19,
              col_offset=40,
              end_lineno=19,
              end_col_offset=43),
            ctx=Load(),
            lineno=19,
            col_offset=35,
            end_lineno=19,
            end_col_offset=44),
          lineno=19,
          col_offset=4,
          end_lineno=20,
          end_col_offset=33)],
      decorator_list=[],
      lineno=6,
      col_offset=0,
      end_lineno=20,
      end_col_offset=33),
    ClassDef(
      name='LinkGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=23,
          col_offset=20,
          end_lineno=23,
          end_col_offset=31)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=24,
                col_offset=17,
                end_lineno=24,
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
                  lineno=25,
                  col_offset=8,
                  end_lineno=25,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=25,
                col_offset=8,
                end_lineno=25,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=25,
                  col_offset=24,
                  end_lineno=25,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=25,
                  col_offset=29,
                  end_lineno=25,
                  end_col_offset=43),
                ctx=Load(),
                lineno=25,
                col_offset=24,
                end_lineno=25,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=25,
                col_offset=47,
                end_lineno=25,
                end_col_offset=49),
              simple=0,
              lineno=25,
              col_offset=8,
              end_lineno=25,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=26,
                  col_offset=8,
                  end_lineno=26,
                  end_col_offset=12),
                attr='prev_node',
                ctx=Store(),
                lineno=26,
                col_offset=8,
                end_lineno=26,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='Optional',
                  ctx=Load(),
                  lineno=26,
                  col_offset=25,
                  end_lineno=26,
                  end_col_offset=33),
                slice=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=26,
                  col_offset=34,
                  end_lineno=26,
                  end_col_offset=37),
                ctx=Load(),
                lineno=26,
                col_offset=25,
                end_lineno=26,
                end_col_offset=38),
              value=Constant(
                value=None,
                lineno=26,
                col_offset=41,
                end_lineno=26,
                end_col_offset=45),
              simple=0,
              lineno=26,
              col_offset=8,
              end_lineno=26,
              end_col_offset=45),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=27,
                col_offset=8,
                end_lineno=27,
                end_col_offset=18),
              annotation=Name(
                id='int',
                ctx=Load(),
                lineno=27,
                col_offset=21,
                end_lineno=27,
                end_col_offset=24),
              value=Constant(
                value=0,
                lineno=27,
                col_offset=27,
                end_lineno=27,
                end_col_offset=28),
              simple=0,
              lineno=27,
              col_offset=8,
              end_lineno=27,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=24,
            col_offset=26,
            end_lineno=24,
            end_col_offset=30),
          lineno=24,
          col_offset=4,
          end_lineno=27,
          end_col_offset=28),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=29,
                col_offset=21,
                end_lineno=29,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=29,
                  col_offset=33,
                  end_lineno=29,
                  end_col_offset=39),
                lineno=29,
                col_offset=27,
                end_lineno=29,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=30,
              col_offset=8,
              end_lineno=30,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=29,
            col_offset=44,
            end_lineno=29,
            end_col_offset=48),
          lineno=29,
          col_offset=4,
          end_lineno=30,
          end_col_offset=12),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=32,
                col_offset=25,
                end_lineno=32,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=32,
                  col_offset=37,
                  end_lineno=32,
                  end_col_offset=47),
                lineno=32,
                col_offset=31,
                end_lineno=32,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=33,
              col_offset=8,
              end_lineno=33,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=32,
            col_offset=52,
            end_lineno=32,
            end_col_offset=56),
          lineno=32,
          col_offset=4,
          end_lineno=33,
          end_col_offset=12),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=35,
                col_offset=22,
                end_lineno=35,
                end_col_offset=26),
              arg(
                arg='node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=35,
                  col_offset=34,
                  end_lineno=35,
                  end_col_offset=37),
                lineno=35,
                col_offset=28,
                end_lineno=35,
                end_col_offset=37)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='mermaid_data',
                  ctx=Store(),
                  lineno=36,
                  col_offset=8,
                  end_lineno=36,
                  end_col_offset=20)],
              value=Call(
                func=Name(
                  id='MermaidNode',
                  ctx=Load(),
                  lineno=36,
                  col_offset=23,
                  end_lineno=36,
                  end_col_offset=34),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='node',
                      ctx=Load(),
                      lineno=37,
                      col_offset=21,
                      end_lineno=37,
                      end_col_offset=25),
                    lineno=37,
                    col_offset=12,
                    end_lineno=37,
                    end_col_offset=25),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        Constant(
                          value='node_',
                          lineno=38,
                          col_offset=30,
                          end_lineno=38,
                          end_col_offset=50),
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=38,
                              col_offset=38,
                              end_lineno=38,
                              end_col_offset=42),
                            attr='count',
                            ctx=Load(),
                            lineno=38,
                            col_offset=38,
                            end_lineno=38,
                            end_col_offset=48),
                          conversion=-1,
                          lineno=38,
                          col_offset=30,
                          end_lineno=38,
                          end_col_offset=50)],
                      lineno=38,
                      col_offset=30,
                      end_lineno=38,
                      end_col_offset=50),
                    lineno=38,
                    col_offset=12,
                    end_lineno=38,
                    end_col_offset=50)],
                lineno=36,
                col_offset=23,
                end_lineno=39,
                end_col_offset=9),
              lineno=36,
              col_offset=8,
              end_lineno=39,
              end_col_offset=9),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=40,
                  col_offset=8,
                  end_lineno=40,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=40,
                col_offset=8,
                end_lineno=40,
                end_col_offset=18),
              op=Add(),
              value=Constant(
                value=1,
                lineno=40,
                col_offset=22,
                end_lineno=40,
                end_col_offset=23),
              lineno=40,
              col_offset=8,
              end_lineno=40,
              end_col_offset=23),
            If(
              test=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=41,
                  col_offset=11,
                  end_lineno=41,
                  end_col_offset=15),
                attr='prev_node',
                ctx=Load(),
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=42,
                          col_offset=12,
                          end_lineno=42,
                          end_col_offset=16),
                        attr='elements',
                        ctx=Load(),
                        lineno=42,
                        col_offset=12,
                        end_lineno=42,
                        end_col_offset=25),
                      attr='append',
                      ctx=Load(),
                      lineno=42,
                      col_offset=12,
                      end_lineno=42,
                      end_col_offset=32),
                    args=[
                      Call(
                        func=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=42,
                          col_offset=33,
                          end_lineno=42,
                          end_col_offset=44),
                        args=[],
                        keywords=[
                          keyword(
                            arg='from_',
                            value=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=42,
                                col_offset=51,
                                end_lineno=42,
                                end_col_offset=55),
                              attr='prev_node',
                              ctx=Load(),
                              lineno=42,
                              col_offset=51,
                              end_lineno=42,
                              end_col_offset=65),
                            lineno=42,
                            col_offset=45,
                            end_lineno=42,
                            end_col_offset=65),
                          keyword(
                            arg='to',
                            value=Name(
                              id='mermaid_data',
                              ctx=Load(),
                              lineno=42,
                              col_offset=70,
                              end_lineno=42,
                              end_col_offset=82),
                            lineno=42,
                            col_offset=67,
                            end_lineno=42,
                            end_col_offset=82)],
                        lineno=42,
                        col_offset=33,
                        end_lineno=42,
                        end_col_offset=83)],
                    keywords=[],
                    lineno=42,
                    col_offset=12,
                    end_lineno=42,
                    end_col_offset=84),
                  lineno=42,
                  col_offset=12,
                  end_lineno=42,
                  end_col_offset=84)],
              orelse=[],
              lineno=41,
              col_offset=8,
              end_lineno=42,
              end_col_offset=84),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=43,
                    col_offset=8,
                    end_lineno=43,
                    end_col_offset=12),
                  attr='prev_node',
                  ctx=Store(),
                  lineno=43,
                  col_offset=8,
                  end_lineno=43,
                  end_col_offset=22)],
              value=Name(
                id='mermaid_data',
                ctx=Load(),
                lineno=43,
                col_offset=25,
                end_lineno=43,
                end_col_offset=37),
              lineno=43,
              col_offset=8,
              end_lineno=43,
              end_col_offset=37),
            Return(
              value=Call(
                func=Attribute(
                  value=Call(
                    func=Name(
                      id='super',
                      ctx=Load(),
                      lineno=46,
                      col_offset=15,
                      end_lineno=46,
                      end_col_offset=20),
                    args=[],
                    keywords=[],
                    lineno=46,
                    col_offset=15,
                    end_lineno=46,
                    end_col_offset=22),
                  attr='generic_visit',
                  ctx=Load(),
                  lineno=46,
                  col_offset=15,
                  end_lineno=46,
                  end_col_offset=36),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=46,
                    col_offset=37,
                    end_lineno=46,
                    end_col_offset=41)],
                keywords=[],
                lineno=46,
                col_offset=15,
                end_lineno=46,
                end_col_offset=42),
              lineno=46,
              col_offset=8,
              end_lineno=46,
              end_col_offset=42)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=35,
            col_offset=42,
            end_lineno=35,
            end_col_offset=45),
          lineno=35,
          col_offset=4,
          end_lineno=46,
          end_col_offset=42),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=48,
                col_offset=29,
                end_lineno=48,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=49,
                  col_offset=15,
                  end_lineno=49,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=49,
                col_offset=15,
                end_lineno=49,
                end_col_offset=28),
              lineno=49,
              col_offset=8,
              end_lineno=49,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=48,
              col_offset=38,
              end_lineno=48,
              end_col_offset=42),
            slice=Name(
              id='MermaidLink',
              ctx=Load(),
              lineno=48,
              col_offset=43,
              end_lineno=48,
              end_col_offset=54),
            ctx=Load(),
            lineno=48,
            col_offset=38,
            end_lineno=48,
            end_col_offset=55),
          lineno=48,
          col_offset=4,
          end_lineno=49,
          end_col_offset=28)],
      decorator_list=[],
      lineno=23,
      col_offset=0,
      end_lineno=49,
      end_col_offset=28),
    ClassDef(
      name='BlockGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=52,
          col_offset=21,
          end_lineno=52,
          end_col_offset=32)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=53,
                col_offset=17,
                end_lineno=53,
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
                  lineno=54,
                  col_offset=8,
                  end_lineno=54,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=54,
                col_offset=8,
                end_lineno=54,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=54,
                  col_offset=24,
                  end_lineno=54,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=54,
                  col_offset=29,
                  end_lineno=54,
                  end_col_offset=43),
                ctx=Load(),
                lineno=54,
                col_offset=24,
                end_lineno=54,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=54,
                col_offset=47,
                end_lineno=54,
                end_col_offset=49),
              simple=0,
              lineno=54,
              col_offset=8,
              end_lineno=54,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=55,
                  col_offset=8,
                  end_lineno=55,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=55,
                col_offset=8,
                end_lineno=55,
                end_col_offset=18),
              annotation=Name(
                id='int',
                ctx=Load(),
                lineno=55,
                col_offset=21,
                end_lineno=55,
                end_col_offset=24),
              value=Constant(
                value=0,
                lineno=55,
                col_offset=27,
                end_lineno=55,
                end_col_offset=28),
              simple=0,
              lineno=55,
              col_offset=8,
              end_lineno=55,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=53,
            col_offset=26,
            end_lineno=53,
            end_col_offset=30),
          lineno=53,
          col_offset=4,
          end_lineno=55,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=57,
                col_offset=15,
                end_lineno=57,
                end_col_offset=19)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='value',
                  ctx=Store(),
                  lineno=58,
                  col_offset=8,
                  end_lineno=58,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=58,
                  col_offset=16,
                  end_lineno=58,
                  end_col_offset=20),
                attr='count',
                ctx=Load(),
                lineno=58,
                col_offset=16,
                end_lineno=58,
                end_col_offset=26),
              lineno=58,
              col_offset=8,
              end_lineno=58,
              end_col_offset=26),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=59,
                  col_offset=8,
                  end_lineno=59,
                  end_col_offset=12),
                attr='count',
                ctx=Store(),
                lineno=59,
                col_offset=8,
                end_lineno=59,
                end_col_offset=18),
              op=Add(),
              value=Constant(
                value=1,
                lineno=59,
                col_offset=21,
                end_lineno=59,
                end_col_offset=22),
              lineno=59,
              col_offset=8,
              end_lineno=59,
              end_col_offset=22),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=60,
                col_offset=15,
                end_lineno=60,
                end_col_offset=20),
              lineno=60,
              col_offset=8,
              end_lineno=60,
              end_col_offset=20)],
          decorator_list=[],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=57,
            col_offset=24,
            end_lineno=57,
            end_col_offset=27),
          lineno=57,
          col_offset=4,
          end_lineno=60,
          end_col_offset=20),
        FunctionDef(
          name='visit_Module',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=62,
                col_offset=21,
                end_lineno=62,
                end_col_offset=25),
              arg(
                arg='block_node',
                annotation=Name(
                  id='Module',
                  ctx=Load(),
                  lineno=62,
                  col_offset=39,
                  end_lineno=62,
                  end_col_offset=45),
                lineno=62,
                col_offset=27,
                end_lineno=62,
                end_col_offset=45)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we might want a subgraph, so parse content',
                lineno=63,
                col_offset=8,
                end_lineno=63,
                end_col_offset=73),
              lineno=63,
              col_offset=8,
              end_lineno=63,
              end_col_offset=73),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=64,
                  col_offset=8,
                  end_lineno=64,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=64,
                  col_offset=25,
                  end_lineno=64,
                  end_col_offset=38),
                args=[],
                keywords=[],
                lineno=64,
                col_offset=25,
                end_lineno=64,
                end_col_offset=40),
              lineno=64,
              col_offset=8,
              end_lineno=64,
              end_col_offset=40),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='link_generator',
                    ctx=Load(),
                    lineno=65,
                    col_offset=8,
                    end_lineno=65,
                    end_col_offset=22),
                  attr='visit',
                  ctx=Load(),
                  lineno=65,
                  col_offset=8,
                  end_lineno=65,
                  end_col_offset=28),
                args=[],
                keywords=[
                  keyword(
                    arg='node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=65,
                      col_offset=34,
                      end_lineno=65,
                      end_col_offset=44),
                    lineno=65,
                    col_offset=29,
                    end_lineno=65,
                    end_col_offset=44)],
                lineno=65,
                col_offset=8,
                end_lineno=65,
                end_col_offset=45),
              lineno=65,
              col_offset=8,
              end_lineno=65,
              end_col_offset=45),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=67,
                  col_offset=8,
                  end_lineno=67,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidBlock',
                  ctx=Load(),
                  lineno=67,
                  col_offset=24,
                  end_lineno=67,
                  end_col_offset=36),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=68,
                      col_offset=23,
                      end_lineno=68,
                      end_col_offset=33),
                    lineno=68,
                    col_offset=12,
                    end_lineno=68,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        Constant(
                          value='module_',
                          lineno=69,
                          col_offset=32,
                          end_lineno=69,
                          end_col_offset=57),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=69,
                                col_offset=42,
                                end_lineno=69,
                                end_col_offset=46),
                              attr='_count',
                              ctx=Load(),
                              lineno=69,
                              col_offset=42,
                              end_lineno=69,
                              end_col_offset=53),
                            args=[],
                            keywords=[],
                            lineno=69,
                            col_offset=42,
                            end_lineno=69,
                            end_col_offset=55),
                          conversion=-1,
                          lineno=69,
                          col_offset=32,
                          end_lineno=69,
                          end_col_offset=57)],
                      lineno=69,
                      col_offset=32,
                      end_lineno=69,
                      end_col_offset=57),
                    lineno=69,
                    col_offset=12,
                    end_lineno=69,
                    end_col_offset=57),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=70,
                          col_offset=29,
                          end_lineno=70,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=70,
                        col_offset=29,
                        end_lineno=70,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=70,
                      col_offset=29,
                      end_lineno=70,
                      end_col_offset=66),
                    lineno=70,
                    col_offset=12,
                    end_lineno=70,
                    end_col_offset=66)],
                lineno=67,
                col_offset=24,
                end_lineno=71,
                end_col_offset=9),
              lineno=67,
              col_offset=8,
              end_lineno=71,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=73,
                      col_offset=8,
                      end_lineno=73,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=73,
                    col_offset=8,
                    end_lineno=73,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=73,
                  col_offset=8,
                  end_lineno=73,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=73,
                    col_offset=29,
                    end_lineno=73,
                    end_col_offset=42)],
                keywords=[],
                lineno=73,
                col_offset=8,
                end_lineno=73,
                end_col_offset=43),
              lineno=73,
              col_offset=8,
              end_lineno=73,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=62,
            col_offset=50,
            end_lineno=62,
            end_col_offset=53),
          lineno=62,
          col_offset=4,
          end_lineno=73,
          end_col_offset=43),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=75,
                col_offset=22,
                end_lineno=75,
                end_col_offset=26),
              arg(
                arg='_node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=75,
                  col_offset=35,
                  end_lineno=75,
                  end_col_offset=38),
                lineno=75,
                col_offset=28,
                end_lineno=75,
                end_col_offset=38)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='Non block nodes are not interesting here',
                lineno=76,
                col_offset=8,
                end_lineno=76,
                end_col_offset=54),
              lineno=76,
              col_offset=8,
              end_lineno=76,
              end_col_offset=54),
            Pass(
              lineno=77,
              col_offset=8,
              end_lineno=77,
              end_col_offset=12)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=75,
            col_offset=43,
            end_lineno=75,
            end_col_offset=46),
          lineno=75,
          col_offset=4,
          end_lineno=77,
          end_col_offset=12),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=79,
                col_offset=29,
                end_lineno=79,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=80,
                  col_offset=15,
                  end_lineno=80,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=80,
                col_offset=15,
                end_lineno=80,
                end_col_offset=28),
              lineno=80,
              col_offset=8,
              end_lineno=80,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=79,
              col_offset=38,
              end_lineno=79,
              end_col_offset=42),
            slice=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=79,
              col_offset=43,
              end_lineno=79,
              end_col_offset=57),
            ctx=Load(),
            lineno=79,
            col_offset=38,
            end_lineno=79,
            end_col_offset=58),
          lineno=79,
          col_offset=4,
          end_lineno=80,
          end_col_offset=28)],
      decorator_list=[],
      lineno=52,
      col_offset=0,
      end_lineno=80,
      end_col_offset=28)],
  type_ignores=[])
```
</details>

