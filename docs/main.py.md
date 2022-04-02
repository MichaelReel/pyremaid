# ./src/main.py

### Imports

  - [pyremaid.pyremaid.create_mermaid_analysis_from_python](/docs/pyremaid/pyremaid.py.md)

---
```mermaid
flowchart TB
  _n0["If"]
  _n1["__name__ == '__main__'"]
  _n2["input_path = './src/'"]
  _n3["output_path = './docs/'"]
  _n4["Expr"]
  _n5["create_mermaid_analysis_from_python(input_path=input_path, output_path=output_path)"]

  _n0 --> _n1
  _n1 --> _n2
  _n2 --> _n3
  _n3 --> _n4
  _n4 --> _n5

```
---

<details>
<summary>Debug AST model dump</summary>

```
Module(
  body=[
    ImportFrom(
      module='pyremaid.pyremaid',
      names=[
        alias(
          name='create_mermaid_analysis_from_python',
          lineno=3,
          col_offset=30,
          end_lineno=3,
          end_col_offset=65)],
      level=0,
      lineno=3,
      col_offset=0,
      end_lineno=3,
      end_col_offset=65),
    If(
      test=Compare(
        left=Name(
          id='__name__',
          ctx=Load(),
          lineno=5,
          col_offset=3,
          end_lineno=5,
          end_col_offset=11),
        ops=[
          Eq()],
        comparators=[
          Constant(
            value='__main__',
            lineno=5,
            col_offset=15,
            end_lineno=5,
            end_col_offset=25)],
        lineno=5,
        col_offset=3,
        end_lineno=5,
        end_col_offset=25),
      body=[
        Assign(
          targets=[
            Name(
              id='input_path',
              ctx=Store(),
              lineno=8,
              col_offset=4,
              end_lineno=8,
              end_col_offset=14)],
          value=Constant(
            value='./src/',
            lineno=8,
            col_offset=17,
            end_lineno=8,
            end_col_offset=25),
          lineno=8,
          col_offset=4,
          end_lineno=8,
          end_col_offset=25),
        Assign(
          targets=[
            Name(
              id='output_path',
              ctx=Store(),
              lineno=9,
              col_offset=4,
              end_lineno=9,
              end_col_offset=15)],
          value=Constant(
            value='./docs/',
            lineno=9,
            col_offset=18,
            end_lineno=9,
            end_col_offset=27),
          lineno=9,
          col_offset=4,
          end_lineno=9,
          end_col_offset=27),
        Expr(
          value=Call(
            func=Name(
              id='create_mermaid_analysis_from_python',
              ctx=Load(),
              lineno=10,
              col_offset=4,
              end_lineno=10,
              end_col_offset=39),
            args=[],
            keywords=[
              keyword(
                arg='input_path',
                value=Name(
                  id='input_path',
                  ctx=Load(),
                  lineno=10,
                  col_offset=51,
                  end_lineno=10,
                  end_col_offset=61),
                lineno=10,
                col_offset=40,
                end_lineno=10,
                end_col_offset=61),
              keyword(
                arg='output_path',
                value=Name(
                  id='output_path',
                  ctx=Load(),
                  lineno=10,
                  col_offset=75,
                  end_lineno=10,
                  end_col_offset=86),
                lineno=10,
                col_offset=63,
                end_lineno=10,
                end_col_offset=86)],
            lineno=10,
            col_offset=4,
            end_lineno=10,
            end_col_offset=87),
          lineno=10,
          col_offset=4,
          end_lineno=10,
          end_col_offset=87)],
      orelse=[],
      lineno=5,
      col_offset=0,
      end_lineno=10,
      end_col_offset=87)],
  type_ignores=[])
```
</details>

