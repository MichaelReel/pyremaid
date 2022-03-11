# ./src/pyremaid/ast_tools/visitors.py

### Imports

  - ast.AST
  - ast.ClassDef
  - ast.For
  - ast.FunctionDef
  - ast.Import
  - ast.ImportFrom
  - ast.Module
  - ast.NodeVisitor
  - ast.unparse
  - [models.MermaidClass](/docs/pyremaid/models.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)
  - [models.MermaidFor](/docs/pyremaid/models.py.md)
  - [models.MermaidFunction](/docs/pyremaid/models.py.md)
  - [models.MermaidLink](/docs/pyremaid/models.py.md)
  - [models.MermaidModule](/docs/pyremaid/models.py.md)
  - [models.MermaidNode](/docs/pyremaid/models.py.md)
  - typing.Any
  - typing.Optional

---
```mermaid
flowchart TB
  _c31_f32_n943["AnnAssign"]
  _c31_f32_n944["Attribute"]
  _c31_f32_n945["Name"]
  _c31_f32_n946["Load"]
  _c31_f32_n947["Store"]
  _c31_f32_n948["Subscript"]
  _c31_f32_n949["Name"]
  _c31_f32_n950["Load"]
  _c31_f32_n951["Name"]
  _c31_f32_n952["Load"]
  _c31_f32_n953["Load"]
  _c31_f32_n954["List"]
  _c31_f32_n955["Load"]
  _c31_f33_l34_n956["Expr"]
  _c31_f33_l34_n957["Call"]
  _c31_f33_l34_n958["Attribute"]
  _c31_f33_l34_n959["Attribute"]
  _c31_f33_l34_n960["Name"]
  _c31_f33_l34_n961["Load"]
  _c31_f33_l34_n962["Load"]
  _c31_f33_l34_n963["Load"]
  _c31_f33_l34_n964["JoinedStr"]
  _c31_f33_l34_n965["FormattedValue"]
  _c31_f33_l34_n966["Attribute"]
  _c31_f33_l34_n967["Name"]
  _c31_f33_l34_n968["Load"]
  _c31_f33_l34_n969["Load"]
  _c31_f33_l34_n970["Constant"]
  _c31_f35_n971["Assign"]
  _c31_f35_n972["Name"]
  _c31_f35_n973["Store"]
  _c31_f35_n974["Attribute"]
  _c31_f35_n975["Name"]
  _c31_f35_n976["Load"]
  _c31_f35_n977["Load"]
  _c31_f35_l36["i"]
  _c31_f35_l36_n978["Expr"]
  _c31_f35_l36_n979["Call"]
  _c31_f35_l36_n980["Attribute"]
  _c31_f35_l36_n981["Attribute"]
  _c31_f35_l36_n982["Name"]
  _c31_f35_l36_n983["Load"]
  _c31_f35_l36_n984["Load"]
  _c31_f35_l36_n985["Load"]
  _c31_f35_l36_n986["JoinedStr"]
  _c31_f35_l36_n987["FormattedValue"]
  _c31_f35_l36_n988["Name"]
  _c31_f35_l36_n989["Load"]
  _c31_f35_l36_n990["Constant"]
  _c31_f35_l36_n991["FormattedValue"]
  _c31_f35_l36_n992["Attribute"]
  _c31_f35_l36_n993["Name"]
  _c31_f35_l36_n994["Load"]
  _c31_f35_l36_n995["Load"]
  _c31_f37_n996["Return"]
  _c31_f37_n997["Attribute"]
  _c31_f37_n998["Name"]
  _c31_f37_n999["Load"]
  _c31_f37_n1000["Load"]
  _c38_n1001["AnnAssign"]
  _c38_n1002["Name"]
  _c38_n1003["Store"]
  _c38_n1004["Name"]
  _c38_n1005["Load"]
  _c38_n1006["Constant"]
  _c38_f39_n1007["AnnAssign"]
  _c38_f39_n1008["Attribute"]
  _c38_f39_n1009["Name"]
  _c38_f39_n1010["Load"]
  _c38_f39_n1011["Store"]
  _c38_f39_n1012["Subscript"]
  _c38_f39_n1013["Name"]
  _c38_f39_n1014["Load"]
  _c38_f39_n1015["Name"]
  _c38_f39_n1016["Load"]
  _c38_f39_n1017["Load"]
  _c38_f39_n1018["List"]
  _c38_f39_n1019["Load"]
  _c38_f39_n1020["AnnAssign"]
  _c38_f39_n1021["Attribute"]
  _c38_f39_n1022["Name"]
  _c38_f39_n1023["Load"]
  _c38_f39_n1024["Store"]
  _c38_f39_n1025["Subscript"]
  _c38_f39_n1026["Name"]
  _c38_f39_n1027["Load"]
  _c38_f39_n1028["Name"]
  _c38_f39_n1029["Load"]
  _c38_f39_n1030["Load"]
  _c38_f39_n1031["Constant"]
  _c38_f39_n1032["Assign"]
  _c38_f39_n1033["Attribute"]
  _c38_f39_n1034["Name"]
  _c38_f39_n1035["Load"]
  _c38_f39_n1036["Store"]
  _c38_f39_n1037["Name"]
  _c38_f39_n1038["Load"]
  _c38_f40_n1039["Assign"]
  _c38_f40_n1040["Name"]
  _c38_f40_n1041["Store"]
  _c38_f40_n1042["Attribute"]
  _c38_f40_n1043["Name"]
  _c38_f40_n1044["Load"]
  _c38_f40_n1045["Load"]
  _c38_f40_n1046["AugAssign"]
  _c38_f40_n1047["Attribute"]
  _c38_f40_n1048["Name"]
  _c38_f40_n1049["Load"]
  _c38_f40_n1050["Store"]
  _c38_f40_n1051["Add"]
  _c38_f40_n1052["Constant"]
  _c38_f40_n1053["Return"]
  _c38_f40_n1054["Name"]
  _c38_f40_n1055["Load"]
  _c38_f43_n1058["Assign"]
  _c38_f43_n1059["Name"]
  _c38_f43_n1060["Store"]
  _c38_f43_n1061["Call"]
  _c38_f43_n1062["Name"]
  _c38_f43_n1063["Load"]
  _c38_f43_n1064["keyword"]
  _c38_f43_n1065["Attribute"]
  _c38_f43_n1066["Name"]
  _c38_f43_n1067["Load"]
  _c38_f43_n1068["Load"]
  _c38_f43_n1069["Expr"]
  _c38_f43_n1070["Call"]
  _c38_f43_n1071["Attribute"]
  _c38_f43_n1072["Name"]
  _c38_f43_n1073["Load"]
  _c38_f43_n1074["Load"]
  _c38_f43_n1075["Name"]
  _c38_f43_n1076["Load"]
  _c38_f43_n1077["Expr"]
  _c38_f43_n1078["Call"]
  _c38_f43_n1079["Attribute"]
  _c38_f43_n1080["Attribute"]
  _c38_f43_n1081["Name"]
  _c38_f43_n1082["Load"]
  _c38_f43_n1083["Load"]
  _c38_f43_n1084["Load"]
  _c38_f43_n1085["Call"]
  _c38_f43_n1086["Attribute"]
  _c38_f43_n1087["Name"]
  _c38_f43_n1088["Load"]
  _c38_f43_n1089["Load"]
  _c38_f44_n1090["Assign"]
  _c38_f44_n1091["Name"]
  _c38_f44_n1092["Store"]
  _c38_f44_n1093["Call"]
  _c38_f44_n1094["Name"]
  _c38_f44_n1095["Load"]
  _c38_f44_n1096["keyword"]
  _c38_f44_n1097["Attribute"]
  _c38_f44_n1098["Name"]
  _c38_f44_n1099["Load"]
  _c38_f44_n1100["Load"]
  _c38_f44_n1101["Expr"]
  _c38_f44_n1102["Call"]
  _c38_f44_n1103["Attribute"]
  _c38_f44_n1104["Name"]
  _c38_f44_n1105["Load"]
  _c38_f44_n1106["Load"]
  _c38_f44_n1107["Name"]
  _c38_f44_n1108["Load"]
  _c38_f44_n1109["Expr"]
  _c38_f44_n1110["Call"]
  _c38_f44_n1111["Attribute"]
  _c38_f44_n1112["Attribute"]
  _c38_f44_n1113["Name"]
  _c38_f44_n1114["Load"]
  _c38_f44_n1115["Load"]
  _c38_f44_n1116["Load"]
  _c38_f44_n1117["Call"]
  _c38_f44_n1118["Attribute"]
  _c38_f44_n1119["Name"]
  _c38_f44_n1120["Load"]
  _c38_f44_n1121["Load"]
  _c38_f45_n1122["Assign"]
  _c38_f45_n1123["Name"]
  _c38_f45_n1124["Store"]
  _c38_f45_n1125["Call"]
  _c38_f45_n1126["Name"]
  _c38_f45_n1127["Load"]
  _c38_f45_n1128["keyword"]
  _c38_f45_n1129["Attribute"]
  _c38_f45_n1130["Name"]
  _c38_f45_n1131["Load"]
  _c38_f45_n1132["Load"]
  _c38_f45_n1133["Expr"]
  _c38_f45_n1134["Call"]
  _c38_f45_n1135["Attribute"]
  _c38_f45_n1136["Name"]
  _c38_f45_n1137["Load"]
  _c38_f45_n1138["Load"]
  _c38_f45_n1139["Name"]
  _c38_f45_n1140["Load"]
  _c38_f45_n1141["Assign"]
  _c38_f45_n1142["Name"]
  _c38_f45_n1143["Store"]
  _c38_f45_n1144["Call"]
  _c38_f45_n1145["Attribute"]
  _c38_f45_n1146["Name"]
  _c38_f45_n1147["Load"]
  _c38_f45_n1148["Load"]
  _c38_f45_n1149["Assign"]
  _c38_f45_n1150["Name"]
  _c38_f45_n1151["Store"]
  _c38_f45_n1152["Subscript"]
  _c38_f45_n1153["Name"]
  _c38_f45_n1154["Load"]
  _c38_f45_n1155["Constant"]
  _c38_f45_n1156["Load"]
  _c38_f45_n1157["If"]
  _c38_f45_n1158["Call"]
  _c38_f45_n1159["Name"]
  _c38_f45_n1160["Load"]
  _c38_f45_n1161["Name"]
  _c38_f45_n1162["Load"]
  _c38_f45_n1163["Name"]
  _c38_f45_n1164["Load"]
  _c38_f45_n1165["Assign"]
  _c38_f45_n1166["Name"]
  _c38_f45_n1167["Store"]
  _c38_f45_n1168["Attribute"]
  _c38_f45_n1169["Name"]
  _c38_f45_n1170["Load"]
  _c38_f45_n1171["Load"]
  _c38_f45_n1172["Assign"]
  _c38_f45_n1173["Name"]
  _c38_f45_n1174["Store"]
  _c38_f45_n1175["Subscript"]
  _c38_f45_n1176["Name"]
  _c38_f45_n1177["Load"]
  _c38_f45_n1178["UnaryOp"]
  _c38_f45_n1179["USub"]
  _c38_f45_n1180["Constant"]
  _c38_f45_n1181["Load"]
  _c38_f45_n1182["If"]
  _c38_f45_n1183["Call"]
  _c38_f45_n1184["Name"]
  _c38_f45_n1185["Load"]
  _c38_f45_n1186["Name"]
  _c38_f45_n1187["Load"]
  _c38_f45_n1188["Name"]
  _c38_f45_n1189["Load"]
  _c38_f45_n1190["Assign"]
  _c38_f45_n1191["Name"]
  _c38_f45_n1192["Store"]
  _c38_f45_n1193["Attribute"]
  _c38_f45_n1194["Name"]
  _c38_f45_n1195["Load"]
  _c38_f45_n1196["Load"]
  _c38_f45_n1197["If"]
  _c38_f45_n1198["Attribute"]
  _c38_f45_n1199["Name"]
  _c38_f45_n1200["Load"]
  _c38_f45_n1201["Load"]
  _c38_f45_n1202["Expr"]
  _c38_f45_n1203["Call"]
  _c38_f45_n1204["Attribute"]
  _c38_f45_n1205["Attribute"]
  _c38_f45_n1206["Name"]
  _c38_f45_n1207["Load"]
  _c38_f45_n1208["Load"]
  _c38_f45_n1209["Load"]
  _c38_f45_n1210["Call"]
  _c38_f45_n1211["Name"]
  _c38_f45_n1212["Load"]
  _c38_f45_n1213["keyword"]
  _c38_f45_n1214["Attribute"]
  _c38_f45_n1215["Name"]
  _c38_f45_n1216["Load"]
  _c38_f45_n1217["Load"]
  _c38_f45_n1218["keyword"]
  _c38_f45_n1219["Name"]
  _c38_f45_n1220["Load"]
  _c38_f45_n1221["Expr"]
  _c38_f45_n1222["Call"]
  _c38_f45_n1223["Attribute"]
  _c38_f45_n1224["Attribute"]
  _c38_f45_n1225["Name"]
  _c38_f45_n1226["Load"]
  _c38_f45_n1227["Load"]
  _c38_f45_n1228["Load"]
  _c38_f45_n1229["Name"]
  _c38_f45_n1230["Load"]
  _c38_f45_n1231["Assign"]
  _c38_f45_n1232["Attribute"]
  _c38_f45_n1233["Name"]
  _c38_f45_n1234["Load"]
  _c38_f45_n1235["Store"]
  _c38_f45_n1236["Name"]
  _c38_f45_n1237["Load"]
  _c38_f46_n1238["Assign"]
  _c38_f46_n1239["Name"]
  _c38_f46_n1240["Store"]
  _c38_f46_n1241["Call"]
  _c38_f46_n1242["Name"]
  _c38_f46_n1243["Load"]
  _c38_f46_n1244["keyword"]
  _c38_f46_n1245["Name"]
  _c38_f46_n1246["Load"]
  _c38_f46_n1247["keyword"]
  _c38_f46_n1248["JoinedStr"]
  _c38_f46_n1249["FormattedValue"]
  _c38_f46_n1250["Attribute"]
  _c38_f46_n1251["Name"]
  _c38_f46_n1252["Load"]
  _c38_f46_n1253["Load"]
  _c38_f46_n1254["Constant"]
  _c38_f46_n1255["FormattedValue"]
  _c38_f46_n1256["Call"]
  _c38_f46_n1257["Attribute"]
  _c38_f46_n1258["Name"]
  _c38_f46_n1259["Load"]
  _c38_f46_n1260["Load"]
  _c38_f46_n1261["keyword"]
  _c38_f46_n1262["Attribute"]
  _c38_f46_n1263["Call"]
  _c38_f46_n1264["Name"]
  _c38_f46_n1265["Load"]
  _c38_f46_n1266["Name"]
  _c38_f46_n1267["Load"]
  _c38_f46_n1268["Load"]
  _c38_f46_n1269["If"]
  _c38_f46_n1270["Attribute"]
  _c38_f46_n1271["Name"]
  _c38_f46_n1272["Load"]
  _c38_f46_n1273["Load"]
  _c38_f46_n1274["Expr"]
  _c38_f46_n1275["Call"]
  _c38_f46_n1276["Attribute"]
  _c38_f46_n1277["Attribute"]
  _c38_f46_n1278["Name"]
  _c38_f46_n1279["Load"]
  _c38_f46_n1280["Load"]
  _c38_f46_n1281["Load"]
  _c38_f46_n1282["Call"]
  _c38_f46_n1283["Name"]
  _c38_f46_n1284["Load"]
  _c38_f46_n1285["keyword"]
  _c38_f46_n1286["Attribute"]
  _c38_f46_n1287["Name"]
  _c38_f46_n1288["Load"]
  _c38_f46_n1289["Load"]
  _c38_f46_n1290["keyword"]
  _c38_f46_n1291["Name"]
  _c38_f46_n1292["Load"]
  _c38_f46_n1293["Assign"]
  _c38_f46_n1294["Attribute"]
  _c38_f46_n1295["Name"]
  _c38_f46_n1296["Load"]
  _c38_f46_n1297["Store"]
  _c38_f46_n1298["Name"]
  _c38_f46_n1299["Load"]
  _c38_f46_n1300["Return"]
  _c38_f46_n1301["Call"]
  _c38_f46_n1302["Attribute"]
  _c38_f46_n1303["Call"]
  _c38_f46_n1304["Name"]
  _c38_f46_n1305["Load"]
  _c38_f46_n1306["Load"]
  _c38_f46_n1307["Name"]
  _c38_f46_n1308["Load"]
  _c38_f47_n1309["Return"]
  _c38_f47_n1310["Attribute"]
  _c38_f47_n1311["Name"]
  _c38_f47_n1312["Load"]
  _c38_f47_n1313["Load"]
  _c48_n1314["AnnAssign"]
  _c48_n1315["Name"]
  _c48_n1316["Store"]
  _c48_n1317["Name"]
  _c48_n1318["Load"]
  _c48_n1319["Constant"]
  _c48_f49_n1320["AnnAssign"]
  _c48_f49_n1321["Attribute"]
  _c48_f49_n1322["Name"]
  _c48_f49_n1323["Load"]
  _c48_f49_n1324["Store"]
  _c48_f49_n1325["Subscript"]
  _c48_f49_n1326["Name"]
  _c48_f49_n1327["Load"]
  _c48_f49_n1328["Name"]
  _c48_f49_n1329["Load"]
  _c48_f49_n1330["Load"]
  _c48_f49_n1331["List"]
  _c48_f49_n1332["Load"]
  _c48_f49_n1333["Assign"]
  _c48_f49_n1334["Attribute"]
  _c48_f49_n1335["Name"]
  _c48_f49_n1336["Load"]
  _c48_f49_n1337["Store"]
  _c48_f49_n1338["Name"]
  _c48_f49_n1339["Load"]
  _c48_f50_n1340["Assign"]
  _c48_f50_n1341["Name"]
  _c48_f50_n1342["Store"]
  _c48_f50_n1343["Attribute"]
  _c48_f50_n1344["Name"]
  _c48_f50_n1345["Load"]
  _c48_f50_n1346["Load"]
  _c48_f50_n1347["AugAssign"]
  _c48_f50_n1348["Attribute"]
  _c48_f50_n1349["Name"]
  _c48_f50_n1350["Load"]
  _c48_f50_n1351["Store"]
  _c48_f50_n1352["Add"]
  _c48_f50_n1353["Constant"]
  _c48_f50_n1354["Return"]
  _c48_f50_n1355["Name"]
  _c48_f50_n1356["Load"]
  _c48_f51_n1357["Expr"]
  _c48_f51_n1358["Constant"]
  _c48_f51_n1359["Assign"]
  _c48_f51_n1360["Name"]
  _c48_f51_n1361["Store"]
  _c48_f51_n1362["Call"]
  _c48_f51_n1363["Name"]
  _c48_f51_n1364["Load"]
  _c48_f51_l52["sub_element"]
  _c48_f51_l52_n1365["Expr"]
  _c48_f51_l52_n1366["Call"]
  _c48_f51_l52_n1367["Attribute"]
  _c48_f51_l52_n1368["Name"]
  _c48_f51_l52_n1369["Load"]
  _c48_f51_l52_n1370["Load"]
  _c48_f51_l52_n1371["keyword"]
  _c48_f51_l52_n1372["Name"]
  _c48_f51_l52_n1373["Load"]
  _c48_f51_n1374["Assign"]
  _c48_f51_n1375["Name"]
  _c48_f51_n1376["Store"]
  _c48_f51_n1377["Call"]
  _c48_f51_n1378["Name"]
  _c48_f51_n1379["Load"]
  _c48_f51_n1380["keyword"]
  _c48_f51_n1381["Name"]
  _c48_f51_n1382["Load"]
  _c48_f51_n1383["keyword"]
  _c48_f51_n1384["JoinedStr"]
  _c48_f51_n1385["FormattedValue"]
  _c48_f51_n1386["Attribute"]
  _c48_f51_n1387["Name"]
  _c48_f51_n1388["Load"]
  _c48_f51_n1389["Load"]
  _c48_f51_n1390["Constant"]
  _c48_f51_n1391["FormattedValue"]
  _c48_f51_n1392["Call"]
  _c48_f51_n1393["Attribute"]
  _c48_f51_n1394["Name"]
  _c48_f51_n1395["Load"]
  _c48_f51_n1396["Load"]
  _c48_f51_n1397["keyword"]
  _c48_f51_n1398["Call"]
  _c48_f51_n1399["Attribute"]
  _c48_f51_n1400["Name"]
  _c48_f51_n1401["Load"]
  _c48_f51_n1402["Load"]
  _c48_f51_n1403["keyword"]
  _c48_f51_n1404["Constant"]
  _c48_f51_n1405["Expr"]
  _c48_f51_n1406["Call"]
  _c48_f51_n1407["Attribute"]
  _c48_f51_n1408["Attribute"]
  _c48_f51_n1409["Name"]
  _c48_f51_n1410["Load"]
  _c48_f51_n1411["Load"]
  _c48_f51_n1412["Load"]
  _c48_f51_n1413["Name"]
  _c48_f51_n1414["Load"]
  _c48_f53_n1415["Expr"]
  _c48_f53_n1416["Constant"]
  _c48_f53_n1417["Assign"]
  _c48_f53_n1418["Name"]
  _c48_f53_n1419["Store"]
  _c48_f53_n1420["JoinedStr"]
  _c48_f53_n1421["FormattedValue"]
  _c48_f53_n1422["Attribute"]
  _c48_f53_n1423["Name"]
  _c48_f53_n1424["Load"]
  _c48_f53_n1425["Load"]
  _c48_f53_n1426["Constant"]
  _c48_f53_n1427["FormattedValue"]
  _c48_f53_n1428["Call"]
  _c48_f53_n1429["Attribute"]
  _c48_f53_n1430["Name"]
  _c48_f53_n1431["Load"]
  _c48_f53_n1432["Load"]
  _c48_f53_n1433["Assign"]
  _c48_f53_n1434["Name"]
  _c48_f53_n1435["Store"]
  _c48_f53_n1436["Call"]
  _c48_f53_n1437["Name"]
  _c48_f53_n1438["Load"]
  _c48_f53_n1439["keyword"]
  _c48_f53_n1440["Name"]
  _c48_f53_n1441["Load"]
  _c48_f53_l54["sub_element"]
  _c48_f53_l54_n1442["Expr"]
  _c48_f53_l54_n1443["Call"]
  _c48_f53_l54_n1444["Attribute"]
  _c48_f53_l54_n1445["Name"]
  _c48_f53_l54_n1446["Load"]
  _c48_f53_l54_n1447["Load"]
  _c48_f53_l54_n1448["keyword"]
  _c48_f53_l54_n1449["Name"]
  _c48_f53_l54_n1450["Load"]
  _c48_f53_n1451["Assign"]
  _c48_f53_n1452["Name"]
  _c48_f53_n1453["Store"]
  _c48_f53_n1454["Call"]
  _c48_f53_n1455["Name"]
  _c48_f53_n1456["Load"]
  _c48_f53_n1457["keyword"]
  _c48_f53_n1458["Name"]
  _c48_f53_n1459["Load"]
  _c48_f53_n1460["keyword"]
  _c48_f53_n1461["Name"]
  _c48_f53_n1462["Load"]
  _c48_f53_n1463["keyword"]
  _c48_f53_n1464["Call"]
  _c48_f53_n1465["Attribute"]
  _c48_f53_n1466["Name"]
  _c48_f53_n1467["Load"]
  _c48_f53_n1468["Load"]
  _c48_f53_n1469["keyword"]
  _c48_f53_n1470["JoinedStr"]
  _c48_f53_n1471["FormattedValue"]
  _c48_f53_n1472["Attribute"]
  _c48_f53_n1473["Name"]
  _c48_f53_n1474["Load"]
  _c48_f53_n1475["Load"]
  _c48_f53_n1476["Constant"]
  _c48_f53_n1477["FormattedValue"]
  _c48_f53_n1478["Attribute"]
  _c48_f53_n1479["Name"]
  _c48_f53_n1480["Load"]
  _c48_f53_n1481["Load"]
  _c48_f53_n1482["Expr"]
  _c48_f53_n1483["Call"]
  _c48_f53_n1484["Attribute"]
  _c48_f53_n1485["Attribute"]
  _c48_f53_n1486["Name"]
  _c48_f53_n1487["Load"]
  _c48_f53_n1488["Load"]
  _c48_f53_n1489["Load"]
  _c48_f53_n1490["Name"]
  _c48_f53_n1491["Load"]
  _c48_f55_n1492["Expr"]
  _c48_f55_n1493["Constant"]
  _c48_f55_n1494["Assign"]
  _c48_f55_n1495["Name"]
  _c48_f55_n1496["Store"]
  _c48_f55_n1497["JoinedStr"]
  _c48_f55_n1498["FormattedValue"]
  _c48_f55_n1499["Attribute"]
  _c48_f55_n1500["Name"]
  _c48_f55_n1501["Load"]
  _c48_f55_n1502["Load"]
  _c48_f55_n1503["Constant"]
  _c48_f55_n1504["FormattedValue"]
  _c48_f55_n1505["Call"]
  _c48_f55_n1506["Attribute"]
  _c48_f55_n1507["Name"]
  _c48_f55_n1508["Load"]
  _c48_f55_n1509["Load"]
  _c48_f55_n1510["Assign"]
  _c48_f55_n1511["Name"]
  _c48_f55_n1512["Store"]
  _c48_f55_n1513["Call"]
  _c48_f55_n1514["Name"]
  _c48_f55_n1515["Load"]
  _c48_f55_n1516["keyword"]
  _c48_f55_n1517["Name"]
  _c48_f55_n1518["Load"]
  _c48_f55_l56["sub_element"]
  _c48_f55_l56_n1519["Expr"]
  _c48_f55_l56_n1520["Call"]
  _c48_f55_l56_n1521["Attribute"]
  _c48_f55_l56_n1522["Name"]
  _c48_f55_l56_n1523["Load"]
  _c48_f55_l56_n1524["Load"]
  _c48_f55_l56_n1525["keyword"]
  _c48_f55_l56_n1526["Name"]
  _c48_f55_l56_n1527["Load"]
  _c48_f55_n1528["Assign"]
  _c48_f55_n1529["Name"]
  _c48_f55_n1530["Store"]
  _c48_f55_n1531["Call"]
  _c48_f55_n1532["Name"]
  _c48_f55_n1533["Load"]
  _c48_f55_n1534["keyword"]
  _c48_f55_n1535["Name"]
  _c48_f55_n1536["Load"]
  _c48_f55_n1537["keyword"]
  _c48_f55_n1538["Name"]
  _c48_f55_n1539["Load"]
  _c48_f55_n1540["keyword"]
  _c48_f55_n1541["Call"]
  _c48_f55_n1542["Attribute"]
  _c48_f55_n1543["Name"]
  _c48_f55_n1544["Load"]
  _c48_f55_n1545["Load"]
  _c48_f55_n1546["keyword"]
  _c48_f55_n1547["Attribute"]
  _c48_f55_n1548["Name"]
  _c48_f55_n1549["Load"]
  _c48_f55_n1550["Load"]
  _c48_f55_n1551["Expr"]
  _c48_f55_n1552["Call"]
  _c48_f55_n1553["Attribute"]
  _c48_f55_n1554["Attribute"]
  _c48_f55_n1555["Name"]
  _c48_f55_n1556["Load"]
  _c48_f55_n1557["Load"]
  _c48_f55_n1558["Load"]
  _c48_f55_n1559["Name"]
  _c48_f55_n1560["Load"]
  _c48_f57_n1561["Expr"]
  _c48_f57_n1562["Constant"]
  _c48_f57_n1563["Assign"]
  _c48_f57_n1564["Name"]
  _c48_f57_n1565["Store"]
  _c48_f57_n1566["JoinedStr"]
  _c48_f57_n1567["FormattedValue"]
  _c48_f57_n1568["Attribute"]
  _c48_f57_n1569["Name"]
  _c48_f57_n1570["Load"]
  _c48_f57_n1571["Load"]
  _c48_f57_n1572["Constant"]
  _c48_f57_n1573["FormattedValue"]
  _c48_f57_n1574["Call"]
  _c48_f57_n1575["Attribute"]
  _c48_f57_n1576["Name"]
  _c48_f57_n1577["Load"]
  _c48_f57_n1578["Load"]
  _c48_f57_n1579["Assign"]
  _c48_f57_n1580["Name"]
  _c48_f57_n1581["Store"]
  _c48_f57_n1582["Call"]
  _c48_f57_n1583["Name"]
  _c48_f57_n1584["Load"]
  _c48_f57_n1585["keyword"]
  _c48_f57_n1586["Name"]
  _c48_f57_n1587["Load"]
  _c48_f57_l58["sub_element"]
  _c48_f57_l58_n1588["Expr"]
  _c48_f57_l58_n1589["Call"]
  _c48_f57_l58_n1590["Attribute"]
  _c48_f57_l58_n1591["Name"]
  _c48_f57_l58_n1592["Load"]
  _c48_f57_l58_n1593["Load"]
  _c48_f57_l58_n1594["keyword"]
  _c48_f57_l58_n1595["Name"]
  _c48_f57_l58_n1596["Load"]
  _c48_f57_n1597["Assign"]
  _c48_f57_n1598["Name"]
  _c48_f57_n1599["Store"]
  _c48_f57_n1600["Call"]
  _c48_f57_n1601["Attribute"]
  _c48_f57_n1602["Name"]
  _c48_f57_n1603["Load"]
  _c48_f57_n1604["Load"]
  _c48_f57_n1605["Assign"]
  _c48_f57_n1606["Name"]
  _c48_f57_n1607["Store"]
  _c48_f57_n1608["Subscript"]
  _c48_f57_n1609["Name"]
  _c48_f57_n1610["Load"]
  _c48_f57_n1611["Constant"]
  _c48_f57_n1612["Load"]
  _c48_f57_n1613["If"]
  _c48_f57_n1614["Call"]
  _c48_f57_n1615["Name"]
  _c48_f57_n1616["Load"]
  _c48_f57_n1617["Name"]
  _c48_f57_n1618["Load"]
  _c48_f57_n1619["Name"]
  _c48_f57_n1620["Load"]
  _c48_f57_n1621["Assign"]
  _c48_f57_n1622["Name"]
  _c48_f57_n1623["Store"]
  _c48_f57_n1624["Attribute"]
  _c48_f57_n1625["Name"]
  _c48_f57_n1626["Load"]
  _c48_f57_n1627["Load"]
  _c48_f57_n1628["Assign"]
  _c48_f57_n1629["Name"]
  _c48_f57_n1630["Store"]
  _c48_f57_n1631["Subscript"]
  _c48_f57_n1632["Name"]
  _c48_f57_n1633["Load"]
  _c48_f57_n1634["UnaryOp"]
  _c48_f57_n1635["USub"]
  _c48_f57_n1636["Constant"]
  _c48_f57_n1637["Load"]
  _c48_f57_n1638["If"]
  _c48_f57_n1639["Call"]
  _c48_f57_n1640["Name"]
  _c48_f57_n1641["Load"]
  _c48_f57_n1642["Name"]
  _c48_f57_n1643["Load"]
  _c48_f57_n1644["Name"]
  _c48_f57_n1645["Load"]
  _c48_f57_n1646["Assign"]
  _c48_f57_n1647["Name"]
  _c48_f57_n1648["Store"]
  _c48_f57_n1649["Attribute"]
  _c48_f57_n1650["Name"]
  _c48_f57_n1651["Load"]
  _c48_f57_n1652["Load"]
  _c48_f57_n1653["Assign"]
  _c48_f57_n1654["Name"]
  _c48_f57_n1655["Store"]
  _c48_f57_n1656["Call"]
  _c48_f57_n1657["Name"]
  _c48_f57_n1658["Load"]
  _c48_f57_n1659["keyword"]
  _c48_f57_n1660["Name"]
  _c48_f57_n1661["Load"]
  _c48_f57_n1662["keyword"]
  _c48_f57_n1663["Name"]
  _c48_f57_n1664["Load"]
  _c48_f57_n1665["keyword"]
  _c48_f57_n1666["Name"]
  _c48_f57_n1667["Load"]
  _c48_f57_n1668["keyword"]
  _c48_f57_n1669["Call"]
  _c48_f57_n1670["Name"]
  _c48_f57_n1671["Load"]
  _c48_f57_n1672["Attribute"]
  _c48_f57_n1673["Name"]
  _c48_f57_n1674["Load"]
  _c48_f57_n1675["Load"]
  _c48_f57_n1676["keyword"]
  _c48_f57_n1677["Call"]
  _c48_f57_n1678["Name"]
  _c48_f57_n1679["Load"]
  _c48_f57_n1680["Attribute"]
  _c48_f57_n1681["Name"]
  _c48_f57_n1682["Load"]
  _c48_f57_n1683["Load"]
  _c48_f57_n1684["keyword"]
  _c48_f57_n1685["Call"]
  _c48_f57_n1686["Name"]
  _c48_f57_n1687["Load"]
  _c48_f57_n1688["Attribute"]
  _c48_f57_n1689["Name"]
  _c48_f57_n1690["Load"]
  _c48_f57_n1691["Load"]
  _c48_f57_n1692["Expr"]
  _c48_f57_n1693["Call"]
  _c48_f57_n1694["Attribute"]
  _c48_f57_n1695["Attribute"]
  _c48_f57_n1696["Name"]
  _c48_f57_n1697["Load"]
  _c48_f57_n1698["Load"]
  _c48_f57_n1699["Load"]
  _c48_f57_n1700["Name"]
  _c48_f57_n1701["Load"]
  _c48_f57_n1702["Expr"]
  _c48_f57_n1703["Call"]
  _c48_f57_n1704["Attribute"]
  _c48_f57_n1705["Attribute"]
  _c48_f57_n1706["Name"]
  _c48_f57_n1707["Load"]
  _c48_f57_n1708["Load"]
  _c48_f57_n1709["Load"]
  _c48_f57_n1710["Call"]
  _c48_f57_n1711["Name"]
  _c48_f57_n1712["Load"]
  _c48_f57_n1713["keyword"]
  _c48_f57_n1714["Name"]
  _c48_f57_n1715["Load"]
  _c48_f57_n1716["keyword"]
  _c48_f57_n1717["Name"]
  _c48_f57_n1718["Load"]
  _c48_f59_n1719["Expr"]
  _c48_f59_n1720["Constant"]
  _c48_f59_n1721["Pass"]
  _c48_f60_n1722["Return"]
  _c48_f60_n1723["Attribute"]
  _c48_f60_n1724["Name"]
  _c48_f60_n1725["Load"]
  _c48_f60_n1726["Load"]

  subgraph ImportNodeFinder
    direction TB
    subgraph _c31___init__
      direction TB
      _c31_f32_n943 --> _c31_f32_n944
      _c31_f32_n944 --> _c31_f32_n945
      _c31_f32_n945 --> _c31_f32_n946
      _c31_f32_n946 --> _c31_f32_n947
      _c31_f32_n947 --> _c31_f32_n948
      _c31_f32_n948 --> _c31_f32_n949
      _c31_f32_n949 --> _c31_f32_n950
      _c31_f32_n950 --> _c31_f32_n951
      _c31_f32_n951 --> _c31_f32_n952
      _c31_f32_n952 --> _c31_f32_n953
      _c31_f32_n953 --> _c31_f32_n954
      _c31_f32_n954 --> _c31_f32_n955
    end
    subgraph _c31_visit_Import
      direction TB
      %% loop i
        _c31_f33_l34_n956 --> _c31_f33_l34_n957
        _c31_f33_l34_n957 --> _c31_f33_l34_n958
        _c31_f33_l34_n958 --> _c31_f33_l34_n959
        _c31_f33_l34_n959 --> _c31_f33_l34_n960
        _c31_f33_l34_n960 --> _c31_f33_l34_n961
        _c31_f33_l34_n961 --> _c31_f33_l34_n962
        _c31_f33_l34_n962 --> _c31_f33_l34_n963
        _c31_f33_l34_n963 --> _c31_f33_l34_n964
        _c31_f33_l34_n964 --> _c31_f33_l34_n965
        _c31_f33_l34_n965 --> _c31_f33_l34_n966
        _c31_f33_l34_n966 --> _c31_f33_l34_n967
        _c31_f33_l34_n967 --> _c31_f33_l34_n968
        _c31_f33_l34_n968 --> _c31_f33_l34_n969
        _c31_f33_l34_n969 --> _c31_f33_l34_n970
      %% end i
      _c31_f33_l34_n970 --> _c31_f33_l34_n956
    end
    subgraph _c31_visit_ImportFrom
      direction TB
      _c31_f35_n971 --> _c31_f35_n972
      _c31_f35_n972 --> _c31_f35_n973
      _c31_f35_n973 --> _c31_f35_n974
      _c31_f35_n974 --> _c31_f35_n975
      _c31_f35_n975 --> _c31_f35_n976
      _c31_f35_n976 --> _c31_f35_n977
      _c31_f35_n977 --> _c31_f35_l36
      %% loop i
        _c31_f35_l36_n978 --> _c31_f35_l36_n979
        _c31_f35_l36_n979 --> _c31_f35_l36_n980
        _c31_f35_l36_n980 --> _c31_f35_l36_n981
        _c31_f35_l36_n981 --> _c31_f35_l36_n982
        _c31_f35_l36_n982 --> _c31_f35_l36_n983
        _c31_f35_l36_n983 --> _c31_f35_l36_n984
        _c31_f35_l36_n984 --> _c31_f35_l36_n985
        _c31_f35_l36_n985 --> _c31_f35_l36_n986
        _c31_f35_l36_n986 --> _c31_f35_l36_n987
        _c31_f35_l36_n987 --> _c31_f35_l36_n988
        _c31_f35_l36_n988 --> _c31_f35_l36_n989
        _c31_f35_l36_n989 --> _c31_f35_l36_n990
        _c31_f35_l36_n990 --> _c31_f35_l36_n991
        _c31_f35_l36_n991 --> _c31_f35_l36_n992
        _c31_f35_l36_n992 --> _c31_f35_l36_n993
        _c31_f35_l36_n993 --> _c31_f35_l36_n994
        _c31_f35_l36_n994 --> _c31_f35_l36_n995
      %% end i
      _c31_f35_l36_n995 --> _c31_f35_l36_n978
    end
    subgraph _c31_get_found_imports
      direction TB
      _c31_f37_n996 --> _c31_f37_n997
      _c31_f37_n997 --> _c31_f37_n998
      _c31_f37_n998 --> _c31_f37_n999
      _c31_f37_n999 --> _c31_f37_n1000
    end
  end
  subgraph LinkGenerator
    direction TB
    _c38_n1001 --> _c38_n1002
    _c38_n1002 --> _c38_n1003
    _c38_n1003 --> _c38_n1004
    _c38_n1004 --> _c38_n1005
    _c38_n1005 --> _c38_n1006
    subgraph _c38___init__
      direction TB
      _c38_f39_n1007 --> _c38_f39_n1008
      _c38_f39_n1008 --> _c38_f39_n1009
      _c38_f39_n1009 --> _c38_f39_n1010
      _c38_f39_n1010 --> _c38_f39_n1011
      _c38_f39_n1011 --> _c38_f39_n1012
      _c38_f39_n1012 --> _c38_f39_n1013
      _c38_f39_n1013 --> _c38_f39_n1014
      _c38_f39_n1014 --> _c38_f39_n1015
      _c38_f39_n1015 --> _c38_f39_n1016
      _c38_f39_n1016 --> _c38_f39_n1017
      _c38_f39_n1017 --> _c38_f39_n1018
      _c38_f39_n1018 --> _c38_f39_n1019
      _c38_f39_n1019 --> _c38_f39_n1020
      _c38_f39_n1020 --> _c38_f39_n1021
      _c38_f39_n1021 --> _c38_f39_n1022
      _c38_f39_n1022 --> _c38_f39_n1023
      _c38_f39_n1023 --> _c38_f39_n1024
      _c38_f39_n1024 --> _c38_f39_n1025
      _c38_f39_n1025 --> _c38_f39_n1026
      _c38_f39_n1026 --> _c38_f39_n1027
      _c38_f39_n1027 --> _c38_f39_n1028
      _c38_f39_n1028 --> _c38_f39_n1029
      _c38_f39_n1029 --> _c38_f39_n1030
      _c38_f39_n1030 --> _c38_f39_n1031
      _c38_f39_n1031 --> _c38_f39_n1032
      _c38_f39_n1032 --> _c38_f39_n1033
      _c38_f39_n1033 --> _c38_f39_n1034
      _c38_f39_n1034 --> _c38_f39_n1035
      _c38_f39_n1035 --> _c38_f39_n1036
      _c38_f39_n1036 --> _c38_f39_n1037
      _c38_f39_n1037 --> _c38_f39_n1038
    end
    subgraph _c38__count
      direction TB
      _c38_f40_n1039 --> _c38_f40_n1040
      _c38_f40_n1040 --> _c38_f40_n1041
      _c38_f40_n1041 --> _c38_f40_n1042
      _c38_f40_n1042 --> _c38_f40_n1043
      _c38_f40_n1043 --> _c38_f40_n1044
      _c38_f40_n1044 --> _c38_f40_n1045
      _c38_f40_n1045 --> _c38_f40_n1046
      _c38_f40_n1046 --> _c38_f40_n1047
      _c38_f40_n1047 --> _c38_f40_n1048
      _c38_f40_n1048 --> _c38_f40_n1049
      _c38_f40_n1049 --> _c38_f40_n1050
      _c38_f40_n1050 --> _c38_f40_n1051
      _c38_f40_n1051 --> _c38_f40_n1052
      _c38_f40_n1052 --> _c38_f40_n1053
      _c38_f40_n1053 --> _c38_f40_n1054
      _c38_f40_n1054 --> _c38_f40_n1055
    end
    subgraph _c38_visit_Import
      direction TB
    end
    subgraph _c38_visit_ImportFrom
      direction TB
    end
    subgraph _c38_visit_FunctionDef
      direction TB
      _c38_f43_n1058 --> _c38_f43_n1059
      _c38_f43_n1059 --> _c38_f43_n1060
      _c38_f43_n1060 --> _c38_f43_n1061
      _c38_f43_n1061 --> _c38_f43_n1062
      _c38_f43_n1062 --> _c38_f43_n1063
      _c38_f43_n1063 --> _c38_f43_n1064
      _c38_f43_n1064 --> _c38_f43_n1065
      _c38_f43_n1065 --> _c38_f43_n1066
      _c38_f43_n1066 --> _c38_f43_n1067
      _c38_f43_n1067 --> _c38_f43_n1068
      _c38_f43_n1068 --> _c38_f43_n1069
      _c38_f43_n1069 --> _c38_f43_n1070
      _c38_f43_n1070 --> _c38_f43_n1071
      _c38_f43_n1071 --> _c38_f43_n1072
      _c38_f43_n1072 --> _c38_f43_n1073
      _c38_f43_n1073 --> _c38_f43_n1074
      _c38_f43_n1074 --> _c38_f43_n1075
      _c38_f43_n1075 --> _c38_f43_n1076
      _c38_f43_n1076 --> _c38_f43_n1077
      _c38_f43_n1077 --> _c38_f43_n1078
      _c38_f43_n1078 --> _c38_f43_n1079
      _c38_f43_n1079 --> _c38_f43_n1080
      _c38_f43_n1080 --> _c38_f43_n1081
      _c38_f43_n1081 --> _c38_f43_n1082
      _c38_f43_n1082 --> _c38_f43_n1083
      _c38_f43_n1083 --> _c38_f43_n1084
      _c38_f43_n1084 --> _c38_f43_n1085
      _c38_f43_n1085 --> _c38_f43_n1086
      _c38_f43_n1086 --> _c38_f43_n1087
      _c38_f43_n1087 --> _c38_f43_n1088
      _c38_f43_n1088 --> _c38_f43_n1089
    end
    subgraph _c38_visit_ClassDef
      direction TB
      _c38_f44_n1090 --> _c38_f44_n1091
      _c38_f44_n1091 --> _c38_f44_n1092
      _c38_f44_n1092 --> _c38_f44_n1093
      _c38_f44_n1093 --> _c38_f44_n1094
      _c38_f44_n1094 --> _c38_f44_n1095
      _c38_f44_n1095 --> _c38_f44_n1096
      _c38_f44_n1096 --> _c38_f44_n1097
      _c38_f44_n1097 --> _c38_f44_n1098
      _c38_f44_n1098 --> _c38_f44_n1099
      _c38_f44_n1099 --> _c38_f44_n1100
      _c38_f44_n1100 --> _c38_f44_n1101
      _c38_f44_n1101 --> _c38_f44_n1102
      _c38_f44_n1102 --> _c38_f44_n1103
      _c38_f44_n1103 --> _c38_f44_n1104
      _c38_f44_n1104 --> _c38_f44_n1105
      _c38_f44_n1105 --> _c38_f44_n1106
      _c38_f44_n1106 --> _c38_f44_n1107
      _c38_f44_n1107 --> _c38_f44_n1108
      _c38_f44_n1108 --> _c38_f44_n1109
      _c38_f44_n1109 --> _c38_f44_n1110
      _c38_f44_n1110 --> _c38_f44_n1111
      _c38_f44_n1111 --> _c38_f44_n1112
      _c38_f44_n1112 --> _c38_f44_n1113
      _c38_f44_n1113 --> _c38_f44_n1114
      _c38_f44_n1114 --> _c38_f44_n1115
      _c38_f44_n1115 --> _c38_f44_n1116
      _c38_f44_n1116 --> _c38_f44_n1117
      _c38_f44_n1117 --> _c38_f44_n1118
      _c38_f44_n1118 --> _c38_f44_n1119
      _c38_f44_n1119 --> _c38_f44_n1120
      _c38_f44_n1120 --> _c38_f44_n1121
    end
    subgraph _c38_visit_For
      direction TB
      _c38_f45_n1122 --> _c38_f45_n1123
      _c38_f45_n1123 --> _c38_f45_n1124
      _c38_f45_n1124 --> _c38_f45_n1125
      _c38_f45_n1125 --> _c38_f45_n1126
      _c38_f45_n1126 --> _c38_f45_n1127
      _c38_f45_n1127 --> _c38_f45_n1128
      _c38_f45_n1128 --> _c38_f45_n1129
      _c38_f45_n1129 --> _c38_f45_n1130
      _c38_f45_n1130 --> _c38_f45_n1131
      _c38_f45_n1131 --> _c38_f45_n1132
      _c38_f45_n1132 --> _c38_f45_n1133
      _c38_f45_n1133 --> _c38_f45_n1134
      _c38_f45_n1134 --> _c38_f45_n1135
      _c38_f45_n1135 --> _c38_f45_n1136
      _c38_f45_n1136 --> _c38_f45_n1137
      _c38_f45_n1137 --> _c38_f45_n1138
      _c38_f45_n1138 --> _c38_f45_n1139
      _c38_f45_n1139 --> _c38_f45_n1140
      _c38_f45_n1140 --> _c38_f45_n1141
      _c38_f45_n1141 --> _c38_f45_n1142
      _c38_f45_n1142 --> _c38_f45_n1143
      _c38_f45_n1143 --> _c38_f45_n1144
      _c38_f45_n1144 --> _c38_f45_n1145
      _c38_f45_n1145 --> _c38_f45_n1146
      _c38_f45_n1146 --> _c38_f45_n1147
      _c38_f45_n1147 --> _c38_f45_n1148
      _c38_f45_n1148 --> _c38_f45_n1149
      _c38_f45_n1149 --> _c38_f45_n1150
      _c38_f45_n1150 --> _c38_f45_n1151
      _c38_f45_n1151 --> _c38_f45_n1152
      _c38_f45_n1152 --> _c38_f45_n1153
      _c38_f45_n1153 --> _c38_f45_n1154
      _c38_f45_n1154 --> _c38_f45_n1155
      _c38_f45_n1155 --> _c38_f45_n1156
      _c38_f45_n1156 --> _c38_f45_n1157
      _c38_f45_n1157 --> _c38_f45_n1158
      _c38_f45_n1158 --> _c38_f45_n1159
      _c38_f45_n1159 --> _c38_f45_n1160
      _c38_f45_n1160 --> _c38_f45_n1161
      _c38_f45_n1161 --> _c38_f45_n1162
      _c38_f45_n1162 --> _c38_f45_n1163
      _c38_f45_n1163 --> _c38_f45_n1164
      _c38_f45_n1164 --> _c38_f45_n1165
      _c38_f45_n1165 --> _c38_f45_n1166
      _c38_f45_n1166 --> _c38_f45_n1167
      _c38_f45_n1167 --> _c38_f45_n1168
      _c38_f45_n1168 --> _c38_f45_n1169
      _c38_f45_n1169 --> _c38_f45_n1170
      _c38_f45_n1170 --> _c38_f45_n1171
      _c38_f45_n1171 --> _c38_f45_n1172
      _c38_f45_n1172 --> _c38_f45_n1173
      _c38_f45_n1173 --> _c38_f45_n1174
      _c38_f45_n1174 --> _c38_f45_n1175
      _c38_f45_n1175 --> _c38_f45_n1176
      _c38_f45_n1176 --> _c38_f45_n1177
      _c38_f45_n1177 --> _c38_f45_n1178
      _c38_f45_n1178 --> _c38_f45_n1179
      _c38_f45_n1179 --> _c38_f45_n1180
      _c38_f45_n1180 --> _c38_f45_n1181
      _c38_f45_n1181 --> _c38_f45_n1182
      _c38_f45_n1182 --> _c38_f45_n1183
      _c38_f45_n1183 --> _c38_f45_n1184
      _c38_f45_n1184 --> _c38_f45_n1185
      _c38_f45_n1185 --> _c38_f45_n1186
      _c38_f45_n1186 --> _c38_f45_n1187
      _c38_f45_n1187 --> _c38_f45_n1188
      _c38_f45_n1188 --> _c38_f45_n1189
      _c38_f45_n1189 --> _c38_f45_n1190
      _c38_f45_n1190 --> _c38_f45_n1191
      _c38_f45_n1191 --> _c38_f45_n1192
      _c38_f45_n1192 --> _c38_f45_n1193
      _c38_f45_n1193 --> _c38_f45_n1194
      _c38_f45_n1194 --> _c38_f45_n1195
      _c38_f45_n1195 --> _c38_f45_n1196
      _c38_f45_n1196 --> _c38_f45_n1197
      _c38_f45_n1197 --> _c38_f45_n1198
      _c38_f45_n1198 --> _c38_f45_n1199
      _c38_f45_n1199 --> _c38_f45_n1200
      _c38_f45_n1200 --> _c38_f45_n1201
      _c38_f45_n1201 --> _c38_f45_n1202
      _c38_f45_n1202 --> _c38_f45_n1203
      _c38_f45_n1203 --> _c38_f45_n1204
      _c38_f45_n1204 --> _c38_f45_n1205
      _c38_f45_n1205 --> _c38_f45_n1206
      _c38_f45_n1206 --> _c38_f45_n1207
      _c38_f45_n1207 --> _c38_f45_n1208
      _c38_f45_n1208 --> _c38_f45_n1209
      _c38_f45_n1209 --> _c38_f45_n1210
      _c38_f45_n1210 --> _c38_f45_n1211
      _c38_f45_n1211 --> _c38_f45_n1212
      _c38_f45_n1212 --> _c38_f45_n1213
      _c38_f45_n1213 --> _c38_f45_n1214
      _c38_f45_n1214 --> _c38_f45_n1215
      _c38_f45_n1215 --> _c38_f45_n1216
      _c38_f45_n1216 --> _c38_f45_n1217
      _c38_f45_n1217 --> _c38_f45_n1218
      _c38_f45_n1218 --> _c38_f45_n1219
      _c38_f45_n1219 --> _c38_f45_n1220
      _c38_f45_n1220 --> _c38_f45_n1221
      _c38_f45_n1221 --> _c38_f45_n1222
      _c38_f45_n1222 --> _c38_f45_n1223
      _c38_f45_n1223 --> _c38_f45_n1224
      _c38_f45_n1224 --> _c38_f45_n1225
      _c38_f45_n1225 --> _c38_f45_n1226
      _c38_f45_n1226 --> _c38_f45_n1227
      _c38_f45_n1227 --> _c38_f45_n1228
      _c38_f45_n1228 --> _c38_f45_n1229
      _c38_f45_n1229 --> _c38_f45_n1230
      _c38_f45_n1230 --> _c38_f45_n1231
      _c38_f45_n1231 --> _c38_f45_n1232
      _c38_f45_n1232 --> _c38_f45_n1233
      _c38_f45_n1233 --> _c38_f45_n1234
      _c38_f45_n1234 --> _c38_f45_n1235
      _c38_f45_n1235 --> _c38_f45_n1236
      _c38_f45_n1236 --> _c38_f45_n1237
    end
    subgraph _c38_generic_visit
      direction TB
      _c38_f46_n1238 --> _c38_f46_n1239
      _c38_f46_n1239 --> _c38_f46_n1240
      _c38_f46_n1240 --> _c38_f46_n1241
      _c38_f46_n1241 --> _c38_f46_n1242
      _c38_f46_n1242 --> _c38_f46_n1243
      _c38_f46_n1243 --> _c38_f46_n1244
      _c38_f46_n1244 --> _c38_f46_n1245
      _c38_f46_n1245 --> _c38_f46_n1246
      _c38_f46_n1246 --> _c38_f46_n1247
      _c38_f46_n1247 --> _c38_f46_n1248
      _c38_f46_n1248 --> _c38_f46_n1249
      _c38_f46_n1249 --> _c38_f46_n1250
      _c38_f46_n1250 --> _c38_f46_n1251
      _c38_f46_n1251 --> _c38_f46_n1252
      _c38_f46_n1252 --> _c38_f46_n1253
      _c38_f46_n1253 --> _c38_f46_n1254
      _c38_f46_n1254 --> _c38_f46_n1255
      _c38_f46_n1255 --> _c38_f46_n1256
      _c38_f46_n1256 --> _c38_f46_n1257
      _c38_f46_n1257 --> _c38_f46_n1258
      _c38_f46_n1258 --> _c38_f46_n1259
      _c38_f46_n1259 --> _c38_f46_n1260
      _c38_f46_n1260 --> _c38_f46_n1261
      _c38_f46_n1261 --> _c38_f46_n1262
      _c38_f46_n1262 --> _c38_f46_n1263
      _c38_f46_n1263 --> _c38_f46_n1264
      _c38_f46_n1264 --> _c38_f46_n1265
      _c38_f46_n1265 --> _c38_f46_n1266
      _c38_f46_n1266 --> _c38_f46_n1267
      _c38_f46_n1267 --> _c38_f46_n1268
      _c38_f46_n1268 --> _c38_f46_n1269
      _c38_f46_n1269 --> _c38_f46_n1270
      _c38_f46_n1270 --> _c38_f46_n1271
      _c38_f46_n1271 --> _c38_f46_n1272
      _c38_f46_n1272 --> _c38_f46_n1273
      _c38_f46_n1273 --> _c38_f46_n1274
      _c38_f46_n1274 --> _c38_f46_n1275
      _c38_f46_n1275 --> _c38_f46_n1276
      _c38_f46_n1276 --> _c38_f46_n1277
      _c38_f46_n1277 --> _c38_f46_n1278
      _c38_f46_n1278 --> _c38_f46_n1279
      _c38_f46_n1279 --> _c38_f46_n1280
      _c38_f46_n1280 --> _c38_f46_n1281
      _c38_f46_n1281 --> _c38_f46_n1282
      _c38_f46_n1282 --> _c38_f46_n1283
      _c38_f46_n1283 --> _c38_f46_n1284
      _c38_f46_n1284 --> _c38_f46_n1285
      _c38_f46_n1285 --> _c38_f46_n1286
      _c38_f46_n1286 --> _c38_f46_n1287
      _c38_f46_n1287 --> _c38_f46_n1288
      _c38_f46_n1288 --> _c38_f46_n1289
      _c38_f46_n1289 --> _c38_f46_n1290
      _c38_f46_n1290 --> _c38_f46_n1291
      _c38_f46_n1291 --> _c38_f46_n1292
      _c38_f46_n1292 --> _c38_f46_n1293
      _c38_f46_n1293 --> _c38_f46_n1294
      _c38_f46_n1294 --> _c38_f46_n1295
      _c38_f46_n1295 --> _c38_f46_n1296
      _c38_f46_n1296 --> _c38_f46_n1297
      _c38_f46_n1297 --> _c38_f46_n1298
      _c38_f46_n1298 --> _c38_f46_n1299
      _c38_f46_n1299 --> _c38_f46_n1300
      _c38_f46_n1300 --> _c38_f46_n1301
      _c38_f46_n1301 --> _c38_f46_n1302
      _c38_f46_n1302 --> _c38_f46_n1303
      _c38_f46_n1303 --> _c38_f46_n1304
      _c38_f46_n1304 --> _c38_f46_n1305
      _c38_f46_n1305 --> _c38_f46_n1306
      _c38_f46_n1306 --> _c38_f46_n1307
      _c38_f46_n1307 --> _c38_f46_n1308
    end
    subgraph _c38_get_list_of_elements
      direction TB
      _c38_f47_n1309 --> _c38_f47_n1310
      _c38_f47_n1310 --> _c38_f47_n1311
      _c38_f47_n1311 --> _c38_f47_n1312
      _c38_f47_n1312 --> _c38_f47_n1313
    end
  end
  subgraph BlockGenerator
    direction TB
    _c48_n1314 --> _c48_n1315
    _c48_n1315 --> _c48_n1316
    _c48_n1316 --> _c48_n1317
    _c48_n1317 --> _c48_n1318
    _c48_n1318 --> _c48_n1319
    subgraph _c48___init__
      direction TB
      _c48_f49_n1320 --> _c48_f49_n1321
      _c48_f49_n1321 --> _c48_f49_n1322
      _c48_f49_n1322 --> _c48_f49_n1323
      _c48_f49_n1323 --> _c48_f49_n1324
      _c48_f49_n1324 --> _c48_f49_n1325
      _c48_f49_n1325 --> _c48_f49_n1326
      _c48_f49_n1326 --> _c48_f49_n1327
      _c48_f49_n1327 --> _c48_f49_n1328
      _c48_f49_n1328 --> _c48_f49_n1329
      _c48_f49_n1329 --> _c48_f49_n1330
      _c48_f49_n1330 --> _c48_f49_n1331
      _c48_f49_n1331 --> _c48_f49_n1332
      _c48_f49_n1332 --> _c48_f49_n1333
      _c48_f49_n1333 --> _c48_f49_n1334
      _c48_f49_n1334 --> _c48_f49_n1335
      _c48_f49_n1335 --> _c48_f49_n1336
      _c48_f49_n1336 --> _c48_f49_n1337
      _c48_f49_n1337 --> _c48_f49_n1338
      _c48_f49_n1338 --> _c48_f49_n1339
    end
    subgraph _c48__count
      direction TB
      _c48_f50_n1340 --> _c48_f50_n1341
      _c48_f50_n1341 --> _c48_f50_n1342
      _c48_f50_n1342 --> _c48_f50_n1343
      _c48_f50_n1343 --> _c48_f50_n1344
      _c48_f50_n1344 --> _c48_f50_n1345
      _c48_f50_n1345 --> _c48_f50_n1346
      _c48_f50_n1346 --> _c48_f50_n1347
      _c48_f50_n1347 --> _c48_f50_n1348
      _c48_f50_n1348 --> _c48_f50_n1349
      _c48_f50_n1349 --> _c48_f50_n1350
      _c48_f50_n1350 --> _c48_f50_n1351
      _c48_f50_n1351 --> _c48_f50_n1352
      _c48_f50_n1352 --> _c48_f50_n1353
      _c48_f50_n1353 --> _c48_f50_n1354
      _c48_f50_n1354 --> _c48_f50_n1355
      _c48_f50_n1355 --> _c48_f50_n1356
    end
    subgraph _c48_visit_Module
      direction TB
      _c48_f51_n1357 --> _c48_f51_n1358
      _c48_f51_n1358 --> _c48_f51_n1359
      _c48_f51_n1359 --> _c48_f51_n1360
      _c48_f51_n1360 --> _c48_f51_n1361
      _c48_f51_n1361 --> _c48_f51_n1362
      _c48_f51_n1362 --> _c48_f51_n1363
      _c48_f51_n1363 --> _c48_f51_n1364
      _c48_f51_n1364 --> _c48_f51_l52
      %% loop sub_element
        _c48_f51_l52_n1365 --> _c48_f51_l52_n1366
        _c48_f51_l52_n1366 --> _c48_f51_l52_n1367
        _c48_f51_l52_n1367 --> _c48_f51_l52_n1368
        _c48_f51_l52_n1368 --> _c48_f51_l52_n1369
        _c48_f51_l52_n1369 --> _c48_f51_l52_n1370
        _c48_f51_l52_n1370 --> _c48_f51_l52_n1371
        _c48_f51_l52_n1371 --> _c48_f51_l52_n1372
        _c48_f51_l52_n1372 --> _c48_f51_l52_n1373
      %% end sub_element
      _c48_f51_l52_n1373 --> _c48_f51_l52_n1365
      _c48_f51_l52_n1365 --> _c48_f51_n1374
      _c48_f51_n1374 --> _c48_f51_n1375
      _c48_f51_n1375 --> _c48_f51_n1376
      _c48_f51_n1376 --> _c48_f51_n1377
      _c48_f51_n1377 --> _c48_f51_n1378
      _c48_f51_n1378 --> _c48_f51_n1379
      _c48_f51_n1379 --> _c48_f51_n1380
      _c48_f51_n1380 --> _c48_f51_n1381
      _c48_f51_n1381 --> _c48_f51_n1382
      _c48_f51_n1382 --> _c48_f51_n1383
      _c48_f51_n1383 --> _c48_f51_n1384
      _c48_f51_n1384 --> _c48_f51_n1385
      _c48_f51_n1385 --> _c48_f51_n1386
      _c48_f51_n1386 --> _c48_f51_n1387
      _c48_f51_n1387 --> _c48_f51_n1388
      _c48_f51_n1388 --> _c48_f51_n1389
      _c48_f51_n1389 --> _c48_f51_n1390
      _c48_f51_n1390 --> _c48_f51_n1391
      _c48_f51_n1391 --> _c48_f51_n1392
      _c48_f51_n1392 --> _c48_f51_n1393
      _c48_f51_n1393 --> _c48_f51_n1394
      _c48_f51_n1394 --> _c48_f51_n1395
      _c48_f51_n1395 --> _c48_f51_n1396
      _c48_f51_n1396 --> _c48_f51_n1397
      _c48_f51_n1397 --> _c48_f51_n1398
      _c48_f51_n1398 --> _c48_f51_n1399
      _c48_f51_n1399 --> _c48_f51_n1400
      _c48_f51_n1400 --> _c48_f51_n1401
      _c48_f51_n1401 --> _c48_f51_n1402
      _c48_f51_n1402 --> _c48_f51_n1403
      _c48_f51_n1403 --> _c48_f51_n1404
      _c48_f51_n1404 --> _c48_f51_n1405
      _c48_f51_n1405 --> _c48_f51_n1406
      _c48_f51_n1406 --> _c48_f51_n1407
      _c48_f51_n1407 --> _c48_f51_n1408
      _c48_f51_n1408 --> _c48_f51_n1409
      _c48_f51_n1409 --> _c48_f51_n1410
      _c48_f51_n1410 --> _c48_f51_n1411
      _c48_f51_n1411 --> _c48_f51_n1412
      _c48_f51_n1412 --> _c48_f51_n1413
      _c48_f51_n1413 --> _c48_f51_n1414
    end
    subgraph _c48_visit_FunctionDef
      direction TB
      _c48_f53_n1415 --> _c48_f53_n1416
      _c48_f53_n1416 --> _c48_f53_n1417
      _c48_f53_n1417 --> _c48_f53_n1418
      _c48_f53_n1418 --> _c48_f53_n1419
      _c48_f53_n1419 --> _c48_f53_n1420
      _c48_f53_n1420 --> _c48_f53_n1421
      _c48_f53_n1421 --> _c48_f53_n1422
      _c48_f53_n1422 --> _c48_f53_n1423
      _c48_f53_n1423 --> _c48_f53_n1424
      _c48_f53_n1424 --> _c48_f53_n1425
      _c48_f53_n1425 --> _c48_f53_n1426
      _c48_f53_n1426 --> _c48_f53_n1427
      _c48_f53_n1427 --> _c48_f53_n1428
      _c48_f53_n1428 --> _c48_f53_n1429
      _c48_f53_n1429 --> _c48_f53_n1430
      _c48_f53_n1430 --> _c48_f53_n1431
      _c48_f53_n1431 --> _c48_f53_n1432
      _c48_f53_n1432 --> _c48_f53_n1433
      _c48_f53_n1433 --> _c48_f53_n1434
      _c48_f53_n1434 --> _c48_f53_n1435
      _c48_f53_n1435 --> _c48_f53_n1436
      _c48_f53_n1436 --> _c48_f53_n1437
      _c48_f53_n1437 --> _c48_f53_n1438
      _c48_f53_n1438 --> _c48_f53_n1439
      _c48_f53_n1439 --> _c48_f53_n1440
      _c48_f53_n1440 --> _c48_f53_n1441
      _c48_f53_n1441 --> _c48_f53_l54
      %% loop sub_element
        _c48_f53_l54_n1442 --> _c48_f53_l54_n1443
        _c48_f53_l54_n1443 --> _c48_f53_l54_n1444
        _c48_f53_l54_n1444 --> _c48_f53_l54_n1445
        _c48_f53_l54_n1445 --> _c48_f53_l54_n1446
        _c48_f53_l54_n1446 --> _c48_f53_l54_n1447
        _c48_f53_l54_n1447 --> _c48_f53_l54_n1448
        _c48_f53_l54_n1448 --> _c48_f53_l54_n1449
        _c48_f53_l54_n1449 --> _c48_f53_l54_n1450
      %% end sub_element
      _c48_f53_l54_n1450 --> _c48_f53_l54_n1442
      _c48_f53_l54_n1442 --> _c48_f53_n1451
      _c48_f53_n1451 --> _c48_f53_n1452
      _c48_f53_n1452 --> _c48_f53_n1453
      _c48_f53_n1453 --> _c48_f53_n1454
      _c48_f53_n1454 --> _c48_f53_n1455
      _c48_f53_n1455 --> _c48_f53_n1456
      _c48_f53_n1456 --> _c48_f53_n1457
      _c48_f53_n1457 --> _c48_f53_n1458
      _c48_f53_n1458 --> _c48_f53_n1459
      _c48_f53_n1459 --> _c48_f53_n1460
      _c48_f53_n1460 --> _c48_f53_n1461
      _c48_f53_n1461 --> _c48_f53_n1462
      _c48_f53_n1462 --> _c48_f53_n1463
      _c48_f53_n1463 --> _c48_f53_n1464
      _c48_f53_n1464 --> _c48_f53_n1465
      _c48_f53_n1465 --> _c48_f53_n1466
      _c48_f53_n1466 --> _c48_f53_n1467
      _c48_f53_n1467 --> _c48_f53_n1468
      _c48_f53_n1468 --> _c48_f53_n1469
      _c48_f53_n1469 --> _c48_f53_n1470
      _c48_f53_n1470 --> _c48_f53_n1471
      _c48_f53_n1471 --> _c48_f53_n1472
      _c48_f53_n1472 --> _c48_f53_n1473
      _c48_f53_n1473 --> _c48_f53_n1474
      _c48_f53_n1474 --> _c48_f53_n1475
      _c48_f53_n1475 --> _c48_f53_n1476
      _c48_f53_n1476 --> _c48_f53_n1477
      _c48_f53_n1477 --> _c48_f53_n1478
      _c48_f53_n1478 --> _c48_f53_n1479
      _c48_f53_n1479 --> _c48_f53_n1480
      _c48_f53_n1480 --> _c48_f53_n1481
      _c48_f53_n1481 --> _c48_f53_n1482
      _c48_f53_n1482 --> _c48_f53_n1483
      _c48_f53_n1483 --> _c48_f53_n1484
      _c48_f53_n1484 --> _c48_f53_n1485
      _c48_f53_n1485 --> _c48_f53_n1486
      _c48_f53_n1486 --> _c48_f53_n1487
      _c48_f53_n1487 --> _c48_f53_n1488
      _c48_f53_n1488 --> _c48_f53_n1489
      _c48_f53_n1489 --> _c48_f53_n1490
      _c48_f53_n1490 --> _c48_f53_n1491
    end
    subgraph _c48_visit_ClassDef
      direction TB
      _c48_f55_n1492 --> _c48_f55_n1493
      _c48_f55_n1493 --> _c48_f55_n1494
      _c48_f55_n1494 --> _c48_f55_n1495
      _c48_f55_n1495 --> _c48_f55_n1496
      _c48_f55_n1496 --> _c48_f55_n1497
      _c48_f55_n1497 --> _c48_f55_n1498
      _c48_f55_n1498 --> _c48_f55_n1499
      _c48_f55_n1499 --> _c48_f55_n1500
      _c48_f55_n1500 --> _c48_f55_n1501
      _c48_f55_n1501 --> _c48_f55_n1502
      _c48_f55_n1502 --> _c48_f55_n1503
      _c48_f55_n1503 --> _c48_f55_n1504
      _c48_f55_n1504 --> _c48_f55_n1505
      _c48_f55_n1505 --> _c48_f55_n1506
      _c48_f55_n1506 --> _c48_f55_n1507
      _c48_f55_n1507 --> _c48_f55_n1508
      _c48_f55_n1508 --> _c48_f55_n1509
      _c48_f55_n1509 --> _c48_f55_n1510
      _c48_f55_n1510 --> _c48_f55_n1511
      _c48_f55_n1511 --> _c48_f55_n1512
      _c48_f55_n1512 --> _c48_f55_n1513
      _c48_f55_n1513 --> _c48_f55_n1514
      _c48_f55_n1514 --> _c48_f55_n1515
      _c48_f55_n1515 --> _c48_f55_n1516
      _c48_f55_n1516 --> _c48_f55_n1517
      _c48_f55_n1517 --> _c48_f55_n1518
      _c48_f55_n1518 --> _c48_f55_l56
      %% loop sub_element
        _c48_f55_l56_n1519 --> _c48_f55_l56_n1520
        _c48_f55_l56_n1520 --> _c48_f55_l56_n1521
        _c48_f55_l56_n1521 --> _c48_f55_l56_n1522
        _c48_f55_l56_n1522 --> _c48_f55_l56_n1523
        _c48_f55_l56_n1523 --> _c48_f55_l56_n1524
        _c48_f55_l56_n1524 --> _c48_f55_l56_n1525
        _c48_f55_l56_n1525 --> _c48_f55_l56_n1526
        _c48_f55_l56_n1526 --> _c48_f55_l56_n1527
      %% end sub_element
      _c48_f55_l56_n1527 --> _c48_f55_l56_n1519
      _c48_f55_l56_n1519 --> _c48_f55_n1528
      _c48_f55_n1528 --> _c48_f55_n1529
      _c48_f55_n1529 --> _c48_f55_n1530
      _c48_f55_n1530 --> _c48_f55_n1531
      _c48_f55_n1531 --> _c48_f55_n1532
      _c48_f55_n1532 --> _c48_f55_n1533
      _c48_f55_n1533 --> _c48_f55_n1534
      _c48_f55_n1534 --> _c48_f55_n1535
      _c48_f55_n1535 --> _c48_f55_n1536
      _c48_f55_n1536 --> _c48_f55_n1537
      _c48_f55_n1537 --> _c48_f55_n1538
      _c48_f55_n1538 --> _c48_f55_n1539
      _c48_f55_n1539 --> _c48_f55_n1540
      _c48_f55_n1540 --> _c48_f55_n1541
      _c48_f55_n1541 --> _c48_f55_n1542
      _c48_f55_n1542 --> _c48_f55_n1543
      _c48_f55_n1543 --> _c48_f55_n1544
      _c48_f55_n1544 --> _c48_f55_n1545
      _c48_f55_n1545 --> _c48_f55_n1546
      _c48_f55_n1546 --> _c48_f55_n1547
      _c48_f55_n1547 --> _c48_f55_n1548
      _c48_f55_n1548 --> _c48_f55_n1549
      _c48_f55_n1549 --> _c48_f55_n1550
      _c48_f55_n1550 --> _c48_f55_n1551
      _c48_f55_n1551 --> _c48_f55_n1552
      _c48_f55_n1552 --> _c48_f55_n1553
      _c48_f55_n1553 --> _c48_f55_n1554
      _c48_f55_n1554 --> _c48_f55_n1555
      _c48_f55_n1555 --> _c48_f55_n1556
      _c48_f55_n1556 --> _c48_f55_n1557
      _c48_f55_n1557 --> _c48_f55_n1558
      _c48_f55_n1558 --> _c48_f55_n1559
      _c48_f55_n1559 --> _c48_f55_n1560
    end
    subgraph _c48_visit_For
      direction TB
      _c48_f57_n1561 --> _c48_f57_n1562
      _c48_f57_n1562 --> _c48_f57_n1563
      _c48_f57_n1563 --> _c48_f57_n1564
      _c48_f57_n1564 --> _c48_f57_n1565
      _c48_f57_n1565 --> _c48_f57_n1566
      _c48_f57_n1566 --> _c48_f57_n1567
      _c48_f57_n1567 --> _c48_f57_n1568
      _c48_f57_n1568 --> _c48_f57_n1569
      _c48_f57_n1569 --> _c48_f57_n1570
      _c48_f57_n1570 --> _c48_f57_n1571
      _c48_f57_n1571 --> _c48_f57_n1572
      _c48_f57_n1572 --> _c48_f57_n1573
      _c48_f57_n1573 --> _c48_f57_n1574
      _c48_f57_n1574 --> _c48_f57_n1575
      _c48_f57_n1575 --> _c48_f57_n1576
      _c48_f57_n1576 --> _c48_f57_n1577
      _c48_f57_n1577 --> _c48_f57_n1578
      _c48_f57_n1578 --> _c48_f57_n1579
      _c48_f57_n1579 --> _c48_f57_n1580
      _c48_f57_n1580 --> _c48_f57_n1581
      _c48_f57_n1581 --> _c48_f57_n1582
      _c48_f57_n1582 --> _c48_f57_n1583
      _c48_f57_n1583 --> _c48_f57_n1584
      _c48_f57_n1584 --> _c48_f57_n1585
      _c48_f57_n1585 --> _c48_f57_n1586
      _c48_f57_n1586 --> _c48_f57_n1587
      _c48_f57_n1587 --> _c48_f57_l58
      %% loop sub_element
        _c48_f57_l58_n1588 --> _c48_f57_l58_n1589
        _c48_f57_l58_n1589 --> _c48_f57_l58_n1590
        _c48_f57_l58_n1590 --> _c48_f57_l58_n1591
        _c48_f57_l58_n1591 --> _c48_f57_l58_n1592
        _c48_f57_l58_n1592 --> _c48_f57_l58_n1593
        _c48_f57_l58_n1593 --> _c48_f57_l58_n1594
        _c48_f57_l58_n1594 --> _c48_f57_l58_n1595
        _c48_f57_l58_n1595 --> _c48_f57_l58_n1596
      %% end sub_element
      _c48_f57_l58_n1596 --> _c48_f57_l58_n1588
      _c48_f57_l58_n1588 --> _c48_f57_n1597
      _c48_f57_n1597 --> _c48_f57_n1598
      _c48_f57_n1598 --> _c48_f57_n1599
      _c48_f57_n1599 --> _c48_f57_n1600
      _c48_f57_n1600 --> _c48_f57_n1601
      _c48_f57_n1601 --> _c48_f57_n1602
      _c48_f57_n1602 --> _c48_f57_n1603
      _c48_f57_n1603 --> _c48_f57_n1604
      _c48_f57_n1604 --> _c48_f57_n1605
      _c48_f57_n1605 --> _c48_f57_n1606
      _c48_f57_n1606 --> _c48_f57_n1607
      _c48_f57_n1607 --> _c48_f57_n1608
      _c48_f57_n1608 --> _c48_f57_n1609
      _c48_f57_n1609 --> _c48_f57_n1610
      _c48_f57_n1610 --> _c48_f57_n1611
      _c48_f57_n1611 --> _c48_f57_n1612
      _c48_f57_n1612 --> _c48_f57_n1613
      _c48_f57_n1613 --> _c48_f57_n1614
      _c48_f57_n1614 --> _c48_f57_n1615
      _c48_f57_n1615 --> _c48_f57_n1616
      _c48_f57_n1616 --> _c48_f57_n1617
      _c48_f57_n1617 --> _c48_f57_n1618
      _c48_f57_n1618 --> _c48_f57_n1619
      _c48_f57_n1619 --> _c48_f57_n1620
      _c48_f57_n1620 --> _c48_f57_n1621
      _c48_f57_n1621 --> _c48_f57_n1622
      _c48_f57_n1622 --> _c48_f57_n1623
      _c48_f57_n1623 --> _c48_f57_n1624
      _c48_f57_n1624 --> _c48_f57_n1625
      _c48_f57_n1625 --> _c48_f57_n1626
      _c48_f57_n1626 --> _c48_f57_n1627
      _c48_f57_n1627 --> _c48_f57_n1628
      _c48_f57_n1628 --> _c48_f57_n1629
      _c48_f57_n1629 --> _c48_f57_n1630
      _c48_f57_n1630 --> _c48_f57_n1631
      _c48_f57_n1631 --> _c48_f57_n1632
      _c48_f57_n1632 --> _c48_f57_n1633
      _c48_f57_n1633 --> _c48_f57_n1634
      _c48_f57_n1634 --> _c48_f57_n1635
      _c48_f57_n1635 --> _c48_f57_n1636
      _c48_f57_n1636 --> _c48_f57_n1637
      _c48_f57_n1637 --> _c48_f57_n1638
      _c48_f57_n1638 --> _c48_f57_n1639
      _c48_f57_n1639 --> _c48_f57_n1640
      _c48_f57_n1640 --> _c48_f57_n1641
      _c48_f57_n1641 --> _c48_f57_n1642
      _c48_f57_n1642 --> _c48_f57_n1643
      _c48_f57_n1643 --> _c48_f57_n1644
      _c48_f57_n1644 --> _c48_f57_n1645
      _c48_f57_n1645 --> _c48_f57_n1646
      _c48_f57_n1646 --> _c48_f57_n1647
      _c48_f57_n1647 --> _c48_f57_n1648
      _c48_f57_n1648 --> _c48_f57_n1649
      _c48_f57_n1649 --> _c48_f57_n1650
      _c48_f57_n1650 --> _c48_f57_n1651
      _c48_f57_n1651 --> _c48_f57_n1652
      _c48_f57_n1652 --> _c48_f57_n1653
      _c48_f57_n1653 --> _c48_f57_n1654
      _c48_f57_n1654 --> _c48_f57_n1655
      _c48_f57_n1655 --> _c48_f57_n1656
      _c48_f57_n1656 --> _c48_f57_n1657
      _c48_f57_n1657 --> _c48_f57_n1658
      _c48_f57_n1658 --> _c48_f57_n1659
      _c48_f57_n1659 --> _c48_f57_n1660
      _c48_f57_n1660 --> _c48_f57_n1661
      _c48_f57_n1661 --> _c48_f57_n1662
      _c48_f57_n1662 --> _c48_f57_n1663
      _c48_f57_n1663 --> _c48_f57_n1664
      _c48_f57_n1664 --> _c48_f57_n1665
      _c48_f57_n1665 --> _c48_f57_n1666
      _c48_f57_n1666 --> _c48_f57_n1667
      _c48_f57_n1667 --> _c48_f57_n1668
      _c48_f57_n1668 --> _c48_f57_n1669
      _c48_f57_n1669 --> _c48_f57_n1670
      _c48_f57_n1670 --> _c48_f57_n1671
      _c48_f57_n1671 --> _c48_f57_n1672
      _c48_f57_n1672 --> _c48_f57_n1673
      _c48_f57_n1673 --> _c48_f57_n1674
      _c48_f57_n1674 --> _c48_f57_n1675
      _c48_f57_n1675 --> _c48_f57_n1676
      _c48_f57_n1676 --> _c48_f57_n1677
      _c48_f57_n1677 --> _c48_f57_n1678
      _c48_f57_n1678 --> _c48_f57_n1679
      _c48_f57_n1679 --> _c48_f57_n1680
      _c48_f57_n1680 --> _c48_f57_n1681
      _c48_f57_n1681 --> _c48_f57_n1682
      _c48_f57_n1682 --> _c48_f57_n1683
      _c48_f57_n1683 --> _c48_f57_n1684
      _c48_f57_n1684 --> _c48_f57_n1685
      _c48_f57_n1685 --> _c48_f57_n1686
      _c48_f57_n1686 --> _c48_f57_n1687
      _c48_f57_n1687 --> _c48_f57_n1688
      _c48_f57_n1688 --> _c48_f57_n1689
      _c48_f57_n1689 --> _c48_f57_n1690
      _c48_f57_n1690 --> _c48_f57_n1691
      _c48_f57_n1691 --> _c48_f57_n1692
      _c48_f57_n1692 --> _c48_f57_n1693
      _c48_f57_n1693 --> _c48_f57_n1694
      _c48_f57_n1694 --> _c48_f57_n1695
      _c48_f57_n1695 --> _c48_f57_n1696
      _c48_f57_n1696 --> _c48_f57_n1697
      _c48_f57_n1697 --> _c48_f57_n1698
      _c48_f57_n1698 --> _c48_f57_n1699
      _c48_f57_n1699 --> _c48_f57_n1700
      _c48_f57_n1700 --> _c48_f57_n1701
      _c48_f57_n1701 --> _c48_f57_n1702
      _c48_f57_n1702 --> _c48_f57_n1703
      _c48_f57_n1703 --> _c48_f57_n1704
      _c48_f57_n1704 --> _c48_f57_n1705
      _c48_f57_n1705 --> _c48_f57_n1706
      _c48_f57_n1706 --> _c48_f57_n1707
      _c48_f57_n1707 --> _c48_f57_n1708
      _c48_f57_n1708 --> _c48_f57_n1709
      _c48_f57_n1709 --> _c48_f57_n1710
      _c48_f57_n1710 --> _c48_f57_n1711
      _c48_f57_n1711 --> _c48_f57_n1712
      _c48_f57_n1712 --> _c48_f57_n1713
      _c48_f57_n1713 --> _c48_f57_n1714
      _c48_f57_n1714 --> _c48_f57_n1715
      _c48_f57_n1715 --> _c48_f57_n1716
      _c48_f57_n1716 --> _c48_f57_n1717
      _c48_f57_n1717 --> _c48_f57_n1718
    end
    subgraph _c48_generic_visit
      direction TB
      _c48_f59_n1719 --> _c48_f59_n1720
      _c48_f59_n1720 --> _c48_f59_n1721
    end
    subgraph _c48_get_list_of_elements
      direction TB
      _c48_f60_n1722 --> _c48_f60_n1723
      _c48_f60_n1723 --> _c48_f60_n1724
      _c48_f60_n1724 --> _c48_f60_n1725
      _c48_f60_n1725 --> _c48_f60_n1726
    end
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
        alias(name='ClassDef'),
        alias(name='For'),
        alias(name='FunctionDef'),
        alias(name='Import'),
        alias(name='ImportFrom'),
        alias(name='Module'),
        alias(name='NodeVisitor'),
        alias(name='unparse')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=11,
      end_col_offset=1),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidClass'),
        alias(name='MermaidElement'),
        alias(name='MermaidFor'),
        alias(name='MermaidFunction'),
        alias(name='MermaidLink'),
        alias(name='MermaidModule'),
        alias(name='MermaidNode')],
      level=0,
      lineno=12,
      col_offset=0,
      end_lineno=20,
      end_col_offset=1),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Any'),
        alias(name='Optional')],
      level=0,
      lineno=22,
      col_offset=0,
      end_lineno=22,
      end_col_offset=32),
    ClassDef(
      name='ImportNodeFinder',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=25,
          col_offset=23,
          end_lineno=25,
          end_col_offset=34)],
      keywords=[],
      body=[
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=26,
                col_offset=17,
                end_lineno=26,
                end_col_offset=21)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=27,
                  col_offset=8,
                  end_lineno=27,
                  end_col_offset=12),
                attr='found_imports',
                ctx=Store(),
                lineno=27,
                col_offset=8,
                end_lineno=27,
                end_col_offset=26),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=27,
                  col_offset=29,
                  end_lineno=27,
                  end_col_offset=33),
                slice=Name(
                  id='str',
                  ctx=Load(),
                  lineno=27,
                  col_offset=34,
                  end_lineno=27,
                  end_col_offset=37),
                ctx=Load(),
                lineno=27,
                col_offset=29,
                end_lineno=27,
                end_col_offset=38),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=27,
                col_offset=41,
                end_lineno=27,
                end_col_offset=43),
              simple=0,
              lineno=27,
              col_offset=8,
              end_lineno=27,
              end_col_offset=43)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=26,
            col_offset=26,
            end_lineno=26,
            end_col_offset=30),
          lineno=26,
          col_offset=4,
          end_lineno=27,
          end_col_offset=43),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=29,
                col_offset=21,
                end_lineno=29,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=29,
                  col_offset=33,
                  end_lineno=29,
                  end_col_offset=39),
                lineno=29,
                col_offset=27,
                end_lineno=29,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=30,
                col_offset=12,
                end_lineno=30,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=30,
                  col_offset=17,
                  end_lineno=30,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=30,
                col_offset=17,
                end_lineno=30,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=31,
                          col_offset=12,
                          end_lineno=31,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=31,
                        col_offset=12,
                        end_lineno=31,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=31,
                      col_offset=12,
                      end_lineno=31,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=31,
                                col_offset=41,
                                end_lineno=31,
                                end_col_offset=42),
                              attr='name',
                              ctx=Load(),
                              lineno=31,
                              col_offset=41,
                              end_lineno=31,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=31,
                            col_offset=38,
                            end_lineno=31,
                            end_col_offset=51),
                          Constant(
                            value='.*',
                            lineno=31,
                            col_offset=38,
                            end_lineno=31,
                            end_col_offset=51)],
                        lineno=31,
                        col_offset=38,
                        end_lineno=31,
                        end_col_offset=51)],
                    keywords=[],
                    lineno=31,
                    col_offset=12,
                    end_lineno=31,
                    end_col_offset=52),
                  lineno=31,
                  col_offset=12,
                  end_lineno=31,
                  end_col_offset=52)],
              orelse=[],
              lineno=30,
              col_offset=8,
              end_lineno=31,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=29,
            col_offset=44,
            end_lineno=29,
            end_col_offset=48),
          lineno=29,
          col_offset=4,
          end_lineno=31,
          end_col_offset=52),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=33,
                col_offset=25,
                end_lineno=33,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=33,
                  col_offset=37,
                  end_lineno=33,
                  end_col_offset=47),
                lineno=33,
                col_offset=31,
                end_lineno=33,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='module',
                  ctx=Store(),
                  lineno=34,
                  col_offset=8,
                  end_lineno=34,
                  end_col_offset=14)],
              value=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=34,
                  col_offset=17,
                  end_lineno=34,
                  end_col_offset=21),
                attr='module',
                ctx=Load(),
                lineno=34,
                col_offset=17,
                end_lineno=34,
                end_col_offset=28),
              lineno=34,
              col_offset=8,
              end_lineno=34,
              end_col_offset=28),
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=35,
                col_offset=12,
                end_lineno=35,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=35,
                  col_offset=17,
                  end_lineno=35,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=35,
                col_offset=17,
                end_lineno=35,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=36,
                          col_offset=12,
                          end_lineno=36,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=36,
                        col_offset=12,
                        end_lineno=36,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=36,
                      col_offset=12,
                      end_lineno=36,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Name(
                              id='module',
                              ctx=Load(),
                              lineno=36,
                              col_offset=41,
                              end_lineno=36,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=36,
                            col_offset=38,
                            end_lineno=36,
                            end_col_offset=58),
                          Constant(
                            value='.',
                            lineno=36,
                            col_offset=38,
                            end_lineno=36,
                            end_col_offset=58),
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=36,
                                col_offset=50,
                                end_lineno=36,
                                end_col_offset=51),
                              attr='name',
                              ctx=Load(),
                              lineno=36,
                              col_offset=50,
                              end_lineno=36,
                              end_col_offset=56),
                            conversion=-1,
                            lineno=36,
                            col_offset=38,
                            end_lineno=36,
                            end_col_offset=58)],
                        lineno=36,
                        col_offset=38,
                        end_lineno=36,
                        end_col_offset=58)],
                    keywords=[],
                    lineno=36,
                    col_offset=12,
                    end_lineno=36,
                    end_col_offset=59),
                  lineno=36,
                  col_offset=12,
                  end_lineno=36,
                  end_col_offset=59)],
              orelse=[],
              lineno=35,
              col_offset=8,
              end_lineno=36,
              end_col_offset=59)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=33,
            col_offset=52,
            end_lineno=33,
            end_col_offset=56),
          lineno=33,
          col_offset=4,
          end_lineno=36,
          end_col_offset=59),
        FunctionDef(
          name='get_found_imports',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=38,
                col_offset=26,
                end_lineno=38,
                end_col_offset=30)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=39,
                  col_offset=15,
                  end_lineno=39,
                  end_col_offset=19),
                attr='found_imports',
                ctx=Load(),
                lineno=39,
                col_offset=15,
                end_lineno=39,
                end_col_offset=33),
              lineno=39,
              col_offset=8,
              end_lineno=39,
              end_col_offset=33)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=38,
              col_offset=35,
              end_lineno=38,
              end_col_offset=39),
            slice=Name(
              id='str',
              ctx=Load(),
              lineno=38,
              col_offset=40,
              end_lineno=38,
              end_col_offset=43),
            ctx=Load(),
            lineno=38,
            col_offset=35,
            end_lineno=38,
            end_col_offset=44),
          lineno=38,
          col_offset=4,
          end_lineno=39,
          end_col_offset=33)],
      decorator_list=[],
      lineno=25,
      col_offset=0,
      end_lineno=39,
      end_col_offset=33),
    ClassDef(
      name='LinkGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=42,
          col_offset=20,
          end_lineno=42,
          end_col_offset=31)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='count',
            ctx=Store(),
            lineno=43,
            col_offset=4,
            end_lineno=43,
            end_col_offset=9),
          annotation=Name(
            id='int',
            ctx=Load(),
            lineno=43,
            col_offset=12,
            end_lineno=43,
            end_col_offset=15),
          value=Constant(
            value=0,
            lineno=43,
            col_offset=18,
            end_lineno=43,
            end_col_offset=19),
          simple=1,
          lineno=43,
          col_offset=4,
          end_lineno=43,
          end_col_offset=19),
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=45,
                col_offset=17,
                end_lineno=45,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=45,
                  col_offset=32,
                  end_lineno=45,
                  end_col_offset=35),
                lineno=45,
                col_offset=23,
                end_lineno=45,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=45,
                col_offset=38,
                end_lineno=45,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=46,
                  col_offset=8,
                  end_lineno=46,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=46,
                col_offset=8,
                end_lineno=46,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=46,
                  col_offset=24,
                  end_lineno=46,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=46,
                  col_offset=29,
                  end_lineno=46,
                  end_col_offset=43),
                ctx=Load(),
                lineno=46,
                col_offset=24,
                end_lineno=46,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=46,
                col_offset=47,
                end_lineno=46,
                end_col_offset=49),
              simple=0,
              lineno=46,
              col_offset=8,
              end_lineno=46,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=47,
                  col_offset=8,
                  end_lineno=47,
                  end_col_offset=12),
                attr='prev_node',
                ctx=Store(),
                lineno=47,
                col_offset=8,
                end_lineno=47,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='Optional',
                  ctx=Load(),
                  lineno=47,
                  col_offset=25,
                  end_lineno=47,
                  end_col_offset=33),
                slice=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=47,
                  col_offset=34,
                  end_lineno=47,
                  end_col_offset=37),
                ctx=Load(),
                lineno=47,
                col_offset=25,
                end_lineno=47,
                end_col_offset=38),
              value=Constant(
                value=None,
                lineno=47,
                col_offset=41,
                end_lineno=47,
                end_col_offset=45),
              simple=0,
              lineno=47,
              col_offset=8,
              end_lineno=47,
              end_col_offset=45),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=48,
                    col_offset=8,
                    end_lineno=48,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=48,
                  col_offset=8,
                  end_lineno=48,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=48,
                col_offset=22,
                end_lineno=48,
                end_col_offset=28),
              lineno=48,
              col_offset=8,
              end_lineno=48,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=45,
            col_offset=45,
            end_lineno=45,
            end_col_offset=49),
          lineno=45,
          col_offset=4,
          end_lineno=48,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='cls',
                lineno=51,
                col_offset=15,
                end_lineno=51,
                end_col_offset=18)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='value',
                  ctx=Store(),
                  lineno=52,
                  col_offset=8,
                  end_lineno=52,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=52,
                  col_offset=16,
                  end_lineno=52,
                  end_col_offset=19),
                attr='count',
                ctx=Load(),
                lineno=52,
                col_offset=16,
                end_lineno=52,
                end_col_offset=25),
              lineno=52,
              col_offset=8,
              end_lineno=52,
              end_col_offset=25),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=53,
                  col_offset=8,
                  end_lineno=53,
                  end_col_offset=11),
                attr='count',
                ctx=Store(),
                lineno=53,
                col_offset=8,
                end_lineno=53,
                end_col_offset=17),
              op=Add(),
              value=Constant(
                value=1,
                lineno=53,
                col_offset=20,
                end_lineno=53,
                end_col_offset=21),
              lineno=53,
              col_offset=8,
              end_lineno=53,
              end_col_offset=21),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=54,
                col_offset=15,
                end_lineno=54,
                end_col_offset=20),
              lineno=54,
              col_offset=8,
              end_lineno=54,
              end_col_offset=20)],
          decorator_list=[
            Name(
              id='classmethod',
              ctx=Load(),
              lineno=50,
              col_offset=5,
              end_lineno=50,
              end_col_offset=16)],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=51,
            col_offset=23,
            end_lineno=51,
            end_col_offset=26),
          lineno=51,
          col_offset=4,
          end_lineno=54,
          end_col_offset=20),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=56,
                col_offset=21,
                end_lineno=56,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=56,
                  col_offset=33,
                  end_lineno=56,
                  end_col_offset=39),
                lineno=56,
                col_offset=27,
                end_lineno=56,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=57,
              col_offset=8,
              end_lineno=57,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=56,
            col_offset=44,
            end_lineno=56,
            end_col_offset=48),
          lineno=56,
          col_offset=4,
          end_lineno=57,
          end_col_offset=12),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=59,
                col_offset=25,
                end_lineno=59,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=59,
                  col_offset=37,
                  end_lineno=59,
                  end_col_offset=47),
                lineno=59,
                col_offset=31,
                end_lineno=59,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=60,
              col_offset=8,
              end_lineno=60,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=59,
            col_offset=52,
            end_lineno=59,
            end_col_offset=56),
          lineno=59,
          col_offset=4,
          end_lineno=60,
          end_col_offset=12),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=62,
                col_offset=26,
                end_lineno=62,
                end_col_offset=30),
              arg(
                arg='node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=62,
                  col_offset=38,
                  end_lineno=62,
                  end_col_offset=49),
                lineno=62,
                col_offset=32,
                end_lineno=62,
                end_col_offset=49)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='block_generator',
                  ctx=Store(),
                  lineno=63,
                  col_offset=8,
                  end_lineno=63,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=63,
                  col_offset=26,
                  end_lineno=63,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=63,
                        col_offset=48,
                        end_lineno=63,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=63,
                      col_offset=48,
                      end_lineno=63,
                      end_col_offset=59),
                    lineno=63,
                    col_offset=41,
                    end_lineno=63,
                    end_col_offset=59)],
                lineno=63,
                col_offset=26,
                end_lineno=63,
                end_col_offset=60),
              lineno=63,
              col_offset=8,
              end_lineno=63,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=64,
                    col_offset=8,
                    end_lineno=64,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=64,
                  col_offset=8,
                  end_lineno=64,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=64,
                    col_offset=30,
                    end_lineno=64,
                    end_col_offset=34)],
                keywords=[],
                lineno=64,
                col_offset=8,
                end_lineno=64,
                end_col_offset=35),
              lineno=64,
              col_offset=8,
              end_lineno=64,
              end_col_offset=35),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=65,
                      col_offset=8,
                      end_lineno=65,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=65,
                    col_offset=8,
                    end_lineno=65,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=65,
                  col_offset=8,
                  end_lineno=65,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Attribute(
                      value=Name(
                        id='block_generator',
                        ctx=Load(),
                        lineno=65,
                        col_offset=29,
                        end_lineno=65,
                        end_col_offset=44),
                      attr='get_list_of_elements',
                      ctx=Load(),
                      lineno=65,
                      col_offset=29,
                      end_lineno=65,
                      end_col_offset=65),
                    args=[],
                    keywords=[],
                    lineno=65,
                    col_offset=29,
                    end_lineno=65,
                    end_col_offset=67)],
                keywords=[],
                lineno=65,
                col_offset=8,
                end_lineno=65,
                end_col_offset=68),
              lineno=65,
              col_offset=8,
              end_lineno=65,
              end_col_offset=68)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=62,
            col_offset=54,
            end_lineno=62,
            end_col_offset=57),
          lineno=62,
          col_offset=4,
          end_lineno=65,
          end_col_offset=68),
        FunctionDef(
          name='visit_ClassDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=67,
                col_offset=23,
                end_lineno=67,
                end_col_offset=27),
              arg(
                arg='node',
                annotation=Name(
                  id='ClassDef',
                  ctx=Load(),
                  lineno=67,
                  col_offset=35,
                  end_lineno=67,
                  end_col_offset=43),
                lineno=67,
                col_offset=29,
                end_lineno=67,
                end_col_offset=43)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='block_generator',
                  ctx=Store(),
                  lineno=68,
                  col_offset=8,
                  end_lineno=68,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=68,
                  col_offset=26,
                  end_lineno=68,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=68,
                        col_offset=48,
                        end_lineno=68,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=68,
                      col_offset=48,
                      end_lineno=68,
                      end_col_offset=59),
                    lineno=68,
                    col_offset=41,
                    end_lineno=68,
                    end_col_offset=59)],
                lineno=68,
                col_offset=26,
                end_lineno=68,
                end_col_offset=60),
              lineno=68,
              col_offset=8,
              end_lineno=68,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=69,
                    col_offset=8,
                    end_lineno=69,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=69,
                  col_offset=8,
                  end_lineno=69,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=69,
                    col_offset=30,
                    end_lineno=69,
                    end_col_offset=34)],
                keywords=[],
                lineno=69,
                col_offset=8,
                end_lineno=69,
                end_col_offset=35),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=35),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=70,
                      col_offset=8,
                      end_lineno=70,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=70,
                    col_offset=8,
                    end_lineno=70,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=70,
                  col_offset=8,
                  end_lineno=70,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Attribute(
                      value=Name(
                        id='block_generator',
                        ctx=Load(),
                        lineno=70,
                        col_offset=29,
                        end_lineno=70,
                        end_col_offset=44),
                      attr='get_list_of_elements',
                      ctx=Load(),
                      lineno=70,
                      col_offset=29,
                      end_lineno=70,
                      end_col_offset=65),
                    args=[],
                    keywords=[],
                    lineno=70,
                    col_offset=29,
                    end_lineno=70,
                    end_col_offset=67)],
                keywords=[],
                lineno=70,
                col_offset=8,
                end_lineno=70,
                end_col_offset=68),
              lineno=70,
              col_offset=8,
              end_lineno=70,
              end_col_offset=68)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=67,
            col_offset=48,
            end_lineno=67,
            end_col_offset=51),
          lineno=67,
          col_offset=4,
          end_lineno=70,
          end_col_offset=68),
        FunctionDef(
          name='visit_For',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=72,
                col_offset=18,
                end_lineno=72,
                end_col_offset=22),
              arg(
                arg='node',
                annotation=Name(
                  id='For',
                  ctx=Load(),
                  lineno=72,
                  col_offset=30,
                  end_lineno=72,
                  end_col_offset=33),
                lineno=72,
                col_offset=24,
                end_lineno=72,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='block_generator',
                  ctx=Store(),
                  lineno=73,
                  col_offset=8,
                  end_lineno=73,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=73,
                  col_offset=26,
                  end_lineno=73,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=73,
                        col_offset=48,
                        end_lineno=73,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=73,
                      col_offset=48,
                      end_lineno=73,
                      end_col_offset=59),
                    lineno=73,
                    col_offset=41,
                    end_lineno=73,
                    end_col_offset=59)],
                lineno=73,
                col_offset=26,
                end_lineno=73,
                end_col_offset=60),
              lineno=73,
              col_offset=8,
              end_lineno=73,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=74,
                    col_offset=8,
                    end_lineno=74,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=74,
                  col_offset=8,
                  end_lineno=74,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=74,
                    col_offset=30,
                    end_lineno=74,
                    end_col_offset=34)],
                keywords=[],
                lineno=74,
                col_offset=8,
                end_lineno=74,
                end_col_offset=35),
              lineno=74,
              col_offset=8,
              end_lineno=74,
              end_col_offset=35),
            Assign(
              targets=[
                Name(
                  id='for_loop_elements',
                  ctx=Store(),
                  lineno=76,
                  col_offset=8,
                  end_lineno=76,
                  end_col_offset=25)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=76,
                    col_offset=28,
                    end_lineno=76,
                    end_col_offset=43),
                  attr='get_list_of_elements',
                  ctx=Load(),
                  lineno=76,
                  col_offset=28,
                  end_lineno=76,
                  end_col_offset=64),
                args=[],
                keywords=[],
                lineno=76,
                col_offset=28,
                end_lineno=76,
                end_col_offset=66),
              lineno=76,
              col_offset=8,
              end_lineno=76,
              end_col_offset=66),
            Assign(
              targets=[
                Name(
                  id='loop_start',
                  ctx=Store(),
                  lineno=77,
                  col_offset=8,
                  end_lineno=77,
                  end_col_offset=18)],
              value=Subscript(
                value=Name(
                  id='for_loop_elements',
                  ctx=Load(),
                  lineno=77,
                  col_offset=21,
                  end_lineno=77,
                  end_col_offset=38),
                slice=Constant(
                  value=0,
                  lineno=77,
                  col_offset=39,
                  end_lineno=77,
                  end_col_offset=40),
                ctx=Load(),
                lineno=77,
                col_offset=21,
                end_lineno=77,
                end_col_offset=41),
              lineno=77,
              col_offset=8,
              end_lineno=77,
              end_col_offset=41),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=78,
                  col_offset=11,
                  end_lineno=78,
                  end_col_offset=21),
                args=[
                  Name(
                    id='loop_start',
                    ctx=Load(),
                    lineno=78,
                    col_offset=22,
                    end_lineno=78,
                    end_col_offset=32),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=78,
                    col_offset=34,
                    end_lineno=78,
                    end_col_offset=45)],
                keywords=[],
                lineno=78,
                col_offset=11,
                end_lineno=78,
                end_col_offset=46),
              body=[
                Assign(
                  targets=[
                    Name(
                      id='loop_start',
                      ctx=Store(),
                      lineno=79,
                      col_offset=12,
                      end_lineno=79,
                      end_col_offset=22)],
                  value=Attribute(
                    value=Name(
                      id='loop_start',
                      ctx=Load(),
                      lineno=79,
                      col_offset=25,
                      end_lineno=79,
                      end_col_offset=35),
                    attr='from_',
                    ctx=Load(),
                    lineno=79,
                    col_offset=25,
                    end_lineno=79,
                    end_col_offset=41),
                  lineno=79,
                  col_offset=12,
                  end_lineno=79,
                  end_col_offset=41)],
              orelse=[],
              lineno=78,
              col_offset=8,
              end_lineno=79,
              end_col_offset=41),
            Assign(
              targets=[
                Name(
                  id='loop_end',
                  ctx=Store(),
                  lineno=80,
                  col_offset=8,
                  end_lineno=80,
                  end_col_offset=16)],
              value=Subscript(
                value=Name(
                  id='for_loop_elements',
                  ctx=Load(),
                  lineno=80,
                  col_offset=19,
                  end_lineno=80,
                  end_col_offset=36),
                slice=UnaryOp(
                  op=USub(),
                  operand=Constant(
                    value=1,
                    lineno=80,
                    col_offset=38,
                    end_lineno=80,
                    end_col_offset=39),
                  lineno=80,
                  col_offset=37,
                  end_lineno=80,
                  end_col_offset=39),
                ctx=Load(),
                lineno=80,
                col_offset=19,
                end_lineno=80,
                end_col_offset=40),
              lineno=80,
              col_offset=8,
              end_lineno=80,
              end_col_offset=40),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=81,
                  col_offset=11,
                  end_lineno=81,
                  end_col_offset=21),
                args=[
                  Name(
                    id='loop_end',
                    ctx=Load(),
                    lineno=81,
                    col_offset=22,
                    end_lineno=81,
                    end_col_offset=30),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=81,
                    col_offset=32,
                    end_lineno=81,
                    end_col_offset=43)],
                keywords=[],
                lineno=81,
                col_offset=11,
                end_lineno=81,
                end_col_offset=44),
              body=[
                Assign(
                  targets=[
                    Name(
                      id='loop_end',
                      ctx=Store(),
                      lineno=82,
                      col_offset=12,
                      end_lineno=82,
                      end_col_offset=20)],
                  value=Attribute(
                    value=Name(
                      id='loop_end',
                      ctx=Load(),
                      lineno=82,
                      col_offset=23,
                      end_lineno=82,
                      end_col_offset=31),
                    attr='to',
                    ctx=Load(),
                    lineno=82,
                    col_offset=23,
                    end_lineno=82,
                    end_col_offset=34),
                  lineno=82,
                  col_offset=12,
                  end_lineno=82,
                  end_col_offset=34)],
              orelse=[],
              lineno=81,
              col_offset=8,
              end_lineno=82,
              end_col_offset=34),
            If(
              test=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=85,
                  col_offset=11,
                  end_lineno=85,
                  end_col_offset=15),
                attr='prev_node',
                ctx=Load(),
                lineno=85,
                col_offset=11,
                end_lineno=85,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=86,
                          col_offset=12,
                          end_lineno=86,
                          end_col_offset=16),
                        attr='elements',
                        ctx=Load(),
                        lineno=86,
                        col_offset=12,
                        end_lineno=86,
                        end_col_offset=25),
                      attr='append',
                      ctx=Load(),
                      lineno=86,
                      col_offset=12,
                      end_lineno=86,
                      end_col_offset=32),
                    args=[
                      Call(
                        func=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=86,
                          col_offset=33,
                          end_lineno=86,
                          end_col_offset=44),
                        args=[],
                        keywords=[
                          keyword(
                            arg='from_',
                            value=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=86,
                                col_offset=51,
                                end_lineno=86,
                                end_col_offset=55),
                              attr='prev_node',
                              ctx=Load(),
                              lineno=86,
                              col_offset=51,
                              end_lineno=86,
                              end_col_offset=65),
                            lineno=86,
                            col_offset=45,
                            end_lineno=86,
                            end_col_offset=65),
                          keyword(
                            arg='to',
                            value=Name(
                              id='loop_start',
                              ctx=Load(),
                              lineno=86,
                              col_offset=70,
                              end_lineno=86,
                              end_col_offset=80),
                            lineno=86,
                            col_offset=67,
                            end_lineno=86,
                            end_col_offset=80)],
                        lineno=86,
                        col_offset=33,
                        end_lineno=86,
                        end_col_offset=81)],
                    keywords=[],
                    lineno=86,
                    col_offset=12,
                    end_lineno=86,
                    end_col_offset=82),
                  lineno=86,
                  col_offset=12,
                  end_lineno=86,
                  end_col_offset=82)],
              orelse=[],
              lineno=85,
              col_offset=8,
              end_lineno=86,
              end_col_offset=82),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=88,
                      col_offset=8,
                      end_lineno=88,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=88,
                    col_offset=8,
                    end_lineno=88,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=88,
                  col_offset=8,
                  end_lineno=88,
                  end_col_offset=28),
                args=[
                  Name(
                    id='for_loop_elements',
                    ctx=Load(),
                    lineno=88,
                    col_offset=29,
                    end_lineno=88,
                    end_col_offset=46)],
                keywords=[],
                lineno=88,
                col_offset=8,
                end_lineno=88,
                end_col_offset=47),
              lineno=88,
              col_offset=8,
              end_lineno=88,
              end_col_offset=47),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=89,
                    col_offset=8,
                    end_lineno=89,
                    end_col_offset=12),
                  attr='prev_node',
                  ctx=Store(),
                  lineno=89,
                  col_offset=8,
                  end_lineno=89,
                  end_col_offset=22)],
              value=Name(
                id='loop_end',
                ctx=Load(),
                lineno=89,
                col_offset=25,
                end_lineno=89,
                end_col_offset=33),
              lineno=89,
              col_offset=8,
              end_lineno=89,
              end_col_offset=33)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=72,
            col_offset=38,
            end_lineno=72,
            end_col_offset=41),
          lineno=72,
          col_offset=4,
          end_lineno=89,
          end_col_offset=33),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=91,
                col_offset=22,
                end_lineno=91,
                end_col_offset=26),
              arg(
                arg='node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=91,
                  col_offset=34,
                  end_lineno=91,
                  end_col_offset=37),
                lineno=91,
                col_offset=28,
                end_lineno=91,
                end_col_offset=37)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='mermaid_data',
                  ctx=Store(),
                  lineno=92,
                  col_offset=8,
                  end_lineno=92,
                  end_col_offset=20)],
              value=Call(
                func=Name(
                  id='MermaidNode',
                  ctx=Load(),
                  lineno=92,
                  col_offset=23,
                  end_lineno=92,
                  end_col_offset=34),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='node',
                      ctx=Load(),
                      lineno=93,
                      col_offset=21,
                      end_lineno=93,
                      end_col_offset=25),
                    lineno=93,
                    col_offset=12,
                    end_lineno=93,
                    end_col_offset=25),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=94,
                              col_offset=33,
                              end_lineno=94,
                              end_col_offset=37),
                            attr='prefix',
                            ctx=Load(),
                            lineno=94,
                            col_offset=33,
                            end_lineno=94,
                            end_col_offset=44),
                          conversion=-1,
                          lineno=94,
                          col_offset=30,
                          end_lineno=94,
                          end_col_offset=72),
                        Constant(
                          value='_n',
                          lineno=94,
                          col_offset=30,
                          end_lineno=94,
                          end_col_offset=72),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='LinkGenerator',
                                ctx=Load(),
                                lineno=94,
                                col_offset=48,
                                end_lineno=94,
                                end_col_offset=61),
                              attr='_count',
                              ctx=Load(),
                              lineno=94,
                              col_offset=48,
                              end_lineno=94,
                              end_col_offset=68),
                            args=[],
                            keywords=[],
                            lineno=94,
                            col_offset=48,
                            end_lineno=94,
                            end_col_offset=70),
                          conversion=-1,
                          lineno=94,
                          col_offset=30,
                          end_lineno=94,
                          end_col_offset=72)],
                      lineno=94,
                      col_offset=30,
                      end_lineno=94,
                      end_col_offset=72),
                    lineno=94,
                    col_offset=12,
                    end_lineno=94,
                    end_col_offset=72),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Call(
                        func=Name(
                          id='type',
                          ctx=Load(),
                          lineno=95,
                          col_offset=25,
                          end_lineno=95,
                          end_col_offset=29),
                        args=[
                          Name(
                            id='node',
                            ctx=Load(),
                            lineno=95,
                            col_offset=30,
                            end_lineno=95,
                            end_col_offset=34)],
                        keywords=[],
                        lineno=95,
                        col_offset=25,
                        end_lineno=95,
                        end_col_offset=35),
                      attr='__name__',
                      ctx=Load(),
                      lineno=95,
                      col_offset=25,
                      end_lineno=95,
                      end_col_offset=44),
                    lineno=95,
                    col_offset=12,
                    end_lineno=95,
                    end_col_offset=44)],
                lineno=92,
                col_offset=23,
                end_lineno=96,
                end_col_offset=9),
              lineno=92,
              col_offset=8,
              end_lineno=96,
              end_col_offset=9),
            If(
              test=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=97,
                  col_offset=11,
                  end_lineno=97,
                  end_col_offset=15),
                attr='prev_node',
                ctx=Load(),
                lineno=97,
                col_offset=11,
                end_lineno=97,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=98,
                          col_offset=12,
                          end_lineno=98,
                          end_col_offset=16),
                        attr='elements',
                        ctx=Load(),
                        lineno=98,
                        col_offset=12,
                        end_lineno=98,
                        end_col_offset=25),
                      attr='append',
                      ctx=Load(),
                      lineno=98,
                      col_offset=12,
                      end_lineno=98,
                      end_col_offset=32),
                    args=[
                      Call(
                        func=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=98,
                          col_offset=33,
                          end_lineno=98,
                          end_col_offset=44),
                        args=[],
                        keywords=[
                          keyword(
                            arg='from_',
                            value=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=98,
                                col_offset=51,
                                end_lineno=98,
                                end_col_offset=55),
                              attr='prev_node',
                              ctx=Load(),
                              lineno=98,
                              col_offset=51,
                              end_lineno=98,
                              end_col_offset=65),
                            lineno=98,
                            col_offset=45,
                            end_lineno=98,
                            end_col_offset=65),
                          keyword(
                            arg='to',
                            value=Name(
                              id='mermaid_data',
                              ctx=Load(),
                              lineno=98,
                              col_offset=70,
                              end_lineno=98,
                              end_col_offset=82),
                            lineno=98,
                            col_offset=67,
                            end_lineno=98,
                            end_col_offset=82)],
                        lineno=98,
                        col_offset=33,
                        end_lineno=98,
                        end_col_offset=83)],
                    keywords=[],
                    lineno=98,
                    col_offset=12,
                    end_lineno=98,
                    end_col_offset=84),
                  lineno=98,
                  col_offset=12,
                  end_lineno=98,
                  end_col_offset=84)],
              orelse=[],
              lineno=97,
              col_offset=8,
              end_lineno=98,
              end_col_offset=84),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=99,
                    col_offset=8,
                    end_lineno=99,
                    end_col_offset=12),
                  attr='prev_node',
                  ctx=Store(),
                  lineno=99,
                  col_offset=8,
                  end_lineno=99,
                  end_col_offset=22)],
              value=Name(
                id='mermaid_data',
                ctx=Load(),
                lineno=99,
                col_offset=25,
                end_lineno=99,
                end_col_offset=37),
              lineno=99,
              col_offset=8,
              end_lineno=99,
              end_col_offset=37),
            Return(
              value=Call(
                func=Attribute(
                  value=Call(
                    func=Name(
                      id='super',
                      ctx=Load(),
                      lineno=102,
                      col_offset=15,
                      end_lineno=102,
                      end_col_offset=20),
                    args=[],
                    keywords=[],
                    lineno=102,
                    col_offset=15,
                    end_lineno=102,
                    end_col_offset=22),
                  attr='generic_visit',
                  ctx=Load(),
                  lineno=102,
                  col_offset=15,
                  end_lineno=102,
                  end_col_offset=36),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=102,
                    col_offset=37,
                    end_lineno=102,
                    end_col_offset=41)],
                keywords=[],
                lineno=102,
                col_offset=15,
                end_lineno=102,
                end_col_offset=42),
              lineno=102,
              col_offset=8,
              end_lineno=102,
              end_col_offset=42)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=91,
            col_offset=42,
            end_lineno=91,
            end_col_offset=45),
          lineno=91,
          col_offset=4,
          end_lineno=102,
          end_col_offset=42),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=104,
                col_offset=29,
                end_lineno=104,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=105,
                  col_offset=15,
                  end_lineno=105,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=105,
                col_offset=15,
                end_lineno=105,
                end_col_offset=28),
              lineno=105,
              col_offset=8,
              end_lineno=105,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=104,
              col_offset=38,
              end_lineno=104,
              end_col_offset=42),
            slice=Name(
              id='MermaidLink',
              ctx=Load(),
              lineno=104,
              col_offset=43,
              end_lineno=104,
              end_col_offset=54),
            ctx=Load(),
            lineno=104,
            col_offset=38,
            end_lineno=104,
            end_col_offset=55),
          lineno=104,
          col_offset=4,
          end_lineno=105,
          end_col_offset=28)],
      decorator_list=[],
      lineno=42,
      col_offset=0,
      end_lineno=105,
      end_col_offset=28),
    ClassDef(
      name='BlockGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=108,
          col_offset=21,
          end_lineno=108,
          end_col_offset=32)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='count',
            ctx=Store(),
            lineno=109,
            col_offset=4,
            end_lineno=109,
            end_col_offset=9),
          annotation=Name(
            id='int',
            ctx=Load(),
            lineno=109,
            col_offset=12,
            end_lineno=109,
            end_col_offset=15),
          value=Constant(
            value=0,
            lineno=109,
            col_offset=18,
            end_lineno=109,
            end_col_offset=19),
          simple=1,
          lineno=109,
          col_offset=4,
          end_lineno=109,
          end_col_offset=19),
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=111,
                col_offset=17,
                end_lineno=111,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=111,
                  col_offset=32,
                  end_lineno=111,
                  end_col_offset=35),
                lineno=111,
                col_offset=23,
                end_lineno=111,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=111,
                col_offset=38,
                end_lineno=111,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=112,
                  col_offset=8,
                  end_lineno=112,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=112,
                col_offset=8,
                end_lineno=112,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=112,
                  col_offset=24,
                  end_lineno=112,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=112,
                  col_offset=29,
                  end_lineno=112,
                  end_col_offset=43),
                ctx=Load(),
                lineno=112,
                col_offset=24,
                end_lineno=112,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=112,
                col_offset=47,
                end_lineno=112,
                end_col_offset=49),
              simple=0,
              lineno=112,
              col_offset=8,
              end_lineno=112,
              end_col_offset=49),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=113,
                    col_offset=8,
                    end_lineno=113,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=113,
                  col_offset=8,
                  end_lineno=113,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=113,
                col_offset=22,
                end_lineno=113,
                end_col_offset=28),
              lineno=113,
              col_offset=8,
              end_lineno=113,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=111,
            col_offset=45,
            end_lineno=111,
            end_col_offset=49),
          lineno=111,
          col_offset=4,
          end_lineno=113,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='cls',
                lineno=116,
                col_offset=15,
                end_lineno=116,
                end_col_offset=18)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Assign(
              targets=[
                Name(
                  id='value',
                  ctx=Store(),
                  lineno=117,
                  col_offset=8,
                  end_lineno=117,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=117,
                  col_offset=16,
                  end_lineno=117,
                  end_col_offset=19),
                attr='count',
                ctx=Load(),
                lineno=117,
                col_offset=16,
                end_lineno=117,
                end_col_offset=25),
              lineno=117,
              col_offset=8,
              end_lineno=117,
              end_col_offset=25),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=118,
                  col_offset=8,
                  end_lineno=118,
                  end_col_offset=11),
                attr='count',
                ctx=Store(),
                lineno=118,
                col_offset=8,
                end_lineno=118,
                end_col_offset=17),
              op=Add(),
              value=Constant(
                value=1,
                lineno=118,
                col_offset=20,
                end_lineno=118,
                end_col_offset=21),
              lineno=118,
              col_offset=8,
              end_lineno=118,
              end_col_offset=21),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=119,
                col_offset=15,
                end_lineno=119,
                end_col_offset=20),
              lineno=119,
              col_offset=8,
              end_lineno=119,
              end_col_offset=20)],
          decorator_list=[
            Name(
              id='classmethod',
              ctx=Load(),
              lineno=115,
              col_offset=5,
              end_lineno=115,
              end_col_offset=16)],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=116,
            col_offset=23,
            end_lineno=116,
            end_col_offset=26),
          lineno=116,
          col_offset=4,
          end_lineno=119,
          end_col_offset=20),
        FunctionDef(
          name='visit_Module',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=121,
                col_offset=21,
                end_lineno=121,
                end_col_offset=25),
              arg(
                arg='block_node',
                annotation=Name(
                  id='Module',
                  ctx=Load(),
                  lineno=121,
                  col_offset=39,
                  end_lineno=121,
                  end_col_offset=45),
                lineno=121,
                col_offset=27,
                end_lineno=121,
                end_col_offset=45)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we might want a subgraph, so parse content',
                lineno=122,
                col_offset=8,
                end_lineno=122,
                end_col_offset=73),
              lineno=122,
              col_offset=8,
              end_lineno=122,
              end_col_offset=73),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=123,
                  col_offset=8,
                  end_lineno=123,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=123,
                  col_offset=25,
                  end_lineno=123,
                  end_col_offset=38),
                args=[],
                keywords=[],
                lineno=123,
                col_offset=25,
                end_lineno=123,
                end_col_offset=40),
              lineno=123,
              col_offset=8,
              end_lineno=123,
              end_col_offset=40),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=124,
                col_offset=12,
                end_lineno=124,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=124,
                  col_offset=27,
                  end_lineno=124,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=124,
                col_offset=27,
                end_lineno=124,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=125,
                        col_offset=12,
                        end_lineno=125,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=125,
                      col_offset=12,
                      end_lineno=125,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=125,
                          col_offset=38,
                          end_lineno=125,
                          end_col_offset=49),
                        lineno=125,
                        col_offset=33,
                        end_lineno=125,
                        end_col_offset=49)],
                    lineno=125,
                    col_offset=12,
                    end_lineno=125,
                    end_col_offset=50),
                  lineno=125,
                  col_offset=12,
                  end_lineno=125,
                  end_col_offset=50)],
              orelse=[],
              lineno=124,
              col_offset=8,
              end_lineno=125,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=127,
                  col_offset=8,
                  end_lineno=127,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidModule',
                  ctx=Load(),
                  lineno=127,
                  col_offset=24,
                  end_lineno=127,
                  end_col_offset=37),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=128,
                      col_offset=23,
                      end_lineno=128,
                      end_col_offset=33),
                    lineno=128,
                    col_offset=12,
                    end_lineno=128,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=129,
                              col_offset=35,
                              end_lineno=129,
                              end_col_offset=39),
                            attr='prefix',
                            ctx=Load(),
                            lineno=129,
                            col_offset=35,
                            end_lineno=129,
                            end_col_offset=46),
                          conversion=-1,
                          lineno=129,
                          col_offset=32,
                          end_lineno=129,
                          end_col_offset=75),
                        Constant(
                          value='_m',
                          lineno=129,
                          col_offset=32,
                          end_lineno=129,
                          end_col_offset=75),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='BlockGenerator',
                                ctx=Load(),
                                lineno=129,
                                col_offset=50,
                                end_lineno=129,
                                end_col_offset=64),
                              attr='_count',
                              ctx=Load(),
                              lineno=129,
                              col_offset=50,
                              end_lineno=129,
                              end_col_offset=71),
                            args=[],
                            keywords=[],
                            lineno=129,
                            col_offset=50,
                            end_lineno=129,
                            end_col_offset=73),
                          conversion=-1,
                          lineno=129,
                          col_offset=32,
                          end_lineno=129,
                          end_col_offset=75)],
                      lineno=129,
                      col_offset=32,
                      end_lineno=129,
                      end_col_offset=75),
                    lineno=129,
                    col_offset=12,
                    end_lineno=129,
                    end_col_offset=75),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=130,
                          col_offset=29,
                          end_lineno=130,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=130,
                        col_offset=29,
                        end_lineno=130,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=130,
                      col_offset=29,
                      end_lineno=130,
                      end_col_offset=66),
                    lineno=130,
                    col_offset=12,
                    end_lineno=130,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Constant(
                      value='module',
                      lineno=131,
                      col_offset=25,
                      end_lineno=131,
                      end_col_offset=33),
                    lineno=131,
                    col_offset=12,
                    end_lineno=131,
                    end_col_offset=33)],
                lineno=127,
                col_offset=24,
                end_lineno=132,
                end_col_offset=9),
              lineno=127,
              col_offset=8,
              end_lineno=132,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=134,
                      col_offset=8,
                      end_lineno=134,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=134,
                    col_offset=8,
                    end_lineno=134,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=134,
                  col_offset=8,
                  end_lineno=134,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=134,
                    col_offset=29,
                    end_lineno=134,
                    end_col_offset=42)],
                keywords=[],
                lineno=134,
                col_offset=8,
                end_lineno=134,
                end_col_offset=43),
              lineno=134,
              col_offset=8,
              end_lineno=134,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=121,
            col_offset=50,
            end_lineno=121,
            end_col_offset=53),
          lineno=121,
          col_offset=4,
          end_lineno=134,
          end_col_offset=43),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=136,
                col_offset=26,
                end_lineno=136,
                end_col_offset=30),
              arg(
                arg='block_node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=136,
                  col_offset=44,
                  end_lineno=136,
                  end_col_offset=55),
                lineno=136,
                col_offset=32,
                end_lineno=136,
                end_col_offset=55)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=137,
                col_offset=8,
                end_lineno=137,
                end_col_offset=67),
              lineno=137,
              col_offset=8,
              end_lineno=137,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='mermaid_safe_name',
                  ctx=Store(),
                  lineno=138,
                  col_offset=8,
                  end_lineno=138,
                  end_col_offset=25)],
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=138,
                        col_offset=31,
                        end_lineno=138,
                        end_col_offset=35),
                      attr='prefix',
                      ctx=Load(),
                      lineno=138,
                      col_offset=31,
                      end_lineno=138,
                      end_col_offset=42),
                    conversion=-1,
                    lineno=138,
                    col_offset=28,
                    end_lineno=138,
                    end_col_offset=71),
                  Constant(
                    value='_f',
                    lineno=138,
                    col_offset=28,
                    end_lineno=138,
                    end_col_offset=71),
                  FormattedValue(
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='BlockGenerator',
                          ctx=Load(),
                          lineno=138,
                          col_offset=46,
                          end_lineno=138,
                          end_col_offset=60),
                        attr='_count',
                        ctx=Load(),
                        lineno=138,
                        col_offset=46,
                        end_lineno=138,
                        end_col_offset=67),
                      args=[],
                      keywords=[],
                      lineno=138,
                      col_offset=46,
                      end_lineno=138,
                      end_col_offset=69),
                    conversion=-1,
                    lineno=138,
                    col_offset=28,
                    end_lineno=138,
                    end_col_offset=71)],
                lineno=138,
                col_offset=28,
                end_lineno=138,
                end_col_offset=71),
              lineno=138,
              col_offset=8,
              end_lineno=138,
              end_col_offset=71),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=139,
                  col_offset=8,
                  end_lineno=139,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=139,
                  col_offset=25,
                  end_lineno=139,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=139,
                      col_offset=46,
                      end_lineno=139,
                      end_col_offset=63),
                    lineno=139,
                    col_offset=39,
                    end_lineno=139,
                    end_col_offset=63)],
                lineno=139,
                col_offset=25,
                end_lineno=139,
                end_col_offset=64),
              lineno=139,
              col_offset=8,
              end_lineno=139,
              end_col_offset=64),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=140,
                col_offset=12,
                end_lineno=140,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=140,
                  col_offset=27,
                  end_lineno=140,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=140,
                col_offset=27,
                end_lineno=140,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=141,
                        col_offset=12,
                        end_lineno=141,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=141,
                      col_offset=12,
                      end_lineno=141,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=141,
                          col_offset=38,
                          end_lineno=141,
                          end_col_offset=49),
                        lineno=141,
                        col_offset=33,
                        end_lineno=141,
                        end_col_offset=49)],
                    lineno=141,
                    col_offset=12,
                    end_lineno=141,
                    end_col_offset=50),
                  lineno=141,
                  col_offset=12,
                  end_lineno=141,
                  end_col_offset=50)],
              orelse=[],
              lineno=140,
              col_offset=8,
              end_lineno=141,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=143,
                  col_offset=8,
                  end_lineno=143,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidFunction',
                  ctx=Load(),
                  lineno=143,
                  col_offset=24,
                  end_lineno=143,
                  end_col_offset=39),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=144,
                      col_offset=23,
                      end_lineno=144,
                      end_col_offset=33),
                    lineno=144,
                    col_offset=12,
                    end_lineno=144,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=145,
                      col_offset=32,
                      end_lineno=145,
                      end_col_offset=49),
                    lineno=145,
                    col_offset=12,
                    end_lineno=145,
                    end_col_offset=49),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=146,
                          col_offset=29,
                          end_lineno=146,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=146,
                        col_offset=29,
                        end_lineno=146,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=146,
                      col_offset=29,
                      end_lineno=146,
                      end_col_offset=66),
                    lineno=146,
                    col_offset=12,
                    end_lineno=146,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=JoinedStr(
                      values=[
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='self',
                              ctx=Load(),
                              lineno=147,
                              col_offset=28,
                              end_lineno=147,
                              end_col_offset=32),
                            attr='prefix',
                            ctx=Load(),
                            lineno=147,
                            col_offset=28,
                            end_lineno=147,
                            end_col_offset=39),
                          conversion=-1,
                          lineno=147,
                          col_offset=25,
                          end_lineno=147,
                          end_col_offset=59),
                        Constant(
                          value='_',
                          lineno=147,
                          col_offset=25,
                          end_lineno=147,
                          end_col_offset=59),
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='block_node',
                              ctx=Load(),
                              lineno=147,
                              col_offset=42,
                              end_lineno=147,
                              end_col_offset=52),
                            attr='name',
                            ctx=Load(),
                            lineno=147,
                            col_offset=42,
                            end_lineno=147,
                            end_col_offset=57),
                          conversion=-1,
                          lineno=147,
                          col_offset=25,
                          end_lineno=147,
                          end_col_offset=59)],
                      lineno=147,
                      col_offset=25,
                      end_lineno=147,
                      end_col_offset=59),
                    lineno=147,
                    col_offset=12,
                    end_lineno=147,
                    end_col_offset=59)],
                lineno=143,
                col_offset=24,
                end_lineno=148,
                end_col_offset=9),
              lineno=143,
              col_offset=8,
              end_lineno=148,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=150,
                      col_offset=8,
                      end_lineno=150,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=150,
                    col_offset=8,
                    end_lineno=150,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=150,
                  col_offset=8,
                  end_lineno=150,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=150,
                    col_offset=29,
                    end_lineno=150,
                    end_col_offset=42)],
                keywords=[],
                lineno=150,
                col_offset=8,
                end_lineno=150,
                end_col_offset=43),
              lineno=150,
              col_offset=8,
              end_lineno=150,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=136,
            col_offset=60,
            end_lineno=136,
            end_col_offset=63),
          lineno=136,
          col_offset=4,
          end_lineno=150,
          end_col_offset=43),
        FunctionDef(
          name='visit_ClassDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=152,
                col_offset=23,
                end_lineno=152,
                end_col_offset=27),
              arg(
                arg='block_node',
                annotation=Name(
                  id='ClassDef',
                  ctx=Load(),
                  lineno=152,
                  col_offset=41,
                  end_lineno=152,
                  end_col_offset=49),
                lineno=152,
                col_offset=29,
                end_lineno=152,
                end_col_offset=49)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=153,
                col_offset=8,
                end_lineno=153,
                end_col_offset=67),
              lineno=153,
              col_offset=8,
              end_lineno=153,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='mermaid_safe_name',
                  ctx=Store(),
                  lineno=154,
                  col_offset=8,
                  end_lineno=154,
                  end_col_offset=25)],
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=154,
                        col_offset=31,
                        end_lineno=154,
                        end_col_offset=35),
                      attr='prefix',
                      ctx=Load(),
                      lineno=154,
                      col_offset=31,
                      end_lineno=154,
                      end_col_offset=42),
                    conversion=-1,
                    lineno=154,
                    col_offset=28,
                    end_lineno=154,
                    end_col_offset=71),
                  Constant(
                    value='_c',
                    lineno=154,
                    col_offset=28,
                    end_lineno=154,
                    end_col_offset=71),
                  FormattedValue(
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='BlockGenerator',
                          ctx=Load(),
                          lineno=154,
                          col_offset=46,
                          end_lineno=154,
                          end_col_offset=60),
                        attr='_count',
                        ctx=Load(),
                        lineno=154,
                        col_offset=46,
                        end_lineno=154,
                        end_col_offset=67),
                      args=[],
                      keywords=[],
                      lineno=154,
                      col_offset=46,
                      end_lineno=154,
                      end_col_offset=69),
                    conversion=-1,
                    lineno=154,
                    col_offset=28,
                    end_lineno=154,
                    end_col_offset=71)],
                lineno=154,
                col_offset=28,
                end_lineno=154,
                end_col_offset=71),
              lineno=154,
              col_offset=8,
              end_lineno=154,
              end_col_offset=71),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=155,
                  col_offset=8,
                  end_lineno=155,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=155,
                  col_offset=25,
                  end_lineno=155,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=155,
                      col_offset=46,
                      end_lineno=155,
                      end_col_offset=63),
                    lineno=155,
                    col_offset=39,
                    end_lineno=155,
                    end_col_offset=63)],
                lineno=155,
                col_offset=25,
                end_lineno=155,
                end_col_offset=64),
              lineno=155,
              col_offset=8,
              end_lineno=155,
              end_col_offset=64),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=156,
                col_offset=12,
                end_lineno=156,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=156,
                  col_offset=27,
                  end_lineno=156,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=156,
                col_offset=27,
                end_lineno=156,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=157,
                        col_offset=12,
                        end_lineno=157,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=157,
                      col_offset=12,
                      end_lineno=157,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=157,
                          col_offset=38,
                          end_lineno=157,
                          end_col_offset=49),
                        lineno=157,
                        col_offset=33,
                        end_lineno=157,
                        end_col_offset=49)],
                    lineno=157,
                    col_offset=12,
                    end_lineno=157,
                    end_col_offset=50),
                  lineno=157,
                  col_offset=12,
                  end_lineno=157,
                  end_col_offset=50)],
              orelse=[],
              lineno=156,
              col_offset=8,
              end_lineno=157,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=159,
                  col_offset=8,
                  end_lineno=159,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidClass',
                  ctx=Load(),
                  lineno=159,
                  col_offset=24,
                  end_lineno=159,
                  end_col_offset=36),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=160,
                      col_offset=23,
                      end_lineno=160,
                      end_col_offset=33),
                    lineno=160,
                    col_offset=12,
                    end_lineno=160,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=161,
                      col_offset=32,
                      end_lineno=161,
                      end_col_offset=49),
                    lineno=161,
                    col_offset=12,
                    end_lineno=161,
                    end_col_offset=49),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=162,
                          col_offset=29,
                          end_lineno=162,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=162,
                        col_offset=29,
                        end_lineno=162,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=162,
                      col_offset=29,
                      end_lineno=162,
                      end_col_offset=66),
                    lineno=162,
                    col_offset=12,
                    end_lineno=162,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Name(
                        id='block_node',
                        ctx=Load(),
                        lineno=163,
                        col_offset=25,
                        end_lineno=163,
                        end_col_offset=35),
                      attr='name',
                      ctx=Load(),
                      lineno=163,
                      col_offset=25,
                      end_lineno=163,
                      end_col_offset=40),
                    lineno=163,
                    col_offset=12,
                    end_lineno=163,
                    end_col_offset=40)],
                lineno=159,
                col_offset=24,
                end_lineno=164,
                end_col_offset=9),
              lineno=159,
              col_offset=8,
              end_lineno=164,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=166,
                      col_offset=8,
                      end_lineno=166,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=166,
                    col_offset=8,
                    end_lineno=166,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=166,
                  col_offset=8,
                  end_lineno=166,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=166,
                    col_offset=29,
                    end_lineno=166,
                    end_col_offset=42)],
                keywords=[],
                lineno=166,
                col_offset=8,
                end_lineno=166,
                end_col_offset=43),
              lineno=166,
              col_offset=8,
              end_lineno=166,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=152,
            col_offset=54,
            end_lineno=152,
            end_col_offset=57),
          lineno=152,
          col_offset=4,
          end_lineno=166,
          end_col_offset=43),
        FunctionDef(
          name='visit_For',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=168,
                col_offset=18,
                end_lineno=168,
                end_col_offset=22),
              arg(
                arg='block_node',
                annotation=Name(
                  id='For',
                  ctx=Load(),
                  lineno=168,
                  col_offset=36,
                  end_lineno=168,
                  end_col_offset=39),
                lineno=168,
                col_offset=24,
                end_lineno=168,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=169,
                col_offset=8,
                end_lineno=169,
                end_col_offset=67),
              lineno=169,
              col_offset=8,
              end_lineno=169,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='mermaid_safe_name',
                  ctx=Store(),
                  lineno=170,
                  col_offset=8,
                  end_lineno=170,
                  end_col_offset=25)],
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=170,
                        col_offset=31,
                        end_lineno=170,
                        end_col_offset=35),
                      attr='prefix',
                      ctx=Load(),
                      lineno=170,
                      col_offset=31,
                      end_lineno=170,
                      end_col_offset=42),
                    conversion=-1,
                    lineno=170,
                    col_offset=28,
                    end_lineno=170,
                    end_col_offset=71),
                  Constant(
                    value='_l',
                    lineno=170,
                    col_offset=28,
                    end_lineno=170,
                    end_col_offset=71),
                  FormattedValue(
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='BlockGenerator',
                          ctx=Load(),
                          lineno=170,
                          col_offset=46,
                          end_lineno=170,
                          end_col_offset=60),
                        attr='_count',
                        ctx=Load(),
                        lineno=170,
                        col_offset=46,
                        end_lineno=170,
                        end_col_offset=67),
                      args=[],
                      keywords=[],
                      lineno=170,
                      col_offset=46,
                      end_lineno=170,
                      end_col_offset=69),
                    conversion=-1,
                    lineno=170,
                    col_offset=28,
                    end_lineno=170,
                    end_col_offset=71)],
                lineno=170,
                col_offset=28,
                end_lineno=170,
                end_col_offset=71),
              lineno=170,
              col_offset=8,
              end_lineno=170,
              end_col_offset=71),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=171,
                  col_offset=8,
                  end_lineno=171,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=171,
                  col_offset=25,
                  end_lineno=171,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=171,
                      col_offset=46,
                      end_lineno=171,
                      end_col_offset=63),
                    lineno=171,
                    col_offset=39,
                    end_lineno=171,
                    end_col_offset=63)],
                lineno=171,
                col_offset=25,
                end_lineno=171,
                end_col_offset=64),
              lineno=171,
              col_offset=8,
              end_lineno=171,
              end_col_offset=64),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=172,
                col_offset=12,
                end_lineno=172,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=172,
                  col_offset=27,
                  end_lineno=172,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=172,
                col_offset=27,
                end_lineno=172,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=173,
                        col_offset=12,
                        end_lineno=173,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=173,
                      col_offset=12,
                      end_lineno=173,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=173,
                          col_offset=38,
                          end_lineno=173,
                          end_col_offset=49),
                        lineno=173,
                        col_offset=33,
                        end_lineno=173,
                        end_col_offset=49)],
                    lineno=173,
                    col_offset=12,
                    end_lineno=173,
                    end_col_offset=50),
                  lineno=173,
                  col_offset=12,
                  end_lineno=173,
                  end_col_offset=50)],
              orelse=[],
              lineno=172,
              col_offset=8,
              end_lineno=173,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='for_loop_elements',
                  ctx=Store(),
                  lineno=175,
                  col_offset=8,
                  end_lineno=175,
                  end_col_offset=25)],
              value=Call(
                func=Attribute(
                  value=Name(
                    id='link_generator',
                    ctx=Load(),
                    lineno=175,
                    col_offset=28,
                    end_lineno=175,
                    end_col_offset=42),
                  attr='get_list_of_elements',
                  ctx=Load(),
                  lineno=175,
                  col_offset=28,
                  end_lineno=175,
                  end_col_offset=63),
                args=[],
                keywords=[],
                lineno=175,
                col_offset=28,
                end_lineno=175,
                end_col_offset=65),
              lineno=175,
              col_offset=8,
              end_lineno=175,
              end_col_offset=65),
            Assign(
              targets=[
                Name(
                  id='loop_start',
                  ctx=Store(),
                  lineno=178,
                  col_offset=8,
                  end_lineno=178,
                  end_col_offset=18)],
              value=Subscript(
                value=Name(
                  id='for_loop_elements',
                  ctx=Load(),
                  lineno=178,
                  col_offset=21,
                  end_lineno=178,
                  end_col_offset=38),
                slice=Constant(
                  value=0,
                  lineno=178,
                  col_offset=39,
                  end_lineno=178,
                  end_col_offset=40),
                ctx=Load(),
                lineno=178,
                col_offset=21,
                end_lineno=178,
                end_col_offset=41),
              lineno=178,
              col_offset=8,
              end_lineno=178,
              end_col_offset=41),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=179,
                  col_offset=11,
                  end_lineno=179,
                  end_col_offset=21),
                args=[
                  Name(
                    id='loop_start',
                    ctx=Load(),
                    lineno=179,
                    col_offset=22,
                    end_lineno=179,
                    end_col_offset=32),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=179,
                    col_offset=34,
                    end_lineno=179,
                    end_col_offset=45)],
                keywords=[],
                lineno=179,
                col_offset=11,
                end_lineno=179,
                end_col_offset=46),
              body=[
                Assign(
                  targets=[
                    Name(
                      id='loop_start',
                      ctx=Store(),
                      lineno=180,
                      col_offset=12,
                      end_lineno=180,
                      end_col_offset=22)],
                  value=Attribute(
                    value=Name(
                      id='loop_start',
                      ctx=Load(),
                      lineno=180,
                      col_offset=25,
                      end_lineno=180,
                      end_col_offset=35),
                    attr='from_',
                    ctx=Load(),
                    lineno=180,
                    col_offset=25,
                    end_lineno=180,
                    end_col_offset=41),
                  lineno=180,
                  col_offset=12,
                  end_lineno=180,
                  end_col_offset=41)],
              orelse=[],
              lineno=179,
              col_offset=8,
              end_lineno=180,
              end_col_offset=41),
            Assign(
              targets=[
                Name(
                  id='loop_end',
                  ctx=Store(),
                  lineno=181,
                  col_offset=8,
                  end_lineno=181,
                  end_col_offset=16)],
              value=Subscript(
                value=Name(
                  id='for_loop_elements',
                  ctx=Load(),
                  lineno=181,
                  col_offset=19,
                  end_lineno=181,
                  end_col_offset=36),
                slice=UnaryOp(
                  op=USub(),
                  operand=Constant(
                    value=1,
                    lineno=181,
                    col_offset=38,
                    end_lineno=181,
                    end_col_offset=39),
                  lineno=181,
                  col_offset=37,
                  end_lineno=181,
                  end_col_offset=39),
                ctx=Load(),
                lineno=181,
                col_offset=19,
                end_lineno=181,
                end_col_offset=40),
              lineno=181,
              col_offset=8,
              end_lineno=181,
              end_col_offset=40),
            If(
              test=Call(
                func=Name(
                  id='isinstance',
                  ctx=Load(),
                  lineno=182,
                  col_offset=11,
                  end_lineno=182,
                  end_col_offset=21),
                args=[
                  Name(
                    id='loop_end',
                    ctx=Load(),
                    lineno=182,
                    col_offset=22,
                    end_lineno=182,
                    end_col_offset=30),
                  Name(
                    id='MermaidLink',
                    ctx=Load(),
                    lineno=182,
                    col_offset=32,
                    end_lineno=182,
                    end_col_offset=43)],
                keywords=[],
                lineno=182,
                col_offset=11,
                end_lineno=182,
                end_col_offset=44),
              body=[
                Assign(
                  targets=[
                    Name(
                      id='loop_end',
                      ctx=Store(),
                      lineno=183,
                      col_offset=12,
                      end_lineno=183,
                      end_col_offset=20)],
                  value=Attribute(
                    value=Name(
                      id='loop_end',
                      ctx=Load(),
                      lineno=183,
                      col_offset=23,
                      end_lineno=183,
                      end_col_offset=31),
                    attr='to',
                    ctx=Load(),
                    lineno=183,
                    col_offset=23,
                    end_lineno=183,
                    end_col_offset=34),
                  lineno=183,
                  col_offset=12,
                  end_lineno=183,
                  end_col_offset=34)],
              orelse=[],
              lineno=182,
              col_offset=8,
              end_lineno=183,
              end_col_offset=34),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=189,
                  col_offset=8,
                  end_lineno=189,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidFor',
                  ctx=Load(),
                  lineno=189,
                  col_offset=24,
                  end_lineno=189,
                  end_col_offset=34),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=190,
                      col_offset=23,
                      end_lineno=190,
                      end_col_offset=33),
                    lineno=190,
                    col_offset=12,
                    end_lineno=190,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=191,
                      col_offset=32,
                      end_lineno=191,
                      end_col_offset=49),
                    lineno=191,
                    col_offset=12,
                    end_lineno=191,
                    end_col_offset=49),
                  keyword(
                    arg='block_contents',
                    value=Name(
                      id='for_loop_elements',
                      ctx=Load(),
                      lineno=192,
                      col_offset=29,
                      end_lineno=192,
                      end_col_offset=46),
                    lineno=192,
                    col_offset=12,
                    end_lineno=192,
                    end_col_offset=46),
                  keyword(
                    arg='display_name',
                    value=Call(
                      func=Name(
                        id='unparse',
                        ctx=Load(),
                        lineno=193,
                        col_offset=25,
                        end_lineno=193,
                        end_col_offset=32),
                      args=[
                        Attribute(
                          value=Name(
                            id='block_node',
                            ctx=Load(),
                            lineno=193,
                            col_offset=33,
                            end_lineno=193,
                            end_col_offset=43),
                          attr='target',
                          ctx=Load(),
                          lineno=193,
                          col_offset=33,
                          end_lineno=193,
                          end_col_offset=50)],
                      keywords=[],
                      lineno=193,
                      col_offset=25,
                      end_lineno=193,
                      end_col_offset=51),
                    lineno=193,
                    col_offset=12,
                    end_lineno=193,
                    end_col_offset=51),
                  keyword(
                    arg='target',
                    value=Call(
                      func=Name(
                        id='unparse',
                        ctx=Load(),
                        lineno=194,
                        col_offset=21,
                        end_lineno=194,
                        end_col_offset=28),
                      args=[
                        Attribute(
                          value=Name(
                            id='block_node',
                            ctx=Load(),
                            lineno=194,
                            col_offset=29,
                            end_lineno=194,
                            end_col_offset=39),
                          attr='target',
                          ctx=Load(),
                          lineno=194,
                          col_offset=29,
                          end_lineno=194,
                          end_col_offset=46)],
                      keywords=[],
                      lineno=194,
                      col_offset=21,
                      end_lineno=194,
                      end_col_offset=47),
                    lineno=194,
                    col_offset=12,
                    end_lineno=194,
                    end_col_offset=47),
                  keyword(
                    arg='iterator',
                    value=Call(
                      func=Name(
                        id='unparse',
                        ctx=Load(),
                        lineno=195,
                        col_offset=23,
                        end_lineno=195,
                        end_col_offset=30),
                      args=[
                        Attribute(
                          value=Name(
                            id='block_node',
                            ctx=Load(),
                            lineno=195,
                            col_offset=31,
                            end_lineno=195,
                            end_col_offset=41),
                          attr='iter',
                          ctx=Load(),
                          lineno=195,
                          col_offset=31,
                          end_lineno=195,
                          end_col_offset=46)],
                      keywords=[],
                      lineno=195,
                      col_offset=23,
                      end_lineno=195,
                      end_col_offset=47),
                    lineno=195,
                    col_offset=12,
                    end_lineno=195,
                    end_col_offset=47)],
                lineno=189,
                col_offset=24,
                end_lineno=196,
                end_col_offset=9),
              lineno=189,
              col_offset=8,
              end_lineno=196,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=197,
                      col_offset=8,
                      end_lineno=197,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=197,
                    col_offset=8,
                    end_lineno=197,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=197,
                  col_offset=8,
                  end_lineno=197,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=197,
                    col_offset=29,
                    end_lineno=197,
                    end_col_offset=42)],
                keywords=[],
                lineno=197,
                col_offset=8,
                end_lineno=197,
                end_col_offset=43),
              lineno=197,
              col_offset=8,
              end_lineno=197,
              end_col_offset=43),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=200,
                      col_offset=8,
                      end_lineno=200,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=200,
                    col_offset=8,
                    end_lineno=200,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=200,
                  col_offset=8,
                  end_lineno=200,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Name(
                      id='MermaidLink',
                      ctx=Load(),
                      lineno=200,
                      col_offset=29,
                      end_lineno=200,
                      end_col_offset=40),
                    args=[],
                    keywords=[
                      keyword(
                        arg='from_',
                        value=Name(
                          id='loop_end',
                          ctx=Load(),
                          lineno=200,
                          col_offset=47,
                          end_lineno=200,
                          end_col_offset=55),
                        lineno=200,
                        col_offset=41,
                        end_lineno=200,
                        end_col_offset=55),
                      keyword(
                        arg='to',
                        value=Name(
                          id='loop_start',
                          ctx=Load(),
                          lineno=200,
                          col_offset=60,
                          end_lineno=200,
                          end_col_offset=70),
                        lineno=200,
                        col_offset=57,
                        end_lineno=200,
                        end_col_offset=70)],
                    lineno=200,
                    col_offset=29,
                    end_lineno=200,
                    end_col_offset=71)],
                keywords=[],
                lineno=200,
                col_offset=8,
                end_lineno=200,
                end_col_offset=72),
              lineno=200,
              col_offset=8,
              end_lineno=200,
              end_col_offset=72)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=168,
            col_offset=44,
            end_lineno=168,
            end_col_offset=47),
          lineno=168,
          col_offset=4,
          end_lineno=200,
          end_col_offset=72),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=202,
                col_offset=22,
                end_lineno=202,
                end_col_offset=26),
              arg(
                arg='_node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=202,
                  col_offset=35,
                  end_lineno=202,
                  end_col_offset=38),
                lineno=202,
                col_offset=28,
                end_lineno=202,
                end_col_offset=38)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='Non block nodes are not interesting here',
                lineno=203,
                col_offset=8,
                end_lineno=203,
                end_col_offset=54),
              lineno=203,
              col_offset=8,
              end_lineno=203,
              end_col_offset=54),
            Pass(
              lineno=204,
              col_offset=8,
              end_lineno=204,
              end_col_offset=12)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=202,
            col_offset=43,
            end_lineno=202,
            end_col_offset=46),
          lineno=202,
          col_offset=4,
          end_lineno=204,
          end_col_offset=12),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=206,
                col_offset=29,
                end_lineno=206,
                end_col_offset=33)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Return(
              value=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=207,
                  col_offset=15,
                  end_lineno=207,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=207,
                col_offset=15,
                end_lineno=207,
                end_col_offset=28),
              lineno=207,
              col_offset=8,
              end_lineno=207,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=206,
              col_offset=38,
              end_lineno=206,
              end_col_offset=42),
            slice=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=206,
              col_offset=43,
              end_lineno=206,
              end_col_offset=57),
            ctx=Load(),
            lineno=206,
            col_offset=38,
            end_lineno=206,
            end_col_offset=58),
          lineno=206,
          col_offset=4,
          end_lineno=207,
          end_col_offset=28)],
      decorator_list=[],
      lineno=108,
      col_offset=0,
      end_lineno=207,
      end_col_offset=28)],
  type_ignores=[])
```
</details>

