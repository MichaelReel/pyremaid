# ./src/pyremaid/models.py

### Imports

  - ast.AST
  - dataclasses.dataclass
  - dataclasses.field
  - typing.Optional

---
```mermaid
flowchart TB
  _node_0["ClassDef"]
  _node_1["Pass"]
  _node_2["Call"]
  _node_3["Name"]
  _node_4["Load"]
  _node_5["keyword"]
  _node_6["Constant"]
  _node_7["ClassDef"]
  _node_8["Name"]
  _node_9["Load"]
  _node_10["AnnAssign"]
  _node_11["Name"]
  _node_12["Store"]
  _node_13["Name"]
  _node_14["Load"]
  _node_15["AnnAssign"]
  _node_16["Name"]
  _node_17["Store"]
  _node_18["Name"]
  _node_19["Load"]
  _node_20["AnnAssign"]
  _node_21["Name"]
  _node_22["Store"]
  _node_23["Name"]
  _node_24["Load"]
  _node_25["Call"]
  _node_26["Name"]
  _node_27["Load"]
  _node_28["keyword"]
  _node_29["Constant"]
  _node_30["keyword"]
  _node_31["Constant"]
  _node_32["ClassDef"]
  _node_33["Name"]
  _node_34["Load"]
  _node_35["AnnAssign"]
  _node_36["Name"]
  _node_37["Store"]
  _node_38["Name"]
  _node_39["Load"]
  _node_40["AnnAssign"]
  _node_41["Name"]
  _node_42["Store"]
  _node_43["Name"]
  _node_44["Load"]
  _node_45["Call"]
  _node_46["Name"]
  _node_47["Load"]
  _node_48["keyword"]
  _node_49["Constant"]
  _node_50["ClassDef"]
  _node_51["Name"]
  _node_52["Load"]
  _node_53["AnnAssign"]
  _node_54["Name"]
  _node_55["Store"]
  _node_56["Subscript"]
  _node_57["Name"]
  _node_58["Load"]
  _node_59["Name"]
  _node_60["Load"]
  _node_61["Load"]
  _node_62["Call"]
  _node_63["Name"]
  _node_64["Load"]
  _node_65["keyword"]
  _node_66["Name"]
  _node_67["Load"]
  _node_68["Call"]
  _node_69["Name"]
  _node_70["Load"]
  _node_71["keyword"]
  _node_72["Constant"]
  _node_73["keyword"]
  _node_74["Constant"]
  _node_75["ClassDef"]
  _node_76["Name"]
  _node_77["Load"]
  _node_78["Pass"]
  _node_79["Call"]
  _node_80["Name"]
  _node_81["Load"]
  _node_82["keyword"]
  _node_83["Constant"]
  _node_84["keyword"]
  _node_85["Constant"]
  _node_86["ClassDef"]
  _node_87["Name"]
  _node_88["Load"]
  _node_89["Pass"]
  _node_90["Call"]
  _node_91["Name"]
  _node_92["Load"]
  _node_93["keyword"]
  _node_94["Constant"]
  _node_95["keyword"]
  _node_96["Constant"]

  _node_0 --> _node_1
  _node_1 --> _node_2
  _node_2 --> _node_3
  _node_3 --> _node_4
  _node_4 --> _node_5
  _node_5 --> _node_6
  _node_6 --> _node_7
  _node_7 --> _node_8
  _node_8 --> _node_9
  _node_9 --> _node_10
  _node_10 --> _node_11
  _node_11 --> _node_12
  _node_12 --> _node_13
  _node_13 --> _node_14
  _node_14 --> _node_15
  _node_15 --> _node_16
  _node_16 --> _node_17
  _node_17 --> _node_18
  _node_18 --> _node_19
  _node_19 --> _node_20
  _node_20 --> _node_21
  _node_21 --> _node_22
  _node_22 --> _node_23
  _node_23 --> _node_24
  _node_24 --> _node_25
  _node_25 --> _node_26
  _node_26 --> _node_27
  _node_27 --> _node_28
  _node_28 --> _node_29
  _node_29 --> _node_30
  _node_30 --> _node_31
  _node_31 --> _node_32
  _node_32 --> _node_33
  _node_33 --> _node_34
  _node_34 --> _node_35
  _node_35 --> _node_36
  _node_36 --> _node_37
  _node_37 --> _node_38
  _node_38 --> _node_39
  _node_39 --> _node_40
  _node_40 --> _node_41
  _node_41 --> _node_42
  _node_42 --> _node_43
  _node_43 --> _node_44
  _node_44 --> _node_45
  _node_45 --> _node_46
  _node_46 --> _node_47
  _node_47 --> _node_48
  _node_48 --> _node_49
  _node_49 --> _node_50
  _node_50 --> _node_51
  _node_51 --> _node_52
  _node_52 --> _node_53
  _node_53 --> _node_54
  _node_54 --> _node_55
  _node_55 --> _node_56
  _node_56 --> _node_57
  _node_57 --> _node_58
  _node_58 --> _node_59
  _node_59 --> _node_60
  _node_60 --> _node_61
  _node_61 --> _node_62
  _node_62 --> _node_63
  _node_63 --> _node_64
  _node_64 --> _node_65
  _node_65 --> _node_66
  _node_66 --> _node_67
  _node_67 --> _node_68
  _node_68 --> _node_69
  _node_69 --> _node_70
  _node_70 --> _node_71
  _node_71 --> _node_72
  _node_72 --> _node_73
  _node_73 --> _node_74
  _node_74 --> _node_75
  _node_75 --> _node_76
  _node_76 --> _node_77
  _node_77 --> _node_78
  _node_78 --> _node_79
  _node_79 --> _node_80
  _node_80 --> _node_81
  _node_81 --> _node_82
  _node_82 --> _node_83
  _node_83 --> _node_84
  _node_84 --> _node_85
  _node_85 --> _node_86
  _node_86 --> _node_87
  _node_87 --> _node_88
  _node_88 --> _node_89
  _node_89 --> _node_90
  _node_90 --> _node_91
  _node_91 --> _node_92
  _node_92 --> _node_93
  _node_93 --> _node_94
  _node_94 --> _node_95
  _node_95 --> _node_96

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
        alias(name='AST')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=19),
    ImportFrom(
      module='dataclasses',
      names=[
        alias(name='dataclass'),
        alias(name='field')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=2,
      end_col_offset=40),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Optional')],
      level=0,
      lineno=3,
      col_offset=0,
      end_lineno=3,
      end_col_offset=27),
    ClassDef(
      name='MermaidElement',
      bases=[],
      keywords=[],
      body=[
        Pass(
          lineno=8,
          col_offset=4,
          end_lineno=8,
          end_col_offset=8)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=6,
            col_offset=1,
            end_lineno=6,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=6,
                col_offset=18,
                end_lineno=6,
                end_col_offset=22),
              lineno=6,
              col_offset=11,
              end_lineno=6,
              end_col_offset=22)],
          lineno=6,
          col_offset=1,
          end_lineno=6,
          end_col_offset=23)],
      lineno=7,
      col_offset=0,
      end_lineno=8,
      end_col_offset=8),
    ClassDef(
      name='MermaidNode',
      bases=[
        Name(
          id='MermaidElement',
          ctx=Load(),
          lineno=12,
          col_offset=18,
          end_lineno=12,
          end_col_offset=32)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='ast_node',
            ctx=Store(),
            lineno=13,
            col_offset=4,
            end_lineno=13,
            end_col_offset=12),
          annotation=Name(
            id='AST',
            ctx=Load(),
            lineno=13,
            col_offset=14,
            end_lineno=13,
            end_col_offset=17),
          simple=1,
          lineno=13,
          col_offset=4,
          end_lineno=13,
          end_col_offset=17),
        AnnAssign(
          target=Name(
            id='mermaid_safe_name',
            ctx=Store(),
            lineno=14,
            col_offset=4,
            end_lineno=14,
            end_col_offset=21),
          annotation=Name(
            id='str',
            ctx=Load(),
            lineno=14,
            col_offset=23,
            end_lineno=14,
            end_col_offset=26),
          simple=1,
          lineno=14,
          col_offset=4,
          end_lineno=14,
          end_col_offset=26),
        AnnAssign(
          target=Name(
            id='display_name',
            ctx=Store(),
            lineno=15,
            col_offset=4,
            end_lineno=15,
            end_col_offset=16),
          annotation=Name(
            id='str',
            ctx=Load(),
            lineno=15,
            col_offset=18,
            end_lineno=15,
            end_col_offset=21),
          simple=1,
          lineno=15,
          col_offset=4,
          end_lineno=15,
          end_col_offset=21)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=11,
            col_offset=1,
            end_lineno=11,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='unsafe_hash',
              value=Constant(
                value=True,
                lineno=11,
                col_offset=23,
                end_lineno=11,
                end_col_offset=27),
              lineno=11,
              col_offset=11,
              end_lineno=11,
              end_col_offset=27),
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=11,
                col_offset=36,
                end_lineno=11,
                end_col_offset=40),
              lineno=11,
              col_offset=29,
              end_lineno=11,
              end_col_offset=40)],
          lineno=11,
          col_offset=1,
          end_lineno=11,
          end_col_offset=41)],
      lineno=12,
      col_offset=0,
      end_lineno=15,
      end_col_offset=21),
    ClassDef(
      name='MermaidLink',
      bases=[
        Name(
          id='MermaidElement',
          ctx=Load(),
          lineno=19,
          col_offset=18,
          end_lineno=19,
          end_col_offset=32)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='from_',
            ctx=Store(),
            lineno=20,
            col_offset=4,
            end_lineno=20,
            end_col_offset=9),
          annotation=Name(
            id='MermaidNode',
            ctx=Load(),
            lineno=20,
            col_offset=11,
            end_lineno=20,
            end_col_offset=22),
          simple=1,
          lineno=20,
          col_offset=4,
          end_lineno=20,
          end_col_offset=22),
        AnnAssign(
          target=Name(
            id='to',
            ctx=Store(),
            lineno=21,
            col_offset=4,
            end_lineno=21,
            end_col_offset=6),
          annotation=Name(
            id='MermaidNode',
            ctx=Load(),
            lineno=21,
            col_offset=8,
            end_lineno=21,
            end_col_offset=19),
          simple=1,
          lineno=21,
          col_offset=4,
          end_lineno=21,
          end_col_offset=19)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=18,
            col_offset=1,
            end_lineno=18,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=18,
                col_offset=18,
                end_lineno=18,
                end_col_offset=22),
              lineno=18,
              col_offset=11,
              end_lineno=18,
              end_col_offset=22)],
          lineno=18,
          col_offset=1,
          end_lineno=18,
          end_col_offset=23)],
      lineno=19,
      col_offset=0,
      end_lineno=21,
      end_col_offset=19),
    ClassDef(
      name='MermaidBlock',
      bases=[
        Name(
          id='MermaidNode',
          ctx=Load(),
          lineno=25,
          col_offset=19,
          end_lineno=25,
          end_col_offset=30)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='block_contents',
            ctx=Store(),
            lineno=26,
            col_offset=4,
            end_lineno=26,
            end_col_offset=18),
          annotation=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=26,
              col_offset=20,
              end_lineno=26,
              end_col_offset=24),
            slice=Name(
              id='MermaidLink',
              ctx=Load(),
              lineno=26,
              col_offset=25,
              end_lineno=26,
              end_col_offset=36),
            ctx=Load(),
            lineno=26,
            col_offset=20,
            end_lineno=26,
            end_col_offset=37),
          value=Call(
            func=Name(
              id='field',
              ctx=Load(),
              lineno=26,
              col_offset=40,
              end_lineno=26,
              end_col_offset=45),
            args=[],
            keywords=[
              keyword(
                arg='default_factory',
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=26,
                  col_offset=62,
                  end_lineno=26,
                  end_col_offset=66),
                lineno=26,
                col_offset=46,
                end_lineno=26,
                end_col_offset=66)],
            lineno=26,
            col_offset=40,
            end_lineno=26,
            end_col_offset=67),
          simple=1,
          lineno=26,
          col_offset=4,
          end_lineno=26,
          end_col_offset=67)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=24,
            col_offset=1,
            end_lineno=24,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='unsafe_hash',
              value=Constant(
                value=True,
                lineno=24,
                col_offset=23,
                end_lineno=24,
                end_col_offset=27),
              lineno=24,
              col_offset=11,
              end_lineno=24,
              end_col_offset=27),
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=24,
                col_offset=36,
                end_lineno=24,
                end_col_offset=40),
              lineno=24,
              col_offset=29,
              end_lineno=24,
              end_col_offset=40)],
          lineno=24,
          col_offset=1,
          end_lineno=24,
          end_col_offset=41)],
      lineno=25,
      col_offset=0,
      end_lineno=26,
      end_col_offset=67),
    ClassDef(
      name='MermaidModule',
      bases=[
        Name(
          id='MermaidBlock',
          ctx=Load(),
          lineno=30,
          col_offset=20,
          end_lineno=30,
          end_col_offset=32)],
      keywords=[],
      body=[
        Pass(
          lineno=31,
          col_offset=4,
          end_lineno=31,
          end_col_offset=8)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=29,
            col_offset=1,
            end_lineno=29,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='unsafe_hash',
              value=Constant(
                value=True,
                lineno=29,
                col_offset=23,
                end_lineno=29,
                end_col_offset=27),
              lineno=29,
              col_offset=11,
              end_lineno=29,
              end_col_offset=27),
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=29,
                col_offset=36,
                end_lineno=29,
                end_col_offset=40),
              lineno=29,
              col_offset=29,
              end_lineno=29,
              end_col_offset=40)],
          lineno=29,
          col_offset=1,
          end_lineno=29,
          end_col_offset=41)],
      lineno=30,
      col_offset=0,
      end_lineno=31,
      end_col_offset=8),
    ClassDef(
      name='MermaidFunction',
      bases=[
        Name(
          id='MermaidBlock',
          ctx=Load(),
          lineno=35,
          col_offset=22,
          end_lineno=35,
          end_col_offset=34)],
      keywords=[],
      body=[
        Pass(
          lineno=36,
          col_offset=4,
          end_lineno=36,
          end_col_offset=8)],
      decorator_list=[
        Call(
          func=Name(
            id='dataclass',
            ctx=Load(),
            lineno=34,
            col_offset=1,
            end_lineno=34,
            end_col_offset=10),
          args=[],
          keywords=[
            keyword(
              arg='unsafe_hash',
              value=Constant(
                value=True,
                lineno=34,
                col_offset=23,
                end_lineno=34,
                end_col_offset=27),
              lineno=34,
              col_offset=11,
              end_lineno=34,
              end_col_offset=27),
            keyword(
              arg='frozen',
              value=Constant(
                value=True,
                lineno=34,
                col_offset=36,
                end_lineno=34,
                end_col_offset=40),
              lineno=34,
              col_offset=29,
              end_lineno=34,
              end_col_offset=40)],
          lineno=34,
          col_offset=1,
          end_lineno=34,
          end_col_offset=41)],
      lineno=35,
      col_offset=0,
      end_lineno=36,
      end_col_offset=8)],
  type_ignores=[])
```
</details>

