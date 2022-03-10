# ./src/pyremaid/mermaid_tools/mermaid_tools.py

### Imports

  - models.MermaidBlock
  - models.MermaidElement
  - models.MermaidLink
  - models.MermaidNode

---
```mermaid
flowchart TB
  node_0["ast.Module object at 0x1068da3a0"]
  node_1["ast.Assign object at 0x1068da1c0"]
  node_2["ast.Name object at 0x1068da190"]
  node_3["ast.Store object at 0x1067e7070"]
  node_4["ast.Constant object at 0x1068da160"]
  node_5["ast.FunctionDef object at 0x1068da130"]
  node_6["ast.arguments object at 0x1068da100"]
  node_7["ast.arg object at 0x1068da0d0"]
  node_8["ast.Name object at 0x1068da0a0"]
  node_9["ast.Load object at 0x1067e70d0"]
  node_10["ast.Return object at 0x1068da070"]
  node_11["ast.Call object at 0x1068da040"]
  node_12["ast.Attribute object at 0x1068f3fd0"]
  node_13["ast.Call object at 0x1068f3fa0"]
  node_14["ast.Attribute object at 0x1068f3f70"]
  node_15["ast.Name object at 0x1068f3f40"]
  node_16["ast.Load object at 0x1067e70d0"]
  node_17["ast.Load object at 0x1067e70d0"]
  node_18["ast.Constant object at 0x1068f3f10"]
  node_19["ast.Constant object at 0x1068f3ee0"]
  node_20["ast.Load object at 0x1067e70d0"]
  node_21["ast.Constant object at 0x1068f3eb0"]
  node_22["ast.Constant object at 0x1068f3e80"]
  node_23["ast.Name object at 0x1068f3e20"]
  node_24["ast.Load object at 0x1067e70d0"]
  node_25["ast.FunctionDef object at 0x1068f3df0"]
  node_26["ast.arguments object at 0x1068f3dc0"]
  node_27["ast.arg object at 0x1068f3d90"]
  node_28["ast.Subscript object at 0x1068f3d60"]
  node_29["ast.Name object at 0x1068f3d30"]
  node_30["ast.Load object at 0x1067e70d0"]
  node_31["ast.Name object at 0x1068f3d00"]
  node_32["ast.Load object at 0x1067e70d0"]
  node_33["ast.Load object at 0x1067e70d0"]
  node_34["ast.Assign object at 0x1068f3cd0"]
  node_35["ast.Name object at 0x1068f3ca0"]
  node_36["ast.Store object at 0x1067e7070"]
  node_37["ast.List object at 0x1068f3c70"]
  node_38["ast.Load object at 0x1067e70d0"]
  node_39["ast.For object at 0x1068f3c40"]
  node_40["ast.Name object at 0x1068f3c10"]
  node_41["ast.Store object at 0x1067e7070"]
  node_42["ast.Name object at 0x1068f3be0"]
  node_43["ast.Load object at 0x1067e70d0"]
  node_44["ast.If object at 0x1068f3bb0"]
  node_45["ast.Call object at 0x1068f3b80"]
  node_46["ast.Name object at 0x1068f3b50"]
  node_47["ast.Load object at 0x1067e70d0"]
  node_48["ast.Name object at 0x1068f3b20"]
  node_49["ast.Load object at 0x1067e70d0"]
  node_50["ast.Name object at 0x1068f3af0"]
  node_51["ast.Load object at 0x1067e70d0"]
  node_52["ast.AnnAssign object at 0x1068f3ac0"]
  node_53["ast.Name object at 0x1068f3a90"]
  node_54["ast.Store object at 0x1067e7070"]
  node_55["ast.Name object at 0x1068f3a60"]
  node_56["ast.Load object at 0x1067e70d0"]
  node_57["ast.Name object at 0x1068f3a30"]
  node_58["ast.Load object at 0x1067e70d0"]
  node_59["ast.If object at 0x1068f3a00"]
  node_60["ast.Compare object at 0x1068f39d0"]
  node_61["ast.Attribute object at 0x1068f39a0"]
  node_62["ast.Name object at 0x1068f3970"]
  node_63["ast.Load object at 0x1067e70d0"]
  node_64["ast.Load object at 0x1067e70d0"]
  node_65["ast.NotIn object at 0x10681a1f0"]
  node_66["ast.Name object at 0x1068f3940"]
  node_67["ast.Load object at 0x1067e70d0"]
  node_68["ast.Expr object at 0x1068f3910"]
  node_69["ast.Call object at 0x1068f38e0"]
  node_70["ast.Attribute object at 0x1068f38b0"]
  node_71["ast.Name object at 0x1068f3880"]
  node_72["ast.Load object at 0x1067e70d0"]
  node_73["ast.Load object at 0x1067e70d0"]
  node_74["ast.Attribute object at 0x1068f3850"]
  node_75["ast.Name object at 0x1068f3820"]
  node_76["ast.Load object at 0x1067e70d0"]
  node_77["ast.Load object at 0x1067e70d0"]
  node_78["ast.If object at 0x1068f37c0"]
  node_79["ast.Compare object at 0x1068f3790"]
  node_80["ast.Attribute object at 0x1068f3760"]
  node_81["ast.Name object at 0x1068f3730"]
  node_82["ast.Load object at 0x1067e70d0"]
  node_83["ast.Load object at 0x1067e70d0"]
  node_84["ast.NotIn object at 0x10681a1f0"]
  node_85["ast.Name object at 0x1068f3700"]
  node_86["ast.Load object at 0x1067e70d0"]
  node_87["ast.Expr object at 0x1068f36d0"]
  node_88["ast.Call object at 0x1068f36a0"]
  node_89["ast.Attribute object at 0x1068f3670"]
  node_90["ast.Name object at 0x1068f3640"]
  node_91["ast.Load object at 0x1067e70d0"]
  node_92["ast.Load object at 0x1067e70d0"]
  node_93["ast.Attribute object at 0x1068f3610"]
  node_94["ast.Name object at 0x1068f35e0"]
  node_95["ast.Load object at 0x1067e70d0"]
  node_96["ast.Load object at 0x1067e70d0"]
  node_97["ast.If object at 0x1068f3580"]
  node_98["ast.Call object at 0x1068f3550"]
  node_99["ast.Name object at 0x1068f3520"]
  node_100["ast.Load object at 0x1067e70d0"]
  node_101["ast.Name object at 0x1068f34f0"]
  node_102["ast.Load object at 0x1067e70d0"]
  node_103["ast.Name object at 0x1068f34c0"]
  node_104["ast.Load object at 0x1067e70d0"]
  node_105["ast.AnnAssign object at 0x1068f3490"]
  node_106["ast.Name object at 0x1068f3460"]
  node_107["ast.Store object at 0x1067e7070"]
  node_108["ast.Name object at 0x1068f3430"]
  node_109["ast.Load object at 0x1067e70d0"]
  node_110["ast.Name object at 0x1068f3400"]
  node_111["ast.Load object at 0x1067e70d0"]
  node_112["ast.Expr object at 0x1068f3220"]
  node_113["ast.Call object at 0x1068f3250"]
  node_114["ast.Attribute object at 0x1068f32e0"]
  node_115["ast.Name object at 0x1068f3340"]
  node_116["ast.Load object at 0x1067e70d0"]
  node_117["ast.Load object at 0x1067e70d0"]
  node_118["ast.Call object at 0x1068f33d0"]
  node_119["ast.Name object at 0x1068f1c40"]
  node_120["ast.Load object at 0x1067e70d0"]
  node_121["ast.Attribute object at 0x1068f1c10"]
  node_122["ast.Name object at 0x1068f1d00"]
  node_123["ast.Load object at 0x1067e70d0"]
  node_124["ast.Load object at 0x1067e70d0"]
  node_125["ast.Return object at 0x1068f1d90"]
  node_126["ast.Name object at 0x1068f1dc0"]
  node_127["ast.Load object at 0x1067e70d0"]
  node_128["ast.Subscript object at 0x1068f1d60"]
  node_129["ast.Name object at 0x1068f1ac0"]
  node_130["ast.Load object at 0x1067e70d0"]
  node_131["ast.Name object at 0x1068f1df0"]
  node_132["ast.Load object at 0x1067e70d0"]
  node_133["ast.Load object at 0x1067e70d0"]
  node_134["ast.FunctionDef object at 0x1068f18e0"]
  node_135["ast.arguments object at 0x1068f19d0"]
  node_136["ast.arg object at 0x1068f1a00"]
  node_137["ast.Subscript object at 0x1068f1940"]
  node_138["ast.Name object at 0x1068f1a90"]
  node_139["ast.Load object at 0x1067e70d0"]
  node_140["ast.Name object at 0x1068f1910"]
  node_141["ast.Load object at 0x1067e70d0"]
  node_142["ast.Load object at 0x1067e70d0"]
  node_143["ast.arg object at 0x1068f19a0"]
  node_144["ast.Name object at 0x1068f1b20"]
  node_145["ast.Load object at 0x1067e70d0"]
  node_146["ast.Constant object at 0x1068f1a30"]
  node_147["ast.Assign object at 0x1068f1970"]
  node_148["ast.Name object at 0x1068f1a60"]
  node_149["ast.Store object at 0x1067e7070"]
  node_150["ast.Constant object at 0x1068f1af0"]
  node_151["ast.For object at 0x1068f1f10"]
  node_152["ast.Name object at 0x1068f1eb0"]
  node_153["ast.Store object at 0x1067e7070"]
  node_154["ast.Call object at 0x1068f1e80"]
  node_155["ast.Name object at 0x1068f1e50"]
  node_156["ast.Load object at 0x1067e70d0"]
  node_157["ast.keyword object at 0x1068f1e20"]
  node_158["ast.Name object at 0x1068f1ee0"]
  node_159["ast.Load object at 0x1067e70d0"]
  node_160["ast.AugAssign object at 0x1068f18b0"]
  node_161["ast.Name object at 0x1068f1640"]
  node_162["ast.Store object at 0x1067e7070"]
  node_163["ast.Add object at 0x1067e7760"]
  node_164["ast.JoinedStr object at 0x1068f1610"]
  node_165["ast.FormattedValue object at 0x1068f14f0"]
  node_166["ast.BinOp object at 0x1068f1670"]
  node_167["ast.Name object at 0x1068f1040"]
  node_168["ast.Load object at 0x1067e70d0"]
  node_169["ast.Mult object at 0x1067e7820"]
  node_170["ast.Name object at 0x1068f1580"]
  node_171["ast.Load object at 0x1067e70d0"]
  node_172["ast.FormattedValue object at 0x1068f15e0"]
  node_173["ast.Attribute object at 0x1068f15b0"]
  node_174["ast.Name object at 0x1068f1070"]
  node_175["ast.Load object at 0x1067e70d0"]
  node_176["ast.Load object at 0x1067e70d0"]
  node_177["ast.Constant object at 0x1068e8dc0"]
  node_178["ast.FormattedValue object at 0x1068e8340"]
  node_179["ast.Attribute object at 0x1068e86a0"]
  node_180["ast.Name object at 0x1068e8b20"]
  node_181["ast.Load object at 0x1067e70d0"]
  node_182["ast.Load object at 0x1067e70d0"]
  node_183["ast.Constant object at 0x1068e8e50"]
  node_184["ast.Return object at 0x1068e8a60"]
  node_185["ast.Call object at 0x1068e8a30"]
  node_186["ast.Name object at 0x1068e8e20"]
  node_187["ast.Load object at 0x1067e70d0"]
  node_188["ast.Name object at 0x1068e8460"]
  node_189["ast.Load object at 0x1067e70d0"]
  node_190["ast.Name object at 0x1068e8670"]
  node_191["ast.Load object at 0x1067e70d0"]
  node_192["ast.FunctionDef object at 0x1068e8fd0"]
  node_193["ast.arguments object at 0x1068e87c0"]
  node_194["ast.arg object at 0x1068e8760"]
  node_195["ast.Name object at 0x1068e8130"]
  node_196["ast.Load object at 0x1067e70d0"]
  node_197["ast.arg object at 0x1068e8ee0"]
  node_198["ast.Name object at 0x1068e8f40"]
  node_199["ast.Load object at 0x1067e70d0"]
  node_200["ast.Assign object at 0x1068e8730"]
  node_201["ast.Name object at 0x1068e8940"]
  node_202["ast.Store object at 0x1067e7070"]
  node_203["ast.Attribute object at 0x1068e85e0"]
  node_204["ast.Attribute object at 0x1068e8f10"]
  node_205["ast.Name object at 0x1068e8040"]
  node_206["ast.Load object at 0x1067e70d0"]
  node_207["ast.Load object at 0x1067e70d0"]
  node_208["ast.Load object at 0x1067e70d0"]
  node_209["ast.Assign object at 0x1068e85b0"]
  node_210["ast.Name object at 0x1068e8640"]
  node_211["ast.Store object at 0x1067e7070"]
  node_212["ast.Attribute object at 0x1068e8e80"]
  node_213["ast.Attribute object at 0x1068e8b50"]
  node_214["ast.Name object at 0x1068e8550"]
  node_215["ast.Load object at 0x1067e70d0"]
  node_216["ast.Load object at 0x1067e70d0"]
  node_217["ast.Load object at 0x1067e70d0"]
  node_218["ast.Return object at 0x1068e8970"]
  node_219["ast.JoinedStr object at 0x1068e84f0"]
  node_220["ast.FormattedValue object at 0x1068e8490"]
  node_221["ast.BinOp object at 0x1068e86d0"]
  node_222["ast.Name object at 0x1068e8a90"]
  node_223["ast.Load object at 0x1067e70d0"]
  node_224["ast.Mult object at 0x1067e7820"]
  node_225["ast.Name object at 0x1068e8ac0"]
  node_226["ast.Load object at 0x1067e70d0"]
  node_227["ast.FormattedValue object at 0x1068e8a00"]
  node_228["ast.Name object at 0x1068e89d0"]
  node_229["ast.Load object at 0x1067e70d0"]
  node_230["ast.Constant object at 0x1068e8c10"]
  node_231["ast.FormattedValue object at 0x1068e8bb0"]
  node_232["ast.Name object at 0x1068e8ca0"]
  node_233["ast.Load object at 0x1067e70d0"]
  node_234["ast.Constant object at 0x1068e8d00"]
  node_235["ast.Name object at 0x1068e8820"]
  node_236["ast.Load object at 0x1067e70d0"]
  node_237["ast.FunctionDef object at 0x1068e87f0"]
  node_238["ast.arguments object at 0x1068e84c0"]
  node_239["ast.arg object at 0x1068e8c70"]
  node_240["ast.Subscript object at 0x1068e8700"]
  node_241["ast.Name object at 0x1068e8eb0"]
  node_242["ast.Load object at 0x1067e70d0"]
  node_243["ast.Name object at 0x1068e8610"]
  node_244["ast.Load object at 0x1067e70d0"]
  node_245["ast.Load object at 0x1067e70d0"]
  node_246["ast.arg object at 0x1068e8790"]
  node_247["ast.Name object at 0x1068e8d90"]
  node_248["ast.Load object at 0x1067e70d0"]
  node_249["ast.Constant object at 0x1068e8d60"]
  node_250["ast.Assign object at 0x1068e8df0"]
  node_251["ast.Name object at 0x1068e8850"]
  node_252["ast.Store object at 0x1067e7070"]
  node_253["ast.Constant object at 0x1068e8d30"]
  node_254["ast.For object at 0x1068e8f70"]
  node_255["ast.Name object at 0x1068e80d0"]
  node_256["ast.Store object at 0x1067e7070"]
  node_257["ast.Name object at 0x1068e83a0"]
  node_258["ast.Load object at 0x1067e70d0"]
  node_259["ast.If object at 0x1068e88b0"]
  node_260["ast.Call object at 0x1068e88e0"]
  node_261["ast.Name object at 0x1068e8be0"]
  node_262["ast.Load object at 0x1067e70d0"]
  node_263["ast.Name object at 0x1068e8910"]
  node_264["ast.Load object at 0x1067e70d0"]
  node_265["ast.Name object at 0x1068e8400"]
  node_266["ast.Load object at 0x1067e70d0"]
  node_267["ast.AnnAssign object at 0x1068e83d0"]
  node_268["ast.Name object at 0x1068e8310"]
  node_269["ast.Store object at 0x1067e7070"]
  node_270["ast.Name object at 0x1068e8880"]
  node_271["ast.Load object at 0x1067e70d0"]
  node_272["ast.Name object at 0x1068e8250"]
  node_273["ast.Load object at 0x1067e70d0"]
  node_274["ast.AugAssign object at 0x1068e81c0"]
  node_275["ast.Name object at 0x1068e81f0"]
  node_276["ast.Store object at 0x1067e7070"]
  node_277["ast.Add object at 0x1067e7760"]
  node_278["ast.Call object at 0x1068e8430"]
  node_279["ast.Name object at 0x1068e8220"]
  node_280["ast.Load object at 0x1067e70d0"]
  node_281["ast.keyword object at 0x1068e8160"]
  node_282["ast.Name object at 0x1068e8070"]
  node_283["ast.Load object at 0x1067e70d0"]
  node_284["ast.keyword object at 0x1068e8370"]
  node_285["ast.Name object at 0x1068e8190"]
  node_286["ast.Load object at 0x1067e70d0"]
  node_287["ast.If object at 0x1068e82b0"]
  node_288["ast.Call object at 0x1068e80a0"]
  node_289["ast.Name object at 0x1068e8100"]
  node_290["ast.Load object at 0x1067e70d0"]
  node_291["ast.Name object at 0x1068e82e0"]
  node_292["ast.Load object at 0x1067e70d0"]
  node_293["ast.Name object at 0x1068e8280"]
  node_294["ast.Load object at 0x1067e70d0"]
  node_295["ast.AnnAssign object at 0x1068cfb80"]
  node_296["ast.Name object at 0x1068cfd00"]
  node_297["ast.Store object at 0x1067e7070"]
  node_298["ast.Name object at 0x1068cf760"]
  node_299["ast.Load object at 0x1067e70d0"]
  node_300["ast.Name object at 0x1068cffa0"]
  node_301["ast.Load object at 0x1067e70d0"]
  node_302["ast.AugAssign object at 0x1068cff70"]
  node_303["ast.Name object at 0x1068cf130"]
  node_304["ast.Store object at 0x1067e7070"]
  node_305["ast.Add object at 0x1067e7760"]
  node_306["ast.Call object at 0x1068cf0a0"]
  node_307["ast.Name object at 0x1068cf0d0"]
  node_308["ast.Load object at 0x1067e70d0"]
  node_309["ast.keyword object at 0x1067e4fa0"]
  node_310["ast.Name object at 0x1067e4fd0"]
  node_311["ast.Load object at 0x1067e70d0"]
  node_312["ast.keyword object at 0x1067e4f70"]
  node_313["ast.Name object at 0x1068c7fd0"]
  node_314["ast.Load object at 0x1067e70d0"]
  node_315["ast.Return object at 0x1068c7ca0"]
  node_316["ast.Name object at 0x1068c7dc0"]
  node_317["ast.Load object at 0x1067e70d0"]
  node_318["ast.Name object at 0x1068c7c10"]
  node_319["ast.Load object at 0x1067e70d0"]
  node_320["ast.FunctionDef object at 0x1068c7cd0"]
  node_321["ast.arguments object at 0x1068c7730"]
  node_322["ast.arg object at 0x1068c7220"]
  node_323["ast.Name object at 0x1068c7790"]
  node_324["ast.Load object at 0x1067e70d0"]
  node_325["ast.arg object at 0x1068c7340"]
  node_326["ast.Name object at 0x1068c77f0"]
  node_327["ast.Load object at 0x1067e70d0"]
  node_328["ast.Assign object at 0x1068c7e20"]
  node_329["ast.Name object at 0x1068c78b0"]
  node_330["ast.Store object at 0x1067e7070"]
  node_331["ast.Call object at 0x1068c7d90"]
  node_332["ast.Name object at 0x1068c7880"]
  node_333["ast.Load object at 0x1067e70d0"]
  node_334["ast.Attribute object at 0x1068c75e0"]
  node_335["ast.Name object at 0x1068c76a0"]
  node_336["ast.Load object at 0x1067e70d0"]
  node_337["ast.Load object at 0x1067e70d0"]
  node_338["ast.Name object at 0x1068c7df0"]
  node_339["ast.Load object at 0x1067e70d0"]
  node_340["ast.Return object at 0x1068c76d0"]
  node_341["ast.Name object at 0x1068c7d00"]
  node_342["ast.Load object at 0x1067e70d0"]
  node_343["ast.Name object at 0x1068c7ac0"]
  node_344["ast.Load object at 0x1067e70d0"]
  node_345["ast.FunctionDef object at 0x1068c7e80"]
  node_346["ast.arguments object at 0x1068c7610"]
  node_347["ast.arg object at 0x1068c7bb0"]
  node_348["ast.Subscript object at 0x1068c70a0"]
  node_349["ast.Name object at 0x1068c79d0"]
  node_350["ast.Load object at 0x1067e70d0"]
  node_351["ast.Name object at 0x1068c7940"]
  node_352["ast.Load object at 0x1067e70d0"]
  node_353["ast.Load object at 0x1067e70d0"]
  node_354["ast.Assign object at 0x1068c72b0"]
  node_355["ast.Name object at 0x1068c7760"]
  node_356["ast.Store object at 0x1067e7070"]
  node_357["ast.Call object at 0x1068c7b50"]
  node_358["ast.Name object at 0x1068c7d30"]
  node_359["ast.Load object at 0x1067e70d0"]
  node_360["ast.keyword object at 0x1068c7100"]
  node_361["ast.Name object at 0x1068c7b20"]
  node_362["ast.Load object at 0x1067e70d0"]
  node_363["ast.Assign object at 0x1068c7520"]
  node_364["ast.Name object at 0x1068c77c0"]
  node_365["ast.Store object at 0x1067e7070"]
  node_366["ast.Call object at 0x1068c7580"]
  node_367["ast.Name object at 0x1068c7640"]
  node_368["ast.Load object at 0x1067e70d0"]
  node_369["ast.keyword object at 0x1068c7820"]
  node_370["ast.Name object at 0x1068c7f70"]
  node_371["ast.Load object at 0x1067e70d0"]
  node_372["ast.Return object at 0x1068c7c70"]
  node_373["ast.JoinedStr object at 0x1068c7700"]
  node_374["ast.Constant object at 0x1068c7af0"]
  node_375["ast.FormattedValue object at 0x1068c7c40"]
  node_376["ast.Name object at 0x1068c7550"]
  node_377["ast.Load object at 0x1067e70d0"]
  node_378["ast.Constant object at 0x1068c7970"]
  node_379["ast.FormattedValue object at 0x1068c7130"]
  node_380["ast.Name object at 0x1068c7850"]
  node_381["ast.Load object at 0x1067e70d0"]
  node_382["ast.Constant object at 0x1068c7ee0"]
  node_383["ast.Name object at 0x1068c72e0"]
  node_384["ast.Load object at 0x1067e70d0"]

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
  node_378 --> node_379
  node_379 --> node_380
  node_380 --> node_381
  node_381 --> node_382
  node_382 --> node_383
  node_383 --> node_384

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidBlock'),
        alias(name='MermaidElement'),
        alias(name='MermaidLink'),
        alias(name='MermaidNode')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=73),
    Assign(
      targets=[
        Name(
          id='TAB',
          ctx=Store(),
          lineno=3,
          col_offset=0,
          end_lineno=3,
          end_col_offset=3)],
      value=Constant(
        value='  ',
        lineno=3,
        col_offset=6,
        end_lineno=3,
        end_col_offset=10),
      lineno=3,
      col_offset=0,
      end_lineno=3,
      end_col_offset=10),
    FunctionDef(
      name='_sanitize',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='markdown',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=6,
              col_offset=24,
              end_lineno=6,
              end_col_offset=27),
            lineno=6,
            col_offset=14,
            end_lineno=6,
            end_col_offset=27)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Attribute(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='markdown',
                    ctx=Load(),
                    lineno=8,
                    col_offset=8,
                    end_lineno=8,
                    end_col_offset=16),
                  attr='replace',
                  ctx=Load(),
                  lineno=8,
                  col_offset=8,
                  end_lineno=9,
                  end_col_offset=16),
                args=[
                  Constant(
                    value='<',
                    lineno=9,
                    col_offset=17,
                    end_lineno=9,
                    end_col_offset=20),
                  Constant(
                    value='',
                    lineno=9,
                    col_offset=21,
                    end_lineno=9,
                    end_col_offset=23)],
                keywords=[],
                lineno=8,
                col_offset=8,
                end_lineno=9,
                end_col_offset=24),
              attr='replace',
              ctx=Load(),
              lineno=8,
              col_offset=8,
              end_lineno=10,
              end_col_offset=16),
            args=[
              Constant(
                value='>',
                lineno=10,
                col_offset=17,
                end_lineno=10,
                end_col_offset=20),
              Constant(
                value='',
                lineno=10,
                col_offset=21,
                end_lineno=10,
                end_col_offset=23)],
            keywords=[],
            lineno=8,
            col_offset=8,
            end_lineno=10,
            end_col_offset=24),
          lineno=7,
          col_offset=4,
          end_lineno=11,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=6,
        col_offset=32,
        end_lineno=6,
        end_col_offset=35),
      lineno=6,
      col_offset=0,
      end_lineno=11,
      end_col_offset=5),
    FunctionDef(
      name='_get_unique_nodes',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=14,
                col_offset=32,
                end_lineno=14,
                end_col_offset=36),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=14,
                col_offset=37,
                end_lineno=14,
                end_col_offset=51),
              ctx=Load(),
              lineno=14,
              col_offset=32,
              end_lineno=14,
              end_col_offset=52),
            lineno=14,
            col_offset=22,
            end_lineno=14,
            end_col_offset=52)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='node_set',
              ctx=Store(),
              lineno=16,
              col_offset=4,
              end_lineno=16,
              end_col_offset=12)],
          value=List(
            elts=[],
            ctx=Load(),
            lineno=16,
            col_offset=15,
            end_lineno=16,
            end_col_offset=17),
          lineno=16,
          col_offset=4,
          end_lineno=16,
          end_col_offset=17),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=17,
            col_offset=8,
            end_lineno=17,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=17,
            col_offset=19,
            end_lineno=17,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=18,
                  col_offset=11,
                  end_lineno=18,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=18,
                    col_offset=22,
                    end_lineno=18,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=18,
                    col_offset=31,
                    end_lineno=18,
                    end_col_offset=42)],
                keywords=[],
                lineno=18,
                col_offset=11,
                end_lineno=18,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=19,
                    col_offset=12,
                    end_lineno=19,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=19,
                    col_offset=19,
                    end_lineno=19,
                    end_col_offset=30),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=19,
                    col_offset=33,
                    end_lineno=19,
                    end_col_offset=40),
                  simple=1,
                  lineno=19,
                  col_offset=12,
                  end_lineno=19,
                  end_col_offset=40),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=20,
                        col_offset=15,
                        end_lineno=20,
                        end_col_offset=19),
                      attr='from_',
                      ctx=Load(),
                      lineno=20,
                      col_offset=15,
                      end_lineno=20,
                      end_col_offset=25),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=20,
                        col_offset=33,
                        end_lineno=20,
                        end_col_offset=41)],
                    lineno=20,
                    col_offset=15,
                    end_lineno=20,
                    end_col_offset=41),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=21,
                            col_offset=16,
                            end_lineno=21,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=21,
                          col_offset=16,
                          end_lineno=21,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=21,
                              col_offset=32,
                              end_lineno=21,
                              end_col_offset=36),
                            attr='from_',
                            ctx=Load(),
                            lineno=21,
                            col_offset=32,
                            end_lineno=21,
                            end_col_offset=42)],
                        keywords=[],
                        lineno=21,
                        col_offset=16,
                        end_lineno=21,
                        end_col_offset=43),
                      lineno=21,
                      col_offset=16,
                      end_lineno=21,
                      end_col_offset=43)],
                  orelse=[],
                  lineno=20,
                  col_offset=12,
                  end_lineno=21,
                  end_col_offset=43),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=22,
                        col_offset=15,
                        end_lineno=22,
                        end_col_offset=19),
                      attr='to',
                      ctx=Load(),
                      lineno=22,
                      col_offset=15,
                      end_lineno=22,
                      end_col_offset=22),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=22,
                        col_offset=30,
                        end_lineno=22,
                        end_col_offset=38)],
                    lineno=22,
                    col_offset=15,
                    end_lineno=22,
                    end_col_offset=38),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=23,
                            col_offset=16,
                            end_lineno=23,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=23,
                          col_offset=16,
                          end_lineno=23,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=23,
                              col_offset=32,
                              end_lineno=23,
                              end_col_offset=36),
                            attr='to',
                            ctx=Load(),
                            lineno=23,
                            col_offset=32,
                            end_lineno=23,
                            end_col_offset=39)],
                        keywords=[],
                        lineno=23,
                        col_offset=16,
                        end_lineno=23,
                        end_col_offset=40),
                      lineno=23,
                      col_offset=16,
                      end_lineno=23,
                      end_col_offset=40)],
                  orelse=[],
                  lineno=22,
                  col_offset=12,
                  end_lineno=23,
                  end_col_offset=40)],
              orelse=[],
              lineno=18,
              col_offset=8,
              end_lineno=23,
              end_col_offset=40),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=24,
                  col_offset=11,
                  end_lineno=24,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=24,
                    col_offset=22,
                    end_lineno=24,
                    end_col_offset=29),
                  Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=24,
                    col_offset=31,
                    end_lineno=24,
                    end_col_offset=43)],
                keywords=[],
                lineno=24,
                col_offset=11,
                end_lineno=24,
                end_col_offset=44),
              body=[
                AnnAssign(
                  target=Name(
                    id='block',
                    ctx=Store(),
                    lineno=25,
                    col_offset=12,
                    end_lineno=25,
                    end_col_offset=17),
                  annotation=Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=25,
                    col_offset=20,
                    end_lineno=25,
                    end_col_offset=32),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=25,
                    col_offset=35,
                    end_lineno=25,
                    end_col_offset=42),
                  simple=1,
                  lineno=25,
                  col_offset=12,
                  end_lineno=25,
                  end_col_offset=42),
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=26,
                        col_offset=12,
                        end_lineno=26,
                        end_col_offset=20),
                      attr='extend',
                      ctx=Load(),
                      lineno=26,
                      col_offset=12,
                      end_lineno=26,
                      end_col_offset=27),
                    args=[
                      Call(
                        func=Name(
                          id='_get_unique_nodes',
                          ctx=Load(),
                          lineno=26,
                          col_offset=28,
                          end_lineno=26,
                          end_col_offset=45),
                        args=[
                          Attribute(
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=26,
                              col_offset=46,
                              end_lineno=26,
                              end_col_offset=51),
                            attr='block_contents',
                            ctx=Load(),
                            lineno=26,
                            col_offset=46,
                            end_lineno=26,
                            end_col_offset=66)],
                        keywords=[],
                        lineno=26,
                        col_offset=28,
                        end_lineno=26,
                        end_col_offset=67)],
                    keywords=[],
                    lineno=26,
                    col_offset=12,
                    end_lineno=26,
                    end_col_offset=68),
                  lineno=26,
                  col_offset=12,
                  end_lineno=26,
                  end_col_offset=68)],
              orelse=[],
              lineno=24,
              col_offset=8,
              end_lineno=26,
              end_col_offset=68)],
          orelse=[],
          lineno=17,
          col_offset=4,
          end_lineno=26,
          end_col_offset=68),
        Return(
          value=Name(
            id='node_set',
            ctx=Load(),
            lineno=27,
            col_offset=11,
            end_lineno=27,
            end_col_offset=19),
          lineno=27,
          col_offset=4,
          end_lineno=27,
          end_col_offset=19)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=14,
          col_offset=57,
          end_lineno=14,
          end_col_offset=61),
        slice=Name(
          id='MermaidNode',
          ctx=Load(),
          lineno=14,
          col_offset=62,
          end_lineno=14,
          end_col_offset=73),
        ctx=Load(),
        lineno=14,
        col_offset=57,
        end_lineno=14,
        end_col_offset=74),
      lineno=14,
      col_offset=0,
      end_lineno=27,
      end_col_offset=19),
    FunctionDef(
      name='_get_aliases_for_safe_names',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=30,
                col_offset=42,
                end_lineno=30,
                end_col_offset=46),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=30,
                col_offset=47,
                end_lineno=30,
                end_col_offset=61),
              ctx=Load(),
              lineno=30,
              col_offset=42,
              end_lineno=30,
              end_col_offset=62),
            lineno=30,
            col_offset=32,
            end_lineno=30,
            end_col_offset=62),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=30,
              col_offset=72,
              end_lineno=30,
              end_col_offset=75),
            lineno=30,
            col_offset=64,
            end_lineno=30,
            end_col_offset=75)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=30,
            col_offset=78,
            end_lineno=30,
            end_col_offset=79)]),
      body=[
        Assign(
          targets=[
            Name(
              id='alias_string',
              ctx=Store(),
              lineno=31,
              col_offset=4,
              end_lineno=31,
              end_col_offset=16)],
          value=Constant(
            value='',
            lineno=31,
            col_offset=19,
            end_lineno=31,
            end_col_offset=21),
          lineno=31,
          col_offset=4,
          end_lineno=31,
          end_col_offset=21),
        For(
          target=Name(
            id='node',
            ctx=Store(),
            lineno=32,
            col_offset=8,
            end_lineno=32,
            end_col_offset=12),
          iter=Call(
            func=Name(
              id='_get_unique_nodes',
              ctx=Load(),
              lineno=32,
              col_offset=16,
              end_lineno=32,
              end_col_offset=33),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=32,
                  col_offset=43,
                  end_lineno=32,
                  end_col_offset=51),
                lineno=32,
                col_offset=34,
                end_lineno=32,
                end_col_offset=51)],
            lineno=32,
            col_offset=16,
            end_lineno=32,
            end_col_offset=52),
          body=[
            AugAssign(
              target=Name(
                id='alias_string',
                ctx=Store(),
                lineno=33,
                col_offset=8,
                end_lineno=33,
                end_col_offset=20),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=33,
                        col_offset=27,
                        end_lineno=33,
                        end_col_offset=30),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=33,
                        col_offset=31,
                        end_lineno=33,
                        end_col_offset=37),
                      lineno=33,
                      col_offset=27,
                      end_lineno=33,
                      end_col_offset=37),
                    conversion=-1,
                    lineno=33,
                    col_offset=24,
                    end_lineno=33,
                    end_col_offset=86),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=33,
                        col_offset=39,
                        end_lineno=33,
                        end_col_offset=43),
                      attr='mermaid_safe_name',
                      ctx=Load(),
                      lineno=33,
                      col_offset=39,
                      end_lineno=33,
                      end_col_offset=61),
                    conversion=-1,
                    lineno=33,
                    col_offset=24,
                    end_lineno=33,
                    end_col_offset=86),
                  Constant(
                    value='["',
                    lineno=33,
                    col_offset=24,
                    end_lineno=33,
                    end_col_offset=86),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=33,
                        col_offset=66,
                        end_lineno=33,
                        end_col_offset=70),
                      attr='ast_node',
                      ctx=Load(),
                      lineno=33,
                      col_offset=66,
                      end_lineno=33,
                      end_col_offset=79),
                    conversion=-1,
                    lineno=33,
                    col_offset=24,
                    end_lineno=33,
                    end_col_offset=86),
                  Constant(
                    value='"]\n',
                    lineno=33,
                    col_offset=24,
                    end_lineno=33,
                    end_col_offset=86)],
                lineno=33,
                col_offset=24,
                end_lineno=33,
                end_col_offset=86),
              lineno=33,
              col_offset=8,
              end_lineno=33,
              end_col_offset=86)],
          orelse=[],
          lineno=32,
          col_offset=4,
          end_lineno=33,
          end_col_offset=86),
        Return(
          value=Call(
            func=Name(
              id='_sanitize',
              ctx=Load(),
              lineno=34,
              col_offset=11,
              end_lineno=34,
              end_col_offset=20),
            args=[
              Name(
                id='alias_string',
                ctx=Load(),
                lineno=34,
                col_offset=21,
                end_lineno=34,
                end_col_offset=33)],
            keywords=[],
            lineno=34,
            col_offset=11,
            end_lineno=34,
            end_col_offset=34),
          lineno=34,
          col_offset=4,
          end_lineno=34,
          end_col_offset=34)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=30,
        col_offset=84,
        end_lineno=30,
        end_col_offset=87),
      lineno=30,
      col_offset=0,
      end_lineno=34,
      end_col_offset=34),
    FunctionDef(
      name='_get_flow_link_text',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='link',
            annotation=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=37,
              col_offset=30,
              end_lineno=37,
              end_col_offset=44),
            lineno=37,
            col_offset=24,
            end_lineno=37,
            end_col_offset=44),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=37,
              col_offset=54,
              end_lineno=37,
              end_col_offset=57),
            lineno=37,
            col_offset=46,
            end_lineno=37,
            end_col_offset=57)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='from_name',
              ctx=Store(),
              lineno=38,
              col_offset=4,
              end_lineno=38,
              end_col_offset=13)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=38,
                col_offset=16,
                end_lineno=38,
                end_col_offset=20),
              attr='from_',
              ctx=Load(),
              lineno=38,
              col_offset=16,
              end_lineno=38,
              end_col_offset=26),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=38,
            col_offset=16,
            end_lineno=38,
            end_col_offset=44),
          lineno=38,
          col_offset=4,
          end_lineno=38,
          end_col_offset=44),
        Assign(
          targets=[
            Name(
              id='to_name',
              ctx=Store(),
              lineno=39,
              col_offset=4,
              end_lineno=39,
              end_col_offset=11)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=39,
                col_offset=14,
                end_lineno=39,
                end_col_offset=18),
              attr='to',
              ctx=Load(),
              lineno=39,
              col_offset=14,
              end_lineno=39,
              end_col_offset=21),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=39,
            col_offset=14,
            end_lineno=39,
            end_col_offset=39),
          lineno=39,
          col_offset=4,
          end_lineno=39,
          end_col_offset=39),
        Return(
          value=JoinedStr(
            values=[
              FormattedValue(
                value=BinOp(
                  left=Name(
                    id='TAB',
                    ctx=Load(),
                    lineno=41,
                    col_offset=14,
                    end_lineno=41,
                    end_col_offset=17),
                  op=Mult(),
                  right=Name(
                    id='indent',
                    ctx=Load(),
                    lineno=41,
                    col_offset=18,
                    end_lineno=41,
                    end_col_offset=24),
                  lineno=41,
                  col_offset=14,
                  end_lineno=41,
                  end_col_offset=24),
                conversion=-1,
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='from_name',
                  ctx=Load(),
                  lineno=41,
                  col_offset=26,
                  end_lineno=41,
                  end_col_offset=35),
                conversion=-1,
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=53),
              Constant(
                value=' --> ',
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='to_name',
                  ctx=Load(),
                  lineno=41,
                  col_offset=42,
                  end_lineno=41,
                  end_col_offset=49),
                conversion=-1,
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=53),
              Constant(
                value='\n',
                lineno=41,
                col_offset=11,
                end_lineno=41,
                end_col_offset=53)],
            lineno=41,
            col_offset=11,
            end_lineno=41,
            end_col_offset=53),
          lineno=41,
          col_offset=4,
          end_lineno=41,
          end_col_offset=53)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=37,
        col_offset=62,
        end_lineno=37,
        end_col_offset=65),
      lineno=37,
      col_offset=0,
      end_lineno=41,
      end_col_offset=53),
    FunctionDef(
      name='_get_flow_connections',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=44,
                col_offset=36,
                end_lineno=44,
                end_col_offset=40),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=44,
                col_offset=41,
                end_lineno=44,
                end_col_offset=55),
              ctx=Load(),
              lineno=44,
              col_offset=36,
              end_lineno=44,
              end_col_offset=56),
            lineno=44,
            col_offset=26,
            end_lineno=44,
            end_col_offset=56),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=44,
              col_offset=66,
              end_lineno=44,
              end_col_offset=69),
            lineno=44,
            col_offset=58,
            end_lineno=44,
            end_col_offset=69)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=44,
            col_offset=72,
            end_lineno=44,
            end_col_offset=73)]),
      body=[
        Assign(
          targets=[
            Name(
              id='connection_text',
              ctx=Store(),
              lineno=45,
              col_offset=4,
              end_lineno=45,
              end_col_offset=19)],
          value=Constant(
            value='',
            lineno=45,
            col_offset=22,
            end_lineno=45,
            end_col_offset=24),
          lineno=45,
          col_offset=4,
          end_lineno=45,
          end_col_offset=24),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=46,
            col_offset=8,
            end_lineno=46,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=46,
            col_offset=19,
            end_lineno=46,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=47,
                  col_offset=11,
                  end_lineno=47,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=47,
                    col_offset=22,
                    end_lineno=47,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=47,
                    col_offset=31,
                    end_lineno=47,
                    end_col_offset=42)],
                keywords=[],
                lineno=47,
                col_offset=11,
                end_lineno=47,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=48,
                    col_offset=12,
                    end_lineno=48,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=48,
                    col_offset=18,
                    end_lineno=48,
                    end_col_offset=29),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=48,
                    col_offset=32,
                    end_lineno=48,
                    end_col_offset=39),
                  simple=1,
                  lineno=48,
                  col_offset=12,
                  end_lineno=48,
                  end_col_offset=39),
                AugAssign(
                  target=Name(
                    id='connection_text',
                    ctx=Store(),
                    lineno=49,
                    col_offset=12,
                    end_lineno=49,
                    end_col_offset=27),
                  op=Add(),
                  value=Call(
                    func=Name(
                      id='_get_flow_link_text',
                      ctx=Load(),
                      lineno=49,
                      col_offset=31,
                      end_lineno=49,
                      end_col_offset=50),
                    args=[],
                    keywords=[
                      keyword(
                        arg='link',
                        value=Name(
                          id='link',
                          ctx=Load(),
                          lineno=49,
                          col_offset=56,
                          end_lineno=49,
                          end_col_offset=60),
                        lineno=49,
                        col_offset=51,
                        end_lineno=49,
                        end_col_offset=60),
                      keyword(
                        arg='indent',
                        value=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=49,
                          col_offset=69,
                          end_lineno=49,
                          end_col_offset=75),
                        lineno=49,
                        col_offset=62,
                        end_lineno=49,
                        end_col_offset=75)],
                    lineno=49,
                    col_offset=31,
                    end_lineno=49,
                    end_col_offset=76),
                  lineno=49,
                  col_offset=12,
                  end_lineno=49,
                  end_col_offset=76)],
              orelse=[
                If(
                  test=Call(
                    func=Name(
                      id='isinstance',
                      ctx=Load(),
                      lineno=50,
                      col_offset=13,
                      end_lineno=50,
                      end_col_offset=23),
                    args=[
                      Name(
                        id='element',
                        ctx=Load(),
                        lineno=50,
                        col_offset=24,
                        end_lineno=50,
                        end_col_offset=31),
                      Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=50,
                        col_offset=33,
                        end_lineno=50,
                        end_col_offset=45)],
                    keywords=[],
                    lineno=50,
                    col_offset=13,
                    end_lineno=50,
                    end_col_offset=46),
                  body=[
                    AnnAssign(
                      target=Name(
                        id='block',
                        ctx=Store(),
                        lineno=51,
                        col_offset=12,
                        end_lineno=51,
                        end_col_offset=17),
                      annotation=Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=51,
                        col_offset=19,
                        end_lineno=51,
                        end_col_offset=31),
                      value=Name(
                        id='element',
                        ctx=Load(),
                        lineno=51,
                        col_offset=34,
                        end_lineno=51,
                        end_col_offset=41),
                      simple=1,
                      lineno=51,
                      col_offset=12,
                      end_lineno=51,
                      end_col_offset=41),
                    AugAssign(
                      target=Name(
                        id='connection_text',
                        ctx=Store(),
                        lineno=52,
                        col_offset=12,
                        end_lineno=52,
                        end_col_offset=27),
                      op=Add(),
                      value=Call(
                        func=Name(
                          id='_get_block_text',
                          ctx=Load(),
                          lineno=52,
                          col_offset=31,
                          end_lineno=52,
                          end_col_offset=46),
                        args=[],
                        keywords=[
                          keyword(
                            arg='block',
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=52,
                              col_offset=53,
                              end_lineno=52,
                              end_col_offset=58),
                            lineno=52,
                            col_offset=47,
                            end_lineno=52,
                            end_col_offset=58),
                          keyword(
                            arg='indent',
                            value=Name(
                              id='indent',
                              ctx=Load(),
                              lineno=52,
                              col_offset=67,
                              end_lineno=52,
                              end_col_offset=73),
                            lineno=52,
                            col_offset=60,
                            end_lineno=52,
                            end_col_offset=73)],
                        lineno=52,
                        col_offset=31,
                        end_lineno=52,
                        end_col_offset=74),
                      lineno=52,
                      col_offset=12,
                      end_lineno=52,
                      end_col_offset=74)],
                  orelse=[],
                  lineno=50,
                  col_offset=8,
                  end_lineno=52,
                  end_col_offset=74)],
              lineno=47,
              col_offset=8,
              end_lineno=52,
              end_col_offset=74)],
          orelse=[],
          lineno=46,
          col_offset=4,
          end_lineno=52,
          end_col_offset=74),
        Return(
          value=Name(
            id='connection_text',
            ctx=Load(),
            lineno=54,
            col_offset=11,
            end_lineno=54,
            end_col_offset=26),
          lineno=54,
          col_offset=4,
          end_lineno=54,
          end_col_offset=26)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=44,
        col_offset=78,
        end_lineno=44,
        end_col_offset=81),
      lineno=44,
      col_offset=0,
      end_lineno=54,
      end_col_offset=26),
    FunctionDef(
      name='_get_block_text',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='block',
            annotation=Name(
              id='MermaidBlock',
              ctx=Load(),
              lineno=57,
              col_offset=27,
              end_lineno=57,
              end_col_offset=39),
            lineno=57,
            col_offset=20,
            end_lineno=57,
            end_col_offset=39),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=57,
              col_offset=49,
              end_lineno=57,
              end_col_offset=52),
            lineno=57,
            col_offset=41,
            end_lineno=57,
            end_col_offset=52)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='block_text',
              ctx=Store(),
              lineno=58,
              col_offset=4,
              end_lineno=58,
              end_col_offset=14)],
          value=Call(
            func=Name(
              id='_get_flow_connections',
              ctx=Load(),
              lineno=58,
              col_offset=17,
              end_lineno=58,
              end_col_offset=38),
            args=[
              Attribute(
                value=Name(
                  id='block',
                  ctx=Load(),
                  lineno=58,
                  col_offset=39,
                  end_lineno=58,
                  end_col_offset=44),
                attr='block_contents',
                ctx=Load(),
                lineno=58,
                col_offset=39,
                end_lineno=58,
                end_col_offset=59),
              Name(
                id='indent',
                ctx=Load(),
                lineno=58,
                col_offset=61,
                end_lineno=58,
                end_col_offset=67)],
            keywords=[],
            lineno=58,
            col_offset=17,
            end_lineno=58,
            end_col_offset=68),
          lineno=58,
          col_offset=4,
          end_lineno=58,
          end_col_offset=68),
        Return(
          value=Name(
            id='block_text',
            ctx=Load(),
            lineno=59,
            col_offset=11,
            end_lineno=59,
            end_col_offset=21),
          lineno=59,
          col_offset=4,
          end_lineno=59,
          end_col_offset=21)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=57,
        col_offset=57,
        end_lineno=57,
        end_col_offset=60),
      lineno=57,
      col_offset=0,
      end_lineno=59,
      end_col_offset=21),
    FunctionDef(
      name='create_mermaid_flow_graph_from_links',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='elements',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=62,
                col_offset=51,
                end_lineno=62,
                end_col_offset=55),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=62,
                col_offset=56,
                end_lineno=62,
                end_col_offset=70),
              ctx=Load(),
              lineno=62,
              col_offset=51,
              end_lineno=62,
              end_col_offset=71),
            lineno=62,
            col_offset=41,
            end_lineno=62,
            end_col_offset=71)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='alaises',
              ctx=Store(),
              lineno=63,
              col_offset=4,
              end_lineno=63,
              end_col_offset=11)],
          value=Call(
            func=Name(
              id='_get_aliases_for_safe_names',
              ctx=Load(),
              lineno=63,
              col_offset=14,
              end_lineno=63,
              end_col_offset=41),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=63,
                  col_offset=51,
                  end_lineno=63,
                  end_col_offset=59),
                lineno=63,
                col_offset=42,
                end_lineno=63,
                end_col_offset=59)],
            lineno=63,
            col_offset=14,
            end_lineno=63,
            end_col_offset=60),
          lineno=63,
          col_offset=4,
          end_lineno=63,
          end_col_offset=60),
        Assign(
          targets=[
            Name(
              id='flow_connections',
              ctx=Store(),
              lineno=64,
              col_offset=4,
              end_lineno=64,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_get_flow_connections',
              ctx=Load(),
              lineno=64,
              col_offset=23,
              end_lineno=64,
              end_col_offset=44),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=64,
                  col_offset=54,
                  end_lineno=64,
                  end_col_offset=62),
                lineno=64,
                col_offset=45,
                end_lineno=64,
                end_col_offset=62)],
            lineno=64,
            col_offset=23,
            end_lineno=64,
            end_col_offset=63),
          lineno=64,
          col_offset=4,
          end_lineno=64,
          end_col_offset=63),
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='```mermaid\nflowchart TB\n',
                lineno=66,
                col_offset=8,
                end_lineno=70,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='alaises',
                  ctx=Load(),
                  lineno=68,
                  col_offset=11,
                  end_lineno=68,
                  end_col_offset=18),
                conversion=-1,
                lineno=66,
                col_offset=8,
                end_lineno=70,
                end_col_offset=15),
              Constant(
                value='\n',
                lineno=66,
                col_offset=8,
                end_lineno=70,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='flow_connections',
                  ctx=Load(),
                  lineno=69,
                  col_offset=11,
                  end_lineno=69,
                  end_col_offset=27),
                conversion=-1,
                lineno=66,
                col_offset=8,
                end_lineno=70,
                end_col_offset=15),
              Constant(
                value='\n```\n',
                lineno=66,
                col_offset=8,
                end_lineno=70,
                end_col_offset=15)],
            lineno=66,
            col_offset=8,
            end_lineno=70,
            end_col_offset=15),
          lineno=65,
          col_offset=4,
          end_lineno=71,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=62,
        col_offset=76,
        end_lineno=62,
        end_col_offset=79),
      lineno=62,
      col_offset=0,
      end_lineno=71,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

