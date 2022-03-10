# ./src/pyremaid/mermaid_tools/mermaid_tools.py

### Imports

  - [models.MermaidBlock](/docs/pyremaid/models.py.md)
  - [models.MermaidClass](/docs/pyremaid/models.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)
  - [models.MermaidFunction](/docs/pyremaid/models.py.md)
  - [models.MermaidLink](/docs/pyremaid/models.py.md)
  - [models.MermaidNode](/docs/pyremaid/models.py.md)

---
```mermaid
flowchart TB
  _n424["Assign"]
  _n425["Name"]
  _n426["Store"]
  _n427["Constant"]
  _f16_n428["Return"]
  _f16_n429["Call"]
  _f16_n430["Attribute"]
  _f16_n431["Call"]
  _f16_n432["Attribute"]
  _f16_n433["Name"]
  _f16_n434["Load"]
  _f16_n435["Load"]
  _f16_n436["Constant"]
  _f16_n437["Constant"]
  _f16_n438["Load"]
  _f16_n439["Constant"]
  _f16_n440["Constant"]
  _f17_n441["Assign"]
  _f17_n442["Name"]
  _f17_n443["Store"]
  _f17_n444["List"]
  _f17_n445["Load"]
  _f17_n446["For"]
  _f17_n447["Name"]
  _f17_n448["Store"]
  _f17_n449["Name"]
  _f17_n450["Load"]
  _f17_n451["If"]
  _f17_n452["Call"]
  _f17_n453["Name"]
  _f17_n454["Load"]
  _f17_n455["Name"]
  _f17_n456["Load"]
  _f17_n457["Name"]
  _f17_n458["Load"]
  _f17_n459["AnnAssign"]
  _f17_n460["Name"]
  _f17_n461["Store"]
  _f17_n462["Name"]
  _f17_n463["Load"]
  _f17_n464["Name"]
  _f17_n465["Load"]
  _f17_n466["If"]
  _f17_n467["Compare"]
  _f17_n468["Attribute"]
  _f17_n469["Name"]
  _f17_n470["Load"]
  _f17_n471["Load"]
  _f17_n472["NotIn"]
  _f17_n473["Name"]
  _f17_n474["Load"]
  _f17_n475["Expr"]
  _f17_n476["Call"]
  _f17_n477["Attribute"]
  _f17_n478["Name"]
  _f17_n479["Load"]
  _f17_n480["Load"]
  _f17_n481["Attribute"]
  _f17_n482["Name"]
  _f17_n483["Load"]
  _f17_n484["Load"]
  _f17_n485["If"]
  _f17_n486["Compare"]
  _f17_n487["Attribute"]
  _f17_n488["Name"]
  _f17_n489["Load"]
  _f17_n490["Load"]
  _f17_n491["NotIn"]
  _f17_n492["Name"]
  _f17_n493["Load"]
  _f17_n494["Expr"]
  _f17_n495["Call"]
  _f17_n496["Attribute"]
  _f17_n497["Name"]
  _f17_n498["Load"]
  _f17_n499["Load"]
  _f17_n500["Attribute"]
  _f17_n501["Name"]
  _f17_n502["Load"]
  _f17_n503["Load"]
  _f17_n504["If"]
  _f17_n505["Call"]
  _f17_n506["Name"]
  _f17_n507["Load"]
  _f17_n508["Name"]
  _f17_n509["Load"]
  _f17_n510["Name"]
  _f17_n511["Load"]
  _f17_n512["AnnAssign"]
  _f17_n513["Name"]
  _f17_n514["Store"]
  _f17_n515["Name"]
  _f17_n516["Load"]
  _f17_n517["Name"]
  _f17_n518["Load"]
  _f17_n519["Expr"]
  _f17_n520["Call"]
  _f17_n521["Attribute"]
  _f17_n522["Name"]
  _f17_n523["Load"]
  _f17_n524["Load"]
  _f17_n525["Call"]
  _f17_n526["Name"]
  _f17_n527["Load"]
  _f17_n528["Attribute"]
  _f17_n529["Name"]
  _f17_n530["Load"]
  _f17_n531["Load"]
  _f17_n532["Return"]
  _f17_n533["Name"]
  _f17_n534["Load"]
  _f18_n535["Assign"]
  _f18_n536["Name"]
  _f18_n537["Store"]
  _f18_n538["Constant"]
  _f18_n539["For"]
  _f18_n540["Name"]
  _f18_n541["Store"]
  _f18_n542["Call"]
  _f18_n543["Name"]
  _f18_n544["Load"]
  _f18_n545["keyword"]
  _f18_n546["Name"]
  _f18_n547["Load"]
  _f18_n548["AugAssign"]
  _f18_n549["Name"]
  _f18_n550["Store"]
  _f18_n551["Add"]
  _f18_n552["JoinedStr"]
  _f18_n553["FormattedValue"]
  _f18_n554["BinOp"]
  _f18_n555["Name"]
  _f18_n556["Load"]
  _f18_n557["Mult"]
  _f18_n558["Name"]
  _f18_n559["Load"]
  _f18_n560["FormattedValue"]
  _f18_n561["Attribute"]
  _f18_n562["Name"]
  _f18_n563["Load"]
  _f18_n564["Load"]
  _f18_n565["Constant"]
  _f18_n566["FormattedValue"]
  _f18_n567["Attribute"]
  _f18_n568["Name"]
  _f18_n569["Load"]
  _f18_n570["Load"]
  _f18_n571["Constant"]
  _f18_n572["Return"]
  _f18_n573["Call"]
  _f18_n574["Name"]
  _f18_n575["Load"]
  _f18_n576["Name"]
  _f18_n577["Load"]
  _f19_n578["Assign"]
  _f19_n579["Name"]
  _f19_n580["Store"]
  _f19_n581["Attribute"]
  _f19_n582["Attribute"]
  _f19_n583["Name"]
  _f19_n584["Load"]
  _f19_n585["Load"]
  _f19_n586["Load"]
  _f19_n587["Assign"]
  _f19_n588["Name"]
  _f19_n589["Store"]
  _f19_n590["Attribute"]
  _f19_n591["Attribute"]
  _f19_n592["Name"]
  _f19_n593["Load"]
  _f19_n594["Load"]
  _f19_n595["Load"]
  _f19_n596["Return"]
  _f19_n597["JoinedStr"]
  _f19_n598["FormattedValue"]
  _f19_n599["BinOp"]
  _f19_n600["Name"]
  _f19_n601["Load"]
  _f19_n602["Mult"]
  _f19_n603["Name"]
  _f19_n604["Load"]
  _f19_n605["FormattedValue"]
  _f19_n606["Name"]
  _f19_n607["Load"]
  _f19_n608["Constant"]
  _f19_n609["FormattedValue"]
  _f19_n610["Name"]
  _f19_n611["Load"]
  _f19_n612["Constant"]
  _f20_n613["Assign"]
  _f20_n614["Name"]
  _f20_n615["Store"]
  _f20_n616["Constant"]
  _f20_n617["For"]
  _f20_n618["Name"]
  _f20_n619["Store"]
  _f20_n620["Name"]
  _f20_n621["Load"]
  _f20_n622["If"]
  _f20_n623["Call"]
  _f20_n624["Name"]
  _f20_n625["Load"]
  _f20_n626["Name"]
  _f20_n627["Load"]
  _f20_n628["Name"]
  _f20_n629["Load"]
  _f20_n630["AnnAssign"]
  _f20_n631["Name"]
  _f20_n632["Store"]
  _f20_n633["Name"]
  _f20_n634["Load"]
  _f20_n635["Name"]
  _f20_n636["Load"]
  _f20_n637["AugAssign"]
  _f20_n638["Name"]
  _f20_n639["Store"]
  _f20_n640["Add"]
  _f20_n641["Call"]
  _f20_n642["Name"]
  _f20_n643["Load"]
  _f20_n644["keyword"]
  _f20_n645["Name"]
  _f20_n646["Load"]
  _f20_n647["keyword"]
  _f20_n648["Name"]
  _f20_n649["Load"]
  _f20_n650["If"]
  _f20_n651["Call"]
  _f20_n652["Name"]
  _f20_n653["Load"]
  _f20_n654["Name"]
  _f20_n655["Load"]
  _f20_n656["Name"]
  _f20_n657["Load"]
  _f20_n658["AnnAssign"]
  _f20_n659["Name"]
  _f20_n660["Store"]
  _f20_n661["Name"]
  _f20_n662["Load"]
  _f20_n663["Name"]
  _f20_n664["Load"]
  _f20_n665["AugAssign"]
  _f20_n666["Name"]
  _f20_n667["Store"]
  _f20_n668["Add"]
  _f20_n669["Call"]
  _f20_n670["Name"]
  _f20_n671["Load"]
  _f20_n672["keyword"]
  _f20_n673["Name"]
  _f20_n674["Load"]
  _f20_n675["keyword"]
  _f20_n676["Name"]
  _f20_n677["Load"]
  _f20_n678["Return"]
  _f20_n679["Name"]
  _f20_n680["Load"]
  _f21_n681["Assign"]
  _f21_n682["Name"]
  _f21_n683["Store"]
  _f21_n684["Constant"]
  _f21_n685["If"]
  _f21_n686["Call"]
  _f21_n687["Name"]
  _f21_n688["Load"]
  _f21_n689["Name"]
  _f21_n690["Load"]
  _f21_n691["Name"]
  _f21_n692["Load"]
  _f21_n693["AnnAssign"]
  _f21_n694["Name"]
  _f21_n695["Store"]
  _f21_n696["Name"]
  _f21_n697["Load"]
  _f21_n698["Name"]
  _f21_n699["Load"]
  _f21_n700["AugAssign"]
  _f21_n701["Name"]
  _f21_n702["Store"]
  _f21_n703["Add"]
  _f21_n704["JoinedStr"]
  _f21_n705["FormattedValue"]
  _f21_n706["BinOp"]
  _f21_n707["Name"]
  _f21_n708["Load"]
  _f21_n709["Mult"]
  _f21_n710["Name"]
  _f21_n711["Load"]
  _f21_n712["Constant"]
  _f21_n713["FormattedValue"]
  _f21_n714["Attribute"]
  _f21_n715["Name"]
  _f21_n716["Load"]
  _f21_n717["Load"]
  _f21_n718["Constant"]
  _f21_n719["AugAssign"]
  _f21_n720["Name"]
  _f21_n721["Store"]
  _f21_n722["Add"]
  _f21_n723["JoinedStr"]
  _f21_n724["FormattedValue"]
  _f21_n725["BinOp"]
  _f21_n726["Name"]
  _f21_n727["Load"]
  _f21_n728["Mult"]
  _f21_n729["BinOp"]
  _f21_n730["Name"]
  _f21_n731["Load"]
  _f21_n732["Add"]
  _f21_n733["Constant"]
  _f21_n734["Constant"]
  _f21_n735["AugAssign"]
  _f21_n736["Name"]
  _f21_n737["Store"]
  _f21_n738["Add"]
  _f21_n739["Call"]
  _f21_n740["Name"]
  _f21_n741["Load"]
  _f21_n742["Attribute"]
  _f21_n743["Name"]
  _f21_n744["Load"]
  _f21_n745["Load"]
  _f21_n746["BinOp"]
  _f21_n747["Name"]
  _f21_n748["Load"]
  _f21_n749["Add"]
  _f21_n750["Constant"]
  _f21_n751["AugAssign"]
  _f21_n752["Name"]
  _f21_n753["Store"]
  _f21_n754["Add"]
  _f21_n755["JoinedStr"]
  _f21_n756["FormattedValue"]
  _f21_n757["BinOp"]
  _f21_n758["Name"]
  _f21_n759["Load"]
  _f21_n760["Mult"]
  _f21_n761["Name"]
  _f21_n762["Load"]
  _f21_n763["Constant"]
  _f21_n764["If"]
  _f21_n765["Call"]
  _f21_n766["Name"]
  _f21_n767["Load"]
  _f21_n768["Name"]
  _f21_n769["Load"]
  _f21_n770["Name"]
  _f21_n771["Load"]
  _f21_n772["AnnAssign"]
  _f21_n773["Name"]
  _f21_n774["Store"]
  _f21_n775["Name"]
  _f21_n776["Load"]
  _f21_n777["Name"]
  _f21_n778["Load"]
  _f21_n779["AugAssign"]
  _f21_n780["Name"]
  _f21_n781["Store"]
  _f21_n782["Add"]
  _f21_n783["JoinedStr"]
  _f21_n784["FormattedValue"]
  _f21_n785["BinOp"]
  _f21_n786["Name"]
  _f21_n787["Load"]
  _f21_n788["Mult"]
  _f21_n789["Name"]
  _f21_n790["Load"]
  _f21_n791["Constant"]
  _f21_n792["FormattedValue"]
  _f21_n793["Attribute"]
  _f21_n794["Name"]
  _f21_n795["Load"]
  _f21_n796["Load"]
  _f21_n797["Constant"]
  _f21_n798["AugAssign"]
  _f21_n799["Name"]
  _f21_n800["Store"]
  _f21_n801["Add"]
  _f21_n802["JoinedStr"]
  _f21_n803["FormattedValue"]
  _f21_n804["BinOp"]
  _f21_n805["Name"]
  _f21_n806["Load"]
  _f21_n807["Mult"]
  _f21_n808["BinOp"]
  _f21_n809["Name"]
  _f21_n810["Load"]
  _f21_n811["Add"]
  _f21_n812["Constant"]
  _f21_n813["Constant"]
  _f21_n814["AugAssign"]
  _f21_n815["Name"]
  _f21_n816["Store"]
  _f21_n817["Add"]
  _f21_n818["Call"]
  _f21_n819["Name"]
  _f21_n820["Load"]
  _f21_n821["Attribute"]
  _f21_n822["Name"]
  _f21_n823["Load"]
  _f21_n824["Load"]
  _f21_n825["BinOp"]
  _f21_n826["Name"]
  _f21_n827["Load"]
  _f21_n828["Add"]
  _f21_n829["Constant"]
  _f21_n830["AugAssign"]
  _f21_n831["Name"]
  _f21_n832["Store"]
  _f21_n833["Add"]
  _f21_n834["JoinedStr"]
  _f21_n835["FormattedValue"]
  _f21_n836["BinOp"]
  _f21_n837["Name"]
  _f21_n838["Load"]
  _f21_n839["Mult"]
  _f21_n840["Name"]
  _f21_n841["Load"]
  _f21_n842["Constant"]
  _f21_n843["AugAssign"]
  _f21_n844["Name"]
  _f21_n845["Store"]
  _f21_n846["Add"]
  _f21_n847["Call"]
  _f21_n848["Name"]
  _f21_n849["Load"]
  _f21_n850["Attribute"]
  _f21_n851["Name"]
  _f21_n852["Load"]
  _f21_n853["Load"]
  _f21_n854["Name"]
  _f21_n855["Load"]
  _f21_n856["Return"]
  _f21_n857["Name"]
  _f21_n858["Load"]
  _f22_n859["Assign"]
  _f22_n860["Name"]
  _f22_n861["Store"]
  _f22_n862["Call"]
  _f22_n863["Name"]
  _f22_n864["Load"]
  _f22_n865["keyword"]
  _f22_n866["Name"]
  _f22_n867["Load"]
  _f22_n868["Assign"]
  _f22_n869["Name"]
  _f22_n870["Store"]
  _f22_n871["Call"]
  _f22_n872["Name"]
  _f22_n873["Load"]
  _f22_n874["keyword"]
  _f22_n875["Name"]
  _f22_n876["Load"]
  _f22_n877["Return"]
  _f22_n878["JoinedStr"]
  _f22_n879["Constant"]
  _f22_n880["FormattedValue"]
  _f22_n881["Name"]
  _f22_n882["Load"]
  _f22_n883["Constant"]
  _f22_n884["FormattedValue"]
  _f22_n885["Name"]
  _f22_n886["Load"]
  _f22_n887["Constant"]

  _n424 --> _n425
  _n425 --> _n426
  _n426 --> _n427
  subgraph __sanitize
    direction TB
    _f16_n428 --> _f16_n429
    _f16_n429 --> _f16_n430
    _f16_n430 --> _f16_n431
    _f16_n431 --> _f16_n432
    _f16_n432 --> _f16_n433
    _f16_n433 --> _f16_n434
    _f16_n434 --> _f16_n435
    _f16_n435 --> _f16_n436
    _f16_n436 --> _f16_n437
    _f16_n437 --> _f16_n438
    _f16_n438 --> _f16_n439
    _f16_n439 --> _f16_n440
  end
  subgraph __get_unique_nodes
    direction TB
    _f17_n441 --> _f17_n442
    _f17_n442 --> _f17_n443
    _f17_n443 --> _f17_n444
    _f17_n444 --> _f17_n445
    _f17_n445 --> _f17_n446
    _f17_n446 --> _f17_n447
    _f17_n447 --> _f17_n448
    _f17_n448 --> _f17_n449
    _f17_n449 --> _f17_n450
    _f17_n450 --> _f17_n451
    _f17_n451 --> _f17_n452
    _f17_n452 --> _f17_n453
    _f17_n453 --> _f17_n454
    _f17_n454 --> _f17_n455
    _f17_n455 --> _f17_n456
    _f17_n456 --> _f17_n457
    _f17_n457 --> _f17_n458
    _f17_n458 --> _f17_n459
    _f17_n459 --> _f17_n460
    _f17_n460 --> _f17_n461
    _f17_n461 --> _f17_n462
    _f17_n462 --> _f17_n463
    _f17_n463 --> _f17_n464
    _f17_n464 --> _f17_n465
    _f17_n465 --> _f17_n466
    _f17_n466 --> _f17_n467
    _f17_n467 --> _f17_n468
    _f17_n468 --> _f17_n469
    _f17_n469 --> _f17_n470
    _f17_n470 --> _f17_n471
    _f17_n471 --> _f17_n472
    _f17_n472 --> _f17_n473
    _f17_n473 --> _f17_n474
    _f17_n474 --> _f17_n475
    _f17_n475 --> _f17_n476
    _f17_n476 --> _f17_n477
    _f17_n477 --> _f17_n478
    _f17_n478 --> _f17_n479
    _f17_n479 --> _f17_n480
    _f17_n480 --> _f17_n481
    _f17_n481 --> _f17_n482
    _f17_n482 --> _f17_n483
    _f17_n483 --> _f17_n484
    _f17_n484 --> _f17_n485
    _f17_n485 --> _f17_n486
    _f17_n486 --> _f17_n487
    _f17_n487 --> _f17_n488
    _f17_n488 --> _f17_n489
    _f17_n489 --> _f17_n490
    _f17_n490 --> _f17_n491
    _f17_n491 --> _f17_n492
    _f17_n492 --> _f17_n493
    _f17_n493 --> _f17_n494
    _f17_n494 --> _f17_n495
    _f17_n495 --> _f17_n496
    _f17_n496 --> _f17_n497
    _f17_n497 --> _f17_n498
    _f17_n498 --> _f17_n499
    _f17_n499 --> _f17_n500
    _f17_n500 --> _f17_n501
    _f17_n501 --> _f17_n502
    _f17_n502 --> _f17_n503
    _f17_n503 --> _f17_n504
    _f17_n504 --> _f17_n505
    _f17_n505 --> _f17_n506
    _f17_n506 --> _f17_n507
    _f17_n507 --> _f17_n508
    _f17_n508 --> _f17_n509
    _f17_n509 --> _f17_n510
    _f17_n510 --> _f17_n511
    _f17_n511 --> _f17_n512
    _f17_n512 --> _f17_n513
    _f17_n513 --> _f17_n514
    _f17_n514 --> _f17_n515
    _f17_n515 --> _f17_n516
    _f17_n516 --> _f17_n517
    _f17_n517 --> _f17_n518
    _f17_n518 --> _f17_n519
    _f17_n519 --> _f17_n520
    _f17_n520 --> _f17_n521
    _f17_n521 --> _f17_n522
    _f17_n522 --> _f17_n523
    _f17_n523 --> _f17_n524
    _f17_n524 --> _f17_n525
    _f17_n525 --> _f17_n526
    _f17_n526 --> _f17_n527
    _f17_n527 --> _f17_n528
    _f17_n528 --> _f17_n529
    _f17_n529 --> _f17_n530
    _f17_n530 --> _f17_n531
    _f17_n531 --> _f17_n532
    _f17_n532 --> _f17_n533
    _f17_n533 --> _f17_n534
  end
  subgraph __get_aliases_for_safe_names
    direction TB
    _f18_n535 --> _f18_n536
    _f18_n536 --> _f18_n537
    _f18_n537 --> _f18_n538
    _f18_n538 --> _f18_n539
    _f18_n539 --> _f18_n540
    _f18_n540 --> _f18_n541
    _f18_n541 --> _f18_n542
    _f18_n542 --> _f18_n543
    _f18_n543 --> _f18_n544
    _f18_n544 --> _f18_n545
    _f18_n545 --> _f18_n546
    _f18_n546 --> _f18_n547
    _f18_n547 --> _f18_n548
    _f18_n548 --> _f18_n549
    _f18_n549 --> _f18_n550
    _f18_n550 --> _f18_n551
    _f18_n551 --> _f18_n552
    _f18_n552 --> _f18_n553
    _f18_n553 --> _f18_n554
    _f18_n554 --> _f18_n555
    _f18_n555 --> _f18_n556
    _f18_n556 --> _f18_n557
    _f18_n557 --> _f18_n558
    _f18_n558 --> _f18_n559
    _f18_n559 --> _f18_n560
    _f18_n560 --> _f18_n561
    _f18_n561 --> _f18_n562
    _f18_n562 --> _f18_n563
    _f18_n563 --> _f18_n564
    _f18_n564 --> _f18_n565
    _f18_n565 --> _f18_n566
    _f18_n566 --> _f18_n567
    _f18_n567 --> _f18_n568
    _f18_n568 --> _f18_n569
    _f18_n569 --> _f18_n570
    _f18_n570 --> _f18_n571
    _f18_n571 --> _f18_n572
    _f18_n572 --> _f18_n573
    _f18_n573 --> _f18_n574
    _f18_n574 --> _f18_n575
    _f18_n575 --> _f18_n576
    _f18_n576 --> _f18_n577
  end
  subgraph __get_flow_link_text
    direction TB
    _f19_n578 --> _f19_n579
    _f19_n579 --> _f19_n580
    _f19_n580 --> _f19_n581
    _f19_n581 --> _f19_n582
    _f19_n582 --> _f19_n583
    _f19_n583 --> _f19_n584
    _f19_n584 --> _f19_n585
    _f19_n585 --> _f19_n586
    _f19_n586 --> _f19_n587
    _f19_n587 --> _f19_n588
    _f19_n588 --> _f19_n589
    _f19_n589 --> _f19_n590
    _f19_n590 --> _f19_n591
    _f19_n591 --> _f19_n592
    _f19_n592 --> _f19_n593
    _f19_n593 --> _f19_n594
    _f19_n594 --> _f19_n595
    _f19_n595 --> _f19_n596
    _f19_n596 --> _f19_n597
    _f19_n597 --> _f19_n598
    _f19_n598 --> _f19_n599
    _f19_n599 --> _f19_n600
    _f19_n600 --> _f19_n601
    _f19_n601 --> _f19_n602
    _f19_n602 --> _f19_n603
    _f19_n603 --> _f19_n604
    _f19_n604 --> _f19_n605
    _f19_n605 --> _f19_n606
    _f19_n606 --> _f19_n607
    _f19_n607 --> _f19_n608
    _f19_n608 --> _f19_n609
    _f19_n609 --> _f19_n610
    _f19_n610 --> _f19_n611
    _f19_n611 --> _f19_n612
  end
  subgraph __get_flow_connections
    direction TB
    _f20_n613 --> _f20_n614
    _f20_n614 --> _f20_n615
    _f20_n615 --> _f20_n616
    _f20_n616 --> _f20_n617
    _f20_n617 --> _f20_n618
    _f20_n618 --> _f20_n619
    _f20_n619 --> _f20_n620
    _f20_n620 --> _f20_n621
    _f20_n621 --> _f20_n622
    _f20_n622 --> _f20_n623
    _f20_n623 --> _f20_n624
    _f20_n624 --> _f20_n625
    _f20_n625 --> _f20_n626
    _f20_n626 --> _f20_n627
    _f20_n627 --> _f20_n628
    _f20_n628 --> _f20_n629
    _f20_n629 --> _f20_n630
    _f20_n630 --> _f20_n631
    _f20_n631 --> _f20_n632
    _f20_n632 --> _f20_n633
    _f20_n633 --> _f20_n634
    _f20_n634 --> _f20_n635
    _f20_n635 --> _f20_n636
    _f20_n636 --> _f20_n637
    _f20_n637 --> _f20_n638
    _f20_n638 --> _f20_n639
    _f20_n639 --> _f20_n640
    _f20_n640 --> _f20_n641
    _f20_n641 --> _f20_n642
    _f20_n642 --> _f20_n643
    _f20_n643 --> _f20_n644
    _f20_n644 --> _f20_n645
    _f20_n645 --> _f20_n646
    _f20_n646 --> _f20_n647
    _f20_n647 --> _f20_n648
    _f20_n648 --> _f20_n649
    _f20_n649 --> _f20_n650
    _f20_n650 --> _f20_n651
    _f20_n651 --> _f20_n652
    _f20_n652 --> _f20_n653
    _f20_n653 --> _f20_n654
    _f20_n654 --> _f20_n655
    _f20_n655 --> _f20_n656
    _f20_n656 --> _f20_n657
    _f20_n657 --> _f20_n658
    _f20_n658 --> _f20_n659
    _f20_n659 --> _f20_n660
    _f20_n660 --> _f20_n661
    _f20_n661 --> _f20_n662
    _f20_n662 --> _f20_n663
    _f20_n663 --> _f20_n664
    _f20_n664 --> _f20_n665
    _f20_n665 --> _f20_n666
    _f20_n666 --> _f20_n667
    _f20_n667 --> _f20_n668
    _f20_n668 --> _f20_n669
    _f20_n669 --> _f20_n670
    _f20_n670 --> _f20_n671
    _f20_n671 --> _f20_n672
    _f20_n672 --> _f20_n673
    _f20_n673 --> _f20_n674
    _f20_n674 --> _f20_n675
    _f20_n675 --> _f20_n676
    _f20_n676 --> _f20_n677
    _f20_n677 --> _f20_n678
    _f20_n678 --> _f20_n679
    _f20_n679 --> _f20_n680
  end
  subgraph __get_block_text
    direction TB
    _f21_n681 --> _f21_n682
    _f21_n682 --> _f21_n683
    _f21_n683 --> _f21_n684
    _f21_n684 --> _f21_n685
    _f21_n685 --> _f21_n686
    _f21_n686 --> _f21_n687
    _f21_n687 --> _f21_n688
    _f21_n688 --> _f21_n689
    _f21_n689 --> _f21_n690
    _f21_n690 --> _f21_n691
    _f21_n691 --> _f21_n692
    _f21_n692 --> _f21_n693
    _f21_n693 --> _f21_n694
    _f21_n694 --> _f21_n695
    _f21_n695 --> _f21_n696
    _f21_n696 --> _f21_n697
    _f21_n697 --> _f21_n698
    _f21_n698 --> _f21_n699
    _f21_n699 --> _f21_n700
    _f21_n700 --> _f21_n701
    _f21_n701 --> _f21_n702
    _f21_n702 --> _f21_n703
    _f21_n703 --> _f21_n704
    _f21_n704 --> _f21_n705
    _f21_n705 --> _f21_n706
    _f21_n706 --> _f21_n707
    _f21_n707 --> _f21_n708
    _f21_n708 --> _f21_n709
    _f21_n709 --> _f21_n710
    _f21_n710 --> _f21_n711
    _f21_n711 --> _f21_n712
    _f21_n712 --> _f21_n713
    _f21_n713 --> _f21_n714
    _f21_n714 --> _f21_n715
    _f21_n715 --> _f21_n716
    _f21_n716 --> _f21_n717
    _f21_n717 --> _f21_n718
    _f21_n718 --> _f21_n719
    _f21_n719 --> _f21_n720
    _f21_n720 --> _f21_n721
    _f21_n721 --> _f21_n722
    _f21_n722 --> _f21_n723
    _f21_n723 --> _f21_n724
    _f21_n724 --> _f21_n725
    _f21_n725 --> _f21_n726
    _f21_n726 --> _f21_n727
    _f21_n727 --> _f21_n728
    _f21_n728 --> _f21_n729
    _f21_n729 --> _f21_n730
    _f21_n730 --> _f21_n731
    _f21_n731 --> _f21_n732
    _f21_n732 --> _f21_n733
    _f21_n733 --> _f21_n734
    _f21_n734 --> _f21_n735
    _f21_n735 --> _f21_n736
    _f21_n736 --> _f21_n737
    _f21_n737 --> _f21_n738
    _f21_n738 --> _f21_n739
    _f21_n739 --> _f21_n740
    _f21_n740 --> _f21_n741
    _f21_n741 --> _f21_n742
    _f21_n742 --> _f21_n743
    _f21_n743 --> _f21_n744
    _f21_n744 --> _f21_n745
    _f21_n745 --> _f21_n746
    _f21_n746 --> _f21_n747
    _f21_n747 --> _f21_n748
    _f21_n748 --> _f21_n749
    _f21_n749 --> _f21_n750
    _f21_n750 --> _f21_n751
    _f21_n751 --> _f21_n752
    _f21_n752 --> _f21_n753
    _f21_n753 --> _f21_n754
    _f21_n754 --> _f21_n755
    _f21_n755 --> _f21_n756
    _f21_n756 --> _f21_n757
    _f21_n757 --> _f21_n758
    _f21_n758 --> _f21_n759
    _f21_n759 --> _f21_n760
    _f21_n760 --> _f21_n761
    _f21_n761 --> _f21_n762
    _f21_n762 --> _f21_n763
    _f21_n763 --> _f21_n764
    _f21_n764 --> _f21_n765
    _f21_n765 --> _f21_n766
    _f21_n766 --> _f21_n767
    _f21_n767 --> _f21_n768
    _f21_n768 --> _f21_n769
    _f21_n769 --> _f21_n770
    _f21_n770 --> _f21_n771
    _f21_n771 --> _f21_n772
    _f21_n772 --> _f21_n773
    _f21_n773 --> _f21_n774
    _f21_n774 --> _f21_n775
    _f21_n775 --> _f21_n776
    _f21_n776 --> _f21_n777
    _f21_n777 --> _f21_n778
    _f21_n778 --> _f21_n779
    _f21_n779 --> _f21_n780
    _f21_n780 --> _f21_n781
    _f21_n781 --> _f21_n782
    _f21_n782 --> _f21_n783
    _f21_n783 --> _f21_n784
    _f21_n784 --> _f21_n785
    _f21_n785 --> _f21_n786
    _f21_n786 --> _f21_n787
    _f21_n787 --> _f21_n788
    _f21_n788 --> _f21_n789
    _f21_n789 --> _f21_n790
    _f21_n790 --> _f21_n791
    _f21_n791 --> _f21_n792
    _f21_n792 --> _f21_n793
    _f21_n793 --> _f21_n794
    _f21_n794 --> _f21_n795
    _f21_n795 --> _f21_n796
    _f21_n796 --> _f21_n797
    _f21_n797 --> _f21_n798
    _f21_n798 --> _f21_n799
    _f21_n799 --> _f21_n800
    _f21_n800 --> _f21_n801
    _f21_n801 --> _f21_n802
    _f21_n802 --> _f21_n803
    _f21_n803 --> _f21_n804
    _f21_n804 --> _f21_n805
    _f21_n805 --> _f21_n806
    _f21_n806 --> _f21_n807
    _f21_n807 --> _f21_n808
    _f21_n808 --> _f21_n809
    _f21_n809 --> _f21_n810
    _f21_n810 --> _f21_n811
    _f21_n811 --> _f21_n812
    _f21_n812 --> _f21_n813
    _f21_n813 --> _f21_n814
    _f21_n814 --> _f21_n815
    _f21_n815 --> _f21_n816
    _f21_n816 --> _f21_n817
    _f21_n817 --> _f21_n818
    _f21_n818 --> _f21_n819
    _f21_n819 --> _f21_n820
    _f21_n820 --> _f21_n821
    _f21_n821 --> _f21_n822
    _f21_n822 --> _f21_n823
    _f21_n823 --> _f21_n824
    _f21_n824 --> _f21_n825
    _f21_n825 --> _f21_n826
    _f21_n826 --> _f21_n827
    _f21_n827 --> _f21_n828
    _f21_n828 --> _f21_n829
    _f21_n829 --> _f21_n830
    _f21_n830 --> _f21_n831
    _f21_n831 --> _f21_n832
    _f21_n832 --> _f21_n833
    _f21_n833 --> _f21_n834
    _f21_n834 --> _f21_n835
    _f21_n835 --> _f21_n836
    _f21_n836 --> _f21_n837
    _f21_n837 --> _f21_n838
    _f21_n838 --> _f21_n839
    _f21_n839 --> _f21_n840
    _f21_n840 --> _f21_n841
    _f21_n841 --> _f21_n842
    _f21_n842 --> _f21_n843
    _f21_n843 --> _f21_n844
    _f21_n844 --> _f21_n845
    _f21_n845 --> _f21_n846
    _f21_n846 --> _f21_n847
    _f21_n847 --> _f21_n848
    _f21_n848 --> _f21_n849
    _f21_n849 --> _f21_n850
    _f21_n850 --> _f21_n851
    _f21_n851 --> _f21_n852
    _f21_n852 --> _f21_n853
    _f21_n853 --> _f21_n854
    _f21_n854 --> _f21_n855
    _f21_n855 --> _f21_n856
    _f21_n856 --> _f21_n857
    _f21_n857 --> _f21_n858
  end
  subgraph _create_mermaid_flow_graph_from_links
    direction TB
    _f22_n859 --> _f22_n860
    _f22_n860 --> _f22_n861
    _f22_n861 --> _f22_n862
    _f22_n862 --> _f22_n863
    _f22_n863 --> _f22_n864
    _f22_n864 --> _f22_n865
    _f22_n865 --> _f22_n866
    _f22_n866 --> _f22_n867
    _f22_n867 --> _f22_n868
    _f22_n868 --> _f22_n869
    _f22_n869 --> _f22_n870
    _f22_n870 --> _f22_n871
    _f22_n871 --> _f22_n872
    _f22_n872 --> _f22_n873
    _f22_n873 --> _f22_n874
    _f22_n874 --> _f22_n875
    _f22_n875 --> _f22_n876
    _f22_n876 --> _f22_n877
    _f22_n877 --> _f22_n878
    _f22_n878 --> _f22_n879
    _f22_n879 --> _f22_n880
    _f22_n880 --> _f22_n881
    _f22_n881 --> _f22_n882
    _f22_n882 --> _f22_n883
    _f22_n883 --> _f22_n884
    _f22_n884 --> _f22_n885
    _f22_n885 --> _f22_n886
    _f22_n886 --> _f22_n887
  end

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
        alias(name='MermaidClass'),
        alias(name='MermaidElement'),
        alias(name='MermaidFunction'),
        alias(name='MermaidLink'),
        alias(name='MermaidNode')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=8,
      end_col_offset=1),
    Assign(
      targets=[
        Name(
          id='TAB',
          ctx=Store(),
          lineno=10,
          col_offset=0,
          end_lineno=10,
          end_col_offset=3)],
      value=Constant(
        value='  ',
        lineno=10,
        col_offset=6,
        end_lineno=10,
        end_col_offset=10),
      lineno=10,
      col_offset=0,
      end_lineno=10,
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
              lineno=13,
              col_offset=24,
              end_lineno=13,
              end_col_offset=27),
            lineno=13,
            col_offset=14,
            end_lineno=13,
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
                    lineno=15,
                    col_offset=8,
                    end_lineno=15,
                    end_col_offset=16),
                  attr='replace',
                  ctx=Load(),
                  lineno=15,
                  col_offset=8,
                  end_lineno=16,
                  end_col_offset=16),
                args=[
                  Constant(
                    value='<',
                    lineno=16,
                    col_offset=17,
                    end_lineno=16,
                    end_col_offset=20),
                  Constant(
                    value='',
                    lineno=16,
                    col_offset=21,
                    end_lineno=16,
                    end_col_offset=23)],
                keywords=[],
                lineno=15,
                col_offset=8,
                end_lineno=16,
                end_col_offset=24),
              attr='replace',
              ctx=Load(),
              lineno=15,
              col_offset=8,
              end_lineno=17,
              end_col_offset=16),
            args=[
              Constant(
                value='>',
                lineno=17,
                col_offset=17,
                end_lineno=17,
                end_col_offset=20),
              Constant(
                value='',
                lineno=17,
                col_offset=21,
                end_lineno=17,
                end_col_offset=23)],
            keywords=[],
            lineno=15,
            col_offset=8,
            end_lineno=17,
            end_col_offset=24),
          lineno=14,
          col_offset=4,
          end_lineno=18,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=13,
        col_offset=32,
        end_lineno=13,
        end_col_offset=35),
      lineno=13,
      col_offset=0,
      end_lineno=18,
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
                lineno=21,
                col_offset=32,
                end_lineno=21,
                end_col_offset=36),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=21,
                col_offset=37,
                end_lineno=21,
                end_col_offset=51),
              ctx=Load(),
              lineno=21,
              col_offset=32,
              end_lineno=21,
              end_col_offset=52),
            lineno=21,
            col_offset=22,
            end_lineno=21,
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
              lineno=23,
              col_offset=4,
              end_lineno=23,
              end_col_offset=12)],
          value=List(
            elts=[],
            ctx=Load(),
            lineno=23,
            col_offset=15,
            end_lineno=23,
            end_col_offset=17),
          lineno=23,
          col_offset=4,
          end_lineno=23,
          end_col_offset=17),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=24,
            col_offset=8,
            end_lineno=24,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=24,
            col_offset=19,
            end_lineno=24,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=25,
                  col_offset=11,
                  end_lineno=25,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=25,
                    col_offset=22,
                    end_lineno=25,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=25,
                    col_offset=31,
                    end_lineno=25,
                    end_col_offset=42)],
                keywords=[],
                lineno=25,
                col_offset=11,
                end_lineno=25,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=26,
                    col_offset=12,
                    end_lineno=26,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=26,
                    col_offset=19,
                    end_lineno=26,
                    end_col_offset=30),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=26,
                    col_offset=33,
                    end_lineno=26,
                    end_col_offset=40),
                  simple=1,
                  lineno=26,
                  col_offset=12,
                  end_lineno=26,
                  end_col_offset=40),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=27,
                        col_offset=15,
                        end_lineno=27,
                        end_col_offset=19),
                      attr='from_',
                      ctx=Load(),
                      lineno=27,
                      col_offset=15,
                      end_lineno=27,
                      end_col_offset=25),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=27,
                        col_offset=33,
                        end_lineno=27,
                        end_col_offset=41)],
                    lineno=27,
                    col_offset=15,
                    end_lineno=27,
                    end_col_offset=41),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=28,
                            col_offset=16,
                            end_lineno=28,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=28,
                          col_offset=16,
                          end_lineno=28,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=28,
                              col_offset=32,
                              end_lineno=28,
                              end_col_offset=36),
                            attr='from_',
                            ctx=Load(),
                            lineno=28,
                            col_offset=32,
                            end_lineno=28,
                            end_col_offset=42)],
                        keywords=[],
                        lineno=28,
                        col_offset=16,
                        end_lineno=28,
                        end_col_offset=43),
                      lineno=28,
                      col_offset=16,
                      end_lineno=28,
                      end_col_offset=43)],
                  orelse=[],
                  lineno=27,
                  col_offset=12,
                  end_lineno=28,
                  end_col_offset=43),
                If(
                  test=Compare(
                    left=Attribute(
                      value=Name(
                        id='link',
                        ctx=Load(),
                        lineno=29,
                        col_offset=15,
                        end_lineno=29,
                        end_col_offset=19),
                      attr='to',
                      ctx=Load(),
                      lineno=29,
                      col_offset=15,
                      end_lineno=29,
                      end_col_offset=22),
                    ops=[
                      NotIn()],
                    comparators=[
                      Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=29,
                        col_offset=30,
                        end_lineno=29,
                        end_col_offset=38)],
                    lineno=29,
                    col_offset=15,
                    end_lineno=29,
                    end_col_offset=38),
                  body=[
                    Expr(
                      value=Call(
                        func=Attribute(
                          value=Name(
                            id='node_set',
                            ctx=Load(),
                            lineno=30,
                            col_offset=16,
                            end_lineno=30,
                            end_col_offset=24),
                          attr='append',
                          ctx=Load(),
                          lineno=30,
                          col_offset=16,
                          end_lineno=30,
                          end_col_offset=31),
                        args=[
                          Attribute(
                            value=Name(
                              id='link',
                              ctx=Load(),
                              lineno=30,
                              col_offset=32,
                              end_lineno=30,
                              end_col_offset=36),
                            attr='to',
                            ctx=Load(),
                            lineno=30,
                            col_offset=32,
                            end_lineno=30,
                            end_col_offset=39)],
                        keywords=[],
                        lineno=30,
                        col_offset=16,
                        end_lineno=30,
                        end_col_offset=40),
                      lineno=30,
                      col_offset=16,
                      end_lineno=30,
                      end_col_offset=40)],
                  orelse=[],
                  lineno=29,
                  col_offset=12,
                  end_lineno=30,
                  end_col_offset=40)],
              orelse=[],
              lineno=25,
              col_offset=8,
              end_lineno=30,
              end_col_offset=40),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=31,
                  col_offset=11,
                  end_lineno=31,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=31,
                    col_offset=22,
                    end_lineno=31,
                    end_col_offset=29),
                  Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=31,
                    col_offset=31,
                    end_lineno=31,
                    end_col_offset=43)],
                keywords=[],
                lineno=31,
                col_offset=11,
                end_lineno=31,
                end_col_offset=44),
              body=[
                AnnAssign(
                  target=Name(
                    id='block',
                    ctx=Store(),
                    lineno=32,
                    col_offset=12,
                    end_lineno=32,
                    end_col_offset=17),
                  annotation=Name(
                    id='MermaidBlock',
                    ctx=Load(),
                    lineno=32,
                    col_offset=20,
                    end_lineno=32,
                    end_col_offset=32),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=32,
                    col_offset=35,
                    end_lineno=32,
                    end_col_offset=42),
                  simple=1,
                  lineno=32,
                  col_offset=12,
                  end_lineno=32,
                  end_col_offset=42),
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='node_set',
                        ctx=Load(),
                        lineno=33,
                        col_offset=12,
                        end_lineno=33,
                        end_col_offset=20),
                      attr='extend',
                      ctx=Load(),
                      lineno=33,
                      col_offset=12,
                      end_lineno=33,
                      end_col_offset=27),
                    args=[
                      Call(
                        func=Name(
                          id='_get_unique_nodes',
                          ctx=Load(),
                          lineno=33,
                          col_offset=28,
                          end_lineno=33,
                          end_col_offset=45),
                        args=[
                          Attribute(
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=33,
                              col_offset=46,
                              end_lineno=33,
                              end_col_offset=51),
                            attr='block_contents',
                            ctx=Load(),
                            lineno=33,
                            col_offset=46,
                            end_lineno=33,
                            end_col_offset=66)],
                        keywords=[],
                        lineno=33,
                        col_offset=28,
                        end_lineno=33,
                        end_col_offset=67)],
                    keywords=[],
                    lineno=33,
                    col_offset=12,
                    end_lineno=33,
                    end_col_offset=68),
                  lineno=33,
                  col_offset=12,
                  end_lineno=33,
                  end_col_offset=68)],
              orelse=[],
              lineno=31,
              col_offset=8,
              end_lineno=33,
              end_col_offset=68)],
          orelse=[],
          lineno=24,
          col_offset=4,
          end_lineno=33,
          end_col_offset=68),
        Return(
          value=Name(
            id='node_set',
            ctx=Load(),
            lineno=34,
            col_offset=11,
            end_lineno=34,
            end_col_offset=19),
          lineno=34,
          col_offset=4,
          end_lineno=34,
          end_col_offset=19)],
      decorator_list=[],
      returns=Subscript(
        value=Name(
          id='list',
          ctx=Load(),
          lineno=21,
          col_offset=57,
          end_lineno=21,
          end_col_offset=61),
        slice=Name(
          id='MermaidNode',
          ctx=Load(),
          lineno=21,
          col_offset=62,
          end_lineno=21,
          end_col_offset=73),
        ctx=Load(),
        lineno=21,
        col_offset=57,
        end_lineno=21,
        end_col_offset=74),
      lineno=21,
      col_offset=0,
      end_lineno=34,
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
                lineno=37,
                col_offset=42,
                end_lineno=37,
                end_col_offset=46),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=37,
                col_offset=47,
                end_lineno=37,
                end_col_offset=61),
              ctx=Load(),
              lineno=37,
              col_offset=42,
              end_lineno=37,
              end_col_offset=62),
            lineno=37,
            col_offset=32,
            end_lineno=37,
            end_col_offset=62),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=37,
              col_offset=72,
              end_lineno=37,
              end_col_offset=75),
            lineno=37,
            col_offset=64,
            end_lineno=37,
            end_col_offset=75)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=37,
            col_offset=78,
            end_lineno=37,
            end_col_offset=79)]),
      body=[
        Assign(
          targets=[
            Name(
              id='alias_string',
              ctx=Store(),
              lineno=38,
              col_offset=4,
              end_lineno=38,
              end_col_offset=16)],
          value=Constant(
            value='',
            lineno=38,
            col_offset=19,
            end_lineno=38,
            end_col_offset=21),
          lineno=38,
          col_offset=4,
          end_lineno=38,
          end_col_offset=21),
        For(
          target=Name(
            id='node',
            ctx=Store(),
            lineno=39,
            col_offset=8,
            end_lineno=39,
            end_col_offset=12),
          iter=Call(
            func=Name(
              id='_get_unique_nodes',
              ctx=Load(),
              lineno=39,
              col_offset=16,
              end_lineno=39,
              end_col_offset=33),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=39,
                  col_offset=43,
                  end_lineno=39,
                  end_col_offset=51),
                lineno=39,
                col_offset=34,
                end_lineno=39,
                end_col_offset=51)],
            lineno=39,
            col_offset=16,
            end_lineno=39,
            end_col_offset=52),
          body=[
            AugAssign(
              target=Name(
                id='alias_string',
                ctx=Store(),
                lineno=40,
                col_offset=8,
                end_lineno=40,
                end_col_offset=20),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=40,
                        col_offset=27,
                        end_lineno=40,
                        end_col_offset=30),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=40,
                        col_offset=33,
                        end_lineno=40,
                        end_col_offset=39),
                      lineno=40,
                      col_offset=27,
                      end_lineno=40,
                      end_col_offset=39),
                    conversion=-1,
                    lineno=40,
                    col_offset=24,
                    end_lineno=40,
                    end_col_offset=92),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=40,
                        col_offset=41,
                        end_lineno=40,
                        end_col_offset=45),
                      attr='mermaid_safe_name',
                      ctx=Load(),
                      lineno=40,
                      col_offset=41,
                      end_lineno=40,
                      end_col_offset=63),
                    conversion=-1,
                    lineno=40,
                    col_offset=24,
                    end_lineno=40,
                    end_col_offset=92),
                  Constant(
                    value='["',
                    lineno=40,
                    col_offset=24,
                    end_lineno=40,
                    end_col_offset=92),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='node',
                        ctx=Load(),
                        lineno=40,
                        col_offset=68,
                        end_lineno=40,
                        end_col_offset=72),
                      attr='display_name',
                      ctx=Load(),
                      lineno=40,
                      col_offset=68,
                      end_lineno=40,
                      end_col_offset=85),
                    conversion=-1,
                    lineno=40,
                    col_offset=24,
                    end_lineno=40,
                    end_col_offset=92),
                  Constant(
                    value='"]\n',
                    lineno=40,
                    col_offset=24,
                    end_lineno=40,
                    end_col_offset=92)],
                lineno=40,
                col_offset=24,
                end_lineno=40,
                end_col_offset=92),
              lineno=40,
              col_offset=8,
              end_lineno=40,
              end_col_offset=92)],
          orelse=[],
          lineno=39,
          col_offset=4,
          end_lineno=40,
          end_col_offset=92),
        Return(
          value=Call(
            func=Name(
              id='_sanitize',
              ctx=Load(),
              lineno=41,
              col_offset=11,
              end_lineno=41,
              end_col_offset=20),
            args=[
              Name(
                id='alias_string',
                ctx=Load(),
                lineno=41,
                col_offset=21,
                end_lineno=41,
                end_col_offset=33)],
            keywords=[],
            lineno=41,
            col_offset=11,
            end_lineno=41,
            end_col_offset=34),
          lineno=41,
          col_offset=4,
          end_lineno=41,
          end_col_offset=34)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=37,
        col_offset=84,
        end_lineno=37,
        end_col_offset=87),
      lineno=37,
      col_offset=0,
      end_lineno=41,
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
              lineno=44,
              col_offset=30,
              end_lineno=44,
              end_col_offset=44),
            lineno=44,
            col_offset=24,
            end_lineno=44,
            end_col_offset=44),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=44,
              col_offset=54,
              end_lineno=44,
              end_col_offset=57),
            lineno=44,
            col_offset=46,
            end_lineno=44,
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
              lineno=45,
              col_offset=4,
              end_lineno=45,
              end_col_offset=13)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=45,
                col_offset=16,
                end_lineno=45,
                end_col_offset=20),
              attr='from_',
              ctx=Load(),
              lineno=45,
              col_offset=16,
              end_lineno=45,
              end_col_offset=26),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=45,
            col_offset=16,
            end_lineno=45,
            end_col_offset=44),
          lineno=45,
          col_offset=4,
          end_lineno=45,
          end_col_offset=44),
        Assign(
          targets=[
            Name(
              id='to_name',
              ctx=Store(),
              lineno=46,
              col_offset=4,
              end_lineno=46,
              end_col_offset=11)],
          value=Attribute(
            value=Attribute(
              value=Name(
                id='link',
                ctx=Load(),
                lineno=46,
                col_offset=14,
                end_lineno=46,
                end_col_offset=18),
              attr='to',
              ctx=Load(),
              lineno=46,
              col_offset=14,
              end_lineno=46,
              end_col_offset=21),
            attr='mermaid_safe_name',
            ctx=Load(),
            lineno=46,
            col_offset=14,
            end_lineno=46,
            end_col_offset=39),
          lineno=46,
          col_offset=4,
          end_lineno=46,
          end_col_offset=39),
        Return(
          value=JoinedStr(
            values=[
              FormattedValue(
                value=BinOp(
                  left=Name(
                    id='TAB',
                    ctx=Load(),
                    lineno=48,
                    col_offset=14,
                    end_lineno=48,
                    end_col_offset=17),
                  op=Mult(),
                  right=Name(
                    id='indent',
                    ctx=Load(),
                    lineno=48,
                    col_offset=18,
                    end_lineno=48,
                    end_col_offset=24),
                  lineno=48,
                  col_offset=14,
                  end_lineno=48,
                  end_col_offset=24),
                conversion=-1,
                lineno=48,
                col_offset=11,
                end_lineno=48,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='from_name',
                  ctx=Load(),
                  lineno=48,
                  col_offset=26,
                  end_lineno=48,
                  end_col_offset=35),
                conversion=-1,
                lineno=48,
                col_offset=11,
                end_lineno=48,
                end_col_offset=53),
              Constant(
                value=' --> ',
                lineno=48,
                col_offset=11,
                end_lineno=48,
                end_col_offset=53),
              FormattedValue(
                value=Name(
                  id='to_name',
                  ctx=Load(),
                  lineno=48,
                  col_offset=42,
                  end_lineno=48,
                  end_col_offset=49),
                conversion=-1,
                lineno=48,
                col_offset=11,
                end_lineno=48,
                end_col_offset=53),
              Constant(
                value='\n',
                lineno=48,
                col_offset=11,
                end_lineno=48,
                end_col_offset=53)],
            lineno=48,
            col_offset=11,
            end_lineno=48,
            end_col_offset=53),
          lineno=48,
          col_offset=4,
          end_lineno=48,
          end_col_offset=53)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=44,
        col_offset=62,
        end_lineno=44,
        end_col_offset=65),
      lineno=44,
      col_offset=0,
      end_lineno=48,
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
                lineno=51,
                col_offset=36,
                end_lineno=51,
                end_col_offset=40),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=51,
                col_offset=41,
                end_lineno=51,
                end_col_offset=55),
              ctx=Load(),
              lineno=51,
              col_offset=36,
              end_lineno=51,
              end_col_offset=56),
            lineno=51,
            col_offset=26,
            end_lineno=51,
            end_col_offset=56),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=51,
              col_offset=66,
              end_lineno=51,
              end_col_offset=69),
            lineno=51,
            col_offset=58,
            end_lineno=51,
            end_col_offset=69)],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[
          Constant(
            value=1,
            lineno=51,
            col_offset=72,
            end_lineno=51,
            end_col_offset=73)]),
      body=[
        Assign(
          targets=[
            Name(
              id='connection_text',
              ctx=Store(),
              lineno=52,
              col_offset=4,
              end_lineno=52,
              end_col_offset=19)],
          value=Constant(
            value='',
            lineno=52,
            col_offset=22,
            end_lineno=52,
            end_col_offset=24),
          lineno=52,
          col_offset=4,
          end_lineno=52,
          end_col_offset=24),
        For(
          target=Name(
            id='element',
            ctx=Store(),
            lineno=53,
            col_offset=8,
            end_lineno=53,
            end_col_offset=15),
          iter=Name(
            id='elements',
            ctx=Load(),
            lineno=53,
            col_offset=19,
            end_lineno=53,
            end_col_offset=27),
          body=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=54,
                  col_offset=11,
                  end_lineno=54,
                  end_col_offset=21),
                args=[
                  Name(
                    id='element',
                    ctx=Load(),
                    lineno=54,
                    col_offset=22,
                    end_lineno=54,
                    end_col_offset=29),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=54,
                    col_offset=31,
                    end_lineno=54,
                    end_col_offset=42)],
                keywords=[],
                lineno=54,
                col_offset=11,
                end_lineno=54,
                end_col_offset=43),
              body=[
                AnnAssign(
                  target=Name(
                    id='link',
                    ctx=Store(),
                    lineno=55,
                    col_offset=12,
                    end_lineno=55,
                    end_col_offset=16),
                  annotation=Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=55,
                    col_offset=18,
                    end_lineno=55,
                    end_col_offset=29),
                  value=Name(
                    id='element',
                    ctx=Load(),
                    lineno=55,
                    col_offset=32,
                    end_lineno=55,
                    end_col_offset=39),
                  simple=1,
                  lineno=55,
                  col_offset=12,
                  end_lineno=55,
                  end_col_offset=39),
                AugAssign(
                  target=Name(
                    id='connection_text',
                    ctx=Store(),
                    lineno=56,
                    col_offset=12,
                    end_lineno=56,
                    end_col_offset=27),
                  op=Add(),
                  value=Call(
                    func=Name(
                      id='_get_flow_link_text',
                      ctx=Load(),
                      lineno=56,
                      col_offset=31,
                      end_lineno=56,
                      end_col_offset=50),
                    args=[],
                    keywords=[
                      keyword(
                        arg='link',
                        value=Name(
                          id='link',
                          ctx=Load(),
                          lineno=56,
                          col_offset=56,
                          end_lineno=56,
                          end_col_offset=60),
                        lineno=56,
                        col_offset=51,
                        end_lineno=56,
                        end_col_offset=60),
                      keyword(
                        arg='indent',
                        value=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=56,
                          col_offset=69,
                          end_lineno=56,
                          end_col_offset=75),
                        lineno=56,
                        col_offset=62,
                        end_lineno=56,
                        end_col_offset=75)],
                    lineno=56,
                    col_offset=31,
                    end_lineno=56,
                    end_col_offset=76),
                  lineno=56,
                  col_offset=12,
                  end_lineno=56,
                  end_col_offset=76)],
              orelse=[
                If(
                  test=Call(
                    func=Name(
                      id='isinstance',
                      ctx=Load(),
                      lineno=57,
                      col_offset=13,
                      end_lineno=57,
                      end_col_offset=23),
                    args=[
                      Name(
                        id='element',
                        ctx=Load(),
                        lineno=57,
                        col_offset=24,
                        end_lineno=57,
                        end_col_offset=31),
                      Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=57,
                        col_offset=33,
                        end_lineno=57,
                        end_col_offset=45)],
                    keywords=[],
                    lineno=57,
                    col_offset=13,
                    end_lineno=57,
                    end_col_offset=46),
                  body=[
                    AnnAssign(
                      target=Name(
                        id='block',
                        ctx=Store(),
                        lineno=58,
                        col_offset=12,
                        end_lineno=58,
                        end_col_offset=17),
                      annotation=Name(
                        id='MermaidBlock',
                        ctx=Load(),
                        lineno=58,
                        col_offset=19,
                        end_lineno=58,
                        end_col_offset=31),
                      value=Name(
                        id='element',
                        ctx=Load(),
                        lineno=58,
                        col_offset=34,
                        end_lineno=58,
                        end_col_offset=41),
                      simple=1,
                      lineno=58,
                      col_offset=12,
                      end_lineno=58,
                      end_col_offset=41),
                    AugAssign(
                      target=Name(
                        id='connection_text',
                        ctx=Store(),
                        lineno=59,
                        col_offset=12,
                        end_lineno=59,
                        end_col_offset=27),
                      op=Add(),
                      value=Call(
                        func=Name(
                          id='_get_block_text',
                          ctx=Load(),
                          lineno=59,
                          col_offset=31,
                          end_lineno=59,
                          end_col_offset=46),
                        args=[],
                        keywords=[
                          keyword(
                            arg='block',
                            value=Name(
                              id='block',
                              ctx=Load(),
                              lineno=59,
                              col_offset=53,
                              end_lineno=59,
                              end_col_offset=58),
                            lineno=59,
                            col_offset=47,
                            end_lineno=59,
                            end_col_offset=58),
                          keyword(
                            arg='indent',
                            value=Name(
                              id='indent',
                              ctx=Load(),
                              lineno=59,
                              col_offset=67,
                              end_lineno=59,
                              end_col_offset=73),
                            lineno=59,
                            col_offset=60,
                            end_lineno=59,
                            end_col_offset=73)],
                        lineno=59,
                        col_offset=31,
                        end_lineno=59,
                        end_col_offset=74),
                      lineno=59,
                      col_offset=12,
                      end_lineno=59,
                      end_col_offset=74)],
                  orelse=[],
                  lineno=57,
                  col_offset=8,
                  end_lineno=59,
                  end_col_offset=74)],
              lineno=54,
              col_offset=8,
              end_lineno=59,
              end_col_offset=74)],
          orelse=[],
          lineno=53,
          col_offset=4,
          end_lineno=59,
          end_col_offset=74),
        Return(
          value=Name(
            id='connection_text',
            ctx=Load(),
            lineno=61,
            col_offset=11,
            end_lineno=61,
            end_col_offset=26),
          lineno=61,
          col_offset=4,
          end_lineno=61,
          end_col_offset=26)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=51,
        col_offset=78,
        end_lineno=51,
        end_col_offset=81),
      lineno=51,
      col_offset=0,
      end_lineno=61,
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
              lineno=64,
              col_offset=27,
              end_lineno=64,
              end_col_offset=39),
            lineno=64,
            col_offset=20,
            end_lineno=64,
            end_col_offset=39),
          arg(
            arg='indent',
            annotation=Name(
              id='int',
              ctx=Load(),
              lineno=64,
              col_offset=49,
              end_lineno=64,
              end_col_offset=52),
            lineno=64,
            col_offset=41,
            end_lineno=64,
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
              lineno=65,
              col_offset=4,
              end_lineno=65,
              end_col_offset=14)],
          value=Constant(
            value='',
            lineno=65,
            col_offset=17,
            end_lineno=65,
            end_col_offset=19),
          lineno=65,
          col_offset=4,
          end_lineno=65,
          end_col_offset=19),
        If(
          test=Call(
            func=Name(
              id='isinstance',
              ctx=Load(),
              lineno=66,
              col_offset=7,
              end_lineno=66,
              end_col_offset=17),
            args=[
              Name(
                id='block',
                ctx=Load(),
                lineno=66,
                col_offset=18,
                end_lineno=66,
                end_col_offset=23),
              Name(
                id='MermaidFunction',
                ctx=Load(),
                lineno=66,
                col_offset=25,
                end_lineno=66,
                end_col_offset=40)],
            keywords=[],
            lineno=66,
            col_offset=7,
            end_lineno=66,
            end_col_offset=41),
          body=[
            AnnAssign(
              target=Name(
                id='function_def',
                ctx=Store(),
                lineno=67,
                col_offset=8,
                end_lineno=67,
                end_col_offset=20),
              annotation=Name(
                id='MermaidFunction',
                ctx=Load(),
                lineno=67,
                col_offset=23,
                end_lineno=67,
                end_col_offset=38),
              value=Name(
                id='block',
                ctx=Load(),
                lineno=67,
                col_offset=41,
                end_lineno=67,
                end_col_offset=46),
              simple=1,
              lineno=67,
              col_offset=8,
              end_lineno=67,
              end_col_offset=46),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=68,
                col_offset=8,
                end_lineno=68,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=68,
                        col_offset=25,
                        end_lineno=68,
                        end_col_offset=28),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=68,
                        col_offset=31,
                        end_lineno=68,
                        end_col_offset=37),
                      lineno=68,
                      col_offset=25,
                      end_lineno=68,
                      end_col_offset=37),
                    conversion=-1,
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=77),
                  Constant(
                    value='subgraph ',
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=77),
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='function_def',
                        ctx=Load(),
                        lineno=68,
                        col_offset=48,
                        end_lineno=68,
                        end_col_offset=60),
                      attr='display_name',
                      ctx=Load(),
                      lineno=68,
                      col_offset=48,
                      end_lineno=68,
                      end_col_offset=73),
                    conversion=-1,
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=77),
                  Constant(
                    value='\n',
                    lineno=68,
                    col_offset=22,
                    end_lineno=68,
                    end_col_offset=77)],
                lineno=68,
                col_offset=22,
                end_lineno=68,
                end_col_offset=77),
              lineno=68,
              col_offset=8,
              end_lineno=68,
              end_col_offset=77),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=69,
                        col_offset=25,
                        end_lineno=69,
                        end_col_offset=28),
                      op=Mult(),
                      right=BinOp(
                        left=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=69,
                          col_offset=32,
                          end_lineno=69,
                          end_col_offset=38),
                        op=Add(),
                        right=Constant(
                          value=1,
                          lineno=69,
                          col_offset=41,
                          end_lineno=69,
                          end_col_offset=42),
                        lineno=69,
                        col_offset=32,
                        end_lineno=69,
                        end_col_offset=42),
                      lineno=69,
                      col_offset=25,
                      end_lineno=69,
                      end_col_offset=43),
                    conversion=-1,
                    lineno=69,
                    col_offset=22,
                    end_lineno=69,
                    end_col_offset=59),
                  Constant(
                    value='direction TB\n',
                    lineno=69,
                    col_offset=22,
                    end_lineno=69,
                    end_col_offset=59)],
                lineno=69,
                col_offset=22,
                end_lineno=69,
                end_col_offset=59),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=59),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=70,
                col_offset=8,
                end_lineno=70,
                end_col_offset=18),
              op=Add(),
              value=Call(
                func=Name(
                  id='_get_flow_connections',
                  ctx=Load(),
                  lineno=70,
                  col_offset=22,
                  end_lineno=70,
                  end_col_offset=43),
                args=[
                  Attribute(
                    value=Name(
                      id='function_def',
                      ctx=Load(),
                      lineno=70,
                      col_offset=44,
                      end_lineno=70,
                      end_col_offset=56),
                    attr='block_contents',
                    ctx=Load(),
                    lineno=70,
                    col_offset=44,
                    end_lineno=70,
                    end_col_offset=71),
                  BinOp(
                    left=Name(
                      id='indent',
                      ctx=Load(),
                      lineno=70,
                      col_offset=73,
                      end_lineno=70,
                      end_col_offset=79),
                    op=Add(),
                    right=Constant(
                      value=1,
                      lineno=70,
                      col_offset=82,
                      end_lineno=70,
                      end_col_offset=83),
                    lineno=70,
                    col_offset=73,
                    end_lineno=70,
                    end_col_offset=83)],
                keywords=[],
                lineno=70,
                col_offset=22,
                end_lineno=70,
                end_col_offset=84),
              lineno=70,
              col_offset=8,
              end_lineno=70,
              end_col_offset=84),
            AugAssign(
              target=Name(
                id='block_text',
                ctx=Store(),
                lineno=71,
                col_offset=8,
                end_lineno=71,
                end_col_offset=18),
              op=Add(),
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=BinOp(
                      left=Name(
                        id='TAB',
                        ctx=Load(),
                        lineno=71,
                        col_offset=25,
                        end_lineno=71,
                        end_col_offset=28),
                      op=Mult(),
                      right=Name(
                        id='indent',
                        ctx=Load(),
                        lineno=71,
                        col_offset=31,
                        end_lineno=71,
                        end_col_offset=37),
                      lineno=71,
                      col_offset=25,
                      end_lineno=71,
                      end_col_offset=37),
                    conversion=-1,
                    lineno=71,
                    col_offset=22,
                    end_lineno=71,
                    end_col_offset=44),
                  Constant(
                    value='end\n',
                    lineno=71,
                    col_offset=22,
                    end_lineno=71,
                    end_col_offset=44)],
                lineno=71,
                col_offset=22,
                end_lineno=71,
                end_col_offset=44),
              lineno=71,
              col_offset=8,
              end_lineno=71,
              end_col_offset=44)],
          orelse=[
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=72,
                  col_offset=9,
                  end_lineno=72,
                  end_col_offset=19),
                args=[
                  Name(
                    id='block',
                    ctx=Load(),
                    lineno=72,
                    col_offset=20,
                    end_lineno=72,
                    end_col_offset=25),
                  Name(
                    id='MermaidClass',
                    ctx=Load(),
                    lineno=72,
                    col_offset=27,
                    end_lineno=72,
                    end_col_offset=39)],
                keywords=[],
                lineno=72,
                col_offset=9,
                end_lineno=72,
                end_col_offset=40),
              body=[
                AnnAssign(
                  target=Name(
                    id='class_def',
                    ctx=Store(),
                    lineno=73,
                    col_offset=8,
                    end_lineno=73,
                    end_col_offset=17),
                  annotation=Name(
                    id='MermaidClass',
                    ctx=Load(),
                    lineno=73,
                    col_offset=20,
                    end_lineno=73,
                    end_col_offset=32),
                  value=Name(
                    id='block',
                    ctx=Load(),
                    lineno=73,
                    col_offset=35,
                    end_lineno=73,
                    end_col_offset=40),
                  simple=1,
                  lineno=73,
                  col_offset=8,
                  end_lineno=73,
                  end_col_offset=40),
                AugAssign(
                  target=Name(
                    id='block_text',
                    ctx=Store(),
                    lineno=74,
                    col_offset=8,
                    end_lineno=74,
                    end_col_offset=18),
                  op=Add(),
                  value=JoinedStr(
                    values=[
                      FormattedValue(
                        value=BinOp(
                          left=Name(
                            id='TAB',
                            ctx=Load(),
                            lineno=74,
                            col_offset=25,
                            end_lineno=74,
                            end_col_offset=28),
                          op=Mult(),
                          right=Name(
                            id='indent',
                            ctx=Load(),
                            lineno=74,
                            col_offset=31,
                            end_lineno=74,
                            end_col_offset=37),
                          lineno=74,
                          col_offset=25,
                          end_lineno=74,
                          end_col_offset=37),
                        conversion=-1,
                        lineno=74,
                        col_offset=22,
                        end_lineno=74,
                        end_col_offset=74),
                      Constant(
                        value='subgraph ',
                        lineno=74,
                        col_offset=22,
                        end_lineno=74,
                        end_col_offset=74),
                      FormattedValue(
                        value=Attribute(
                          value=Name(
                            id='class_def',
                            ctx=Load(),
                            lineno=74,
                            col_offset=48,
                            end_lineno=74,
                            end_col_offset=57),
                          attr='display_name',
                          ctx=Load(),
                          lineno=74,
                          col_offset=48,
                          end_lineno=74,
                          end_col_offset=70),
                        conversion=-1,
                        lineno=74,
                        col_offset=22,
                        end_lineno=74,
                        end_col_offset=74),
                      Constant(
                        value='\n',
                        lineno=74,
                        col_offset=22,
                        end_lineno=74,
                        end_col_offset=74)],
                    lineno=74,
                    col_offset=22,
                    end_lineno=74,
                    end_col_offset=74),
                  lineno=74,
                  col_offset=8,
                  end_lineno=74,
                  end_col_offset=74),
                AugAssign(
                  target=Name(
                    id='block_text',
                    ctx=Store(),
                    lineno=75,
                    col_offset=8,
                    end_lineno=75,
                    end_col_offset=18),
                  op=Add(),
                  value=JoinedStr(
                    values=[
                      FormattedValue(
                        value=BinOp(
                          left=Name(
                            id='TAB',
                            ctx=Load(),
                            lineno=75,
                            col_offset=25,
                            end_lineno=75,
                            end_col_offset=28),
                          op=Mult(),
                          right=BinOp(
                            left=Name(
                              id='indent',
                              ctx=Load(),
                              lineno=75,
                              col_offset=32,
                              end_lineno=75,
                              end_col_offset=38),
                            op=Add(),
                            right=Constant(
                              value=1,
                              lineno=75,
                              col_offset=41,
                              end_lineno=75,
                              end_col_offset=42),
                            lineno=75,
                            col_offset=32,
                            end_lineno=75,
                            end_col_offset=42),
                          lineno=75,
                          col_offset=25,
                          end_lineno=75,
                          end_col_offset=43),
                        conversion=-1,
                        lineno=75,
                        col_offset=22,
                        end_lineno=75,
                        end_col_offset=59),
                      Constant(
                        value='direction TB\n',
                        lineno=75,
                        col_offset=22,
                        end_lineno=75,
                        end_col_offset=59)],
                    lineno=75,
                    col_offset=22,
                    end_lineno=75,
                    end_col_offset=59),
                  lineno=75,
                  col_offset=8,
                  end_lineno=75,
                  end_col_offset=59),
                AugAssign(
                  target=Name(
                    id='block_text',
                    ctx=Store(),
                    lineno=76,
                    col_offset=8,
                    end_lineno=76,
                    end_col_offset=18),
                  op=Add(),
                  value=Call(
                    func=Name(
                      id='_get_flow_connections',
                      ctx=Load(),
                      lineno=76,
                      col_offset=22,
                      end_lineno=76,
                      end_col_offset=43),
                    args=[
                      Attribute(
                        value=Name(
                          id='class_def',
                          ctx=Load(),
                          lineno=76,
                          col_offset=44,
                          end_lineno=76,
                          end_col_offset=53),
                        attr='block_contents',
                        ctx=Load(),
                        lineno=76,
                        col_offset=44,
                        end_lineno=76,
                        end_col_offset=68),
                      BinOp(
                        left=Name(
                          id='indent',
                          ctx=Load(),
                          lineno=76,
                          col_offset=70,
                          end_lineno=76,
                          end_col_offset=76),
                        op=Add(),
                        right=Constant(
                          value=1,
                          lineno=76,
                          col_offset=79,
                          end_lineno=76,
                          end_col_offset=80),
                        lineno=76,
                        col_offset=70,
                        end_lineno=76,
                        end_col_offset=80)],
                    keywords=[],
                    lineno=76,
                    col_offset=22,
                    end_lineno=76,
                    end_col_offset=81),
                  lineno=76,
                  col_offset=8,
                  end_lineno=76,
                  end_col_offset=81),
                AugAssign(
                  target=Name(
                    id='block_text',
                    ctx=Store(),
                    lineno=77,
                    col_offset=8,
                    end_lineno=77,
                    end_col_offset=18),
                  op=Add(),
                  value=JoinedStr(
                    values=[
                      FormattedValue(
                        value=BinOp(
                          left=Name(
                            id='TAB',
                            ctx=Load(),
                            lineno=77,
                            col_offset=25,
                            end_lineno=77,
                            end_col_offset=28),
                          op=Mult(),
                          right=Name(
                            id='indent',
                            ctx=Load(),
                            lineno=77,
                            col_offset=31,
                            end_lineno=77,
                            end_col_offset=37),
                          lineno=77,
                          col_offset=25,
                          end_lineno=77,
                          end_col_offset=37),
                        conversion=-1,
                        lineno=77,
                        col_offset=22,
                        end_lineno=77,
                        end_col_offset=44),
                      Constant(
                        value='end\n',
                        lineno=77,
                        col_offset=22,
                        end_lineno=77,
                        end_col_offset=44)],
                    lineno=77,
                    col_offset=22,
                    end_lineno=77,
                    end_col_offset=44),
                  lineno=77,
                  col_offset=8,
                  end_lineno=77,
                  end_col_offset=44)],
              orelse=[
                AugAssign(
                  target=Name(
                    id='block_text',
                    ctx=Store(),
                    lineno=79,
                    col_offset=8,
                    end_lineno=79,
                    end_col_offset=18),
                  op=Add(),
                  value=Call(
                    func=Name(
                      id='_get_flow_connections',
                      ctx=Load(),
                      lineno=79,
                      col_offset=22,
                      end_lineno=79,
                      end_col_offset=43),
                    args=[
                      Attribute(
                        value=Name(
                          id='block',
                          ctx=Load(),
                          lineno=79,
                          col_offset=44,
                          end_lineno=79,
                          end_col_offset=49),
                        attr='block_contents',
                        ctx=Load(),
                        lineno=79,
                        col_offset=44,
                        end_lineno=79,
                        end_col_offset=64),
                      Name(
                        id='indent',
                        ctx=Load(),
                        lineno=79,
                        col_offset=66,
                        end_lineno=79,
                        end_col_offset=72)],
                    keywords=[],
                    lineno=79,
                    col_offset=22,
                    end_lineno=79,
                    end_col_offset=73),
                  lineno=79,
                  col_offset=8,
                  end_lineno=79,
                  end_col_offset=73)],
              lineno=72,
              col_offset=4,
              end_lineno=79,
              end_col_offset=73)],
          lineno=66,
          col_offset=4,
          end_lineno=79,
          end_col_offset=73),
        Return(
          value=Name(
            id='block_text',
            ctx=Load(),
            lineno=80,
            col_offset=11,
            end_lineno=80,
            end_col_offset=21),
          lineno=80,
          col_offset=4,
          end_lineno=80,
          end_col_offset=21)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=64,
        col_offset=57,
        end_lineno=64,
        end_col_offset=60),
      lineno=64,
      col_offset=0,
      end_lineno=80,
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
                lineno=83,
                col_offset=51,
                end_lineno=83,
                end_col_offset=55),
              slice=Name(
                id='MermaidElement',
                ctx=Load(),
                lineno=83,
                col_offset=56,
                end_lineno=83,
                end_col_offset=70),
              ctx=Load(),
              lineno=83,
              col_offset=51,
              end_lineno=83,
              end_col_offset=71),
            lineno=83,
            col_offset=41,
            end_lineno=83,
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
              lineno=84,
              col_offset=4,
              end_lineno=84,
              end_col_offset=11)],
          value=Call(
            func=Name(
              id='_get_aliases_for_safe_names',
              ctx=Load(),
              lineno=84,
              col_offset=14,
              end_lineno=84,
              end_col_offset=41),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=84,
                  col_offset=51,
                  end_lineno=84,
                  end_col_offset=59),
                lineno=84,
                col_offset=42,
                end_lineno=84,
                end_col_offset=59)],
            lineno=84,
            col_offset=14,
            end_lineno=84,
            end_col_offset=60),
          lineno=84,
          col_offset=4,
          end_lineno=84,
          end_col_offset=60),
        Assign(
          targets=[
            Name(
              id='flow_connections',
              ctx=Store(),
              lineno=85,
              col_offset=4,
              end_lineno=85,
              end_col_offset=20)],
          value=Call(
            func=Name(
              id='_get_flow_connections',
              ctx=Load(),
              lineno=85,
              col_offset=23,
              end_lineno=85,
              end_col_offset=44),
            args=[],
            keywords=[
              keyword(
                arg='elements',
                value=Name(
                  id='elements',
                  ctx=Load(),
                  lineno=85,
                  col_offset=54,
                  end_lineno=85,
                  end_col_offset=62),
                lineno=85,
                col_offset=45,
                end_lineno=85,
                end_col_offset=62)],
            lineno=85,
            col_offset=23,
            end_lineno=85,
            end_col_offset=63),
          lineno=85,
          col_offset=4,
          end_lineno=85,
          end_col_offset=63),
        Return(
          value=JoinedStr(
            values=[
              Constant(
                value='```mermaid\nflowchart TB\n',
                lineno=87,
                col_offset=8,
                end_lineno=91,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='alaises',
                  ctx=Load(),
                  lineno=89,
                  col_offset=11,
                  end_lineno=89,
                  end_col_offset=18),
                conversion=-1,
                lineno=87,
                col_offset=8,
                end_lineno=91,
                end_col_offset=15),
              Constant(
                value='\n',
                lineno=87,
                col_offset=8,
                end_lineno=91,
                end_col_offset=15),
              FormattedValue(
                value=Name(
                  id='flow_connections',
                  ctx=Load(),
                  lineno=90,
                  col_offset=11,
                  end_lineno=90,
                  end_col_offset=27),
                conversion=-1,
                lineno=87,
                col_offset=8,
                end_lineno=91,
                end_col_offset=15),
              Constant(
                value='\n```\n',
                lineno=87,
                col_offset=8,
                end_lineno=91,
                end_col_offset=15)],
            lineno=87,
            col_offset=8,
            end_lineno=91,
            end_col_offset=15),
          lineno=86,
          col_offset=4,
          end_lineno=92,
          end_col_offset=5)],
      decorator_list=[],
      returns=Name(
        id='str',
        ctx=Load(),
        lineno=83,
        col_offset=76,
        end_lineno=83,
        end_col_offset=79),
      lineno=83,
      col_offset=0,
      end_lineno=92,
      end_col_offset=5)],
  type_ignores=[])
```
</details>

