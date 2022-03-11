# ./src/pyremaid/ast_tools/ast_tools.py

### Imports

  - ast.AST
  - ast.dump
  - ast.parse
  - typing.Optional
  - [ast_tools.visitors.BlockGenerator](/docs/pyremaid/ast_tools/visitors.py.md)
  - [ast_tools.visitors.ImportNodeFinder](/docs/pyremaid/ast_tools/visitors.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)

---
```mermaid
flowchart TB
  _f63_n1727["Return"]
  _f63_n1728["Call"]
  _f63_n1729["Name"]
  _f63_n1730["Load"]
  _f63_n1731["keyword"]
  _f63_n1732["Name"]
  _f63_n1733["Load"]
  _f63_n1734["keyword"]
  _f63_n1735["Name"]
  _f63_n1736["Load"]
  _f63_n1737["keyword"]
  _f63_n1738["Constant"]
  _f63_n1739["keyword"]
  _f63_n1740["Constant"]
  _f64_n1741["Return"]
  _f64_n1742["Call"]
  _f64_n1743["Name"]
  _f64_n1744["Load"]
  _f64_n1745["Name"]
  _f64_n1746["Load"]
  _f64_n1747["keyword"]
  _f64_n1748["Constant"]
  _f64_n1749["keyword"]
  _f64_n1750["Constant"]
  _f64_n1751["keyword"]
  _f64_n1752["Constant"]
  _f65_n1753["Assign"]
  _f65_n1754["Name"]
  _f65_n1755["Store"]
  _f65_n1756["Call"]
  _f65_n1757["Name"]
  _f65_n1758["Load"]
  _f65_n1759["Expr"]
  _f65_n1760["Call"]
  _f65_n1761["Attribute"]
  _f65_n1762["Name"]
  _f65_n1763["Load"]
  _f65_n1764["Load"]
  _f65_n1765["Name"]
  _f65_n1766["Load"]
  _f65_n1767["Return"]
  _f65_n1768["Call"]
  _f65_n1769["Attribute"]
  _f65_n1770["Name"]
  _f65_n1771["Load"]
  _f65_n1772["Load"]
  _f66_n1773["Assign"]
  _f66_n1774["Name"]
  _f66_n1775["Store"]
  _f66_n1776["Call"]
  _f66_n1777["Name"]
  _f66_n1778["Load"]
  _f66_n1779["Expr"]
  _f66_n1780["Call"]
  _f66_n1781["Attribute"]
  _f66_n1782["Name"]
  _f66_n1783["Load"]
  _f66_n1784["Load"]
  _f66_n1785["keyword"]
  _f66_n1786["Name"]
  _f66_n1787["Load"]
  _f66_n1788["Return"]
  _f66_n1789["Call"]
  _f66_n1790["Attribute"]
  _f66_n1791["Name"]
  _f66_n1792["Load"]
  _f66_n1793["Load"]

  subgraph _get_ast_root_node_for_file
    direction TB
    _f63_n1727 --> _f63_n1728
    _f63_n1728 --> _f63_n1729
    _f63_n1729 --> _f63_n1730
    _f63_n1730 --> _f63_n1731
    _f63_n1731 --> _f63_n1732
    _f63_n1732 --> _f63_n1733
    _f63_n1733 --> _f63_n1734
    _f63_n1734 --> _f63_n1735
    _f63_n1735 --> _f63_n1736
    _f63_n1736 --> _f63_n1737
    _f63_n1737 --> _f63_n1738
    _f63_n1738 --> _f63_n1739
    _f63_n1739 --> _f63_n1740
  end
  subgraph _get_markdown_dump_for_ast_node
    direction TB
    _f64_n1741 --> _f64_n1742
    _f64_n1742 --> _f64_n1743
    _f64_n1743 --> _f64_n1744
    _f64_n1744 --> _f64_n1745
    _f64_n1745 --> _f64_n1746
    _f64_n1746 --> _f64_n1747
    _f64_n1747 --> _f64_n1748
    _f64_n1748 --> _f64_n1749
    _f64_n1749 --> _f64_n1750
    _f64_n1750 --> _f64_n1751
    _f64_n1751 --> _f64_n1752
  end
  subgraph _get_used_import_list
    direction TB
    _f65_n1753 --> _f65_n1754
    _f65_n1754 --> _f65_n1755
    _f65_n1755 --> _f65_n1756
    _f65_n1756 --> _f65_n1757
    _f65_n1757 --> _f65_n1758
    _f65_n1758 --> _f65_n1759
    _f65_n1759 --> _f65_n1760
    _f65_n1760 --> _f65_n1761
    _f65_n1761 --> _f65_n1762
    _f65_n1762 --> _f65_n1763
    _f65_n1763 --> _f65_n1764
    _f65_n1764 --> _f65_n1765
    _f65_n1765 --> _f65_n1766
    _f65_n1766 --> _f65_n1767
    _f65_n1767 --> _f65_n1768
    _f65_n1768 --> _f65_n1769
    _f65_n1769 --> _f65_n1770
    _f65_n1770 --> _f65_n1771
    _f65_n1771 --> _f65_n1772
  end
  subgraph _create_mermaid_model_from_ast_model
    direction TB
    _f66_n1773 --> _f66_n1774
    _f66_n1774 --> _f66_n1775
    _f66_n1775 --> _f66_n1776
    _f66_n1776 --> _f66_n1777
    _f66_n1777 --> _f66_n1778
    _f66_n1778 --> _f66_n1779
    _f66_n1779 --> _f66_n1780
    _f66_n1780 --> _f66_n1781
    _f66_n1781 --> _f66_n1782
    _f66_n1782 --> _f66_n1783
    _f66_n1783 --> _f66_n1784
    _f66_n1784 --> _f66_n1785
    _f66_n1785 --> _f66_n1786
    _f66_n1786 --> _f66_n1787
    _f66_n1787 --> _f66_n1788
    _f66_n1788 --> _f66_n1789
    _f66_n1789 --> _f66_n1790
    _f66_n1790 --> _f66_n1791
    _f66_n1791 --> _f66_n1792
    _f66_n1792 --> _f66_n1793
  end

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
        alias(name='dump'),
        alias(name='parse')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=32),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Optional')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=27),
    ImportFrom(
      module='ast_tools.visitors',
      names=[
        alias(name='BlockGenerator'),
        alias(name='ImportNodeFinder')],
      level=0,
      lineno=4,
      col_offset=0,
      end_lineno=4,
      end_col_offset=63),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidElement')],
      level=0,
      lineno=5,
      col_offset=0,
      end_lineno=5,
      end_col_offset=33),
    FunctionDef(
      name='get_ast_root_node_for_file',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='source_code',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=8,
              col_offset=44,
              end_lineno=8,
              end_col_offset=47),
            lineno=8,
            col_offset=31,
            end_lineno=8,
            end_col_offset=47),
          arg(
            arg='input_file',
            annotation=Name(
              id='str',
              ctx=Load(),
              lineno=8,
              col_offset=61,
              end_lineno=8,
              end_col_offset=64),
            lineno=8,
            col_offset=49,
            end_lineno=8,
            end_col_offset=64)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Name(
              id='parse',
              ctx=Load(),
              lineno=9,
              col_offset=11,
              end_lineno=9,
              end_col_offset=16),
            args=[],
            keywords=[
              keyword(
                arg='source',
                value=Name(
                  id='source_code',
                  ctx=Load(),
                  lineno=10,
                  col_offset=15,
                  end_lineno=10,
                  end_col_offset=26),
                lineno=10,
                col_offset=8,
                end_lineno=10,
                end_col_offset=26),
              keyword(
                arg='filename',
                value=Name(
                  id='input_file',
                  ctx=Load(),
                  lineno=11,
                  col_offset=17,
                  end_lineno=11,
                  end_col_offset=27),
                lineno=11,
                col_offset=8,
                end_lineno=11,
                end_col_offset=27),
              keyword(
                arg='mode',
                value=Constant(
                  value='exec',
                  lineno=12,
                  col_offset=13,
                  end_lineno=12,
                  end_col_offset=19),
                lineno=12,
                col_offset=8,
                end_lineno=12,
                end_col_offset=19),
              keyword(
                arg='type_comments',
                value=Constant(
                  value=True,
                  lineno=13,
                  col_offset=22,
                  end_lineno=13,
                  end_col_offset=26),
                lineno=13,
                col_offset=8,
                end_lineno=13,
                end_col_offset=26)],
            lineno=9,
            col_offset=11,
            end_lineno=14,
            end_col_offset=5),
          lineno=9,
          col_offset=4,
          end_lineno=14,
          end_col_offset=5)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='Optional',
          ctx=Load(),
          lineno=8,
          col_offset=69,
          end_lineno=8,
          end_col_offset=77),
        slice=Name(
          id='AST',
          ctx=Load(),
          lineno=8,
          col_offset=78,
          end_lineno=8,
          end_col_offset=81),
        ctx=Load(),
        lineno=8,
        col_offset=69,
        end_lineno=8,
        end_col_offset=82),
      lineno=8,
      col_offset=0,
      end_lineno=14,
      end_col_offset=5),
    FunctionDef(
      name='get_markdown_dump_for_ast_node',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='ast_node',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=17,
              col_offset=45,
              end_lineno=17,
              end_col_offset=48),
            lineno=17,
            col_offset=35,
            end_lineno=17,
            end_col_offset=48)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Return(
          value=Call(
            func=Name(
              id='dump',
              ctx=Load(),
              lineno=18,
              col_offset=11,
              end_lineno=18,
              end_col_offset=15),
            args=[
              Name(
                id='ast_node',
                ctx=Load(),
                lineno=18,
                col_offset=16,
                end_lineno=18,
                end_col_offset=24)],
            keywords=[
              keyword(
                arg='annotate_fields',
                value=Constant(
                  value=True,
                  lineno=18,
                  col_offset=42,
                  end_lineno=18,
                  end_col_offset=46),
                lineno=18,
                col_offset=26,
                end_lineno=18,
                end_col_offset=46),
              keyword(
                arg='include_attributes',
                value=Constant(
                  value=True,
                  lineno=18,
                  col_offset=67,
                  end_lineno=18,
                  end_col_offset=71),
                lineno=18,
                col_offset=48,
                end_lineno=18,
                end_col_offset=71),
              keyword(
                arg='indent',
                value=Constant(
                  value=2,
                  lineno=18,
                  col_offset=80,
                  end_lineno=18,
                  end_col_offset=81),
                lineno=18,
                col_offset=73,
                end_lineno=18,
                end_col_offset=81)],
            lineno=18,
            col_offset=11,
            end_lineno=18,
            end_col_offset=82),
          lineno=18,
          col_offset=4,
          end_lineno=18,
          end_col_offset=82)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=17,
        col_offset=53,
        end_lineno=17,
        end_col_offset=56),
      lineno=17,
      col_offset=0,
      end_lineno=18,
      end_col_offset=82),
    FunctionDef(
      name='get_used_import_list',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='ast_node',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=21,
              col_offset=35,
              end_lineno=21,
              end_col_offset=38),
            lineno=21,
            col_offset=25,
            end_lineno=21,
            end_col_offset=38)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='finder',
              ctx=Store(),
              lineno=22,
              col_offset=4,
              end_lineno=22,
              end_col_offset=10)],
          value=Call(
            func=Name(
              id='ImportNodeFinder',
              ctx=Load(),
              lineno=22,
              col_offset=13,
              end_lineno=22,
              end_col_offset=29),
            args=[],
            keywords=[],
            lineno=22,
            col_offset=13,
            end_lineno=22,
            end_col_offset=31),
          lineno=22,
          col_offset=4,
          end_lineno=22,
          end_col_offset=31),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(
                id='finder',
                ctx=Load(),
                lineno=23,
                col_offset=4,
                end_lineno=23,
                end_col_offset=10),
              attr='visit',
              ctx=Load(),
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=16),
            args=[
              Name(
                id='ast_node',
                ctx=Load(),
                lineno=23,
                col_offset=17,
                end_lineno=23,
                end_col_offset=25)],
            keywords=[],
            lineno=23,
            col_offset=4,
            end_lineno=23,
            end_col_offset=26),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=26),
        Return(
          value=Call(
            func=Attribute(
              value=Name(
                id='finder',
                ctx=Load(),
                lineno=24,
                col_offset=11,
                end_lineno=24,
                end_col_offset=17),
              attr='get_found_imports',
              ctx=Load(),
              lineno=24,
              col_offset=11,
              end_lineno=24,
              end_col_offset=35),
            args=[],
            keywords=[],
            lineno=24,
            col_offset=11,
            end_lineno=24,
            end_col_offset=37),
          lineno=24,
          col_offset=4,
          end_lineno=24,
          end_col_offset=37)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=21,
          col_offset=43,
          end_lineno=21,
          end_col_offset=47),
        slice=Name(
          id='str',
          ctx=Load(),
          lineno=21,
          col_offset=48,
          end_lineno=21,
          end_col_offset=51),
        ctx=Load(),
        lineno=21,
        col_offset=43,
        end_lineno=21,
        end_col_offset=52),
      lineno=21,
      col_offset=0,
      end_lineno=24,
      end_col_offset=37),
    FunctionDef(
      name='create_mermaid_model_from_ast_model',
      args=arguments(
        posonlyargs=[],
        args=[
          arg(
            arg='model',
            annotation=Name(
              id='AST',
              ctx=Load(),
              lineno=27,
              col_offset=47,
              end_lineno=27,
              end_col_offset=50),
            lineno=27,
            col_offset=40,
            end_lineno=27,
            end_col_offset=50)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(
              id='generator',
              ctx=Store(),
              lineno=28,
              col_offset=4,
              end_lineno=28,
              end_col_offset=13)],
          value=Call(
            func=Name(
              id='BlockGenerator',
              ctx=Load(),
              lineno=28,
              col_offset=16,
              end_lineno=28,
              end_col_offset=30),
            args=[],
            keywords=[],
            lineno=28,
            col_offset=16,
            end_lineno=28,
            end_col_offset=32),
          lineno=28,
          col_offset=4,
          end_lineno=28,
          end_col_offset=32),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(
                id='generator',
                ctx=Load(),
                lineno=29,
                col_offset=4,
                end_lineno=29,
                end_col_offset=13),
              attr='visit',
              ctx=Load(),
              lineno=29,
              col_offset=4,
              end_lineno=29,
              end_col_offset=19),
            args=[],
            keywords=[
              keyword(
                arg='node',
                value=Name(
                  id='model',
                  ctx=Load(),
                  lineno=29,
                  col_offset=25,
                  end_lineno=29,
                  end_col_offset=30),
                lineno=29,
                col_offset=20,
                end_lineno=29,
                end_col_offset=30)],
            lineno=29,
            col_offset=4,
            end_lineno=29,
            end_col_offset=31),
          lineno=29,
          col_offset=4,
          end_lineno=29,
          end_col_offset=31),
        Return(
          value=Call(
            func=Attribute(
              value=Name(
                id='generator',
                ctx=Load(),
                lineno=30,
                col_offset=11,
                end_lineno=30,
                end_col_offset=20),
              attr='get_list_of_elements',
              ctx=Load(),
              lineno=30,
              col_offset=11,
              end_lineno=30,
              end_col_offset=41),
            args=[],
            keywords=[],
            lineno=30,
            col_offset=11,
            end_lineno=30,
            end_col_offset=43),
          lineno=30,
          col_offset=4,
          end_lineno=30,
          end_col_offset=43)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=27,
          col_offset=55,
          end_lineno=27,
          end_col_offset=59),
        slice=Name(
          id='MermaidElement',
          ctx=Load(),
          lineno=27,
          col_offset=60,
          end_lineno=27,
          end_col_offset=74),
        ctx=Load(),
        lineno=27,
        col_offset=55,
        end_lineno=27,
        end_col_offset=75),
      lineno=27,
      col_offset=0,
      end_lineno=30,
      end_col_offset=43)],
  type_ignores=[])
```
</details>

