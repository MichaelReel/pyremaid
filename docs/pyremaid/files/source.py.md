# ./src/pyremaid/files/source.py

### Imports

  - os.*
  - re.match

---
```mermaid
flowchart TB
  _f87_n2170["Assign"]
  _f87_n2171["Name"]
  _f87_n2172["Store"]
  _f87_n2173["List"]
  _f87_n2174["Load"]
  _f87_l88["(dirpath, _dirnames, filenames)"]
  _f87_l88_l89_n2175["If"]
  _f87_l88_l89_n2176["Call"]
  _f87_l88_l89_n2177["Name"]
  _f87_l88_l89_n2178["Load"]
  _f87_l88_l89_n2179["Constant"]
  _f87_l88_l89_n2180["Name"]
  _f87_l88_l89_n2181["Load"]
  _f87_l88_l89_n2182["Expr"]
  _f87_l88_l89_n2183["Call"]
  _f87_l88_l89_n2184["Attribute"]
  _f87_l88_l89_n2185["Name"]
  _f87_l88_l89_n2186["Load"]
  _f87_l88_l89_n2187["Load"]
  _f87_l88_l89_n2188["Call"]
  _f87_l88_l89_n2189["Attribute"]
  _f87_l88_l89_n2190["Attribute"]
  _f87_l88_l89_n2191["Name"]
  _f87_l88_l89_n2192["Load"]
  _f87_l88_l89_n2193["Load"]
  _f87_l88_l89_n2194["Load"]
  _f87_l88_l89_n2195["Name"]
  _f87_l88_l89_n2196["Load"]
  _f87_l88_l89_n2197["Name"]
  _f87_l88_l89_n2198["Load"]
  _f87_l88_l89["filename"]
  _f87_n2199["Return"]
  _f87_n2200["Name"]
  _f87_n2201["Load"]
  _f90_n2202["Assign"]
  _f90_n2203["Name"]
  _f90_n2204["Store"]
  _f90_n2205["Constant"]
  _f90_n2206["With"]
  _f90_n2207["withitem"]
  _f90_n2208["Call"]
  _f90_n2209["Name"]
  _f90_n2210["Load"]
  _f90_n2211["Name"]
  _f90_n2212["Load"]
  _f90_n2213["Constant"]
  _f90_n2214["Name"]
  _f90_n2215["Store"]
  _f90_n2216["Assign"]
  _f90_n2217["Name"]
  _f90_n2218["Store"]
  _f90_n2219["Call"]
  _f90_n2220["Attribute"]
  _f90_n2221["Name"]
  _f90_n2222["Load"]
  _f90_n2223["Load"]
  _f90_n2224["Return"]
  _f90_n2225["Name"]
  _f90_n2226["Load"]
  _f91_n2227["Return"]
  _f91_n2228["Call"]
  _f91_n2229["Attribute"]
  _f91_n2230["Call"]
  _f91_n2231["Attribute"]
  _f91_n2232["Call"]
  _f91_n2233["Attribute"]
  _f91_n2234["Call"]
  _f91_n2235["Attribute"]
  _f91_n2236["Call"]
  _f91_n2237["Attribute"]
  _f91_n2238["Call"]
  _f91_n2239["Attribute"]
  _f91_n2240["Name"]
  _f91_n2241["Load"]
  _f91_n2242["Load"]
  _f91_n2243["Name"]
  _f91_n2244["Load"]
  _f91_n2245["Constant"]
  _f91_n2246["Load"]
  _f91_n2247["Constant"]
  _f91_n2248["Constant"]
  _f91_n2249["Load"]
  _f91_n2250["Constant"]
  _f91_n2251["Constant"]
  _f91_n2252["Load"]
  _f91_n2253["Attribute"]
  _f91_n2254["Name"]
  _f91_n2255["Load"]
  _f91_n2256["Load"]
  _f91_n2257["Constant"]
  _f91_n2258["Load"]
  _f91_n2259["Constant"]
  _f91_n2260["Constant"]
  _f91_n2261["Load"]
  _f91_n2262["Constant"]
  _f91_n2263["Constant"]

  subgraph _find_all_python_files
    direction TB
    _f87_n2170 --> _f87_n2171
    _f87_n2171 --> _f87_n2172
    _f87_n2172 --> _f87_n2173
    _f87_n2173 --> _f87_n2174
    _f87_n2174 --> _f87_l88
    %% loop (dirpath, _dirnames, filenames)
      %% loop filename
        _f87_l88_l89_n2175 --> _f87_l88_l89_n2176
        _f87_l88_l89_n2176 --> _f87_l88_l89_n2177
        _f87_l88_l89_n2177 --> _f87_l88_l89_n2178
        _f87_l88_l89_n2178 --> _f87_l88_l89_n2179
        _f87_l88_l89_n2179 --> _f87_l88_l89_n2180
        _f87_l88_l89_n2180 --> _f87_l88_l89_n2181
        _f87_l88_l89_n2181 --> _f87_l88_l89_n2182
        _f87_l88_l89_n2182 --> _f87_l88_l89_n2183
        _f87_l88_l89_n2183 --> _f87_l88_l89_n2184
        _f87_l88_l89_n2184 --> _f87_l88_l89_n2185
        _f87_l88_l89_n2185 --> _f87_l88_l89_n2186
        _f87_l88_l89_n2186 --> _f87_l88_l89_n2187
        _f87_l88_l89_n2187 --> _f87_l88_l89_n2188
        _f87_l88_l89_n2188 --> _f87_l88_l89_n2189
        _f87_l88_l89_n2189 --> _f87_l88_l89_n2190
        _f87_l88_l89_n2190 --> _f87_l88_l89_n2191
        _f87_l88_l89_n2191 --> _f87_l88_l89_n2192
        _f87_l88_l89_n2192 --> _f87_l88_l89_n2193
        _f87_l88_l89_n2193 --> _f87_l88_l89_n2194
        _f87_l88_l89_n2194 --> _f87_l88_l89_n2195
        _f87_l88_l89_n2195 --> _f87_l88_l89_n2196
        _f87_l88_l89_n2196 --> _f87_l88_l89_n2197
        _f87_l88_l89_n2197 --> _f87_l88_l89_n2198
      %% end filename
      _f87_l88_l89_n2198 --> _f87_l88_l89_n2175
    %% end (dirpath, _dirnames, filenames)
    _f87_l88_l89_n2175 --> _f87_l88_l89
    _f87_l88_l89 --> _f87_n2199
    _f87_n2199 --> _f87_n2200
    _f87_n2200 --> _f87_n2201
  end
  subgraph _get_source_code_from_file
    direction TB
    _f90_n2202 --> _f90_n2203
    _f90_n2203 --> _f90_n2204
    _f90_n2204 --> _f90_n2205
    _f90_n2205 --> _f90_n2206
    _f90_n2206 --> _f90_n2207
    _f90_n2207 --> _f90_n2208
    _f90_n2208 --> _f90_n2209
    _f90_n2209 --> _f90_n2210
    _f90_n2210 --> _f90_n2211
    _f90_n2211 --> _f90_n2212
    _f90_n2212 --> _f90_n2213
    _f90_n2213 --> _f90_n2214
    _f90_n2214 --> _f90_n2215
    _f90_n2215 --> _f90_n2216
    _f90_n2216 --> _f90_n2217
    _f90_n2217 --> _f90_n2218
    _f90_n2218 --> _f90_n2219
    _f90_n2219 --> _f90_n2220
    _f90_n2220 --> _f90_n2221
    _f90_n2221 --> _f90_n2222
    _f90_n2222 --> _f90_n2223
    _f90_n2223 --> _f90_n2224
    _f90_n2224 --> _f90_n2225
    _f90_n2225 --> _f90_n2226
  end
  subgraph _get_import_name_from_path
    direction TB
    _f91_n2227 --> _f91_n2228
    _f91_n2228 --> _f91_n2229
    _f91_n2229 --> _f91_n2230
    _f91_n2230 --> _f91_n2231
    _f91_n2231 --> _f91_n2232
    _f91_n2232 --> _f91_n2233
    _f91_n2233 --> _f91_n2234
    _f91_n2234 --> _f91_n2235
    _f91_n2235 --> _f91_n2236
    _f91_n2236 --> _f91_n2237
    _f91_n2237 --> _f91_n2238
    _f91_n2238 --> _f91_n2239
    _f91_n2239 --> _f91_n2240
    _f91_n2240 --> _f91_n2241
    _f91_n2241 --> _f91_n2242
    _f91_n2242 --> _f91_n2243
    _f91_n2243 --> _f91_n2244
    _f91_n2244 --> _f91_n2245
    _f91_n2245 --> _f91_n2246
    _f91_n2246 --> _f91_n2247
    _f91_n2247 --> _f91_n2248
    _f91_n2248 --> _f91_n2249
    _f91_n2249 --> _f91_n2250
    _f91_n2250 --> _f91_n2251
    _f91_n2251 --> _f91_n2252
    _f91_n2252 --> _f91_n2253
    _f91_n2253 --> _f91_n2254
    _f91_n2254 --> _f91_n2255
    _f91_n2255 --> _f91_n2256
    _f91_n2256 --> _f91_n2257
    _f91_n2257 --> _f91_n2258
    _f91_n2258 --> _f91_n2259
    _f91_n2259 --> _f91_n2260
    _f91_n2260 --> _f91_n2261
    _f91_n2261 --> _f91_n2262
    _f91_n2262 --> _f91_n2263
  end

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

