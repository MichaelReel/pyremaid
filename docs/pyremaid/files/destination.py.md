# ./src/pyremaid/files/destination.py

### Imports

  - os.*

---
```mermaid
flowchart TB
  _f79_n2042["If"]
  _f79_n2043["UnaryOp"]
  _f79_n2044["Not"]
  _f79_n2045["Call"]
  _f79_n2046["Attribute"]
  _f79_n2047["Attribute"]
  _f79_n2048["Name"]
  _f79_n2049["Load"]
  _f79_n2050["Load"]
  _f79_n2051["Load"]
  _f79_n2052["Name"]
  _f79_n2053["Load"]
  _f79_n2054["Expr"]
  _f79_n2055["Call"]
  _f79_n2056["Attribute"]
  _f79_n2057["Name"]
  _f79_n2058["Load"]
  _f79_n2059["Load"]
  _f79_n2060["Name"]
  _f79_n2061["Load"]
  _f80_n2062["Expr"]
  _f80_n2063["Call"]
  _f80_n2064["Name"]
  _f80_n2065["Load"]
  _f80_n2066["keyword"]
  _f80_n2067["Name"]
  _f80_n2068["Load"]
  _f80_l81["(root, dirs, files)"]
  _f80_l81_l82_n2069["Expr"]
  _f80_l81_l82_n2070["Call"]
  _f80_l81_l82_n2071["Attribute"]
  _f80_l81_l82_n2072["Name"]
  _f80_l81_l82_n2073["Load"]
  _f80_l81_l82_n2074["Load"]
  _f80_l81_l82_n2075["Call"]
  _f80_l81_l82_n2076["Attribute"]
  _f80_l81_l82_n2077["Attribute"]
  _f80_l81_l82_n2078["Name"]
  _f80_l81_l82_n2079["Load"]
  _f80_l81_l82_n2080["Load"]
  _f80_l81_l82_n2081["Load"]
  _f80_l81_l82_n2082["Name"]
  _f80_l81_l82_n2083["Load"]
  _f80_l81_l82_n2084["Name"]
  _f80_l81_l82_n2085["Load"]
  _f80_l81_l83["name"]
  _f80_l81_l83_n2086["Expr"]
  _f80_l81_l83_n2087["Call"]
  _f80_l81_l83_n2088["Attribute"]
  _f80_l81_l83_n2089["Name"]
  _f80_l81_l83_n2090["Load"]
  _f80_l81_l83_n2091["Load"]
  _f80_l81_l83_n2092["Call"]
  _f80_l81_l83_n2093["Attribute"]
  _f80_l81_l83_n2094["Attribute"]
  _f80_l81_l83_n2095["Name"]
  _f80_l81_l83_n2096["Load"]
  _f80_l81_l83_n2097["Load"]
  _f80_l81_l83_n2098["Load"]
  _f80_l81_l83_n2099["Name"]
  _f80_l81_l83_n2100["Load"]
  _f80_l81_l83_n2101["Name"]
  _f80_l81_l83_n2102["Load"]
  _f80_l81_l82["name"]
  _f84_n2103["Return"]
  _f84_n2104["Call"]
  _f84_n2105["Attribute"]
  _f84_n2106["Attribute"]
  _f84_n2107["Name"]
  _f84_n2108["Load"]
  _f84_n2109["Load"]
  _f84_n2110["Load"]
  _f84_n2111["Name"]
  _f84_n2112["Load"]
  _f84_n2113["BinOp"]
  _f84_n2114["Name"]
  _f84_n2115["Load"]
  _f84_n2116["Add"]
  _f84_n2117["Constant"]
  _f85_n2118["If"]
  _f85_n2119["UnaryOp"]
  _f85_n2120["Not"]
  _f85_n2121["Call"]
  _f85_n2122["Attribute"]
  _f85_n2123["Attribute"]
  _f85_n2124["Name"]
  _f85_n2125["Load"]
  _f85_n2126["Load"]
  _f85_n2127["Load"]
  _f85_n2128["Call"]
  _f85_n2129["Attribute"]
  _f85_n2130["Attribute"]
  _f85_n2131["Name"]
  _f85_n2132["Load"]
  _f85_n2133["Load"]
  _f85_n2134["Load"]
  _f85_n2135["Name"]
  _f85_n2136["Load"]
  _f85_n2137["Expr"]
  _f85_n2138["Call"]
  _f85_n2139["Attribute"]
  _f85_n2140["Name"]
  _f85_n2141["Load"]
  _f85_n2142["Load"]
  _f85_n2143["Call"]
  _f85_n2144["Attribute"]
  _f85_n2145["Attribute"]
  _f85_n2146["Name"]
  _f85_n2147["Load"]
  _f85_n2148["Load"]
  _f85_n2149["Load"]
  _f85_n2150["Name"]
  _f85_n2151["Load"]
  _f85_n2152["With"]
  _f85_n2153["withitem"]
  _f85_n2154["Call"]
  _f85_n2155["Name"]
  _f85_n2156["Load"]
  _f85_n2157["Name"]
  _f85_n2158["Load"]
  _f85_n2159["Constant"]
  _f85_n2160["Name"]
  _f85_n2161["Store"]
  _f85_n2162["Expr"]
  _f85_n2163["Call"]
  _f85_n2164["Attribute"]
  _f85_n2165["Name"]
  _f85_n2166["Load"]
  _f85_n2167["Load"]
  _f85_n2168["Name"]
  _f85_n2169["Load"]

  subgraph _create_output_folder
    direction TB
    _f79_n2042 --> _f79_n2043
    _f79_n2043 --> _f79_n2044
    _f79_n2044 --> _f79_n2045
    _f79_n2045 --> _f79_n2046
    _f79_n2046 --> _f79_n2047
    _f79_n2047 --> _f79_n2048
    _f79_n2048 --> _f79_n2049
    _f79_n2049 --> _f79_n2050
    _f79_n2050 --> _f79_n2051
    _f79_n2051 --> _f79_n2052
    _f79_n2052 --> _f79_n2053
    _f79_n2053 --> _f79_n2054
    _f79_n2054 --> _f79_n2055
    _f79_n2055 --> _f79_n2056
    _f79_n2056 --> _f79_n2057
    _f79_n2057 --> _f79_n2058
    _f79_n2058 --> _f79_n2059
    _f79_n2059 --> _f79_n2060
    _f79_n2060 --> _f79_n2061
  end
  subgraph _create_cleared_output_folder
    direction TB
    _f80_n2062 --> _f80_n2063
    _f80_n2063 --> _f80_n2064
    _f80_n2064 --> _f80_n2065
    _f80_n2065 --> _f80_n2066
    _f80_n2066 --> _f80_n2067
    _f80_n2067 --> _f80_n2068
    _f80_n2068 --> _f80_l81
    %% loop (root, dirs, files)
      %% loop name
        _f80_l81_l82_n2069 --> _f80_l81_l82_n2070
        _f80_l81_l82_n2070 --> _f80_l81_l82_n2071
        _f80_l81_l82_n2071 --> _f80_l81_l82_n2072
        _f80_l81_l82_n2072 --> _f80_l81_l82_n2073
        _f80_l81_l82_n2073 --> _f80_l81_l82_n2074
        _f80_l81_l82_n2074 --> _f80_l81_l82_n2075
        _f80_l81_l82_n2075 --> _f80_l81_l82_n2076
        _f80_l81_l82_n2076 --> _f80_l81_l82_n2077
        _f80_l81_l82_n2077 --> _f80_l81_l82_n2078
        _f80_l81_l82_n2078 --> _f80_l81_l82_n2079
        _f80_l81_l82_n2079 --> _f80_l81_l82_n2080
        _f80_l81_l82_n2080 --> _f80_l81_l82_n2081
        _f80_l81_l82_n2081 --> _f80_l81_l82_n2082
        _f80_l81_l82_n2082 --> _f80_l81_l82_n2083
        _f80_l81_l82_n2083 --> _f80_l81_l82_n2084
        _f80_l81_l82_n2084 --> _f80_l81_l82_n2085
      %% end name
      _f80_l81_l82_n2085 --> _f80_l81_l82_n2069
      _f80_l81_l82_n2069 --> _f80_l81_l83
      %% loop name
        _f80_l81_l83_n2086 --> _f80_l81_l83_n2087
        _f80_l81_l83_n2087 --> _f80_l81_l83_n2088
        _f80_l81_l83_n2088 --> _f80_l81_l83_n2089
        _f80_l81_l83_n2089 --> _f80_l81_l83_n2090
        _f80_l81_l83_n2090 --> _f80_l81_l83_n2091
        _f80_l81_l83_n2091 --> _f80_l81_l83_n2092
        _f80_l81_l83_n2092 --> _f80_l81_l83_n2093
        _f80_l81_l83_n2093 --> _f80_l81_l83_n2094
        _f80_l81_l83_n2094 --> _f80_l81_l83_n2095
        _f80_l81_l83_n2095 --> _f80_l81_l83_n2096
        _f80_l81_l83_n2096 --> _f80_l81_l83_n2097
        _f80_l81_l83_n2097 --> _f80_l81_l83_n2098
        _f80_l81_l83_n2098 --> _f80_l81_l83_n2099
        _f80_l81_l83_n2099 --> _f80_l81_l83_n2100
        _f80_l81_l83_n2100 --> _f80_l81_l83_n2101
        _f80_l81_l83_n2101 --> _f80_l81_l83_n2102
      %% end name
      _f80_l81_l83_n2102 --> _f80_l81_l83_n2086
    %% end (root, dirs, files)
    _f80_l81_l83_n2086 --> _f80_l81_l82
  end
  subgraph _get_output_file_path_for_input_file
    direction TB
    _f84_n2103 --> _f84_n2104
    _f84_n2104 --> _f84_n2105
    _f84_n2105 --> _f84_n2106
    _f84_n2106 --> _f84_n2107
    _f84_n2107 --> _f84_n2108
    _f84_n2108 --> _f84_n2109
    _f84_n2109 --> _f84_n2110
    _f84_n2110 --> _f84_n2111
    _f84_n2111 --> _f84_n2112
    _f84_n2112 --> _f84_n2113
    _f84_n2113 --> _f84_n2114
    _f84_n2114 --> _f84_n2115
    _f84_n2115 --> _f84_n2116
    _f84_n2116 --> _f84_n2117
  end
  subgraph _update_output_file
    direction TB
    _f85_n2118 --> _f85_n2119
    _f85_n2119 --> _f85_n2120
    _f85_n2120 --> _f85_n2121
    _f85_n2121 --> _f85_n2122
    _f85_n2122 --> _f85_n2123
    _f85_n2123 --> _f85_n2124
    _f85_n2124 --> _f85_n2125
    _f85_n2125 --> _f85_n2126
    _f85_n2126 --> _f85_n2127
    _f85_n2127 --> _f85_n2128
    _f85_n2128 --> _f85_n2129
    _f85_n2129 --> _f85_n2130
    _f85_n2130 --> _f85_n2131
    _f85_n2131 --> _f85_n2132
    _f85_n2132 --> _f85_n2133
    _f85_n2133 --> _f85_n2134
    _f85_n2134 --> _f85_n2135
    _f85_n2135 --> _f85_n2136
    _f85_n2136 --> _f85_n2137
    _f85_n2137 --> _f85_n2138
    _f85_n2138 --> _f85_n2139
    _f85_n2139 --> _f85_n2140
    _f85_n2140 --> _f85_n2141
    _f85_n2141 --> _f85_n2142
    _f85_n2142 --> _f85_n2143
    _f85_n2143 --> _f85_n2144
    _f85_n2144 --> _f85_n2145
    _f85_n2145 --> _f85_n2146
    _f85_n2146 --> _f85_n2147
    _f85_n2147 --> _f85_n2148
    _f85_n2148 --> _f85_n2149
    _f85_n2149 --> _f85_n2150
    _f85_n2150 --> _f85_n2151
    _f85_n2151 --> _f85_n2152
    _f85_n2152 --> _f85_n2153
    _f85_n2153 --> _f85_n2154
    _f85_n2154 --> _f85_n2155
    _f85_n2155 --> _f85_n2156
    _f85_n2156 --> _f85_n2157
    _f85_n2157 --> _f85_n2158
    _f85_n2158 --> _f85_n2159
    _f85_n2159 --> _f85_n2160
    _f85_n2160 --> _f85_n2161
    _f85_n2161 --> _f85_n2162
    _f85_n2162 --> _f85_n2163
    _f85_n2163 --> _f85_n2164
    _f85_n2164 --> _f85_n2165
    _f85_n2165 --> _f85_n2166
    _f85_n2166 --> _f85_n2167
    _f85_n2167 --> _f85_n2168
    _f85_n2168 --> _f85_n2169
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

