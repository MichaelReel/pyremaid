# ./src/pyremaid/__init__.py

### Imports


---
```mermaid
flowchart TB
    node_0["ast.Module object at 0x106152fd0"]
    node_1["ast.FunctionDef object at 0x106152fa0"]
    node_2["ast.arguments object at 0x106152f70"]
    node_3["ast.arg object at 0x106152f40"]
    node_4["ast.Name object at 0x106152f10"]
    node_5["ast.Load object at 0x1060500d0"]
    node_6["ast.arg object at 0x106152ee0"]
    node_7["ast.Subscript object at 0x106152eb0"]
    node_8["ast.Name object at 0x106152e80"]
    node_9["ast.Load object at 0x1060500d0"]
    node_10["ast.Name object at 0x106152e50"]
    node_11["ast.Load object at 0x1060500d0"]
    node_12["ast.Load object at 0x1060500d0"]
    node_13["ast.arg object at 0x106152e20"]
    node_14["ast.Subscript object at 0x106152d30"]
    node_15["ast.Name object at 0x106152d60"]
    node_16["ast.Load object at 0x1060500d0"]
    node_17["ast.Name object at 0x106152dc0"]
    node_18["ast.Load object at 0x1060500d0"]
    node_19["ast.Load object at 0x1060500d0"]
    node_20["ast.arg object at 0x106152df0"]
    node_21["ast.Name object at 0x106152700"]
    node_22["ast.Load object at 0x1060500d0"]
    node_23["ast.Assign object at 0x1061526d0"]
    node_24["ast.Name object at 0x1061526a0"]
    node_25["ast.Store object at 0x106050070"]
    node_26["ast.Call object at 0x106152670"]
    node_27["ast.Name object at 0x106152640"]
    node_28["ast.Load object at 0x1060500d0"]
    node_29["ast.keyword object at 0x106152610"]
    node_30["ast.Name object at 0x1061525e0"]
    node_31["ast.Load object at 0x1060500d0"]
    node_32["ast.Assign object at 0x1061525b0"]
    node_33["ast.Name object at 0x106152580"]
    node_34["ast.Store object at 0x106050070"]
    node_35["ast.Call object at 0x106152550"]
    node_36["ast.Name object at 0x106152520"]
    node_37["ast.Load object at 0x1060500d0"]
    node_38["ast.keyword object at 0x1061524f0"]
    node_39["ast.Name object at 0x1061524c0"]
    node_40["ast.Load object at 0x1060500d0"]
    node_41["ast.Assign object at 0x106152490"]
    node_42["ast.Name object at 0x106152460"]
    node_43["ast.Store object at 0x106050070"]
    node_44["ast.Call object at 0x106152430"]
    node_45["ast.Attribute object at 0x106152400"]
    node_46["ast.Constant object at 0x1061523d0"]
    node_47["ast.Load object at 0x1060500d0"]
    node_48["ast.Name object at 0x1061523a0"]
    node_49["ast.Load object at 0x1060500d0"]
    node_50["ast.Return object at 0x106152370"]
    node_51["ast.JoinedStr object at 0x106152340"]
    node_52["ast.Constant object at 0x106152310"]
    node_53["ast.FormattedValue object at 0x1061522e0"]
    node_54["ast.Name object at 0x1061522b0"]
    node_55["ast.Load object at 0x1060500d0"]
    node_56["ast.Constant object at 0x106152280"]
    node_57["ast.FormattedValue object at 0x106152250"]
    node_58["ast.Name object at 0x106152220"]
    node_59["ast.Load object at 0x1060500d0"]
    node_60["ast.Constant object at 0x1061521f0"]
    node_61["ast.FormattedValue object at 0x1061521c0"]
    node_62["ast.Name object at 0x106152190"]
    node_63["ast.Load object at 0x1060500d0"]
    node_64["ast.Constant object at 0x106152160"]
    node_65["ast.FormattedValue object at 0x106152130"]
    node_66["ast.Name object at 0x106152100"]
    node_67["ast.Load object at 0x1060500d0"]
    node_68["ast.Constant object at 0x1061520d0"]
    node_69["ast.Name object at 0x106152040"]
    node_70["ast.Load object at 0x1060500d0"]
    node_71["ast.FunctionDef object at 0x10614cfd0"]
    node_72["ast.arguments object at 0x10614cfa0"]
    node_73["ast.arg object at 0x10614cf70"]
    node_74["ast.Subscript object at 0x10614cf40"]
    node_75["ast.Name object at 0x10614cf10"]
    node_76["ast.Load object at 0x1060500d0"]
    node_77["ast.Name object at 0x10614cee0"]
    node_78["ast.Load object at 0x1060500d0"]
    node_79["ast.Load object at 0x1060500d0"]
    node_80["ast.Assign object at 0x10614ceb0"]
    node_81["ast.Name object at 0x10614ce80"]
    node_82["ast.Store object at 0x106050070"]
    node_83["ast.Constant object at 0x10614ce50"]
    node_84["ast.For object at 0x10614ce20"]
    node_85["ast.Name object at 0x10614cdf0"]
    node_86["ast.Store object at 0x106050070"]
    node_87["ast.Name object at 0x10614cdc0"]
    node_88["ast.Load object at 0x1060500d0"]
    node_89["ast.AugAssign object at 0x10614cd90"]
    node_90["ast.Name object at 0x10614cd60"]
    node_91["ast.Store object at 0x106050070"]
    node_92["ast.Add object at 0x106050760"]
    node_93["ast.JoinedStr object at 0x10614cd30"]
    node_94["ast.Constant object at 0x10614cd00"]
    node_95["ast.FormattedValue object at 0x10614ccd0"]
    node_96["ast.Name object at 0x10614cca0"]
    node_97["ast.Load object at 0x1060500d0"]
    node_98["ast.Constant object at 0x10614cc70"]
    node_99["ast.Return object at 0x10614cc10"]
    node_100["ast.Name object at 0x10614cbe0"]
    node_101["ast.Load object at 0x1060500d0"]
    node_102["ast.Name object at 0x10614cb80"]
    node_103["ast.Load object at 0x1060500d0"]
    node_104["ast.FunctionDef object at 0x10614cb50"]
    node_105["ast.arguments object at 0x10614cb20"]
    node_106["ast.arg object at 0x10614caf0"]
    node_107["ast.Name object at 0x10614c8e0"]
    node_108["ast.Load object at 0x1060500d0"]
    node_109["ast.Return object at 0x10614c8b0"]
    node_110["ast.JoinedStr object at 0x10614c880"]
    node_111["ast.Constant object at 0x10614c850"]
    node_112["ast.FormattedValue object at 0x10614c820"]
    node_113["ast.Name object at 0x10614c7f0"]
    node_114["ast.Load object at 0x1060500d0"]
    node_115["ast.Constant object at 0x10614c7c0"]
    node_116["ast.Name object at 0x10614c730"]
    node_117["ast.Load object at 0x1060500d0"]

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

```
---

<details>
<summary>Debug AST model dump</summary>

```

```
</details>

