# ./src/pyremaid/files/source.py

### Imports

  - os.*
  - re.match

---
```mermaid
flowchart TB
  _f66_n1923["Assign"]
  _f66_n1924["Name"]
  _f66_n1925["Store"]
  _f66_n1926["List"]
  _f66_n1927["Load"]
  _f66_n1928["For"]
  _f66_n1929["Tuple"]
  _f66_n1930["Name"]
  _f66_n1931["Store"]
  _f66_n1932["Name"]
  _f66_n1933["Store"]
  _f66_n1934["Name"]
  _f66_n1935["Store"]
  _f66_n1936["Store"]
  _f66_n1937["Call"]
  _f66_n1938["Attribute"]
  _f66_n1939["Name"]
  _f66_n1940["Load"]
  _f66_n1941["Load"]
  _f66_n1942["Name"]
  _f66_n1943["Load"]
  _f66_n1944["For"]
  _f66_n1945["Name"]
  _f66_n1946["Store"]
  _f66_n1947["Name"]
  _f66_n1948["Load"]
  _f66_n1949["If"]
  _f66_n1950["Call"]
  _f66_n1951["Name"]
  _f66_n1952["Load"]
  _f66_n1953["Constant"]
  _f66_n1954["Name"]
  _f66_n1955["Load"]
  _f66_n1956["Expr"]
  _f66_n1957["Call"]
  _f66_n1958["Attribute"]
  _f66_n1959["Name"]
  _f66_n1960["Load"]
  _f66_n1961["Load"]
  _f66_n1962["Call"]
  _f66_n1963["Attribute"]
  _f66_n1964["Attribute"]
  _f66_n1965["Name"]
  _f66_n1966["Load"]
  _f66_n1967["Load"]
  _f66_n1968["Load"]
  _f66_n1969["Name"]
  _f66_n1970["Load"]
  _f66_n1971["Name"]
  _f66_n1972["Load"]
  _f66_n1973["Return"]
  _f66_n1974["Name"]
  _f66_n1975["Load"]
  _f67_n1976["Assign"]
  _f67_n1977["Name"]
  _f67_n1978["Store"]
  _f67_n1979["Constant"]
  _f67_n1980["With"]
  _f67_n1981["withitem"]
  _f67_n1982["Call"]
  _f67_n1983["Name"]
  _f67_n1984["Load"]
  _f67_n1985["Name"]
  _f67_n1986["Load"]
  _f67_n1987["Constant"]
  _f67_n1988["Name"]
  _f67_n1989["Store"]
  _f67_n1990["Assign"]
  _f67_n1991["Name"]
  _f67_n1992["Store"]
  _f67_n1993["Call"]
  _f67_n1994["Attribute"]
  _f67_n1995["Name"]
  _f67_n1996["Load"]
  _f67_n1997["Load"]
  _f67_n1998["Return"]
  _f67_n1999["Name"]
  _f67_n2000["Load"]
  _f68_n2001["Return"]
  _f68_n2002["Call"]
  _f68_n2003["Attribute"]
  _f68_n2004["Call"]
  _f68_n2005["Attribute"]
  _f68_n2006["Call"]
  _f68_n2007["Attribute"]
  _f68_n2008["Call"]
  _f68_n2009["Attribute"]
  _f68_n2010["Call"]
  _f68_n2011["Attribute"]
  _f68_n2012["Call"]
  _f68_n2013["Attribute"]
  _f68_n2014["Name"]
  _f68_n2015["Load"]
  _f68_n2016["Load"]
  _f68_n2017["Name"]
  _f68_n2018["Load"]
  _f68_n2019["Constant"]
  _f68_n2020["Load"]
  _f68_n2021["Constant"]
  _f68_n2022["Constant"]
  _f68_n2023["Load"]
  _f68_n2024["Constant"]
  _f68_n2025["Constant"]
  _f68_n2026["Load"]
  _f68_n2027["Attribute"]
  _f68_n2028["Name"]
  _f68_n2029["Load"]
  _f68_n2030["Load"]
  _f68_n2031["Constant"]
  _f68_n2032["Load"]
  _f68_n2033["Constant"]
  _f68_n2034["Constant"]
  _f68_n2035["Load"]
  _f68_n2036["Constant"]
  _f68_n2037["Constant"]

  subgraph _find_all_python_files
    direction TB
    _f66_n1923 --> _f66_n1924
    _f66_n1924 --> _f66_n1925
    _f66_n1925 --> _f66_n1926
    _f66_n1926 --> _f66_n1927
    _f66_n1927 --> _f66_n1928
    _f66_n1928 --> _f66_n1929
    _f66_n1929 --> _f66_n1930
    _f66_n1930 --> _f66_n1931
    _f66_n1931 --> _f66_n1932
    _f66_n1932 --> _f66_n1933
    _f66_n1933 --> _f66_n1934
    _f66_n1934 --> _f66_n1935
    _f66_n1935 --> _f66_n1936
    _f66_n1936 --> _f66_n1937
    _f66_n1937 --> _f66_n1938
    _f66_n1938 --> _f66_n1939
    _f66_n1939 --> _f66_n1940
    _f66_n1940 --> _f66_n1941
    _f66_n1941 --> _f66_n1942
    _f66_n1942 --> _f66_n1943
    _f66_n1943 --> _f66_n1944
    _f66_n1944 --> _f66_n1945
    _f66_n1945 --> _f66_n1946
    _f66_n1946 --> _f66_n1947
    _f66_n1947 --> _f66_n1948
    _f66_n1948 --> _f66_n1949
    _f66_n1949 --> _f66_n1950
    _f66_n1950 --> _f66_n1951
    _f66_n1951 --> _f66_n1952
    _f66_n1952 --> _f66_n1953
    _f66_n1953 --> _f66_n1954
    _f66_n1954 --> _f66_n1955
    _f66_n1955 --> _f66_n1956
    _f66_n1956 --> _f66_n1957
    _f66_n1957 --> _f66_n1958
    _f66_n1958 --> _f66_n1959
    _f66_n1959 --> _f66_n1960
    _f66_n1960 --> _f66_n1961
    _f66_n1961 --> _f66_n1962
    _f66_n1962 --> _f66_n1963
    _f66_n1963 --> _f66_n1964
    _f66_n1964 --> _f66_n1965
    _f66_n1965 --> _f66_n1966
    _f66_n1966 --> _f66_n1967
    _f66_n1967 --> _f66_n1968
    _f66_n1968 --> _f66_n1969
    _f66_n1969 --> _f66_n1970
    _f66_n1970 --> _f66_n1971
    _f66_n1971 --> _f66_n1972
    _f66_n1972 --> _f66_n1973
    _f66_n1973 --> _f66_n1974
    _f66_n1974 --> _f66_n1975
  end
  subgraph _get_source_code_from_file
    direction TB
    _f67_n1976 --> _f67_n1977
    _f67_n1977 --> _f67_n1978
    _f67_n1978 --> _f67_n1979
    _f67_n1979 --> _f67_n1980
    _f67_n1980 --> _f67_n1981
    _f67_n1981 --> _f67_n1982
    _f67_n1982 --> _f67_n1983
    _f67_n1983 --> _f67_n1984
    _f67_n1984 --> _f67_n1985
    _f67_n1985 --> _f67_n1986
    _f67_n1986 --> _f67_n1987
    _f67_n1987 --> _f67_n1988
    _f67_n1988 --> _f67_n1989
    _f67_n1989 --> _f67_n1990
    _f67_n1990 --> _f67_n1991
    _f67_n1991 --> _f67_n1992
    _f67_n1992 --> _f67_n1993
    _f67_n1993 --> _f67_n1994
    _f67_n1994 --> _f67_n1995
    _f67_n1995 --> _f67_n1996
    _f67_n1996 --> _f67_n1997
    _f67_n1997 --> _f67_n1998
    _f67_n1998 --> _f67_n1999
    _f67_n1999 --> _f67_n2000
  end
  subgraph _get_import_name_from_path
    direction TB
    _f68_n2001 --> _f68_n2002
    _f68_n2002 --> _f68_n2003
    _f68_n2003 --> _f68_n2004
    _f68_n2004 --> _f68_n2005
    _f68_n2005 --> _f68_n2006
    _f68_n2006 --> _f68_n2007
    _f68_n2007 --> _f68_n2008
    _f68_n2008 --> _f68_n2009
    _f68_n2009 --> _f68_n2010
    _f68_n2010 --> _f68_n2011
    _f68_n2011 --> _f68_n2012
    _f68_n2012 --> _f68_n2013
    _f68_n2013 --> _f68_n2014
    _f68_n2014 --> _f68_n2015
    _f68_n2015 --> _f68_n2016
    _f68_n2016 --> _f68_n2017
    _f68_n2017 --> _f68_n2018
    _f68_n2018 --> _f68_n2019
    _f68_n2019 --> _f68_n2020
    _f68_n2020 --> _f68_n2021
    _f68_n2021 --> _f68_n2022
    _f68_n2022 --> _f68_n2023
    _f68_n2023 --> _f68_n2024
    _f68_n2024 --> _f68_n2025
    _f68_n2025 --> _f68_n2026
    _f68_n2026 --> _f68_n2027
    _f68_n2027 --> _f68_n2028
    _f68_n2028 --> _f68_n2029
    _f68_n2029 --> _f68_n2030
    _f68_n2030 --> _f68_n2031
    _f68_n2031 --> _f68_n2032
    _f68_n2032 --> _f68_n2033
    _f68_n2033 --> _f68_n2034
    _f68_n2034 --> _f68_n2035
    _f68_n2035 --> _f68_n2036
    _f68_n2036 --> _f68_n2037
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

