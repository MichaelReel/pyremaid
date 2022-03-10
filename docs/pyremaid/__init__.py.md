# ./src/pyremaid/__init__.py

### Imports


---
```mermaid
flowchart TB
    node_73["ast.arg object at 0x10176af70"]
    node_21["ast.Name object at 0x10176fb50"]
    node_87["ast.Name object at 0x10176adc0"]
    node_82["ast.Store object at 0x101673070"]
    node_101["ast.Load object at 0x1016730d0"]
    node_74["ast.Subscript object at 0x10176af40"]
    node_104["ast.FunctionDef object at 0x10176ab50"]
    node_65["ast.FormattedValue object at 0x10176f1c0"]
    node_43["ast.Store object at 0x101673070"]
    node_107["ast.Name object at 0x10176aac0"]
    node_22["ast.Load object at 0x1016730d0"]
    node_44["ast.Call object at 0x10176f5e0"]
    node_112["ast.FormattedValue object at 0x10176aa00"]
    node_96["ast.Name object at 0x10176aca0"]
    node_0["ast.Module object at 0x10176ffa0"]
    node_37["ast.Load object at 0x1016730d0"]
    node_30["ast.Name object at 0x10176f9a0"]
    node_66["ast.Name object at 0x10176f1f0"]
    node_6["ast.arg object at 0x10176fe50"]
    node_31["ast.Load object at 0x1016730d0"]
    node_69["ast.Name object at 0x10176f190"]
    node_102["ast.Name object at 0x10176ab80"]
    node_103["ast.Load object at 0x1016730d0"]
    node_67["ast.Load object at 0x1016730d0"]
    node_24["ast.Name object at 0x10176f910"]
    node_41["ast.Assign object at 0x10176f6d0"]
    node_62["ast.Name object at 0x10176f280"]
    node_111["ast.Constant object at 0x10176aa30"]
    node_113["ast.Name object at 0x10176a9d0"]
    node_75["ast.Name object at 0x10176af10"]
    node_36["ast.Name object at 0x10176fa30"]
    node_54["ast.Name object at 0x10176f8e0"]
    node_28["ast.Load object at 0x1016730d0"]
    node_53["ast.FormattedValue object at 0x10176fc40"]
    node_110["ast.JoinedStr object at 0x10176aa60"]
    node_32["ast.Assign object at 0x10176f940"]
    node_47["ast.Load object at 0x1016730d0"]
    node_10["ast.Name object at 0x10176fd00"]
    node_8["ast.Name object at 0x10176fdf0"]
    node_95["ast.FormattedValue object at 0x10176acd0"]
    node_42["ast.Name object at 0x10176f730"]
    node_17["ast.Name object at 0x10176fbe0"]
    node_9["ast.Load object at 0x1016730d0"]
    node_90["ast.Name object at 0x10176ad60"]
    node_98["ast.Constant object at 0x10176ac70"]
    node_59["ast.Load object at 0x1016730d0"]
    node_18["ast.Load object at 0x1016730d0"]
    node_85["ast.Name object at 0x10176adf0"]
    node_5["ast.Load object at 0x1016730d0"]
    node_50["ast.Return object at 0x10176faf0"]
    node_72["ast.arguments object at 0x10176afa0"]
    node_93["ast.JoinedStr object at 0x10176ad30"]
    node_46["ast.Constant object at 0x10176f5b0"]
    node_14["ast.Subscript object at 0x10176fc70"]
    node_55["ast.Load object at 0x1016730d0"]
    node_23["ast.Assign object at 0x10176fb80"]
    node_70["ast.Load object at 0x1016730d0"]
    node_114["ast.Load object at 0x1016730d0"]
    node_115["ast.Constant object at 0x10176a9a0"]
    node_105["ast.arguments object at 0x10176ab20"]
    node_83["ast.Constant object at 0x10176ae50"]
    node_45["ast.Attribute object at 0x10176f610"]
    node_58["ast.Name object at 0x10176feb0"]
    node_71["ast.FunctionDef object at 0x10176afd0"]
    node_63["ast.Load object at 0x1016730d0"]
    node_26["ast.Call object at 0x10176fa60"]
    node_11["ast.Load object at 0x1016730d0"]
    node_38["ast.keyword object at 0x10176f970"]
    node_92["ast.Add object at 0x101673760"]
    node_64["ast.Constant object at 0x10176f2b0"]
    node_51["ast.JoinedStr object at 0x10176fca0"]
    node_117["ast.Load object at 0x1016730d0"]
    node_80["ast.Assign object at 0x10176aeb0"]
    node_19["ast.Load object at 0x1016730d0"]
    node_106["ast.arg object at 0x10176aaf0"]
    node_100["ast.Name object at 0x10176abe0"]
    node_99["ast.Return object at 0x10176ac10"]
    node_56["ast.Constant object at 0x10176fd90"]
    node_49["ast.Load object at 0x1016730d0"]
    node_13["ast.arg object at 0x10176fb20"]
    node_88["ast.Load object at 0x1016730d0"]
    node_15["ast.Name object at 0x10176fc10"]
    node_3["ast.arg object at 0x10176fee0"]
    node_4["ast.Name object at 0x10176fe80"]
    node_116["ast.Name object at 0x10176a910"]
    node_20["ast.arg object at 0x10176fbb0"]
    node_12["ast.Load object at 0x1016730d0"]
    node_57["ast.FormattedValue object at 0x10176fdc0"]
    node_97["ast.Load object at 0x1016730d0"]
    node_84["ast.For object at 0x10176ae20"]
    node_48["ast.Name object at 0x10176f640"]
    node_16["ast.Load object at 0x1016730d0"]
    node_94["ast.Constant object at 0x10176ad00"]
    node_109["ast.Return object at 0x10176aa90"]
    node_52["ast.Constant object at 0x10176fcd0"]
    node_34["ast.Store object at 0x101673070"]
    node_60["ast.Constant object at 0x10176ff40"]
    node_76["ast.Load object at 0x1016730d0"]
    node_86["ast.Store object at 0x101673070"]
    node_40["ast.Load object at 0x1016730d0"]
    node_89["ast.AugAssign object at 0x10176ad90"]
    node_7["ast.Subscript object at 0x10176fe20"]
    node_79["ast.Load object at 0x1016730d0"]
    node_91["ast.Store object at 0x101673070"]
    node_108["ast.Load object at 0x1016730d0"]
    node_1["ast.FunctionDef object at 0x10176ffd0"]
    node_77["ast.Name object at 0x10176aee0"]
    node_39["ast.Name object at 0x10176f160"]
    node_68["ast.Constant object at 0x10176f220"]
    node_29["ast.keyword object at 0x10176f9d0"]
    node_78["ast.Load object at 0x1016730d0"]
    node_2["ast.arguments object at 0x10176ff10"]
    node_81["ast.Name object at 0x10176ae80"]
    node_35["ast.Call object at 0x10176fa90"]
    node_25["ast.Store object at 0x101673070"]
    node_33["ast.Name object at 0x10176fd60"]
    node_27["ast.Name object at 0x10176fa00"]
    node_61["ast.FormattedValue object at 0x10176ff70"]

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

