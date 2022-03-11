# ./src/pyremaid/pyremaid.py

### Imports

  - [files.destination.create_cleared_output_folder](/docs/pyremaid/files/destination.py.md)
  - [files.destination.get_output_file_path_for_input_file](/docs/pyremaid/files/destination.py.md)
  - [files.destination.update_output_file](/docs/pyremaid/files/destination.py.md)
  - [files.source.find_all_python_files](/docs/pyremaid/files/source.py.md)
  - [files.source.get_source_code_from_file](/docs/pyremaid/files/source.py.md)
  - [files.source.get_import_name_from_path](/docs/pyremaid/files/source.py.md)
  - [ast_tools.create_mermaid_model_from_ast_model](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_ast_root_node_for_file](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_markdown_dump_for_ast_node](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.get_used_import_list](/docs/pyremaid/ast_tools/__init__.py.md)
  - [ast_tools.import_map.get_all_imports_from_files](/docs/pyremaid/ast_tools/import_map.py.md)
  - [markdown_tools.create_markdown_content](/docs/pyremaid/markdown_tools.py.md)
  - [mermaid_tools.create_mermaid_flow_graph_from_links](/docs/pyremaid/mermaid_tools/__init__.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)

---
```mermaid
flowchart TB
  _f14_n163["Expr"]
  _f14_n164["Call"]
  _f14_n165["Name"]
  _f14_n166["Load"]
  _f14_n167["keyword"]
  _f14_n168["Name"]
  _f14_n169["Load"]
  _f14_n170["Assign"]
  _f14_n171["Name"]
  _f14_n172["Store"]
  _f14_n173["Call"]
  _f14_n174["Name"]
  _f14_n175["Load"]
  _f14_n176["keyword"]
  _f14_n177["Name"]
  _f14_n178["Load"]
  _f14_n179["Assign"]
  _f14_n180["Name"]
  _f14_n181["Store"]
  _f14_n182["Call"]
  _f14_n183["Name"]
  _f14_n184["Load"]
  _f14_n185["keyword"]
  _f14_n186["Name"]
  _f14_n187["Load"]
  _f14_n188["keyword"]
  _f14_n189["Name"]
  _f14_n190["Load"]
  _f14_n191["keyword"]
  _f14_n192["Name"]
  _f14_n193["Load"]
  _f14_l15["in_file"]
  _f14_l15_n194["Assign"]
  _f14_l15_n195["Name"]
  _f14_l15_n196["Store"]
  _f14_l15_n197["Call"]
  _f14_l15_n198["Attribute"]
  _f14_l15_n199["Name"]
  _f14_l15_n200["Load"]
  _f14_l15_n201["Load"]
  _f14_l15_n202["Name"]
  _f14_l15_n203["Load"]
  _f14_l15_n204["Constant"]
  _f14_l15_n205["Assign"]
  _f14_l15_n206["Name"]
  _f14_l15_n207["Store"]
  _f14_l15_n208["Call"]
  _f14_l15_n209["Name"]
  _f14_l15_n210["Load"]
  _f14_l15_n211["keyword"]
  _f14_l15_n212["Name"]
  _f14_l15_n213["Load"]
  _f14_l15_n214["keyword"]
  _f14_l15_n215["Name"]
  _f14_l15_n216["Load"]
  _f14_l15_n217["Assign"]
  _f14_l15_n218["Name"]
  _f14_l15_n219["Store"]
  _f14_l15_n220["Constant"]
  _f14_l15_n221["Assign"]
  _f14_l15_n222["Name"]
  _f14_l15_n223["Store"]
  _f14_l15_n224["List"]
  _f14_l15_n225["Load"]
  _f14_l15_n226["If"]
  _f14_l15_n227["NamedExpr"]
  _f14_l15_n228["Name"]
  _f14_l15_n229["Store"]
  _f14_l15_n230["Call"]
  _f14_l15_n231["Name"]
  _f14_l15_n232["Load"]
  _f14_l15_n233["keyword"]
  _f14_l15_n234["Name"]
  _f14_l15_n235["Load"]
  _f14_l15_n236["If"]
  _f14_l15_n237["NamedExpr"]
  _f14_l15_n238["Name"]
  _f14_l15_n239["Store"]
  _f14_l15_n240["Call"]
  _f14_l15_n241["Name"]
  _f14_l15_n242["Load"]
  _f14_l15_n243["keyword"]
  _f14_l15_n244["Name"]
  _f14_l15_n245["Load"]
  _f14_l15_n246["keyword"]
  _f14_l15_n247["Name"]
  _f14_l15_n248["Load"]
  _f14_l15_n249["Assign"]
  _f14_l15_n250["Name"]
  _f14_l15_n251["Store"]
  _f14_l15_n252["Call"]
  _f14_l15_n253["Name"]
  _f14_l15_n254["Load"]
  _f14_l15_n255["keyword"]
  _f14_l15_n256["Name"]
  _f14_l15_n257["Load"]
  _f14_l15_n258["Assign"]
  _f14_l15_n259["Name"]
  _f14_l15_n260["Store"]
  _f14_l15_n261["Call"]
  _f14_l15_n262["Name"]
  _f14_l15_n263["Load"]
  _f14_l15_n264["keyword"]
  _f14_l15_n265["Name"]
  _f14_l15_n266["Load"]
  _f14_l15_n267["AnnAssign"]
  _f14_l15_n268["Name"]
  _f14_l15_n269["Store"]
  _f14_l15_n270["Subscript"]
  _f14_l15_n271["Name"]
  _f14_l15_n272["Load"]
  _f14_l15_n273["Name"]
  _f14_l15_n274["Load"]
  _f14_l15_n275["Load"]
  _f14_l15_n276["Call"]
  _f14_l15_n277["Name"]
  _f14_l15_n278["Load"]
  _f14_l15_n279["keyword"]
  _f14_l15_n280["Name"]
  _f14_l15_n281["Load"]
  _f14_l15_n282["Assign"]
  _f14_l15_n283["Name"]
  _f14_l15_n284["Store"]
  _f14_l15_n285["Call"]
  _f14_l15_n286["Name"]
  _f14_l15_n287["Load"]
  _f14_l15_n288["Name"]
  _f14_l15_n289["Load"]
  _f14_l15_n290["Assign"]
  _f14_l15_n291["Name"]
  _f14_l15_n292["Store"]
  _f14_l15_n293["Call"]
  _f14_l15_n294["Name"]
  _f14_l15_n295["Load"]
  _f14_l15_n296["keyword"]
  _f14_l15_n297["Name"]
  _f14_l15_n298["Load"]
  _f14_l15_n299["keyword"]
  _f14_l15_n300["Name"]
  _f14_l15_n301["Load"]
  _f14_l15_n302["keyword"]
  _f14_l15_n303["Name"]
  _f14_l15_n304["Load"]
  _f14_l15_n305["keyword"]
  _f14_l15_n306["List"]
  _f14_l15_n307["Name"]
  _f14_l15_n308["Load"]
  _f14_l15_n309["Load"]
  _f14_l15_n310["keyword"]
  _f14_l15_n311["Name"]
  _f14_l15_n312["Load"]
  _f14_l15_n313["Expr"]
  _f14_l15_n314["Call"]
  _f14_l15_n315["Name"]
  _f14_l15_n316["Load"]
  _f14_l15_n317["keyword"]
  _f14_l15_n318["Name"]
  _f14_l15_n319["Load"]
  _f14_l15_n320["keyword"]
  _f14_l15_n321["Name"]
  _f14_l15_n322["Load"]
  _f16_n323["Assign"]
  _f16_n324["Name"]
  _f16_n325["Store"]
  _f16_n326["Call"]
  _f16_n327["Name"]
  _f16_n328["Load"]
  _f16_n329["keyword"]
  _f16_n330["Name"]
  _f16_n331["Load"]
  _f16_n332["keyword"]
  _f16_n333["Name"]
  _f16_n334["Load"]
  _f16_l17["global_import"]
  _f16_l17_n335["Assign"]
  _f16_l17_n336["Name"]
  _f16_l17_n337["Store"]
  _f16_l17_n338["Call"]
  _f16_l17_n339["Attribute"]
  _f16_l17_n340["Subscript"]
  _f16_l17_n341["Name"]
  _f16_l17_n342["Load"]
  _f16_l17_n343["Name"]
  _f16_l17_n344["Load"]
  _f16_l17_n345["Load"]
  _f16_l17_n346["Load"]
  _f16_l17_n347["Name"]
  _f16_l17_n348["Load"]
  _f16_l17_n349["Constant"]
  _f16_l17_n350["If"]
  _f16_l17_n351["Name"]
  _f16_l17_n352["Load"]
  _f16_l17_n353["Assign"]
  _f16_l17_n354["Subscript"]
  _f16_l17_n355["Name"]
  _f16_l17_n356["Load"]
  _f16_l17_n357["Name"]
  _f16_l17_n358["Load"]
  _f16_l17_n359["Store"]
  _f16_l17_n360["Call"]
  _f16_l17_n361["Attribute"]
  _f16_l17_n362["Call"]
  _f16_l17_n363["Name"]
  _f16_l17_n364["Load"]
  _f16_l17_n365["keyword"]
  _f16_l17_n366["Name"]
  _f16_l17_n367["Load"]
  _f16_l17_n368["keyword"]
  _f16_l17_n369["Name"]
  _f16_l17_n370["Load"]
  _f16_l17_n371["Load"]
  _f16_l17_n372["Constant"]
  _f16_n373["Expr"]
  _f16_n374["Call"]
  _f16_n375["Name"]
  _f16_n376["Load"]
  _f16_n377["Call"]
  _f16_n378["Attribute"]
  _f16_n379["Constant"]
  _f16_n380["Load"]
  _f16_n381["ListComp"]
  _f16_n382["JoinedStr"]
  _f16_n383["FormattedValue"]
  _f16_n384["Name"]
  _f16_n385["Load"]
  _f16_n386["Constant"]
  _f16_n387["FormattedValue"]
  _f16_n388["Name"]
  _f16_n389["Load"]
  _f16_n390["comprehension"]
  _f16_n391["Tuple"]
  _f16_n392["Name"]
  _f16_n393["Store"]
  _f16_n394["Name"]
  _f16_n395["Store"]
  _f16_n396["Store"]
  _f16_n397["Call"]
  _f16_n398["Attribute"]
  _f16_n399["Name"]
  _f16_n400["Load"]
  _f16_n401["Load"]
  _f16_n402["Return"]
  _f16_n403["Name"]
  _f16_n404["Load"]
  _n405["If"]
  _n406["Compare"]
  _n407["Name"]
  _n408["Load"]
  _n409["Eq"]
  _n410["Constant"]
  _n411["Assign"]
  _n412["Name"]
  _n413["Store"]
  _n414["Constant"]
  _n415["Assign"]
  _n416["Name"]
  _n417["Store"]
  _n418["Constant"]
  _n419["Expr"]
  _n420["Call"]
  _n421["Name"]
  _n422["Load"]
  _n423["keyword"]
  _n424["Name"]
  _n425["Load"]
  _n426["keyword"]
  _n427["Name"]
  _n428["Load"]

  subgraph _create_mermaid_analysis_from_python
    direction TB
    _f14_n163 --> _f14_n164
    _f14_n164 --> _f14_n165
    _f14_n165 --> _f14_n166
    _f14_n166 --> _f14_n167
    _f14_n167 --> _f14_n168
    _f14_n168 --> _f14_n169
    _f14_n169 --> _f14_n170
    _f14_n170 --> _f14_n171
    _f14_n171 --> _f14_n172
    _f14_n172 --> _f14_n173
    _f14_n173 --> _f14_n174
    _f14_n174 --> _f14_n175
    _f14_n175 --> _f14_n176
    _f14_n176 --> _f14_n177
    _f14_n177 --> _f14_n178
    _f14_n178 --> _f14_n179
    _f14_n179 --> _f14_n180
    _f14_n180 --> _f14_n181
    _f14_n181 --> _f14_n182
    _f14_n182 --> _f14_n183
    _f14_n183 --> _f14_n184
    _f14_n184 --> _f14_n185
    _f14_n185 --> _f14_n186
    _f14_n186 --> _f14_n187
    _f14_n187 --> _f14_n188
    _f14_n188 --> _f14_n189
    _f14_n189 --> _f14_n190
    _f14_n190 --> _f14_n191
    _f14_n191 --> _f14_n192
    _f14_n192 --> _f14_n193
    _f14_n193 --> _f14_l15
    %% loop in_file
      _f14_l15_n194 --> _f14_l15_n195
      _f14_l15_n195 --> _f14_l15_n196
      _f14_l15_n196 --> _f14_l15_n197
      _f14_l15_n197 --> _f14_l15_n198
      _f14_l15_n198 --> _f14_l15_n199
      _f14_l15_n199 --> _f14_l15_n200
      _f14_l15_n200 --> _f14_l15_n201
      _f14_l15_n201 --> _f14_l15_n202
      _f14_l15_n202 --> _f14_l15_n203
      _f14_l15_n203 --> _f14_l15_n204
      _f14_l15_n204 --> _f14_l15_n205
      _f14_l15_n205 --> _f14_l15_n206
      _f14_l15_n206 --> _f14_l15_n207
      _f14_l15_n207 --> _f14_l15_n208
      _f14_l15_n208 --> _f14_l15_n209
      _f14_l15_n209 --> _f14_l15_n210
      _f14_l15_n210 --> _f14_l15_n211
      _f14_l15_n211 --> _f14_l15_n212
      _f14_l15_n212 --> _f14_l15_n213
      _f14_l15_n213 --> _f14_l15_n214
      _f14_l15_n214 --> _f14_l15_n215
      _f14_l15_n215 --> _f14_l15_n216
      _f14_l15_n216 --> _f14_l15_n217
      _f14_l15_n217 --> _f14_l15_n218
      _f14_l15_n218 --> _f14_l15_n219
      _f14_l15_n219 --> _f14_l15_n220
      _f14_l15_n220 --> _f14_l15_n221
      _f14_l15_n221 --> _f14_l15_n222
      _f14_l15_n222 --> _f14_l15_n223
      _f14_l15_n223 --> _f14_l15_n224
      _f14_l15_n224 --> _f14_l15_n225
      _f14_l15_n225 --> _f14_l15_n226
      _f14_l15_n226 --> _f14_l15_n227
      _f14_l15_n227 --> _f14_l15_n228
      _f14_l15_n228 --> _f14_l15_n229
      _f14_l15_n229 --> _f14_l15_n230
      _f14_l15_n230 --> _f14_l15_n231
      _f14_l15_n231 --> _f14_l15_n232
      _f14_l15_n232 --> _f14_l15_n233
      _f14_l15_n233 --> _f14_l15_n234
      _f14_l15_n234 --> _f14_l15_n235
      _f14_l15_n235 --> _f14_l15_n236
      _f14_l15_n236 --> _f14_l15_n237
      _f14_l15_n237 --> _f14_l15_n238
      _f14_l15_n238 --> _f14_l15_n239
      _f14_l15_n239 --> _f14_l15_n240
      _f14_l15_n240 --> _f14_l15_n241
      _f14_l15_n241 --> _f14_l15_n242
      _f14_l15_n242 --> _f14_l15_n243
      _f14_l15_n243 --> _f14_l15_n244
      _f14_l15_n244 --> _f14_l15_n245
      _f14_l15_n245 --> _f14_l15_n246
      _f14_l15_n246 --> _f14_l15_n247
      _f14_l15_n247 --> _f14_l15_n248
      _f14_l15_n248 --> _f14_l15_n249
      _f14_l15_n249 --> _f14_l15_n250
      _f14_l15_n250 --> _f14_l15_n251
      _f14_l15_n251 --> _f14_l15_n252
      _f14_l15_n252 --> _f14_l15_n253
      _f14_l15_n253 --> _f14_l15_n254
      _f14_l15_n254 --> _f14_l15_n255
      _f14_l15_n255 --> _f14_l15_n256
      _f14_l15_n256 --> _f14_l15_n257
      _f14_l15_n257 --> _f14_l15_n258
      _f14_l15_n258 --> _f14_l15_n259
      _f14_l15_n259 --> _f14_l15_n260
      _f14_l15_n260 --> _f14_l15_n261
      _f14_l15_n261 --> _f14_l15_n262
      _f14_l15_n262 --> _f14_l15_n263
      _f14_l15_n263 --> _f14_l15_n264
      _f14_l15_n264 --> _f14_l15_n265
      _f14_l15_n265 --> _f14_l15_n266
      _f14_l15_n266 --> _f14_l15_n267
      _f14_l15_n267 --> _f14_l15_n268
      _f14_l15_n268 --> _f14_l15_n269
      _f14_l15_n269 --> _f14_l15_n270
      _f14_l15_n270 --> _f14_l15_n271
      _f14_l15_n271 --> _f14_l15_n272
      _f14_l15_n272 --> _f14_l15_n273
      _f14_l15_n273 --> _f14_l15_n274
      _f14_l15_n274 --> _f14_l15_n275
      _f14_l15_n275 --> _f14_l15_n276
      _f14_l15_n276 --> _f14_l15_n277
      _f14_l15_n277 --> _f14_l15_n278
      _f14_l15_n278 --> _f14_l15_n279
      _f14_l15_n279 --> _f14_l15_n280
      _f14_l15_n280 --> _f14_l15_n281
      _f14_l15_n281 --> _f14_l15_n282
      _f14_l15_n282 --> _f14_l15_n283
      _f14_l15_n283 --> _f14_l15_n284
      _f14_l15_n284 --> _f14_l15_n285
      _f14_l15_n285 --> _f14_l15_n286
      _f14_l15_n286 --> _f14_l15_n287
      _f14_l15_n287 --> _f14_l15_n288
      _f14_l15_n288 --> _f14_l15_n289
      _f14_l15_n289 --> _f14_l15_n290
      _f14_l15_n290 --> _f14_l15_n291
      _f14_l15_n291 --> _f14_l15_n292
      _f14_l15_n292 --> _f14_l15_n293
      _f14_l15_n293 --> _f14_l15_n294
      _f14_l15_n294 --> _f14_l15_n295
      _f14_l15_n295 --> _f14_l15_n296
      _f14_l15_n296 --> _f14_l15_n297
      _f14_l15_n297 --> _f14_l15_n298
      _f14_l15_n298 --> _f14_l15_n299
      _f14_l15_n299 --> _f14_l15_n300
      _f14_l15_n300 --> _f14_l15_n301
      _f14_l15_n301 --> _f14_l15_n302
      _f14_l15_n302 --> _f14_l15_n303
      _f14_l15_n303 --> _f14_l15_n304
      _f14_l15_n304 --> _f14_l15_n305
      _f14_l15_n305 --> _f14_l15_n306
      _f14_l15_n306 --> _f14_l15_n307
      _f14_l15_n307 --> _f14_l15_n308
      _f14_l15_n308 --> _f14_l15_n309
      _f14_l15_n309 --> _f14_l15_n310
      _f14_l15_n310 --> _f14_l15_n311
      _f14_l15_n311 --> _f14_l15_n312
      _f14_l15_n312 --> _f14_l15_n313
      _f14_l15_n313 --> _f14_l15_n314
      _f14_l15_n314 --> _f14_l15_n315
      _f14_l15_n315 --> _f14_l15_n316
      _f14_l15_n316 --> _f14_l15_n317
      _f14_l15_n317 --> _f14_l15_n318
      _f14_l15_n318 --> _f14_l15_n319
      _f14_l15_n319 --> _f14_l15_n320
      _f14_l15_n320 --> _f14_l15_n321
      _f14_l15_n321 --> _f14_l15_n322
    %% end in_file
    _f14_l15_n322 --> _f14_l15_n194
  end
  subgraph _get_global_input_table
    direction TB
    _f16_n323 --> _f16_n324
    _f16_n324 --> _f16_n325
    _f16_n325 --> _f16_n326
    _f16_n326 --> _f16_n327
    _f16_n327 --> _f16_n328
    _f16_n328 --> _f16_n329
    _f16_n329 --> _f16_n330
    _f16_n330 --> _f16_n331
    _f16_n331 --> _f16_n332
    _f16_n332 --> _f16_n333
    _f16_n333 --> _f16_n334
    _f16_n334 --> _f16_l17
    %% loop global_import
      _f16_l17_n335 --> _f16_l17_n336
      _f16_l17_n336 --> _f16_l17_n337
      _f16_l17_n337 --> _f16_l17_n338
      _f16_l17_n338 --> _f16_l17_n339
      _f16_l17_n339 --> _f16_l17_n340
      _f16_l17_n340 --> _f16_l17_n341
      _f16_l17_n341 --> _f16_l17_n342
      _f16_l17_n342 --> _f16_l17_n343
      _f16_l17_n343 --> _f16_l17_n344
      _f16_l17_n344 --> _f16_l17_n345
      _f16_l17_n345 --> _f16_l17_n346
      _f16_l17_n346 --> _f16_l17_n347
      _f16_l17_n347 --> _f16_l17_n348
      _f16_l17_n348 --> _f16_l17_n349
      _f16_l17_n349 --> _f16_l17_n350
      _f16_l17_n350 --> _f16_l17_n351
      _f16_l17_n351 --> _f16_l17_n352
      _f16_l17_n352 --> _f16_l17_n353
      _f16_l17_n353 --> _f16_l17_n354
      _f16_l17_n354 --> _f16_l17_n355
      _f16_l17_n355 --> _f16_l17_n356
      _f16_l17_n356 --> _f16_l17_n357
      _f16_l17_n357 --> _f16_l17_n358
      _f16_l17_n358 --> _f16_l17_n359
      _f16_l17_n359 --> _f16_l17_n360
      _f16_l17_n360 --> _f16_l17_n361
      _f16_l17_n361 --> _f16_l17_n362
      _f16_l17_n362 --> _f16_l17_n363
      _f16_l17_n363 --> _f16_l17_n364
      _f16_l17_n364 --> _f16_l17_n365
      _f16_l17_n365 --> _f16_l17_n366
      _f16_l17_n366 --> _f16_l17_n367
      _f16_l17_n367 --> _f16_l17_n368
      _f16_l17_n368 --> _f16_l17_n369
      _f16_l17_n369 --> _f16_l17_n370
      _f16_l17_n370 --> _f16_l17_n371
      _f16_l17_n371 --> _f16_l17_n372
    %% end global_import
    _f16_l17_n372 --> _f16_l17_n335
    _f16_l17_n335 --> _f16_n373
    _f16_n373 --> _f16_n374
    _f16_n374 --> _f16_n375
    _f16_n375 --> _f16_n376
    _f16_n376 --> _f16_n377
    _f16_n377 --> _f16_n378
    _f16_n378 --> _f16_n379
    _f16_n379 --> _f16_n380
    _f16_n380 --> _f16_n381
    _f16_n381 --> _f16_n382
    _f16_n382 --> _f16_n383
    _f16_n383 --> _f16_n384
    _f16_n384 --> _f16_n385
    _f16_n385 --> _f16_n386
    _f16_n386 --> _f16_n387
    _f16_n387 --> _f16_n388
    _f16_n388 --> _f16_n389
    _f16_n389 --> _f16_n390
    _f16_n390 --> _f16_n391
    _f16_n391 --> _f16_n392
    _f16_n392 --> _f16_n393
    _f16_n393 --> _f16_n394
    _f16_n394 --> _f16_n395
    _f16_n395 --> _f16_n396
    _f16_n396 --> _f16_n397
    _f16_n397 --> _f16_n398
    _f16_n398 --> _f16_n399
    _f16_n399 --> _f16_n400
    _f16_n400 --> _f16_n401
    _f16_n401 --> _f16_n402
    _f16_n402 --> _f16_n403
    _f16_n403 --> _f16_n404
  end
  _n405 --> _n406
  _n406 --> _n407
  _n407 --> _n408
  _n408 --> _n409
  _n409 --> _n410
  _n410 --> _n411
  _n411 --> _n412
  _n412 --> _n413
  _n413 --> _n414
  _n414 --> _n415
  _n415 --> _n416
  _n416 --> _n417
  _n417 --> _n418
  _n418 --> _n419
  _n419 --> _n420
  _n420 --> _n421
  _n421 --> _n422
  _n422 --> _n423
  _n423 --> _n424
  _n424 --> _n425
  _n425 --> _n426
  _n426 --> _n427
  _n427 --> _n428

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
        alias(name='create_mermaid_model_from_ast_model'),
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
        alias(name='MermaidElement')],
      level=0,
      lineno=18,
      col_offset=0,
      end_lineno=18,
      end_col_offset=33),
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
              id='global_import_table',
              ctx=Store(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=23)],
          value=Call(
            func=Name(
              id='get_global_input_table',
              ctx=Load(),
              lineno=23,
              col_offset=26,
              end_lineno=23,
              end_col_offset=48),
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
                end_col_offset=56),
              keyword(
                arg='output_root',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=24,
                  col_offset=70,
                  end_lineno=24,
                  end_col_offset=81),
                lineno=24,
                col_offset=58,
                end_lineno=24,
                end_col_offset=81)],
            lineno=23,
            col_offset=26,
            end_lineno=25,
            end_col_offset=5),
          lineno=23,
          col_offset=4,
          end_lineno=25,
          end_col_offset=5),
        For(
          target=Name(
            id='in_file',
            ctx=Store(),
            lineno=27,
            col_offset=8,
            end_lineno=27,
            end_col_offset=15),
          iter=Name(
            id='python_files',
            ctx=Load(),
            lineno=27,
            col_offset=19,
            end_lineno=27,
            end_col_offset=31),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=28,
                  col_offset=8,
                  end_lineno=28,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='in_file',
                    ctx=Load(),
                    lineno=28,
                    col_offset=27,
                    end_lineno=28,
                    end_col_offset=34),
                  attr='replace',
                  ctx=Load(),
                  lineno=28,
                  col_offset=27,
                  end_lineno=28,
                  end_col_offset=42),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=28,
                    col_offset=43,
                    end_lineno=28,
                    end_col_offset=53),
                  Constant(
                    value='',
                    lineno=28,
                    col_offset=55,
                    end_lineno=28,
                    end_col_offset=57)],
                keywords=[],
                lineno=28,
                col_offset=27,
                end_lineno=28,
                end_col_offset=58),
              lineno=28,
              col_offset=8,
              end_lineno=28,
              end_col_offset=58),
            Assign(
              targets=[
                Name(
                  id='out_file',
                  ctx=Store(),
                  lineno=29,
                  col_offset=8,
                  end_lineno=29,
                  end_col_offset=16)],
              value=Call(
                func=Name(
                  id='get_output_file_path_for_input_file',
                  ctx=Load(),
                  lineno=29,
                  col_offset=19,
                  end_lineno=29,
                  end_col_offset=54),
                args=[],
                keywords=[
                  keyword(
                    arg='input_path',
                    value=Name(
                      id='relative_in_file',
                      ctx=Load(),
                      lineno=30,
                      col_offset=23,
                      end_lineno=30,
                      end_col_offset=39),
                    lineno=30,
                    col_offset=12,
                    end_lineno=30,
                    end_col_offset=39),
                  keyword(
                    arg='output_root',
                    value=Name(
                      id='output_path',
                      ctx=Load(),
                      lineno=30,
                      col_offset=53,
                      end_lineno=30,
                      end_col_offset=64),
                    lineno=30,
                    col_offset=41,
                    end_lineno=30,
                    end_col_offset=64)],
                lineno=29,
                col_offset=19,
                end_lineno=31,
                end_col_offset=9),
              lineno=29,
              col_offset=8,
              end_lineno=31,
              end_col_offset=9),
            Assign(
              targets=[
                Name(
                  id='debug_dump',
                  ctx=Store(),
                  lineno=33,
                  col_offset=8,
                  end_lineno=33,
                  end_col_offset=18)],
              value=Constant(
                value='',
                lineno=33,
                col_offset=21,
                end_lineno=33,
                end_col_offset=23),
              lineno=33,
              col_offset=8,
              end_lineno=33,
              end_col_offset=23),
            Assign(
              targets=[
                Name(
                  id='import_list',
                  ctx=Store(),
                  lineno=34,
                  col_offset=8,
                  end_lineno=34,
                  end_col_offset=19)],
              value=List(
                elts=[],
                ctx=Load(),
                lineno=34,
                col_offset=22,
                end_lineno=34,
                end_col_offset=24),
              lineno=34,
              col_offset=8,
              end_lineno=34,
              end_col_offset=24),
            If(
              test=NamedExpr(
                target=Name(
                  id='source_code',
                  ctx=Store(),
                  lineno=36,
                  col_offset=11,
                  end_lineno=36,
                  end_col_offset=22),
                value=Call(
                  func=Name(
                    id='get_source_code_from_file',
                    ctx=Load(),
                    lineno=36,
                    col_offset=26,
                    end_lineno=36,
                    end_col_offset=51),
                  args=[],
                  keywords=[
                    keyword(
                      arg='input_file',
                      value=Name(
                        id='in_file',
                        ctx=Load(),
                        lineno=36,
                        col_offset=63,
                        end_lineno=36,
                        end_col_offset=70),
                      lineno=36,
                      col_offset=52,
                      end_lineno=36,
                      end_col_offset=70)],
                  lineno=36,
                  col_offset=26,
                  end_lineno=36,
                  end_col_offset=71),
                lineno=36,
                col_offset=11,
                end_lineno=36,
                end_col_offset=71),
              body=[
                If(
                  test=NamedExpr(
                    target=Name(
                      id='ast_node',
                      ctx=Store(),
                      lineno=37,
                      col_offset=15,
                      end_lineno=37,
                      end_col_offset=23),
                    value=Call(
                      func=Name(
                        id='get_ast_root_node_for_file',
                        ctx=Load(),
                        lineno=37,
                        col_offset=27,
                        end_lineno=37,
                        end_col_offset=53),
                      args=[],
                      keywords=[
                        keyword(
                          arg='source_code',
                          value=Name(
                            id='source_code',
                            ctx=Load(),
                            lineno=38,
                            col_offset=28,
                            end_lineno=38,
                            end_col_offset=39),
                          lineno=38,
                          col_offset=16,
                          end_lineno=38,
                          end_col_offset=39),
                        keyword(
                          arg='input_file',
                          value=Name(
                            id='in_file',
                            ctx=Load(),
                            lineno=39,
                            col_offset=27,
                            end_lineno=39,
                            end_col_offset=34),
                          lineno=39,
                          col_offset=16,
                          end_lineno=39,
                          end_col_offset=34)],
                      lineno=37,
                      col_offset=27,
                      end_lineno=40,
                      end_col_offset=13),
                    lineno=37,
                    col_offset=15,
                    end_lineno=40,
                    end_col_offset=13),
                  body=[
                    Assign(
                      targets=[
                        Name(
                          id='debug_dump',
                          ctx=Store(),
                          lineno=42,
                          col_offset=16,
                          end_lineno=42,
                          end_col_offset=26)],
                      value=Call(
                        func=Name(
                          id='get_markdown_dump_for_ast_node',
                          ctx=Load(),
                          lineno=42,
                          col_offset=29,
                          end_lineno=42,
                          end_col_offset=59),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=42,
                              col_offset=69,
                              end_lineno=42,
                              end_col_offset=77),
                            lineno=42,
                            col_offset=60,
                            end_lineno=42,
                            end_col_offset=77)],
                        lineno=42,
                        col_offset=29,
                        end_lineno=42,
                        end_col_offset=78),
                      lineno=42,
                      col_offset=16,
                      end_lineno=42,
                      end_col_offset=78),
                    Assign(
                      targets=[
                        Name(
                          id='import_list',
                          ctx=Store(),
                          lineno=44,
                          col_offset=16,
                          end_lineno=44,
                          end_col_offset=27)],
                      value=Call(
                        func=Name(
                          id='get_used_import_list',
                          ctx=Load(),
                          lineno=44,
                          col_offset=30,
                          end_lineno=44,
                          end_col_offset=50),
                        args=[],
                        keywords=[
                          keyword(
                            arg='ast_node',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=44,
                              col_offset=60,
                              end_lineno=44,
                              end_col_offset=68),
                            lineno=44,
                            col_offset=51,
                            end_lineno=44,
                            end_col_offset=68)],
                        lineno=44,
                        col_offset=30,
                        end_lineno=44,
                        end_col_offset=69),
                      lineno=44,
                      col_offset=16,
                      end_lineno=44,
                      end_col_offset=69),
                    AnnAssign(
                      target=Name(
                        id='link_info',
                        ctx=Store(),
                        lineno=46,
                        col_offset=16,
                        end_lineno=46,
                        end_col_offset=25),
                      annotation=Subscript(
                        value=Name(
                          id='list',
                          ctx=Load(),
                          lineno=46,
                          col_offset=28,
                          end_lineno=46,
                          end_col_offset=32),
                        slice=Name(
                          id='MermaidElement',
                          ctx=Load(),
                          lineno=46,
                          col_offset=33,
                          end_lineno=46,
                          end_col_offset=47),
                        ctx=Load(),
                        lineno=46,
                        col_offset=28,
                        end_lineno=46,
                        end_col_offset=48),
                      value=Call(
                        func=Name(
                          id='create_mermaid_model_from_ast_model',
                          ctx=Load(),
                          lineno=47,
                          col_offset=20,
                          end_lineno=47,
                          end_col_offset=55),
                        args=[],
                        keywords=[
                          keyword(
                            arg='model',
                            value=Name(
                              id='ast_node',
                              ctx=Load(),
                              lineno=47,
                              col_offset=62,
                              end_lineno=47,
                              end_col_offset=70),
                            lineno=47,
                            col_offset=56,
                            end_lineno=47,
                            end_col_offset=70)],
                        lineno=47,
                        col_offset=20,
                        end_lineno=47,
                        end_col_offset=71),
                      simple=1,
                      lineno=46,
                      col_offset=16,
                      end_lineno=48,
                      end_col_offset=17),
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
                  lineno=37,
                  col_offset=12,
                  end_lineno=50,
                  end_col_offset=81)],
              orelse=[],
              lineno=36,
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
                    arg='global_import_table',
                    value=Name(
                      id='global_import_table',
                      ctx=Load(),
                      lineno=55,
                      col_offset=32,
                      end_lineno=55,
                      end_col_offset=51),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=51),
                  keyword(
                    arg='mermaid_diagrams',
                    value=List(
                      elts=[
                        Name(
                          id='mermaid_diagram',
                          ctx=Load(),
                          lineno=56,
                          col_offset=30,
                          end_lineno=56,
                          end_col_offset=45)],
                      ctx=Load(),
                      lineno=56,
                      col_offset=29,
                      end_lineno=56,
                      end_col_offset=46),
                    lineno=56,
                    col_offset=12,
                    end_lineno=56,
                    end_col_offset=46),
                  keyword(
                    arg='debug_dump',
                    value=Name(
                      id='debug_dump',
                      ctx=Load(),
                      lineno=57,
                      col_offset=23,
                      end_lineno=57,
                      end_col_offset=33),
                    lineno=57,
                    col_offset=12,
                    end_lineno=57,
                    end_col_offset=33)],
                lineno=52,
                col_offset=27,
                end_lineno=58,
                end_col_offset=9),
              lineno=52,
              col_offset=8,
              end_lineno=58,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Name(
                  id='update_output_file',
                  ctx=Load(),
                  lineno=60,
                  col_offset=8,
                  end_lineno=60,
                  end_col_offset=26),
                args=[],
                keywords=[
                  keyword(
                    arg='content',
                    value=Name(
                      id='markdown_content',
                      ctx=Load(),
                      lineno=60,
                      col_offset=35,
                      end_lineno=60,
                      end_col_offset=51),
                    lineno=60,
                    col_offset=27,
                    end_lineno=60,
                    end_col_offset=51),
                  keyword(
                    arg='output_file',
                    value=Name(
                      id='out_file',
                      ctx=Load(),
                      lineno=60,
                      col_offset=65,
                      end_lineno=60,
                      end_col_offset=73),
                    lineno=60,
                    col_offset=53,
                    end_lineno=60,
                    end_col_offset=73)],
                lineno=60,
                col_offset=8,
                end_lineno=60,
                end_col_offset=74),
              lineno=60,
              col_offset=8,
              end_lineno=60,
              end_col_offset=74)],
          orelse=[],
          lineno=27,
          col_offset=4,
          end_lineno=60,
          end_col_offset=74)],
      decorator_list=[],
      lineno=20,
      col_offset=0,
      end_lineno=60,
      end_col_offset=74),
    FunctionDef(
      name='get_global_input_table',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='input_path',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=63,
              col_offset=16,
              end_lineno=63,
              end_col_offset=19),
            lineno=63,
            col_offset=4,
            end_lineno=63,
            end_col_offset=19),
          arg(
            arg='python_files',
            annotation=Subscript(
              value=Name(
                id='list',
                ctx=Load(),
                lineno=63,
                col_offset=35,
                end_lineno=63,
                end_col_offset=39),
              slice=Name(
                id='str',
                ctx=Load(),
                lineno=63,
                col_offset=40,
                end_lineno=63,
                end_col_offset=43),
              ctx=Load(),
              lineno=63,
              col_offset=35,
              end_lineno=63,
              end_col_offset=44),
            lineno=63,
            col_offset=21,
            end_lineno=63,
            end_col_offset=44),
          arg(
            arg='output_root',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=63,
              col_offset=59,
              end_lineno=63,
              end_col_offset=62),
            lineno=63,
            col_offset=46,
            end_lineno=63,
            end_col_offset=62)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='global_import_table',
              ctx=Store(),
              lineno=65,
              col_offset=4,
              end_lineno=65,
              end_col_offset=23)],
          value=Call(
            func=Name(
              id='get_all_imports_from_files',
              ctx=Load(),
              lineno=65,
              col_offset=26,
              end_lineno=65,
              end_col_offset=52),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=66,
                  col_offset=19,
                  end_lineno=66,
                  end_col_offset=29),
                lineno=66,
                col_offset=8,
                end_lineno=66,
                end_col_offset=29),
              keyword(
                arg='python_files',
                value=Name(
                  id='python_files',
                  ctx=Load(),
                  lineno=66,
                  col_offset=44,
                  end_lineno=66,
                  end_col_offset=56),
                lineno=66,
                col_offset=31,
                end_lineno=66,
                end_col_offset=56)],
            lineno=65,
            col_offset=26,
            end_lineno=67,
            end_col_offset=5),
          lineno=65,
          col_offset=4,
          end_lineno=67,
          end_col_offset=5),
        For(
          target=Name(
            id='global_import',
            ctx=Store(),
            lineno=68,
            col_offset=8,
            end_lineno=68,
            end_col_offset=21),
          iter=Name(
            id='global_import_table',
            ctx=Load(),
            lineno=68,
            col_offset=25,
            end_lineno=68,
            end_col_offset=44),
          body=[
            Assign(
              targets=[
                Name(
                  id='relative_in_file',
                  ctx=Store(),
                  lineno=69,
                  col_offset=8,
                  end_lineno=69,
                  end_col_offset=24)],
              value=Call(
                func=Attribute(
                  value=Subscript(
                    value=Name(
                      id='global_import_table',
                      ctx=Load(),
                      lineno=69,
                      col_offset=27,
                      end_lineno=69,
                      end_col_offset=46),
                    slice=Name(
                      id='global_import',
                      ctx=Load(),
                      lineno=69,
                      col_offset=47,
                      end_lineno=69,
                      end_col_offset=60),
                    ctx=Load(),
                    lineno=69,
                    col_offset=27,
                    end_lineno=69,
                    end_col_offset=61),
                  attr='replace',
                  ctx=Load(),
                  lineno=69,
                  col_offset=27,
                  end_lineno=69,
                  end_col_offset=69),
                args=[
                  Name(
                    id='input_path',
                    ctx=Load(),
                    lineno=69,
                    col_offset=70,
                    end_lineno=69,
                    end_col_offset=80),
                  Constant(
                    value='',
                    lineno=69,
                    col_offset=82,
                    end_lineno=69,
                    end_col_offset=84)],
                keywords=[],
                lineno=69,
                col_offset=27,
                end_lineno=69,
                end_col_offset=85),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=85),
            If(
              test=Name(
                id='relative_in_file',
                ctx=Load(),
                lineno=70,
                col_offset=11,
                end_lineno=70,
                end_col_offset=27),
              body=[
                Assign(
                  targets=[
                    Subscript(
                      value=Name(
                        id='global_import_table',
                        ctx=Load(),
                        lineno=71,
                        col_offset=12,
                        end_lineno=71,
                        end_col_offset=31),
                      slice=Name(
                        id='global_import',
                        ctx=Load(),
                        lineno=71,
                        col_offset=32,
                        end_lineno=71,
                        end_col_offset=45),
                      ctx=Store(),
                      lineno=71,
                      col_offset=12,
                      end_lineno=71,
                      end_col_offset=46)],
                  value=Call(
                    func=Attribute(
                      value=Call(
                        func=Name(
                          id='get_output_file_path_for_input_file',
                          ctx=Load(),
                          lineno=71,
                          col_offset=49,
                          end_lineno=71,
                          end_col_offset=84),
                        args=[],
                        keywords=[
                          keyword(
                            arg='input_path',
                            value=Name(
                              id='relative_in_file',
                              ctx=Load(),
                              lineno=72,
                              col_offset=27,
                              end_lineno=72,
                              end_col_offset=43),
                            lineno=72,
                            col_offset=16,
                            end_lineno=72,
                            end_col_offset=43),
                          keyword(
                            arg='output_root',
                            value=Name(
                              id='output_root',
                              ctx=Load(),
                              lineno=72,
                              col_offset=57,
                              end_lineno=72,
                              end_col_offset=68),
                            lineno=72,
                            col_offset=45,
                            end_lineno=72,
                            end_col_offset=68)],
                        lineno=71,
                        col_offset=49,
                        end_lineno=73,
                        end_col_offset=13),
                      attr='lstrip',
                      ctx=Load(),
                      lineno=71,
                      col_offset=49,
                      end_lineno=73,
                      end_col_offset=20),
                    args=[
                      Constant(
                        value='.',
                        lineno=73,
                        col_offset=21,
                        end_lineno=73,
                        end_col_offset=24)],
                    keywords=[],
                    lineno=71,
                    col_offset=49,
                    end_lineno=73,
                    end_col_offset=25),
                  lineno=71,
                  col_offset=12,
                  end_lineno=73,
                  end_col_offset=25)],
              orelse=[],
              lineno=70,
              col_offset=8,
              end_lineno=73,
              end_col_offset=25)],
          orelse=[],
          lineno=68,
          col_offset=4,
          end_lineno=73,
          end_col_offset=25),
        Expr(
          value=Call(
            func=Name(
              id='print',
              ctx=Load(),
              lineno=74,
              col_offset=4,
              end_lineno=74,
              end_col_offset=9),
            args=[
              Call(
                func=Attribute(
                  value=Constant(
                    value='\n',
                    lineno=74,
                    col_offset=10,
                    end_lineno=74,
                    end_col_offset=14),
                  attr='join',
                  ctx=Load(),
                  lineno=74,
                  col_offset=10,
                  end_lineno=74,
                  end_col_offset=19),
                args=[
                  ListComp(
                    elt=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Name(
                            id='k',
                            ctx=Load(),
                            lineno=74,
                            col_offset=24,
                            end_lineno=74,
                            end_col_offset=25),
                          conversion=-1,
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32),
                        Constant(
                          value=': ',
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32),
                        FormattedValue(
                          value=Name(
                            id='v',
                            ctx=Load(),
                            lineno=74,
                            col_offset=29,
                            end_lineno=74,
                            end_col_offset=30),
                          conversion=-1,
                          lineno=74,
                          col_offset=21,
                          end_lineno=74,
                          end_col_offset=32)],
                      lineno=74,
                      col_offset=21,
                      end_lineno=74,
                      end_col_offset=32),
                    generators=[
                      comprehension(
                        target=Tuple(
                          elts=[
                            Name(
                              id='k',
                              ctx=Store(),
                              lineno=74,
                              col_offset=37,
                              end_lineno=74,
                              end_col_offset=38),
                            Name(
                              id='v',
                              ctx=Store(),
                              lineno=74,
                              col_offset=39,
                              end_lineno=74,
                              end_col_offset=40)],
                          ctx=Store(),
                          lineno=74,
                          col_offset=37,
                          end_lineno=74,
                          end_col_offset=40),
                        iter=Call(
                          func=Attribute(
                            value=Name(
                              id='global_import_table',
                              ctx=Load(),
                              lineno=74,
                              col_offset=44,
                              end_lineno=74,
                              end_col_offset=63),
                            attr='items',
                            ctx=Load(),
                            lineno=74,
                            col_offset=44,
                            end_lineno=74,
                            end_col_offset=69),
                          args=[],
                          keywords=[],
                          lineno=74,
                          col_offset=44,
                          end_lineno=74,
                          end_col_offset=71),
                        ifs=[],
                        is_async=0)],
                    lineno=74,
                    col_offset=20,
                    end_lineno=74,
                    end_col_offset=72)],
                keywords=[],
                lineno=74,
                col_offset=10,
                end_lineno=74,
                end_col_offset=73)],
            keywords=[],
            lineno=74,
            col_offset=4,
            end_lineno=74,
            end_col_offset=74),
          lineno=74,
          col_offset=4,
          end_lineno=74,
          end_col_offset=74),
        Return(
          value=Name(
            id='global_import_table',
            ctx=Load(),
            lineno=75,
            col_offset=11,
            end_lineno=75,
            end_col_offset=30),
          lineno=75,
          col_offset=4,
          end_lineno=75,
          end_col_offset=30)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='dict',
          ctx=Load(),
          lineno=64,
          col_offset=5,
          end_lineno=64,
          end_col_offset=9),
        slice=Tuple(
          elts=[
            Name(
              id='str',
              ctx=Load(),
              lineno=64,
              col_offset=10,
              end_lineno=64,
              end_col_offset=13),
            Name(
              id='str',
              ctx=Load(),
              lineno=64,
              col_offset=14,
              end_lineno=64,
              end_col_offset=17)],
          ctx=Load(),
          lineno=64,
          col_offset=10,
          end_lineno=64,
          end_col_offset=17),
        ctx=Load(),
        lineno=64,
        col_offset=5,
        end_lineno=64,
        end_col_offset=18),
      lineno=62,
      col_offset=0,
      end_lineno=75,
      end_col_offset=30),
    If(
      test=Compare(
        left=Name(
          id='__name__',
          ctx=Load(),
          lineno=78,
          col_offset=3,
          end_lineno=78,
          end_col_offset=11),
        ops=[
          Eq()],
        comparators=[
          Constant(
            value='__main__',
            lineno=78,
            col_offset=15,
            end_lineno=78,
            end_col_offset=25)],
        lineno=78,
        col_offset=3,
        end_lineno=78,
        end_col_offset=25),
      body=[
        Assign(
          targets=[
            Name(
              id='input_path',
              ctx=Store(),
              lineno=81,
              col_offset=4,
              end_lineno=81,
              end_col_offset=14)],
          value=Constant(
            value='./src/pyremaid/',
            lineno=81,
            col_offset=17,
            end_lineno=81,
            end_col_offset=34),
          lineno=81,
          col_offset=4,
          end_lineno=81,
          end_col_offset=34),
        Assign(
          targets=[
            Name(
              id='output_path',
              ctx=Store(),
              lineno=82,
              col_offset=4,
              end_lineno=82,
              end_col_offset=15)],
          value=Constant(
            value='./docs/pyremaid/',
            lineno=82,
            col_offset=18,
            end_lineno=82,
            end_col_offset=36),
          lineno=82,
          col_offset=4,
          end_lineno=82,
          end_col_offset=36),
        Expr(
          value=Call(
            func=Name(
              id='create_mermaid_analysis_from_python',
              ctx=Load(),
              lineno=83,
              col_offset=4,
              end_lineno=83,
              end_col_offset=39),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=83,
                  col_offset=51,
                  end_lineno=83,
                  end_col_offset=61),
                lineno=83,
                col_offset=40,
                end_lineno=83,
                end_col_offset=61),
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=83,
                  col_offset=75,
                  end_lineno=83,
                  end_col_offset=86),
                lineno=83,
                col_offset=63,
                end_lineno=83,
                end_col_offset=86)],
            lineno=83,
            col_offset=4,
            end_lineno=83,
            end_col_offset=87),
          lineno=83,
          col_offset=4,
          end_lineno=83,
          end_col_offset=87)],
      orelse=[],
      lineno=78,
      col_offset=0,
      end_lineno=83,
      end_col_offset=87)],
  type_ignores=[])
```
</details>

