# ./src/pyremaid/ast_tools/visitors.py

### Imports

  - ast.AST
  - ast.ClassDef
  - ast.FunctionDef
  - ast.Import
  - ast.ImportFrom
  - ast.Module
  - ast.NodeVisitor
  - [models.MermaidClass](/docs/pyremaid/models.py.md)
  - [models.MermaidElement](/docs/pyremaid/models.py.md)
  - [models.MermaidFunction](/docs/pyremaid/models.py.md)
  - [models.MermaidLink](/docs/pyremaid/models.py.md)
  - [models.MermaidModule](/docs/pyremaid/models.py.md)
  - [models.MermaidNode](/docs/pyremaid/models.py.md)
  - typing.Any
  - typing.Optional

---
```mermaid
flowchart TB
  _c24_f25_n888["AnnAssign"]
  _c24_f25_n889["Attribute"]
  _c24_f25_n890["Name"]
  _c24_f25_n891["Load"]
  _c24_f25_n892["Store"]
  _c24_f25_n893["Subscript"]
  _c24_f25_n894["Name"]
  _c24_f25_n895["Load"]
  _c24_f25_n896["Name"]
  _c24_f25_n897["Load"]
  _c24_f25_n898["Load"]
  _c24_f25_n899["List"]
  _c24_f25_n900["Load"]
  _c24_f26_n901["For"]
  _c24_f26_n902["Name"]
  _c24_f26_n903["Store"]
  _c24_f26_n904["Attribute"]
  _c24_f26_n905["Name"]
  _c24_f26_n906["Load"]
  _c24_f26_n907["Load"]
  _c24_f26_n908["Expr"]
  _c24_f26_n909["Call"]
  _c24_f26_n910["Attribute"]
  _c24_f26_n911["Attribute"]
  _c24_f26_n912["Name"]
  _c24_f26_n913["Load"]
  _c24_f26_n914["Load"]
  _c24_f26_n915["Load"]
  _c24_f26_n916["JoinedStr"]
  _c24_f26_n917["FormattedValue"]
  _c24_f26_n918["Attribute"]
  _c24_f26_n919["Name"]
  _c24_f26_n920["Load"]
  _c24_f26_n921["Load"]
  _c24_f26_n922["Constant"]
  _c24_f27_n923["Assign"]
  _c24_f27_n924["Name"]
  _c24_f27_n925["Store"]
  _c24_f27_n926["Attribute"]
  _c24_f27_n927["Name"]
  _c24_f27_n928["Load"]
  _c24_f27_n929["Load"]
  _c24_f27_n930["For"]
  _c24_f27_n931["Name"]
  _c24_f27_n932["Store"]
  _c24_f27_n933["Attribute"]
  _c24_f27_n934["Name"]
  _c24_f27_n935["Load"]
  _c24_f27_n936["Load"]
  _c24_f27_n937["Expr"]
  _c24_f27_n938["Call"]
  _c24_f27_n939["Attribute"]
  _c24_f27_n940["Attribute"]
  _c24_f27_n941["Name"]
  _c24_f27_n942["Load"]
  _c24_f27_n943["Load"]
  _c24_f27_n944["Load"]
  _c24_f27_n945["JoinedStr"]
  _c24_f27_n946["FormattedValue"]
  _c24_f27_n947["Name"]
  _c24_f27_n948["Load"]
  _c24_f27_n949["Constant"]
  _c24_f27_n950["FormattedValue"]
  _c24_f27_n951["Attribute"]
  _c24_f27_n952["Name"]
  _c24_f27_n953["Load"]
  _c24_f27_n954["Load"]
  _c24_f28_n955["Return"]
  _c24_f28_n956["Attribute"]
  _c24_f28_n957["Name"]
  _c24_f28_n958["Load"]
  _c24_f28_n959["Load"]
  _c29_n960["AnnAssign"]
  _c29_n961["Name"]
  _c29_n962["Store"]
  _c29_n963["Name"]
  _c29_n964["Load"]
  _c29_n965["Constant"]
  _c29_f30_n966["AnnAssign"]
  _c29_f30_n967["Attribute"]
  _c29_f30_n968["Name"]
  _c29_f30_n969["Load"]
  _c29_f30_n970["Store"]
  _c29_f30_n971["Subscript"]
  _c29_f30_n972["Name"]
  _c29_f30_n973["Load"]
  _c29_f30_n974["Name"]
  _c29_f30_n975["Load"]
  _c29_f30_n976["Load"]
  _c29_f30_n977["List"]
  _c29_f30_n978["Load"]
  _c29_f30_n979["AnnAssign"]
  _c29_f30_n980["Attribute"]
  _c29_f30_n981["Name"]
  _c29_f30_n982["Load"]
  _c29_f30_n983["Store"]
  _c29_f30_n984["Subscript"]
  _c29_f30_n985["Name"]
  _c29_f30_n986["Load"]
  _c29_f30_n987["Name"]
  _c29_f30_n988["Load"]
  _c29_f30_n989["Load"]
  _c29_f30_n990["Constant"]
  _c29_f30_n991["Assign"]
  _c29_f30_n992["Attribute"]
  _c29_f30_n993["Name"]
  _c29_f30_n994["Load"]
  _c29_f30_n995["Store"]
  _c29_f30_n996["Name"]
  _c29_f30_n997["Load"]
  _c29_f31_n998["Assign"]
  _c29_f31_n999["Name"]
  _c29_f31_n1000["Store"]
  _c29_f31_n1001["Attribute"]
  _c29_f31_n1002["Name"]
  _c29_f31_n1003["Load"]
  _c29_f31_n1004["Load"]
  _c29_f31_n1005["AugAssign"]
  _c29_f31_n1006["Attribute"]
  _c29_f31_n1007["Name"]
  _c29_f31_n1008["Load"]
  _c29_f31_n1009["Store"]
  _c29_f31_n1010["Add"]
  _c29_f31_n1011["Constant"]
  _c29_f31_n1012["Return"]
  _c29_f31_n1013["Name"]
  _c29_f31_n1014["Load"]
  _c29_f34_n1017["Assign"]
  _c29_f34_n1018["Name"]
  _c29_f34_n1019["Store"]
  _c29_f34_n1020["Call"]
  _c29_f34_n1021["Name"]
  _c29_f34_n1022["Load"]
  _c29_f34_n1023["keyword"]
  _c29_f34_n1024["Attribute"]
  _c29_f34_n1025["Name"]
  _c29_f34_n1026["Load"]
  _c29_f34_n1027["Load"]
  _c29_f34_n1028["Expr"]
  _c29_f34_n1029["Call"]
  _c29_f34_n1030["Attribute"]
  _c29_f34_n1031["Name"]
  _c29_f34_n1032["Load"]
  _c29_f34_n1033["Load"]
  _c29_f34_n1034["Name"]
  _c29_f34_n1035["Load"]
  _c29_f34_n1036["Expr"]
  _c29_f34_n1037["Call"]
  _c29_f34_n1038["Attribute"]
  _c29_f34_n1039["Attribute"]
  _c29_f34_n1040["Name"]
  _c29_f34_n1041["Load"]
  _c29_f34_n1042["Load"]
  _c29_f34_n1043["Load"]
  _c29_f34_n1044["Call"]
  _c29_f34_n1045["Attribute"]
  _c29_f34_n1046["Name"]
  _c29_f34_n1047["Load"]
  _c29_f34_n1048["Load"]
  _c29_f35_n1049["Assign"]
  _c29_f35_n1050["Name"]
  _c29_f35_n1051["Store"]
  _c29_f35_n1052["Call"]
  _c29_f35_n1053["Name"]
  _c29_f35_n1054["Load"]
  _c29_f35_n1055["keyword"]
  _c29_f35_n1056["Attribute"]
  _c29_f35_n1057["Name"]
  _c29_f35_n1058["Load"]
  _c29_f35_n1059["Load"]
  _c29_f35_n1060["Expr"]
  _c29_f35_n1061["Call"]
  _c29_f35_n1062["Attribute"]
  _c29_f35_n1063["Name"]
  _c29_f35_n1064["Load"]
  _c29_f35_n1065["Load"]
  _c29_f35_n1066["Name"]
  _c29_f35_n1067["Load"]
  _c29_f35_n1068["Expr"]
  _c29_f35_n1069["Call"]
  _c29_f35_n1070["Attribute"]
  _c29_f35_n1071["Attribute"]
  _c29_f35_n1072["Name"]
  _c29_f35_n1073["Load"]
  _c29_f35_n1074["Load"]
  _c29_f35_n1075["Load"]
  _c29_f35_n1076["Call"]
  _c29_f35_n1077["Attribute"]
  _c29_f35_n1078["Name"]
  _c29_f35_n1079["Load"]
  _c29_f35_n1080["Load"]
  _c29_f36_n1081["Assign"]
  _c29_f36_n1082["Name"]
  _c29_f36_n1083["Store"]
  _c29_f36_n1084["Call"]
  _c29_f36_n1085["Name"]
  _c29_f36_n1086["Load"]
  _c29_f36_n1087["keyword"]
  _c29_f36_n1088["Name"]
  _c29_f36_n1089["Load"]
  _c29_f36_n1090["keyword"]
  _c29_f36_n1091["JoinedStr"]
  _c29_f36_n1092["FormattedValue"]
  _c29_f36_n1093["Attribute"]
  _c29_f36_n1094["Name"]
  _c29_f36_n1095["Load"]
  _c29_f36_n1096["Load"]
  _c29_f36_n1097["Constant"]
  _c29_f36_n1098["FormattedValue"]
  _c29_f36_n1099["Call"]
  _c29_f36_n1100["Attribute"]
  _c29_f36_n1101["Name"]
  _c29_f36_n1102["Load"]
  _c29_f36_n1103["Load"]
  _c29_f36_n1104["keyword"]
  _c29_f36_n1105["Attribute"]
  _c29_f36_n1106["Call"]
  _c29_f36_n1107["Name"]
  _c29_f36_n1108["Load"]
  _c29_f36_n1109["Name"]
  _c29_f36_n1110["Load"]
  _c29_f36_n1111["Load"]
  _c29_f36_n1112["If"]
  _c29_f36_n1113["Attribute"]
  _c29_f36_n1114["Name"]
  _c29_f36_n1115["Load"]
  _c29_f36_n1116["Load"]
  _c29_f36_n1117["Expr"]
  _c29_f36_n1118["Call"]
  _c29_f36_n1119["Attribute"]
  _c29_f36_n1120["Attribute"]
  _c29_f36_n1121["Name"]
  _c29_f36_n1122["Load"]
  _c29_f36_n1123["Load"]
  _c29_f36_n1124["Load"]
  _c29_f36_n1125["Call"]
  _c29_f36_n1126["Name"]
  _c29_f36_n1127["Load"]
  _c29_f36_n1128["keyword"]
  _c29_f36_n1129["Attribute"]
  _c29_f36_n1130["Name"]
  _c29_f36_n1131["Load"]
  _c29_f36_n1132["Load"]
  _c29_f36_n1133["keyword"]
  _c29_f36_n1134["Name"]
  _c29_f36_n1135["Load"]
  _c29_f36_n1136["Assign"]
  _c29_f36_n1137["Attribute"]
  _c29_f36_n1138["Name"]
  _c29_f36_n1139["Load"]
  _c29_f36_n1140["Store"]
  _c29_f36_n1141["Name"]
  _c29_f36_n1142["Load"]
  _c29_f36_n1143["Return"]
  _c29_f36_n1144["Call"]
  _c29_f36_n1145["Attribute"]
  _c29_f36_n1146["Call"]
  _c29_f36_n1147["Name"]
  _c29_f36_n1148["Load"]
  _c29_f36_n1149["Load"]
  _c29_f36_n1150["Name"]
  _c29_f36_n1151["Load"]
  _c29_f37_n1152["Return"]
  _c29_f37_n1153["Attribute"]
  _c29_f37_n1154["Name"]
  _c29_f37_n1155["Load"]
  _c29_f37_n1156["Load"]
  _c38_n1157["AnnAssign"]
  _c38_n1158["Name"]
  _c38_n1159["Store"]
  _c38_n1160["Name"]
  _c38_n1161["Load"]
  _c38_n1162["Constant"]
  _c38_f39_n1163["AnnAssign"]
  _c38_f39_n1164["Attribute"]
  _c38_f39_n1165["Name"]
  _c38_f39_n1166["Load"]
  _c38_f39_n1167["Store"]
  _c38_f39_n1168["Subscript"]
  _c38_f39_n1169["Name"]
  _c38_f39_n1170["Load"]
  _c38_f39_n1171["Name"]
  _c38_f39_n1172["Load"]
  _c38_f39_n1173["Load"]
  _c38_f39_n1174["List"]
  _c38_f39_n1175["Load"]
  _c38_f39_n1176["Assign"]
  _c38_f39_n1177["Attribute"]
  _c38_f39_n1178["Name"]
  _c38_f39_n1179["Load"]
  _c38_f39_n1180["Store"]
  _c38_f39_n1181["Name"]
  _c38_f39_n1182["Load"]
  _c38_f40_n1183["Assign"]
  _c38_f40_n1184["Name"]
  _c38_f40_n1185["Store"]
  _c38_f40_n1186["Attribute"]
  _c38_f40_n1187["Name"]
  _c38_f40_n1188["Load"]
  _c38_f40_n1189["Load"]
  _c38_f40_n1190["AugAssign"]
  _c38_f40_n1191["Attribute"]
  _c38_f40_n1192["Name"]
  _c38_f40_n1193["Load"]
  _c38_f40_n1194["Store"]
  _c38_f40_n1195["Add"]
  _c38_f40_n1196["Constant"]
  _c38_f40_n1197["Return"]
  _c38_f40_n1198["Name"]
  _c38_f40_n1199["Load"]
  _c38_f41_n1200["Expr"]
  _c38_f41_n1201["Constant"]
  _c38_f41_n1202["Assign"]
  _c38_f41_n1203["Name"]
  _c38_f41_n1204["Store"]
  _c38_f41_n1205["Call"]
  _c38_f41_n1206["Name"]
  _c38_f41_n1207["Load"]
  _c38_f41_n1208["For"]
  _c38_f41_n1209["Name"]
  _c38_f41_n1210["Store"]
  _c38_f41_n1211["Attribute"]
  _c38_f41_n1212["Name"]
  _c38_f41_n1213["Load"]
  _c38_f41_n1214["Load"]
  _c38_f41_n1215["Expr"]
  _c38_f41_n1216["Call"]
  _c38_f41_n1217["Attribute"]
  _c38_f41_n1218["Name"]
  _c38_f41_n1219["Load"]
  _c38_f41_n1220["Load"]
  _c38_f41_n1221["keyword"]
  _c38_f41_n1222["Name"]
  _c38_f41_n1223["Load"]
  _c38_f41_n1224["Assign"]
  _c38_f41_n1225["Name"]
  _c38_f41_n1226["Store"]
  _c38_f41_n1227["Call"]
  _c38_f41_n1228["Name"]
  _c38_f41_n1229["Load"]
  _c38_f41_n1230["keyword"]
  _c38_f41_n1231["Name"]
  _c38_f41_n1232["Load"]
  _c38_f41_n1233["keyword"]
  _c38_f41_n1234["JoinedStr"]
  _c38_f41_n1235["FormattedValue"]
  _c38_f41_n1236["Attribute"]
  _c38_f41_n1237["Name"]
  _c38_f41_n1238["Load"]
  _c38_f41_n1239["Load"]
  _c38_f41_n1240["Constant"]
  _c38_f41_n1241["FormattedValue"]
  _c38_f41_n1242["Call"]
  _c38_f41_n1243["Attribute"]
  _c38_f41_n1244["Name"]
  _c38_f41_n1245["Load"]
  _c38_f41_n1246["Load"]
  _c38_f41_n1247["keyword"]
  _c38_f41_n1248["Call"]
  _c38_f41_n1249["Attribute"]
  _c38_f41_n1250["Name"]
  _c38_f41_n1251["Load"]
  _c38_f41_n1252["Load"]
  _c38_f41_n1253["keyword"]
  _c38_f41_n1254["Constant"]
  _c38_f41_n1255["Expr"]
  _c38_f41_n1256["Call"]
  _c38_f41_n1257["Attribute"]
  _c38_f41_n1258["Attribute"]
  _c38_f41_n1259["Name"]
  _c38_f41_n1260["Load"]
  _c38_f41_n1261["Load"]
  _c38_f41_n1262["Load"]
  _c38_f41_n1263["Name"]
  _c38_f41_n1264["Load"]
  _c38_f42_n1265["Expr"]
  _c38_f42_n1266["Constant"]
  _c38_f42_n1267["Assign"]
  _c38_f42_n1268["Name"]
  _c38_f42_n1269["Store"]
  _c38_f42_n1270["JoinedStr"]
  _c38_f42_n1271["FormattedValue"]
  _c38_f42_n1272["Attribute"]
  _c38_f42_n1273["Name"]
  _c38_f42_n1274["Load"]
  _c38_f42_n1275["Load"]
  _c38_f42_n1276["Constant"]
  _c38_f42_n1277["FormattedValue"]
  _c38_f42_n1278["Call"]
  _c38_f42_n1279["Attribute"]
  _c38_f42_n1280["Name"]
  _c38_f42_n1281["Load"]
  _c38_f42_n1282["Load"]
  _c38_f42_n1283["Assign"]
  _c38_f42_n1284["Name"]
  _c38_f42_n1285["Store"]
  _c38_f42_n1286["Call"]
  _c38_f42_n1287["Name"]
  _c38_f42_n1288["Load"]
  _c38_f42_n1289["keyword"]
  _c38_f42_n1290["Name"]
  _c38_f42_n1291["Load"]
  _c38_f42_n1292["For"]
  _c38_f42_n1293["Name"]
  _c38_f42_n1294["Store"]
  _c38_f42_n1295["Attribute"]
  _c38_f42_n1296["Name"]
  _c38_f42_n1297["Load"]
  _c38_f42_n1298["Load"]
  _c38_f42_n1299["Expr"]
  _c38_f42_n1300["Call"]
  _c38_f42_n1301["Attribute"]
  _c38_f42_n1302["Name"]
  _c38_f42_n1303["Load"]
  _c38_f42_n1304["Load"]
  _c38_f42_n1305["keyword"]
  _c38_f42_n1306["Name"]
  _c38_f42_n1307["Load"]
  _c38_f42_n1308["Assign"]
  _c38_f42_n1309["Name"]
  _c38_f42_n1310["Store"]
  _c38_f42_n1311["Call"]
  _c38_f42_n1312["Name"]
  _c38_f42_n1313["Load"]
  _c38_f42_n1314["keyword"]
  _c38_f42_n1315["Name"]
  _c38_f42_n1316["Load"]
  _c38_f42_n1317["keyword"]
  _c38_f42_n1318["Name"]
  _c38_f42_n1319["Load"]
  _c38_f42_n1320["keyword"]
  _c38_f42_n1321["Call"]
  _c38_f42_n1322["Attribute"]
  _c38_f42_n1323["Name"]
  _c38_f42_n1324["Load"]
  _c38_f42_n1325["Load"]
  _c38_f42_n1326["keyword"]
  _c38_f42_n1327["JoinedStr"]
  _c38_f42_n1328["FormattedValue"]
  _c38_f42_n1329["Attribute"]
  _c38_f42_n1330["Name"]
  _c38_f42_n1331["Load"]
  _c38_f42_n1332["Load"]
  _c38_f42_n1333["Constant"]
  _c38_f42_n1334["FormattedValue"]
  _c38_f42_n1335["Attribute"]
  _c38_f42_n1336["Name"]
  _c38_f42_n1337["Load"]
  _c38_f42_n1338["Load"]
  _c38_f42_n1339["Expr"]
  _c38_f42_n1340["Call"]
  _c38_f42_n1341["Attribute"]
  _c38_f42_n1342["Attribute"]
  _c38_f42_n1343["Name"]
  _c38_f42_n1344["Load"]
  _c38_f42_n1345["Load"]
  _c38_f42_n1346["Load"]
  _c38_f42_n1347["Name"]
  _c38_f42_n1348["Load"]
  _c38_f43_n1349["Expr"]
  _c38_f43_n1350["Constant"]
  _c38_f43_n1351["Assign"]
  _c38_f43_n1352["Name"]
  _c38_f43_n1353["Store"]
  _c38_f43_n1354["JoinedStr"]
  _c38_f43_n1355["FormattedValue"]
  _c38_f43_n1356["Attribute"]
  _c38_f43_n1357["Name"]
  _c38_f43_n1358["Load"]
  _c38_f43_n1359["Load"]
  _c38_f43_n1360["Constant"]
  _c38_f43_n1361["FormattedValue"]
  _c38_f43_n1362["Call"]
  _c38_f43_n1363["Attribute"]
  _c38_f43_n1364["Name"]
  _c38_f43_n1365["Load"]
  _c38_f43_n1366["Load"]
  _c38_f43_n1367["Assign"]
  _c38_f43_n1368["Name"]
  _c38_f43_n1369["Store"]
  _c38_f43_n1370["Call"]
  _c38_f43_n1371["Name"]
  _c38_f43_n1372["Load"]
  _c38_f43_n1373["keyword"]
  _c38_f43_n1374["Name"]
  _c38_f43_n1375["Load"]
  _c38_f43_n1376["For"]
  _c38_f43_n1377["Name"]
  _c38_f43_n1378["Store"]
  _c38_f43_n1379["Attribute"]
  _c38_f43_n1380["Name"]
  _c38_f43_n1381["Load"]
  _c38_f43_n1382["Load"]
  _c38_f43_n1383["Expr"]
  _c38_f43_n1384["Call"]
  _c38_f43_n1385["Attribute"]
  _c38_f43_n1386["Name"]
  _c38_f43_n1387["Load"]
  _c38_f43_n1388["Load"]
  _c38_f43_n1389["keyword"]
  _c38_f43_n1390["Name"]
  _c38_f43_n1391["Load"]
  _c38_f43_n1392["Assign"]
  _c38_f43_n1393["Name"]
  _c38_f43_n1394["Store"]
  _c38_f43_n1395["Call"]
  _c38_f43_n1396["Name"]
  _c38_f43_n1397["Load"]
  _c38_f43_n1398["keyword"]
  _c38_f43_n1399["Name"]
  _c38_f43_n1400["Load"]
  _c38_f43_n1401["keyword"]
  _c38_f43_n1402["Name"]
  _c38_f43_n1403["Load"]
  _c38_f43_n1404["keyword"]
  _c38_f43_n1405["Call"]
  _c38_f43_n1406["Attribute"]
  _c38_f43_n1407["Name"]
  _c38_f43_n1408["Load"]
  _c38_f43_n1409["Load"]
  _c38_f43_n1410["keyword"]
  _c38_f43_n1411["Attribute"]
  _c38_f43_n1412["Name"]
  _c38_f43_n1413["Load"]
  _c38_f43_n1414["Load"]
  _c38_f43_n1415["Expr"]
  _c38_f43_n1416["Call"]
  _c38_f43_n1417["Attribute"]
  _c38_f43_n1418["Attribute"]
  _c38_f43_n1419["Name"]
  _c38_f43_n1420["Load"]
  _c38_f43_n1421["Load"]
  _c38_f43_n1422["Load"]
  _c38_f43_n1423["Name"]
  _c38_f43_n1424["Load"]
  _c38_f44_n1425["Expr"]
  _c38_f44_n1426["Constant"]
  _c38_f44_n1427["Pass"]
  _c38_f45_n1428["Return"]
  _c38_f45_n1429["Attribute"]
  _c38_f45_n1430["Name"]
  _c38_f45_n1431["Load"]
  _c38_f45_n1432["Load"]

  subgraph ImportNodeFinder
    direction TB
    subgraph _c24___init__
      direction TB
      _c24_f25_n888 --> _c24_f25_n889
      _c24_f25_n889 --> _c24_f25_n890
      _c24_f25_n890 --> _c24_f25_n891
      _c24_f25_n891 --> _c24_f25_n892
      _c24_f25_n892 --> _c24_f25_n893
      _c24_f25_n893 --> _c24_f25_n894
      _c24_f25_n894 --> _c24_f25_n895
      _c24_f25_n895 --> _c24_f25_n896
      _c24_f25_n896 --> _c24_f25_n897
      _c24_f25_n897 --> _c24_f25_n898
      _c24_f25_n898 --> _c24_f25_n899
      _c24_f25_n899 --> _c24_f25_n900
    end
    subgraph _c24_visit_Import
      direction TB
      _c24_f26_n901 --> _c24_f26_n902
      _c24_f26_n902 --> _c24_f26_n903
      _c24_f26_n903 --> _c24_f26_n904
      _c24_f26_n904 --> _c24_f26_n905
      _c24_f26_n905 --> _c24_f26_n906
      _c24_f26_n906 --> _c24_f26_n907
      _c24_f26_n907 --> _c24_f26_n908
      _c24_f26_n908 --> _c24_f26_n909
      _c24_f26_n909 --> _c24_f26_n910
      _c24_f26_n910 --> _c24_f26_n911
      _c24_f26_n911 --> _c24_f26_n912
      _c24_f26_n912 --> _c24_f26_n913
      _c24_f26_n913 --> _c24_f26_n914
      _c24_f26_n914 --> _c24_f26_n915
      _c24_f26_n915 --> _c24_f26_n916
      _c24_f26_n916 --> _c24_f26_n917
      _c24_f26_n917 --> _c24_f26_n918
      _c24_f26_n918 --> _c24_f26_n919
      _c24_f26_n919 --> _c24_f26_n920
      _c24_f26_n920 --> _c24_f26_n921
      _c24_f26_n921 --> _c24_f26_n922
    end
    subgraph _c24_visit_ImportFrom
      direction TB
      _c24_f27_n923 --> _c24_f27_n924
      _c24_f27_n924 --> _c24_f27_n925
      _c24_f27_n925 --> _c24_f27_n926
      _c24_f27_n926 --> _c24_f27_n927
      _c24_f27_n927 --> _c24_f27_n928
      _c24_f27_n928 --> _c24_f27_n929
      _c24_f27_n929 --> _c24_f27_n930
      _c24_f27_n930 --> _c24_f27_n931
      _c24_f27_n931 --> _c24_f27_n932
      _c24_f27_n932 --> _c24_f27_n933
      _c24_f27_n933 --> _c24_f27_n934
      _c24_f27_n934 --> _c24_f27_n935
      _c24_f27_n935 --> _c24_f27_n936
      _c24_f27_n936 --> _c24_f27_n937
      _c24_f27_n937 --> _c24_f27_n938
      _c24_f27_n938 --> _c24_f27_n939
      _c24_f27_n939 --> _c24_f27_n940
      _c24_f27_n940 --> _c24_f27_n941
      _c24_f27_n941 --> _c24_f27_n942
      _c24_f27_n942 --> _c24_f27_n943
      _c24_f27_n943 --> _c24_f27_n944
      _c24_f27_n944 --> _c24_f27_n945
      _c24_f27_n945 --> _c24_f27_n946
      _c24_f27_n946 --> _c24_f27_n947
      _c24_f27_n947 --> _c24_f27_n948
      _c24_f27_n948 --> _c24_f27_n949
      _c24_f27_n949 --> _c24_f27_n950
      _c24_f27_n950 --> _c24_f27_n951
      _c24_f27_n951 --> _c24_f27_n952
      _c24_f27_n952 --> _c24_f27_n953
      _c24_f27_n953 --> _c24_f27_n954
    end
    subgraph _c24_get_found_imports
      direction TB
      _c24_f28_n955 --> _c24_f28_n956
      _c24_f28_n956 --> _c24_f28_n957
      _c24_f28_n957 --> _c24_f28_n958
      _c24_f28_n958 --> _c24_f28_n959
    end
  end
  subgraph LinkGenerator
    direction TB
    _c29_n960 --> _c29_n961
    _c29_n961 --> _c29_n962
    _c29_n962 --> _c29_n963
    _c29_n963 --> _c29_n964
    _c29_n964 --> _c29_n965
    subgraph _c29___init__
      direction TB
      _c29_f30_n966 --> _c29_f30_n967
      _c29_f30_n967 --> _c29_f30_n968
      _c29_f30_n968 --> _c29_f30_n969
      _c29_f30_n969 --> _c29_f30_n970
      _c29_f30_n970 --> _c29_f30_n971
      _c29_f30_n971 --> _c29_f30_n972
      _c29_f30_n972 --> _c29_f30_n973
      _c29_f30_n973 --> _c29_f30_n974
      _c29_f30_n974 --> _c29_f30_n975
      _c29_f30_n975 --> _c29_f30_n976
      _c29_f30_n976 --> _c29_f30_n977
      _c29_f30_n977 --> _c29_f30_n978
      _c29_f30_n978 --> _c29_f30_n979
      _c29_f30_n979 --> _c29_f30_n980
      _c29_f30_n980 --> _c29_f30_n981
      _c29_f30_n981 --> _c29_f30_n982
      _c29_f30_n982 --> _c29_f30_n983
      _c29_f30_n983 --> _c29_f30_n984
      _c29_f30_n984 --> _c29_f30_n985
      _c29_f30_n985 --> _c29_f30_n986
      _c29_f30_n986 --> _c29_f30_n987
      _c29_f30_n987 --> _c29_f30_n988
      _c29_f30_n988 --> _c29_f30_n989
      _c29_f30_n989 --> _c29_f30_n990
      _c29_f30_n990 --> _c29_f30_n991
      _c29_f30_n991 --> _c29_f30_n992
      _c29_f30_n992 --> _c29_f30_n993
      _c29_f30_n993 --> _c29_f30_n994
      _c29_f30_n994 --> _c29_f30_n995
      _c29_f30_n995 --> _c29_f30_n996
      _c29_f30_n996 --> _c29_f30_n997
    end
    subgraph _c29__count
      direction TB
      _c29_f31_n998 --> _c29_f31_n999
      _c29_f31_n999 --> _c29_f31_n1000
      _c29_f31_n1000 --> _c29_f31_n1001
      _c29_f31_n1001 --> _c29_f31_n1002
      _c29_f31_n1002 --> _c29_f31_n1003
      _c29_f31_n1003 --> _c29_f31_n1004
      _c29_f31_n1004 --> _c29_f31_n1005
      _c29_f31_n1005 --> _c29_f31_n1006
      _c29_f31_n1006 --> _c29_f31_n1007
      _c29_f31_n1007 --> _c29_f31_n1008
      _c29_f31_n1008 --> _c29_f31_n1009
      _c29_f31_n1009 --> _c29_f31_n1010
      _c29_f31_n1010 --> _c29_f31_n1011
      _c29_f31_n1011 --> _c29_f31_n1012
      _c29_f31_n1012 --> _c29_f31_n1013
      _c29_f31_n1013 --> _c29_f31_n1014
    end
    subgraph _c29_visit_Import
      direction TB
    end
    subgraph _c29_visit_ImportFrom
      direction TB
    end
    subgraph _c29_visit_FunctionDef
      direction TB
      _c29_f34_n1017 --> _c29_f34_n1018
      _c29_f34_n1018 --> _c29_f34_n1019
      _c29_f34_n1019 --> _c29_f34_n1020
      _c29_f34_n1020 --> _c29_f34_n1021
      _c29_f34_n1021 --> _c29_f34_n1022
      _c29_f34_n1022 --> _c29_f34_n1023
      _c29_f34_n1023 --> _c29_f34_n1024
      _c29_f34_n1024 --> _c29_f34_n1025
      _c29_f34_n1025 --> _c29_f34_n1026
      _c29_f34_n1026 --> _c29_f34_n1027
      _c29_f34_n1027 --> _c29_f34_n1028
      _c29_f34_n1028 --> _c29_f34_n1029
      _c29_f34_n1029 --> _c29_f34_n1030
      _c29_f34_n1030 --> _c29_f34_n1031
      _c29_f34_n1031 --> _c29_f34_n1032
      _c29_f34_n1032 --> _c29_f34_n1033
      _c29_f34_n1033 --> _c29_f34_n1034
      _c29_f34_n1034 --> _c29_f34_n1035
      _c29_f34_n1035 --> _c29_f34_n1036
      _c29_f34_n1036 --> _c29_f34_n1037
      _c29_f34_n1037 --> _c29_f34_n1038
      _c29_f34_n1038 --> _c29_f34_n1039
      _c29_f34_n1039 --> _c29_f34_n1040
      _c29_f34_n1040 --> _c29_f34_n1041
      _c29_f34_n1041 --> _c29_f34_n1042
      _c29_f34_n1042 --> _c29_f34_n1043
      _c29_f34_n1043 --> _c29_f34_n1044
      _c29_f34_n1044 --> _c29_f34_n1045
      _c29_f34_n1045 --> _c29_f34_n1046
      _c29_f34_n1046 --> _c29_f34_n1047
      _c29_f34_n1047 --> _c29_f34_n1048
    end
    subgraph _c29_visit_ClassDef
      direction TB
      _c29_f35_n1049 --> _c29_f35_n1050
      _c29_f35_n1050 --> _c29_f35_n1051
      _c29_f35_n1051 --> _c29_f35_n1052
      _c29_f35_n1052 --> _c29_f35_n1053
      _c29_f35_n1053 --> _c29_f35_n1054
      _c29_f35_n1054 --> _c29_f35_n1055
      _c29_f35_n1055 --> _c29_f35_n1056
      _c29_f35_n1056 --> _c29_f35_n1057
      _c29_f35_n1057 --> _c29_f35_n1058
      _c29_f35_n1058 --> _c29_f35_n1059
      _c29_f35_n1059 --> _c29_f35_n1060
      _c29_f35_n1060 --> _c29_f35_n1061
      _c29_f35_n1061 --> _c29_f35_n1062
      _c29_f35_n1062 --> _c29_f35_n1063
      _c29_f35_n1063 --> _c29_f35_n1064
      _c29_f35_n1064 --> _c29_f35_n1065
      _c29_f35_n1065 --> _c29_f35_n1066
      _c29_f35_n1066 --> _c29_f35_n1067
      _c29_f35_n1067 --> _c29_f35_n1068
      _c29_f35_n1068 --> _c29_f35_n1069
      _c29_f35_n1069 --> _c29_f35_n1070
      _c29_f35_n1070 --> _c29_f35_n1071
      _c29_f35_n1071 --> _c29_f35_n1072
      _c29_f35_n1072 --> _c29_f35_n1073
      _c29_f35_n1073 --> _c29_f35_n1074
      _c29_f35_n1074 --> _c29_f35_n1075
      _c29_f35_n1075 --> _c29_f35_n1076
      _c29_f35_n1076 --> _c29_f35_n1077
      _c29_f35_n1077 --> _c29_f35_n1078
      _c29_f35_n1078 --> _c29_f35_n1079
      _c29_f35_n1079 --> _c29_f35_n1080
    end
    subgraph _c29_generic_visit
      direction TB
      _c29_f36_n1081 --> _c29_f36_n1082
      _c29_f36_n1082 --> _c29_f36_n1083
      _c29_f36_n1083 --> _c29_f36_n1084
      _c29_f36_n1084 --> _c29_f36_n1085
      _c29_f36_n1085 --> _c29_f36_n1086
      _c29_f36_n1086 --> _c29_f36_n1087
      _c29_f36_n1087 --> _c29_f36_n1088
      _c29_f36_n1088 --> _c29_f36_n1089
      _c29_f36_n1089 --> _c29_f36_n1090
      _c29_f36_n1090 --> _c29_f36_n1091
      _c29_f36_n1091 --> _c29_f36_n1092
      _c29_f36_n1092 --> _c29_f36_n1093
      _c29_f36_n1093 --> _c29_f36_n1094
      _c29_f36_n1094 --> _c29_f36_n1095
      _c29_f36_n1095 --> _c29_f36_n1096
      _c29_f36_n1096 --> _c29_f36_n1097
      _c29_f36_n1097 --> _c29_f36_n1098
      _c29_f36_n1098 --> _c29_f36_n1099
      _c29_f36_n1099 --> _c29_f36_n1100
      _c29_f36_n1100 --> _c29_f36_n1101
      _c29_f36_n1101 --> _c29_f36_n1102
      _c29_f36_n1102 --> _c29_f36_n1103
      _c29_f36_n1103 --> _c29_f36_n1104
      _c29_f36_n1104 --> _c29_f36_n1105
      _c29_f36_n1105 --> _c29_f36_n1106
      _c29_f36_n1106 --> _c29_f36_n1107
      _c29_f36_n1107 --> _c29_f36_n1108
      _c29_f36_n1108 --> _c29_f36_n1109
      _c29_f36_n1109 --> _c29_f36_n1110
      _c29_f36_n1110 --> _c29_f36_n1111
      _c29_f36_n1111 --> _c29_f36_n1112
      _c29_f36_n1112 --> _c29_f36_n1113
      _c29_f36_n1113 --> _c29_f36_n1114
      _c29_f36_n1114 --> _c29_f36_n1115
      _c29_f36_n1115 --> _c29_f36_n1116
      _c29_f36_n1116 --> _c29_f36_n1117
      _c29_f36_n1117 --> _c29_f36_n1118
      _c29_f36_n1118 --> _c29_f36_n1119
      _c29_f36_n1119 --> _c29_f36_n1120
      _c29_f36_n1120 --> _c29_f36_n1121
      _c29_f36_n1121 --> _c29_f36_n1122
      _c29_f36_n1122 --> _c29_f36_n1123
      _c29_f36_n1123 --> _c29_f36_n1124
      _c29_f36_n1124 --> _c29_f36_n1125
      _c29_f36_n1125 --> _c29_f36_n1126
      _c29_f36_n1126 --> _c29_f36_n1127
      _c29_f36_n1127 --> _c29_f36_n1128
      _c29_f36_n1128 --> _c29_f36_n1129
      _c29_f36_n1129 --> _c29_f36_n1130
      _c29_f36_n1130 --> _c29_f36_n1131
      _c29_f36_n1131 --> _c29_f36_n1132
      _c29_f36_n1132 --> _c29_f36_n1133
      _c29_f36_n1133 --> _c29_f36_n1134
      _c29_f36_n1134 --> _c29_f36_n1135
      _c29_f36_n1135 --> _c29_f36_n1136
      _c29_f36_n1136 --> _c29_f36_n1137
      _c29_f36_n1137 --> _c29_f36_n1138
      _c29_f36_n1138 --> _c29_f36_n1139
      _c29_f36_n1139 --> _c29_f36_n1140
      _c29_f36_n1140 --> _c29_f36_n1141
      _c29_f36_n1141 --> _c29_f36_n1142
      _c29_f36_n1142 --> _c29_f36_n1143
      _c29_f36_n1143 --> _c29_f36_n1144
      _c29_f36_n1144 --> _c29_f36_n1145
      _c29_f36_n1145 --> _c29_f36_n1146
      _c29_f36_n1146 --> _c29_f36_n1147
      _c29_f36_n1147 --> _c29_f36_n1148
      _c29_f36_n1148 --> _c29_f36_n1149
      _c29_f36_n1149 --> _c29_f36_n1150
      _c29_f36_n1150 --> _c29_f36_n1151
    end
    subgraph _c29_get_list_of_elements
      direction TB
      _c29_f37_n1152 --> _c29_f37_n1153
      _c29_f37_n1153 --> _c29_f37_n1154
      _c29_f37_n1154 --> _c29_f37_n1155
      _c29_f37_n1155 --> _c29_f37_n1156
    end
  end
  subgraph BlockGenerator
    direction TB
    _c38_n1157 --> _c38_n1158
    _c38_n1158 --> _c38_n1159
    _c38_n1159 --> _c38_n1160
    _c38_n1160 --> _c38_n1161
    _c38_n1161 --> _c38_n1162
    subgraph _c38___init__
      direction TB
      _c38_f39_n1163 --> _c38_f39_n1164
      _c38_f39_n1164 --> _c38_f39_n1165
      _c38_f39_n1165 --> _c38_f39_n1166
      _c38_f39_n1166 --> _c38_f39_n1167
      _c38_f39_n1167 --> _c38_f39_n1168
      _c38_f39_n1168 --> _c38_f39_n1169
      _c38_f39_n1169 --> _c38_f39_n1170
      _c38_f39_n1170 --> _c38_f39_n1171
      _c38_f39_n1171 --> _c38_f39_n1172
      _c38_f39_n1172 --> _c38_f39_n1173
      _c38_f39_n1173 --> _c38_f39_n1174
      _c38_f39_n1174 --> _c38_f39_n1175
      _c38_f39_n1175 --> _c38_f39_n1176
      _c38_f39_n1176 --> _c38_f39_n1177
      _c38_f39_n1177 --> _c38_f39_n1178
      _c38_f39_n1178 --> _c38_f39_n1179
      _c38_f39_n1179 --> _c38_f39_n1180
      _c38_f39_n1180 --> _c38_f39_n1181
      _c38_f39_n1181 --> _c38_f39_n1182
    end
    subgraph _c38__count
      direction TB
      _c38_f40_n1183 --> _c38_f40_n1184
      _c38_f40_n1184 --> _c38_f40_n1185
      _c38_f40_n1185 --> _c38_f40_n1186
      _c38_f40_n1186 --> _c38_f40_n1187
      _c38_f40_n1187 --> _c38_f40_n1188
      _c38_f40_n1188 --> _c38_f40_n1189
      _c38_f40_n1189 --> _c38_f40_n1190
      _c38_f40_n1190 --> _c38_f40_n1191
      _c38_f40_n1191 --> _c38_f40_n1192
      _c38_f40_n1192 --> _c38_f40_n1193
      _c38_f40_n1193 --> _c38_f40_n1194
      _c38_f40_n1194 --> _c38_f40_n1195
      _c38_f40_n1195 --> _c38_f40_n1196
      _c38_f40_n1196 --> _c38_f40_n1197
      _c38_f40_n1197 --> _c38_f40_n1198
      _c38_f40_n1198 --> _c38_f40_n1199
    end
    subgraph _c38_visit_Module
      direction TB
      _c38_f41_n1200 --> _c38_f41_n1201
      _c38_f41_n1201 --> _c38_f41_n1202
      _c38_f41_n1202 --> _c38_f41_n1203
      _c38_f41_n1203 --> _c38_f41_n1204
      _c38_f41_n1204 --> _c38_f41_n1205
      _c38_f41_n1205 --> _c38_f41_n1206
      _c38_f41_n1206 --> _c38_f41_n1207
      _c38_f41_n1207 --> _c38_f41_n1208
      _c38_f41_n1208 --> _c38_f41_n1209
      _c38_f41_n1209 --> _c38_f41_n1210
      _c38_f41_n1210 --> _c38_f41_n1211
      _c38_f41_n1211 --> _c38_f41_n1212
      _c38_f41_n1212 --> _c38_f41_n1213
      _c38_f41_n1213 --> _c38_f41_n1214
      _c38_f41_n1214 --> _c38_f41_n1215
      _c38_f41_n1215 --> _c38_f41_n1216
      _c38_f41_n1216 --> _c38_f41_n1217
      _c38_f41_n1217 --> _c38_f41_n1218
      _c38_f41_n1218 --> _c38_f41_n1219
      _c38_f41_n1219 --> _c38_f41_n1220
      _c38_f41_n1220 --> _c38_f41_n1221
      _c38_f41_n1221 --> _c38_f41_n1222
      _c38_f41_n1222 --> _c38_f41_n1223
      _c38_f41_n1223 --> _c38_f41_n1224
      _c38_f41_n1224 --> _c38_f41_n1225
      _c38_f41_n1225 --> _c38_f41_n1226
      _c38_f41_n1226 --> _c38_f41_n1227
      _c38_f41_n1227 --> _c38_f41_n1228
      _c38_f41_n1228 --> _c38_f41_n1229
      _c38_f41_n1229 --> _c38_f41_n1230
      _c38_f41_n1230 --> _c38_f41_n1231
      _c38_f41_n1231 --> _c38_f41_n1232
      _c38_f41_n1232 --> _c38_f41_n1233
      _c38_f41_n1233 --> _c38_f41_n1234
      _c38_f41_n1234 --> _c38_f41_n1235
      _c38_f41_n1235 --> _c38_f41_n1236
      _c38_f41_n1236 --> _c38_f41_n1237
      _c38_f41_n1237 --> _c38_f41_n1238
      _c38_f41_n1238 --> _c38_f41_n1239
      _c38_f41_n1239 --> _c38_f41_n1240
      _c38_f41_n1240 --> _c38_f41_n1241
      _c38_f41_n1241 --> _c38_f41_n1242
      _c38_f41_n1242 --> _c38_f41_n1243
      _c38_f41_n1243 --> _c38_f41_n1244
      _c38_f41_n1244 --> _c38_f41_n1245
      _c38_f41_n1245 --> _c38_f41_n1246
      _c38_f41_n1246 --> _c38_f41_n1247
      _c38_f41_n1247 --> _c38_f41_n1248
      _c38_f41_n1248 --> _c38_f41_n1249
      _c38_f41_n1249 --> _c38_f41_n1250
      _c38_f41_n1250 --> _c38_f41_n1251
      _c38_f41_n1251 --> _c38_f41_n1252
      _c38_f41_n1252 --> _c38_f41_n1253
      _c38_f41_n1253 --> _c38_f41_n1254
      _c38_f41_n1254 --> _c38_f41_n1255
      _c38_f41_n1255 --> _c38_f41_n1256
      _c38_f41_n1256 --> _c38_f41_n1257
      _c38_f41_n1257 --> _c38_f41_n1258
      _c38_f41_n1258 --> _c38_f41_n1259
      _c38_f41_n1259 --> _c38_f41_n1260
      _c38_f41_n1260 --> _c38_f41_n1261
      _c38_f41_n1261 --> _c38_f41_n1262
      _c38_f41_n1262 --> _c38_f41_n1263
      _c38_f41_n1263 --> _c38_f41_n1264
    end
    subgraph _c38_visit_FunctionDef
      direction TB
      _c38_f42_n1265 --> _c38_f42_n1266
      _c38_f42_n1266 --> _c38_f42_n1267
      _c38_f42_n1267 --> _c38_f42_n1268
      _c38_f42_n1268 --> _c38_f42_n1269
      _c38_f42_n1269 --> _c38_f42_n1270
      _c38_f42_n1270 --> _c38_f42_n1271
      _c38_f42_n1271 --> _c38_f42_n1272
      _c38_f42_n1272 --> _c38_f42_n1273
      _c38_f42_n1273 --> _c38_f42_n1274
      _c38_f42_n1274 --> _c38_f42_n1275
      _c38_f42_n1275 --> _c38_f42_n1276
      _c38_f42_n1276 --> _c38_f42_n1277
      _c38_f42_n1277 --> _c38_f42_n1278
      _c38_f42_n1278 --> _c38_f42_n1279
      _c38_f42_n1279 --> _c38_f42_n1280
      _c38_f42_n1280 --> _c38_f42_n1281
      _c38_f42_n1281 --> _c38_f42_n1282
      _c38_f42_n1282 --> _c38_f42_n1283
      _c38_f42_n1283 --> _c38_f42_n1284
      _c38_f42_n1284 --> _c38_f42_n1285
      _c38_f42_n1285 --> _c38_f42_n1286
      _c38_f42_n1286 --> _c38_f42_n1287
      _c38_f42_n1287 --> _c38_f42_n1288
      _c38_f42_n1288 --> _c38_f42_n1289
      _c38_f42_n1289 --> _c38_f42_n1290
      _c38_f42_n1290 --> _c38_f42_n1291
      _c38_f42_n1291 --> _c38_f42_n1292
      _c38_f42_n1292 --> _c38_f42_n1293
      _c38_f42_n1293 --> _c38_f42_n1294
      _c38_f42_n1294 --> _c38_f42_n1295
      _c38_f42_n1295 --> _c38_f42_n1296
      _c38_f42_n1296 --> _c38_f42_n1297
      _c38_f42_n1297 --> _c38_f42_n1298
      _c38_f42_n1298 --> _c38_f42_n1299
      _c38_f42_n1299 --> _c38_f42_n1300
      _c38_f42_n1300 --> _c38_f42_n1301
      _c38_f42_n1301 --> _c38_f42_n1302
      _c38_f42_n1302 --> _c38_f42_n1303
      _c38_f42_n1303 --> _c38_f42_n1304
      _c38_f42_n1304 --> _c38_f42_n1305
      _c38_f42_n1305 --> _c38_f42_n1306
      _c38_f42_n1306 --> _c38_f42_n1307
      _c38_f42_n1307 --> _c38_f42_n1308
      _c38_f42_n1308 --> _c38_f42_n1309
      _c38_f42_n1309 --> _c38_f42_n1310
      _c38_f42_n1310 --> _c38_f42_n1311
      _c38_f42_n1311 --> _c38_f42_n1312
      _c38_f42_n1312 --> _c38_f42_n1313
      _c38_f42_n1313 --> _c38_f42_n1314
      _c38_f42_n1314 --> _c38_f42_n1315
      _c38_f42_n1315 --> _c38_f42_n1316
      _c38_f42_n1316 --> _c38_f42_n1317
      _c38_f42_n1317 --> _c38_f42_n1318
      _c38_f42_n1318 --> _c38_f42_n1319
      _c38_f42_n1319 --> _c38_f42_n1320
      _c38_f42_n1320 --> _c38_f42_n1321
      _c38_f42_n1321 --> _c38_f42_n1322
      _c38_f42_n1322 --> _c38_f42_n1323
      _c38_f42_n1323 --> _c38_f42_n1324
      _c38_f42_n1324 --> _c38_f42_n1325
      _c38_f42_n1325 --> _c38_f42_n1326
      _c38_f42_n1326 --> _c38_f42_n1327
      _c38_f42_n1327 --> _c38_f42_n1328
      _c38_f42_n1328 --> _c38_f42_n1329
      _c38_f42_n1329 --> _c38_f42_n1330
      _c38_f42_n1330 --> _c38_f42_n1331
      _c38_f42_n1331 --> _c38_f42_n1332
      _c38_f42_n1332 --> _c38_f42_n1333
      _c38_f42_n1333 --> _c38_f42_n1334
      _c38_f42_n1334 --> _c38_f42_n1335
      _c38_f42_n1335 --> _c38_f42_n1336
      _c38_f42_n1336 --> _c38_f42_n1337
      _c38_f42_n1337 --> _c38_f42_n1338
      _c38_f42_n1338 --> _c38_f42_n1339
      _c38_f42_n1339 --> _c38_f42_n1340
      _c38_f42_n1340 --> _c38_f42_n1341
      _c38_f42_n1341 --> _c38_f42_n1342
      _c38_f42_n1342 --> _c38_f42_n1343
      _c38_f42_n1343 --> _c38_f42_n1344
      _c38_f42_n1344 --> _c38_f42_n1345
      _c38_f42_n1345 --> _c38_f42_n1346
      _c38_f42_n1346 --> _c38_f42_n1347
      _c38_f42_n1347 --> _c38_f42_n1348
    end
    subgraph _c38_visit_ClassDef
      direction TB
      _c38_f43_n1349 --> _c38_f43_n1350
      _c38_f43_n1350 --> _c38_f43_n1351
      _c38_f43_n1351 --> _c38_f43_n1352
      _c38_f43_n1352 --> _c38_f43_n1353
      _c38_f43_n1353 --> _c38_f43_n1354
      _c38_f43_n1354 --> _c38_f43_n1355
      _c38_f43_n1355 --> _c38_f43_n1356
      _c38_f43_n1356 --> _c38_f43_n1357
      _c38_f43_n1357 --> _c38_f43_n1358
      _c38_f43_n1358 --> _c38_f43_n1359
      _c38_f43_n1359 --> _c38_f43_n1360
      _c38_f43_n1360 --> _c38_f43_n1361
      _c38_f43_n1361 --> _c38_f43_n1362
      _c38_f43_n1362 --> _c38_f43_n1363
      _c38_f43_n1363 --> _c38_f43_n1364
      _c38_f43_n1364 --> _c38_f43_n1365
      _c38_f43_n1365 --> _c38_f43_n1366
      _c38_f43_n1366 --> _c38_f43_n1367
      _c38_f43_n1367 --> _c38_f43_n1368
      _c38_f43_n1368 --> _c38_f43_n1369
      _c38_f43_n1369 --> _c38_f43_n1370
      _c38_f43_n1370 --> _c38_f43_n1371
      _c38_f43_n1371 --> _c38_f43_n1372
      _c38_f43_n1372 --> _c38_f43_n1373
      _c38_f43_n1373 --> _c38_f43_n1374
      _c38_f43_n1374 --> _c38_f43_n1375
      _c38_f43_n1375 --> _c38_f43_n1376
      _c38_f43_n1376 --> _c38_f43_n1377
      _c38_f43_n1377 --> _c38_f43_n1378
      _c38_f43_n1378 --> _c38_f43_n1379
      _c38_f43_n1379 --> _c38_f43_n1380
      _c38_f43_n1380 --> _c38_f43_n1381
      _c38_f43_n1381 --> _c38_f43_n1382
      _c38_f43_n1382 --> _c38_f43_n1383
      _c38_f43_n1383 --> _c38_f43_n1384
      _c38_f43_n1384 --> _c38_f43_n1385
      _c38_f43_n1385 --> _c38_f43_n1386
      _c38_f43_n1386 --> _c38_f43_n1387
      _c38_f43_n1387 --> _c38_f43_n1388
      _c38_f43_n1388 --> _c38_f43_n1389
      _c38_f43_n1389 --> _c38_f43_n1390
      _c38_f43_n1390 --> _c38_f43_n1391
      _c38_f43_n1391 --> _c38_f43_n1392
      _c38_f43_n1392 --> _c38_f43_n1393
      _c38_f43_n1393 --> _c38_f43_n1394
      _c38_f43_n1394 --> _c38_f43_n1395
      _c38_f43_n1395 --> _c38_f43_n1396
      _c38_f43_n1396 --> _c38_f43_n1397
      _c38_f43_n1397 --> _c38_f43_n1398
      _c38_f43_n1398 --> _c38_f43_n1399
      _c38_f43_n1399 --> _c38_f43_n1400
      _c38_f43_n1400 --> _c38_f43_n1401
      _c38_f43_n1401 --> _c38_f43_n1402
      _c38_f43_n1402 --> _c38_f43_n1403
      _c38_f43_n1403 --> _c38_f43_n1404
      _c38_f43_n1404 --> _c38_f43_n1405
      _c38_f43_n1405 --> _c38_f43_n1406
      _c38_f43_n1406 --> _c38_f43_n1407
      _c38_f43_n1407 --> _c38_f43_n1408
      _c38_f43_n1408 --> _c38_f43_n1409
      _c38_f43_n1409 --> _c38_f43_n1410
      _c38_f43_n1410 --> _c38_f43_n1411
      _c38_f43_n1411 --> _c38_f43_n1412
      _c38_f43_n1412 --> _c38_f43_n1413
      _c38_f43_n1413 --> _c38_f43_n1414
      _c38_f43_n1414 --> _c38_f43_n1415
      _c38_f43_n1415 --> _c38_f43_n1416
      _c38_f43_n1416 --> _c38_f43_n1417
      _c38_f43_n1417 --> _c38_f43_n1418
      _c38_f43_n1418 --> _c38_f43_n1419
      _c38_f43_n1419 --> _c38_f43_n1420
      _c38_f43_n1420 --> _c38_f43_n1421
      _c38_f43_n1421 --> _c38_f43_n1422
      _c38_f43_n1422 --> _c38_f43_n1423
      _c38_f43_n1423 --> _c38_f43_n1424
    end
    subgraph _c38_generic_visit
      direction TB
      _c38_f44_n1425 --> _c38_f44_n1426
      _c38_f44_n1426 --> _c38_f44_n1427
    end
    subgraph _c38_get_list_of_elements
      direction TB
      _c38_f45_n1428 --> _c38_f45_n1429
      _c38_f45_n1429 --> _c38_f45_n1430
      _c38_f45_n1430 --> _c38_f45_n1431
      _c38_f45_n1431 --> _c38_f45_n1432
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
        alias(name='FunctionDef'),
        alias(name='Import'),
        alias(name='ImportFrom'),
        alias(name='Module'),
        alias(name='NodeVisitor')],
      level=0,
      lineno=1,
      col_offset=0,
      end_lineno=1,
      end_col_offset=83),
    ImportFrom(
      module='models',
      names=[
        alias(name='MermaidClass'),
        alias(name='MermaidElement'),
        alias(name='MermaidFunction'),
        alias(name='MermaidLink'),
        alias(name='MermaidModule'),
        alias(name='MermaidNode')],
      level=0,
      lineno=2,
      col_offset=0,
      end_lineno=9,
      end_col_offset=1),
    ImportFrom(
      module='typing',
      names=[
        alias(name='Any'),
        alias(name='Optional')],
      level=0,
      lineno=11,
      col_offset=0,
      end_lineno=11,
      end_col_offset=32),
    ClassDef(
      name='ImportNodeFinder',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=14,
          col_offset=23,
          end_lineno=14,
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
                lineno=15,
                col_offset=17,
                end_lineno=15,
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
                  lineno=16,
                  col_offset=8,
                  end_lineno=16,
                  end_col_offset=12),
                attr='found_imports',
                ctx=Store(),
                lineno=16,
                col_offset=8,
                end_lineno=16,
                end_col_offset=26),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=16,
                  col_offset=29,
                  end_lineno=16,
                  end_col_offset=33),
                slice=Name(
                  id='str',
                  ctx=Load(),
                  lineno=16,
                  col_offset=34,
                  end_lineno=16,
                  end_col_offset=37),
                ctx=Load(),
                lineno=16,
                col_offset=29,
                end_lineno=16,
                end_col_offset=38),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=16,
                col_offset=41,
                end_lineno=16,
                end_col_offset=43),
              simple=0,
              lineno=16,
              col_offset=8,
              end_lineno=16,
              end_col_offset=43)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=15,
            col_offset=26,
            end_lineno=15,
            end_col_offset=30),
          lineno=15,
          col_offset=4,
          end_lineno=16,
          end_col_offset=43),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=18,
                col_offset=21,
                end_lineno=18,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=18,
                  col_offset=33,
                  end_lineno=18,
                  end_col_offset=39),
                lineno=18,
                col_offset=27,
                end_lineno=18,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=19,
                col_offset=12,
                end_lineno=19,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=19,
                  col_offset=17,
                  end_lineno=19,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=19,
                col_offset=17,
                end_lineno=19,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=20,
                          col_offset=12,
                          end_lineno=20,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=20,
                        col_offset=12,
                        end_lineno=20,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=20,
                      col_offset=12,
                      end_lineno=20,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=20,
                                col_offset=41,
                                end_lineno=20,
                                end_col_offset=42),
                              attr='name',
                              ctx=Load(),
                              lineno=20,
                              col_offset=41,
                              end_lineno=20,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=20,
                            col_offset=38,
                            end_lineno=20,
                            end_col_offset=51),
                          Constant(
                            value='.*',
                            lineno=20,
                            col_offset=38,
                            end_lineno=20,
                            end_col_offset=51)],
                        lineno=20,
                        col_offset=38,
                        end_lineno=20,
                        end_col_offset=51)],
                    keywords=[],
                    lineno=20,
                    col_offset=12,
                    end_lineno=20,
                    end_col_offset=52),
                  lineno=20,
                  col_offset=12,
                  end_lineno=20,
                  end_col_offset=52)],
              orelse=[],
              lineno=19,
              col_offset=8,
              end_lineno=20,
              end_col_offset=52)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=18,
            col_offset=44,
            end_lineno=18,
            end_col_offset=48),
          lineno=18,
          col_offset=4,
          end_lineno=20,
          end_col_offset=52),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=22,
                col_offset=25,
                end_lineno=22,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=22,
                  col_offset=37,
                  end_lineno=22,
                  end_col_offset=47),
                lineno=22,
                col_offset=31,
                end_lineno=22,
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
                  lineno=23,
                  col_offset=8,
                  end_lineno=23,
                  end_col_offset=14)],
              value=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=23,
                  col_offset=17,
                  end_lineno=23,
                  end_col_offset=21),
                attr='module',
                ctx=Load(),
                lineno=23,
                col_offset=17,
                end_lineno=23,
                end_col_offset=28),
              lineno=23,
              col_offset=8,
              end_lineno=23,
              end_col_offset=28),
            For(
              target=Name(
                id='i',
                ctx=Store(),
                lineno=24,
                col_offset=12,
                end_lineno=24,
                end_col_offset=13),
              iter=Attribute(
                value=Name(
                  id='node',
                  ctx=Load(),
                  lineno=24,
                  col_offset=17,
                  end_lineno=24,
                  end_col_offset=21),
                attr='names',
                ctx=Load(),
                lineno=24,
                col_offset=17,
                end_lineno=24,
                end_col_offset=27),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=25,
                          col_offset=12,
                          end_lineno=25,
                          end_col_offset=16),
                        attr='found_imports',
                        ctx=Load(),
                        lineno=25,
                        col_offset=12,
                        end_lineno=25,
                        end_col_offset=30),
                      attr='append',
                      ctx=Load(),
                      lineno=25,
                      col_offset=12,
                      end_lineno=25,
                      end_col_offset=37),
                    args=[
                      JoinedStr(
                        values=[
                          FormattedValue(
                            value=Name(
                              id='module',
                              ctx=Load(),
                              lineno=25,
                              col_offset=41,
                              end_lineno=25,
                              end_col_offset=47),
                            conversion=-1,
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58),
                          Constant(
                            value='.',
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58),
                          FormattedValue(
                            value=Attribute(
                              value=Name(
                                id='i',
                                ctx=Load(),
                                lineno=25,
                                col_offset=50,
                                end_lineno=25,
                                end_col_offset=51),
                              attr='name',
                              ctx=Load(),
                              lineno=25,
                              col_offset=50,
                              end_lineno=25,
                              end_col_offset=56),
                            conversion=-1,
                            lineno=25,
                            col_offset=38,
                            end_lineno=25,
                            end_col_offset=58)],
                        lineno=25,
                        col_offset=38,
                        end_lineno=25,
                        end_col_offset=58)],
                    keywords=[],
                    lineno=25,
                    col_offset=12,
                    end_lineno=25,
                    end_col_offset=59),
                  lineno=25,
                  col_offset=12,
                  end_lineno=25,
                  end_col_offset=59)],
              orelse=[],
              lineno=24,
              col_offset=8,
              end_lineno=25,
              end_col_offset=59)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=22,
            col_offset=52,
            end_lineno=22,
            end_col_offset=56),
          lineno=22,
          col_offset=4,
          end_lineno=25,
          end_col_offset=59),
        FunctionDef(
          name='get_found_imports',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=27,
                col_offset=26,
                end_lineno=27,
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
                  lineno=28,
                  col_offset=15,
                  end_lineno=28,
                  end_col_offset=19),
                attr='found_imports',
                ctx=Load(),
                lineno=28,
                col_offset=15,
                end_lineno=28,
                end_col_offset=33),
              lineno=28,
              col_offset=8,
              end_lineno=28,
              end_col_offset=33)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=27,
              col_offset=35,
              end_lineno=27,
              end_col_offset=39),
            slice=Name(
              id='str',
              ctx=Load(),
              lineno=27,
              col_offset=40,
              end_lineno=27,
              end_col_offset=43),
            ctx=Load(),
            lineno=27,
            col_offset=35,
            end_lineno=27,
            end_col_offset=44),
          lineno=27,
          col_offset=4,
          end_lineno=28,
          end_col_offset=33)],
      decorator_list=[],
      lineno=14,
      col_offset=0,
      end_lineno=28,
      end_col_offset=33),
    ClassDef(
      name='LinkGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=31,
          col_offset=20,
          end_lineno=31,
          end_col_offset=31)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='count',
            ctx=Store(),
            lineno=32,
            col_offset=4,
            end_lineno=32,
            end_col_offset=9),
          annotation=Name(
            id='int',
            ctx=Load(),
            lineno=32,
            col_offset=12,
            end_lineno=32,
            end_col_offset=15),
          value=Constant(
            value=0,
            lineno=32,
            col_offset=18,
            end_lineno=32,
            end_col_offset=19),
          simple=1,
          lineno=32,
          col_offset=4,
          end_lineno=32,
          end_col_offset=19),
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=34,
                col_offset=17,
                end_lineno=34,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=34,
                  col_offset=32,
                  end_lineno=34,
                  end_col_offset=35),
                lineno=34,
                col_offset=23,
                end_lineno=34,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=34,
                col_offset=38,
                end_lineno=34,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=35,
                  col_offset=8,
                  end_lineno=35,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=35,
                col_offset=8,
                end_lineno=35,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=35,
                  col_offset=24,
                  end_lineno=35,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=35,
                  col_offset=29,
                  end_lineno=35,
                  end_col_offset=43),
                ctx=Load(),
                lineno=35,
                col_offset=24,
                end_lineno=35,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=35,
                col_offset=47,
                end_lineno=35,
                end_col_offset=49),
              simple=0,
              lineno=35,
              col_offset=8,
              end_lineno=35,
              end_col_offset=49),
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=36,
                  col_offset=8,
                  end_lineno=36,
                  end_col_offset=12),
                attr='prev_node',
                ctx=Store(),
                lineno=36,
                col_offset=8,
                end_lineno=36,
                end_col_offset=22),
              annotation=Subscript(
                value=Name(
                  id='Optional',
                  ctx=Load(),
                  lineno=36,
                  col_offset=25,
                  end_lineno=36,
                  end_col_offset=33),
                slice=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=36,
                  col_offset=34,
                  end_lineno=36,
                  end_col_offset=37),
                ctx=Load(),
                lineno=36,
                col_offset=25,
                end_lineno=36,
                end_col_offset=38),
              value=Constant(
                value=None,
                lineno=36,
                col_offset=41,
                end_lineno=36,
                end_col_offset=45),
              simple=0,
              lineno=36,
              col_offset=8,
              end_lineno=36,
              end_col_offset=45),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=37,
                    col_offset=8,
                    end_lineno=37,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=37,
                  col_offset=8,
                  end_lineno=37,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=37,
                col_offset=22,
                end_lineno=37,
                end_col_offset=28),
              lineno=37,
              col_offset=8,
              end_lineno=37,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=34,
            col_offset=45,
            end_lineno=34,
            end_col_offset=49),
          lineno=34,
          col_offset=4,
          end_lineno=37,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='cls',
                lineno=40,
                col_offset=15,
                end_lineno=40,
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
                  lineno=41,
                  col_offset=8,
                  end_lineno=41,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=41,
                  col_offset=16,
                  end_lineno=41,
                  end_col_offset=19),
                attr='count',
                ctx=Load(),
                lineno=41,
                col_offset=16,
                end_lineno=41,
                end_col_offset=25),
              lineno=41,
              col_offset=8,
              end_lineno=41,
              end_col_offset=25),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=42,
                  col_offset=8,
                  end_lineno=42,
                  end_col_offset=11),
                attr='count',
                ctx=Store(),
                lineno=42,
                col_offset=8,
                end_lineno=42,
                end_col_offset=17),
              op=Add(),
              value=Constant(
                value=1,
                lineno=42,
                col_offset=20,
                end_lineno=42,
                end_col_offset=21),
              lineno=42,
              col_offset=8,
              end_lineno=42,
              end_col_offset=21),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=43,
                col_offset=15,
                end_lineno=43,
                end_col_offset=20),
              lineno=43,
              col_offset=8,
              end_lineno=43,
              end_col_offset=20)],
          decorator_list=[
            Name(
              id='classmethod',
              ctx=Load(),
              lineno=39,
              col_offset=5,
              end_lineno=39,
              end_col_offset=16)],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=40,
            col_offset=23,
            end_lineno=40,
            end_col_offset=26),
          lineno=40,
          col_offset=4,
          end_lineno=43,
          end_col_offset=20),
        FunctionDef(
          name='visit_Import',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=45,
                col_offset=21,
                end_lineno=45,
                end_col_offset=25),
              arg(
                arg='node',
                annotation=Name(
                  id='Import',
                  ctx=Load(),
                  lineno=45,
                  col_offset=33,
                  end_lineno=45,
                  end_col_offset=39),
                lineno=45,
                col_offset=27,
                end_lineno=45,
                end_col_offset=39)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=46,
              col_offset=8,
              end_lineno=46,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=45,
            col_offset=44,
            end_lineno=45,
            end_col_offset=48),
          lineno=45,
          col_offset=4,
          end_lineno=46,
          end_col_offset=12),
        FunctionDef(
          name='visit_ImportFrom',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=48,
                col_offset=25,
                end_lineno=48,
                end_col_offset=29),
              arg(
                arg='node',
                annotation=Name(
                  id='ImportFrom',
                  ctx=Load(),
                  lineno=48,
                  col_offset=37,
                  end_lineno=48,
                  end_col_offset=47),
                lineno=48,
                col_offset=31,
                end_lineno=48,
                end_col_offset=47)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Pass(
              lineno=49,
              col_offset=8,
              end_lineno=49,
              end_col_offset=12)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=48,
            col_offset=52,
            end_lineno=48,
            end_col_offset=56),
          lineno=48,
          col_offset=4,
          end_lineno=49,
          end_col_offset=12),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=51,
                col_offset=26,
                end_lineno=51,
                end_col_offset=30),
              arg(
                arg='node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=51,
                  col_offset=38,
                  end_lineno=51,
                  end_col_offset=49),
                lineno=51,
                col_offset=32,
                end_lineno=51,
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
                  lineno=52,
                  col_offset=8,
                  end_lineno=52,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=52,
                  col_offset=26,
                  end_lineno=52,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=52,
                        col_offset=48,
                        end_lineno=52,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=52,
                      col_offset=48,
                      end_lineno=52,
                      end_col_offset=59),
                    lineno=52,
                    col_offset=41,
                    end_lineno=52,
                    end_col_offset=59)],
                lineno=52,
                col_offset=26,
                end_lineno=52,
                end_col_offset=60),
              lineno=52,
              col_offset=8,
              end_lineno=52,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=53,
                    col_offset=8,
                    end_lineno=53,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=53,
                  col_offset=8,
                  end_lineno=53,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=53,
                    col_offset=30,
                    end_lineno=53,
                    end_col_offset=34)],
                keywords=[],
                lineno=53,
                col_offset=8,
                end_lineno=53,
                end_col_offset=35),
              lineno=53,
              col_offset=8,
              end_lineno=53,
              end_col_offset=35),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=54,
                      col_offset=8,
                      end_lineno=54,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=54,
                    col_offset=8,
                    end_lineno=54,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=54,
                  col_offset=8,
                  end_lineno=54,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Attribute(
                      value=Name(
                        id='block_generator',
                        ctx=Load(),
                        lineno=54,
                        col_offset=29,
                        end_lineno=54,
                        end_col_offset=44),
                      attr='get_list_of_elements',
                      ctx=Load(),
                      lineno=54,
                      col_offset=29,
                      end_lineno=54,
                      end_col_offset=65),
                    args=[],
                    keywords=[],
                    lineno=54,
                    col_offset=29,
                    end_lineno=54,
                    end_col_offset=67)],
                keywords=[],
                lineno=54,
                col_offset=8,
                end_lineno=54,
                end_col_offset=68),
              lineno=54,
              col_offset=8,
              end_lineno=54,
              end_col_offset=68)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=51,
            col_offset=54,
            end_lineno=51,
            end_col_offset=57),
          lineno=51,
          col_offset=4,
          end_lineno=54,
          end_col_offset=68),
        FunctionDef(
          name='visit_ClassDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=56,
                col_offset=23,
                end_lineno=56,
                end_col_offset=27),
              arg(
                arg='node',
                annotation=Name(
                  id='ClassDef',
                  ctx=Load(),
                  lineno=56,
                  col_offset=35,
                  end_lineno=56,
                  end_col_offset=43),
                lineno=56,
                col_offset=29,
                end_lineno=56,
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
                  lineno=57,
                  col_offset=8,
                  end_lineno=57,
                  end_col_offset=23)],
              value=Call(
                func=Name(
                  id='BlockGenerator',
                  ctx=Load(),
                  lineno=57,
                  col_offset=26,
                  end_lineno=57,
                  end_col_offset=40),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=57,
                        col_offset=48,
                        end_lineno=57,
                        end_col_offset=52),
                      attr='prefix',
                      ctx=Load(),
                      lineno=57,
                      col_offset=48,
                      end_lineno=57,
                      end_col_offset=59),
                    lineno=57,
                    col_offset=41,
                    end_lineno=57,
                    end_col_offset=59)],
                lineno=57,
                col_offset=26,
                end_lineno=57,
                end_col_offset=60),
              lineno=57,
              col_offset=8,
              end_lineno=57,
              end_col_offset=60),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(
                    id='block_generator',
                    ctx=Load(),
                    lineno=58,
                    col_offset=8,
                    end_lineno=58,
                    end_col_offset=23),
                  attr='visit',
                  ctx=Load(),
                  lineno=58,
                  col_offset=8,
                  end_lineno=58,
                  end_col_offset=29),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=58,
                    col_offset=30,
                    end_lineno=58,
                    end_col_offset=34)],
                keywords=[],
                lineno=58,
                col_offset=8,
                end_lineno=58,
                end_col_offset=35),
              lineno=58,
              col_offset=8,
              end_lineno=58,
              end_col_offset=35),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=59,
                      col_offset=8,
                      end_lineno=59,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=59,
                    col_offset=8,
                    end_lineno=59,
                    end_col_offset=21),
                  attr='extend',
                  ctx=Load(),
                  lineno=59,
                  col_offset=8,
                  end_lineno=59,
                  end_col_offset=28),
                args=[
                  Call(
                    func=Attribute(
                      value=Name(
                        id='block_generator',
                        ctx=Load(),
                        lineno=59,
                        col_offset=29,
                        end_lineno=59,
                        end_col_offset=44),
                      attr='get_list_of_elements',
                      ctx=Load(),
                      lineno=59,
                      col_offset=29,
                      end_lineno=59,
                      end_col_offset=65),
                    args=[],
                    keywords=[],
                    lineno=59,
                    col_offset=29,
                    end_lineno=59,
                    end_col_offset=67)],
                keywords=[],
                lineno=59,
                col_offset=8,
                end_lineno=59,
                end_col_offset=68),
              lineno=59,
              col_offset=8,
              end_lineno=59,
              end_col_offset=68)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=56,
            col_offset=48,
            end_lineno=56,
            end_col_offset=51),
          lineno=56,
          col_offset=4,
          end_lineno=59,
          end_col_offset=68),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=61,
                col_offset=22,
                end_lineno=61,
                end_col_offset=26),
              arg(
                arg='node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=61,
                  col_offset=34,
                  end_lineno=61,
                  end_col_offset=37),
                lineno=61,
                col_offset=28,
                end_lineno=61,
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
                  lineno=62,
                  col_offset=8,
                  end_lineno=62,
                  end_col_offset=20)],
              value=Call(
                func=Name(
                  id='MermaidNode',
                  ctx=Load(),
                  lineno=62,
                  col_offset=23,
                  end_lineno=62,
                  end_col_offset=34),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='node',
                      ctx=Load(),
                      lineno=63,
                      col_offset=21,
                      end_lineno=63,
                      end_col_offset=25),
                    lineno=63,
                    col_offset=12,
                    end_lineno=63,
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
                              lineno=64,
                              col_offset=33,
                              end_lineno=64,
                              end_col_offset=37),
                            attr='prefix',
                            ctx=Load(),
                            lineno=64,
                            col_offset=33,
                            end_lineno=64,
                            end_col_offset=44),
                          conversion=-1,
                          lineno=64,
                          col_offset=30,
                          end_lineno=64,
                          end_col_offset=72),
                        Constant(
                          value='_n',
                          lineno=64,
                          col_offset=30,
                          end_lineno=64,
                          end_col_offset=72),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='LinkGenerator',
                                ctx=Load(),
                                lineno=64,
                                col_offset=48,
                                end_lineno=64,
                                end_col_offset=61),
                              attr='_count',
                              ctx=Load(),
                              lineno=64,
                              col_offset=48,
                              end_lineno=64,
                              end_col_offset=68),
                            args=[],
                            keywords=[],
                            lineno=64,
                            col_offset=48,
                            end_lineno=64,
                            end_col_offset=70),
                          conversion=-1,
                          lineno=64,
                          col_offset=30,
                          end_lineno=64,
                          end_col_offset=72)],
                      lineno=64,
                      col_offset=30,
                      end_lineno=64,
                      end_col_offset=72),
                    lineno=64,
                    col_offset=12,
                    end_lineno=64,
                    end_col_offset=72),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Call(
                        func=Name(
                          id='type',
                          ctx=Load(),
                          lineno=65,
                          col_offset=25,
                          end_lineno=65,
                          end_col_offset=29),
                        args=[
                          Name(
                            id='node',
                            ctx=Load(),
                            lineno=65,
                            col_offset=30,
                            end_lineno=65,
                            end_col_offset=34)],
                        keywords=[],
                        lineno=65,
                        col_offset=25,
                        end_lineno=65,
                        end_col_offset=35),
                      attr='__name__',
                      ctx=Load(),
                      lineno=65,
                      col_offset=25,
                      end_lineno=65,
                      end_col_offset=44),
                    lineno=65,
                    col_offset=12,
                    end_lineno=65,
                    end_col_offset=44)],
                lineno=62,
                col_offset=23,
                end_lineno=66,
                end_col_offset=9),
              lineno=62,
              col_offset=8,
              end_lineno=66,
              end_col_offset=9),
            If(
              test=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=67,
                  col_offset=11,
                  end_lineno=67,
                  end_col_offset=15),
                attr='prev_node',
                ctx=Load(),
                lineno=67,
                col_offset=11,
                end_lineno=67,
                end_col_offset=25),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Attribute(
                        value=Name(
                          id='self',
                          ctx=Load(),
                          lineno=68,
                          col_offset=12,
                          end_lineno=68,
                          end_col_offset=16),
                        attr='elements',
                        ctx=Load(),
                        lineno=68,
                        col_offset=12,
                        end_lineno=68,
                        end_col_offset=25),
                      attr='append',
                      ctx=Load(),
                      lineno=68,
                      col_offset=12,
                      end_lineno=68,
                      end_col_offset=32),
                    args=[
                      Call(
                        func=Name(
                          id='MermaidLink',
                          ctx=Load(),
                          lineno=68,
                          col_offset=33,
                          end_lineno=68,
                          end_col_offset=44),
                        args=[],
                        keywords=[
                          keyword(
                            arg='from_',
                            value=Attribute(
                              value=Name(
                                id='self',
                                ctx=Load(),
                                lineno=68,
                                col_offset=51,
                                end_lineno=68,
                                end_col_offset=55),
                              attr='prev_node',
                              ctx=Load(),
                              lineno=68,
                              col_offset=51,
                              end_lineno=68,
                              end_col_offset=65),
                            lineno=68,
                            col_offset=45,
                            end_lineno=68,
                            end_col_offset=65),
                          keyword(
                            arg='to',
                            value=Name(
                              id='mermaid_data',
                              ctx=Load(),
                              lineno=68,
                              col_offset=70,
                              end_lineno=68,
                              end_col_offset=82),
                            lineno=68,
                            col_offset=67,
                            end_lineno=68,
                            end_col_offset=82)],
                        lineno=68,
                        col_offset=33,
                        end_lineno=68,
                        end_col_offset=83)],
                    keywords=[],
                    lineno=68,
                    col_offset=12,
                    end_lineno=68,
                    end_col_offset=84),
                  lineno=68,
                  col_offset=12,
                  end_lineno=68,
                  end_col_offset=84)],
              orelse=[],
              lineno=67,
              col_offset=8,
              end_lineno=68,
              end_col_offset=84),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=69,
                    col_offset=8,
                    end_lineno=69,
                    end_col_offset=12),
                  attr='prev_node',
                  ctx=Store(),
                  lineno=69,
                  col_offset=8,
                  end_lineno=69,
                  end_col_offset=22)],
              value=Name(
                id='mermaid_data',
                ctx=Load(),
                lineno=69,
                col_offset=25,
                end_lineno=69,
                end_col_offset=37),
              lineno=69,
              col_offset=8,
              end_lineno=69,
              end_col_offset=37),
            Return(
              value=Call(
                func=Attribute(
                  value=Call(
                    func=Name(
                      id='super',
                      ctx=Load(),
                      lineno=72,
                      col_offset=15,
                      end_lineno=72,
                      end_col_offset=20),
                    args=[],
                    keywords=[],
                    lineno=72,
                    col_offset=15,
                    end_lineno=72,
                    end_col_offset=22),
                  attr='generic_visit',
                  ctx=Load(),
                  lineno=72,
                  col_offset=15,
                  end_lineno=72,
                  end_col_offset=36),
                args=[
                  Name(
                    id='node',
                    ctx=Load(),
                    lineno=72,
                    col_offset=37,
                    end_lineno=72,
                    end_col_offset=41)],
                keywords=[],
                lineno=72,
                col_offset=15,
                end_lineno=72,
                end_col_offset=42),
              lineno=72,
              col_offset=8,
              end_lineno=72,
              end_col_offset=42)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=61,
            col_offset=42,
            end_lineno=61,
            end_col_offset=45),
          lineno=61,
          col_offset=4,
          end_lineno=72,
          end_col_offset=42),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=74,
                col_offset=29,
                end_lineno=74,
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
                  lineno=75,
                  col_offset=15,
                  end_lineno=75,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=75,
                col_offset=15,
                end_lineno=75,
                end_col_offset=28),
              lineno=75,
              col_offset=8,
              end_lineno=75,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=74,
              col_offset=38,
              end_lineno=74,
              end_col_offset=42),
            slice=Name(
              id='MermaidLink',
              ctx=Load(),
              lineno=74,
              col_offset=43,
              end_lineno=74,
              end_col_offset=54),
            ctx=Load(),
            lineno=74,
            col_offset=38,
            end_lineno=74,
            end_col_offset=55),
          lineno=74,
          col_offset=4,
          end_lineno=75,
          end_col_offset=28)],
      decorator_list=[],
      lineno=31,
      col_offset=0,
      end_lineno=75,
      end_col_offset=28),
    ClassDef(
      name='BlockGenerator',
      bases=[
        Name(
          id='NodeVisitor',
          ctx=Load(),
          lineno=78,
          col_offset=21,
          end_lineno=78,
          end_col_offset=32)],
      keywords=[],
      body=[
        AnnAssign(
          target=Name(
            id='count',
            ctx=Store(),
            lineno=79,
            col_offset=4,
            end_lineno=79,
            end_col_offset=9),
          annotation=Name(
            id='int',
            ctx=Load(),
            lineno=79,
            col_offset=12,
            end_lineno=79,
            end_col_offset=15),
          value=Constant(
            value=0,
            lineno=79,
            col_offset=18,
            end_lineno=79,
            end_col_offset=19),
          simple=1,
          lineno=79,
          col_offset=4,
          end_lineno=79,
          end_col_offset=19),
        FunctionDef(
          name='__init__',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=81,
                col_offset=17,
                end_lineno=81,
                end_col_offset=21),
              arg(
                arg='prefix',
                annotation=Name(
                  id='str',
                  ctx=Load(),
                  lineno=81,
                  col_offset=32,
                  end_lineno=81,
                  end_col_offset=35),
                lineno=81,
                col_offset=23,
                end_lineno=81,
                end_col_offset=35)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[
              Constant(
                value='',
                lineno=81,
                col_offset=38,
                end_lineno=81,
                end_col_offset=40)]),
          body=[
            AnnAssign(
              target=Attribute(
                value=Name(
                  id='self',
                  ctx=Load(),
                  lineno=82,
                  col_offset=8,
                  end_lineno=82,
                  end_col_offset=12),
                attr='elements',
                ctx=Store(),
                lineno=82,
                col_offset=8,
                end_lineno=82,
                end_col_offset=21),
              annotation=Subscript(
                value=Name(
                  id='list',
                  ctx=Load(),
                  lineno=82,
                  col_offset=24,
                  end_lineno=82,
                  end_col_offset=28),
                slice=Name(
                  id='MermaidElement',
                  ctx=Load(),
                  lineno=82,
                  col_offset=29,
                  end_lineno=82,
                  end_col_offset=43),
                ctx=Load(),
                lineno=82,
                col_offset=24,
                end_lineno=82,
                end_col_offset=44),
              value=List(
                elts=[],
                ctx=Load(),
                lineno=82,
                col_offset=47,
                end_lineno=82,
                end_col_offset=49),
              simple=0,
              lineno=82,
              col_offset=8,
              end_lineno=82,
              end_col_offset=49),
            Assign(
              targets=[
                Attribute(
                  value=Name(
                    id='self',
                    ctx=Load(),
                    lineno=83,
                    col_offset=8,
                    end_lineno=83,
                    end_col_offset=12),
                  attr='prefix',
                  ctx=Store(),
                  lineno=83,
                  col_offset=8,
                  end_lineno=83,
                  end_col_offset=19)],
              value=Name(
                id='prefix',
                ctx=Load(),
                lineno=83,
                col_offset=22,
                end_lineno=83,
                end_col_offset=28),
              lineno=83,
              col_offset=8,
              end_lineno=83,
              end_col_offset=28)],
          decorator_list=[],
          returns=Constant(
            value=None,
            lineno=81,
            col_offset=45,
            end_lineno=81,
            end_col_offset=49),
          lineno=81,
          col_offset=4,
          end_lineno=83,
          end_col_offset=28),
        FunctionDef(
          name='_count',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='cls',
                lineno=86,
                col_offset=15,
                end_lineno=86,
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
                  lineno=87,
                  col_offset=8,
                  end_lineno=87,
                  end_col_offset=13)],
              value=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=87,
                  col_offset=16,
                  end_lineno=87,
                  end_col_offset=19),
                attr='count',
                ctx=Load(),
                lineno=87,
                col_offset=16,
                end_lineno=87,
                end_col_offset=25),
              lineno=87,
              col_offset=8,
              end_lineno=87,
              end_col_offset=25),
            AugAssign(
              target=Attribute(
                value=Name(
                  id='cls',
                  ctx=Load(),
                  lineno=88,
                  col_offset=8,
                  end_lineno=88,
                  end_col_offset=11),
                attr='count',
                ctx=Store(),
                lineno=88,
                col_offset=8,
                end_lineno=88,
                end_col_offset=17),
              op=Add(),
              value=Constant(
                value=1,
                lineno=88,
                col_offset=20,
                end_lineno=88,
                end_col_offset=21),
              lineno=88,
              col_offset=8,
              end_lineno=88,
              end_col_offset=21),
            Return(
              value=Name(
                id='value',
                ctx=Load(),
                lineno=89,
                col_offset=15,
                end_lineno=89,
                end_col_offset=20),
              lineno=89,
              col_offset=8,
              end_lineno=89,
              end_col_offset=20)],
          decorator_list=[
            Name(
              id='classmethod',
              ctx=Load(),
              lineno=85,
              col_offset=5,
              end_lineno=85,
              end_col_offset=16)],
          returns=Name(
            id='int',
            ctx=Load(),
            lineno=86,
            col_offset=23,
            end_lineno=86,
            end_col_offset=26),
          lineno=86,
          col_offset=4,
          end_lineno=89,
          end_col_offset=20),
        FunctionDef(
          name='visit_Module',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=91,
                col_offset=21,
                end_lineno=91,
                end_col_offset=25),
              arg(
                arg='block_node',
                annotation=Name(
                  id='Module',
                  ctx=Load(),
                  lineno=91,
                  col_offset=39,
                  end_lineno=91,
                  end_col_offset=45),
                lineno=91,
                col_offset=27,
                end_lineno=91,
                end_col_offset=45)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we might want a subgraph, so parse content',
                lineno=92,
                col_offset=8,
                end_lineno=92,
                end_col_offset=73),
              lineno=92,
              col_offset=8,
              end_lineno=92,
              end_col_offset=73),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=93,
                  col_offset=8,
                  end_lineno=93,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=93,
                  col_offset=25,
                  end_lineno=93,
                  end_col_offset=38),
                args=[],
                keywords=[],
                lineno=93,
                col_offset=25,
                end_lineno=93,
                end_col_offset=40),
              lineno=93,
              col_offset=8,
              end_lineno=93,
              end_col_offset=40),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=94,
                col_offset=12,
                end_lineno=94,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=94,
                  col_offset=27,
                  end_lineno=94,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=94,
                col_offset=27,
                end_lineno=94,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=95,
                        col_offset=12,
                        end_lineno=95,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=95,
                      col_offset=12,
                      end_lineno=95,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=95,
                          col_offset=38,
                          end_lineno=95,
                          end_col_offset=49),
                        lineno=95,
                        col_offset=33,
                        end_lineno=95,
                        end_col_offset=49)],
                    lineno=95,
                    col_offset=12,
                    end_lineno=95,
                    end_col_offset=50),
                  lineno=95,
                  col_offset=12,
                  end_lineno=95,
                  end_col_offset=50)],
              orelse=[],
              lineno=94,
              col_offset=8,
              end_lineno=95,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=97,
                  col_offset=8,
                  end_lineno=97,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidModule',
                  ctx=Load(),
                  lineno=97,
                  col_offset=24,
                  end_lineno=97,
                  end_col_offset=37),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=98,
                      col_offset=23,
                      end_lineno=98,
                      end_col_offset=33),
                    lineno=98,
                    col_offset=12,
                    end_lineno=98,
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
                              lineno=99,
                              col_offset=35,
                              end_lineno=99,
                              end_col_offset=39),
                            attr='prefix',
                            ctx=Load(),
                            lineno=99,
                            col_offset=35,
                            end_lineno=99,
                            end_col_offset=46),
                          conversion=-1,
                          lineno=99,
                          col_offset=32,
                          end_lineno=99,
                          end_col_offset=75),
                        Constant(
                          value='_m',
                          lineno=99,
                          col_offset=32,
                          end_lineno=99,
                          end_col_offset=75),
                        FormattedValue(
                          value=Call(
                            func=Attribute(
                              value=Name(
                                id='BlockGenerator',
                                ctx=Load(),
                                lineno=99,
                                col_offset=50,
                                end_lineno=99,
                                end_col_offset=64),
                              attr='_count',
                              ctx=Load(),
                              lineno=99,
                              col_offset=50,
                              end_lineno=99,
                              end_col_offset=71),
                            args=[],
                            keywords=[],
                            lineno=99,
                            col_offset=50,
                            end_lineno=99,
                            end_col_offset=73),
                          conversion=-1,
                          lineno=99,
                          col_offset=32,
                          end_lineno=99,
                          end_col_offset=75)],
                      lineno=99,
                      col_offset=32,
                      end_lineno=99,
                      end_col_offset=75),
                    lineno=99,
                    col_offset=12,
                    end_lineno=99,
                    end_col_offset=75),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=100,
                          col_offset=29,
                          end_lineno=100,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=100,
                        col_offset=29,
                        end_lineno=100,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=100,
                      col_offset=29,
                      end_lineno=100,
                      end_col_offset=66),
                    lineno=100,
                    col_offset=12,
                    end_lineno=100,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Constant(
                      value='module',
                      lineno=101,
                      col_offset=25,
                      end_lineno=101,
                      end_col_offset=33),
                    lineno=101,
                    col_offset=12,
                    end_lineno=101,
                    end_col_offset=33)],
                lineno=97,
                col_offset=24,
                end_lineno=102,
                end_col_offset=9),
              lineno=97,
              col_offset=8,
              end_lineno=102,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=104,
                      col_offset=8,
                      end_lineno=104,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=104,
                    col_offset=8,
                    end_lineno=104,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=104,
                  col_offset=8,
                  end_lineno=104,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=104,
                    col_offset=29,
                    end_lineno=104,
                    end_col_offset=42)],
                keywords=[],
                lineno=104,
                col_offset=8,
                end_lineno=104,
                end_col_offset=43),
              lineno=104,
              col_offset=8,
              end_lineno=104,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=91,
            col_offset=50,
            end_lineno=91,
            end_col_offset=53),
          lineno=91,
          col_offset=4,
          end_lineno=104,
          end_col_offset=43),
        FunctionDef(
          name='visit_FunctionDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=106,
                col_offset=26,
                end_lineno=106,
                end_col_offset=30),
              arg(
                arg='block_node',
                annotation=Name(
                  id='FunctionDef',
                  ctx=Load(),
                  lineno=106,
                  col_offset=44,
                  end_lineno=106,
                  end_col_offset=55),
                lineno=106,
                col_offset=32,
                end_lineno=106,
                end_col_offset=55)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=107,
                col_offset=8,
                end_lineno=107,
                end_col_offset=67),
              lineno=107,
              col_offset=8,
              end_lineno=107,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='mermaid_safe_name',
                  ctx=Store(),
                  lineno=108,
                  col_offset=8,
                  end_lineno=108,
                  end_col_offset=25)],
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=108,
                        col_offset=31,
                        end_lineno=108,
                        end_col_offset=35),
                      attr='prefix',
                      ctx=Load(),
                      lineno=108,
                      col_offset=31,
                      end_lineno=108,
                      end_col_offset=42),
                    conversion=-1,
                    lineno=108,
                    col_offset=28,
                    end_lineno=108,
                    end_col_offset=71),
                  Constant(
                    value='_f',
                    lineno=108,
                    col_offset=28,
                    end_lineno=108,
                    end_col_offset=71),
                  FormattedValue(
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='BlockGenerator',
                          ctx=Load(),
                          lineno=108,
                          col_offset=46,
                          end_lineno=108,
                          end_col_offset=60),
                        attr='_count',
                        ctx=Load(),
                        lineno=108,
                        col_offset=46,
                        end_lineno=108,
                        end_col_offset=67),
                      args=[],
                      keywords=[],
                      lineno=108,
                      col_offset=46,
                      end_lineno=108,
                      end_col_offset=69),
                    conversion=-1,
                    lineno=108,
                    col_offset=28,
                    end_lineno=108,
                    end_col_offset=71)],
                lineno=108,
                col_offset=28,
                end_lineno=108,
                end_col_offset=71),
              lineno=108,
              col_offset=8,
              end_lineno=108,
              end_col_offset=71),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=109,
                  col_offset=8,
                  end_lineno=109,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=109,
                  col_offset=25,
                  end_lineno=109,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=109,
                      col_offset=46,
                      end_lineno=109,
                      end_col_offset=63),
                    lineno=109,
                    col_offset=39,
                    end_lineno=109,
                    end_col_offset=63)],
                lineno=109,
                col_offset=25,
                end_lineno=109,
                end_col_offset=64),
              lineno=109,
              col_offset=8,
              end_lineno=109,
              end_col_offset=64),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=110,
                col_offset=12,
                end_lineno=110,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=110,
                  col_offset=27,
                  end_lineno=110,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=110,
                col_offset=27,
                end_lineno=110,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=111,
                        col_offset=12,
                        end_lineno=111,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=111,
                      col_offset=12,
                      end_lineno=111,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=111,
                          col_offset=38,
                          end_lineno=111,
                          end_col_offset=49),
                        lineno=111,
                        col_offset=33,
                        end_lineno=111,
                        end_col_offset=49)],
                    lineno=111,
                    col_offset=12,
                    end_lineno=111,
                    end_col_offset=50),
                  lineno=111,
                  col_offset=12,
                  end_lineno=111,
                  end_col_offset=50)],
              orelse=[],
              lineno=110,
              col_offset=8,
              end_lineno=111,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=113,
                  col_offset=8,
                  end_lineno=113,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidFunction',
                  ctx=Load(),
                  lineno=113,
                  col_offset=24,
                  end_lineno=113,
                  end_col_offset=39),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=114,
                      col_offset=23,
                      end_lineno=114,
                      end_col_offset=33),
                    lineno=114,
                    col_offset=12,
                    end_lineno=114,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=115,
                      col_offset=32,
                      end_lineno=115,
                      end_col_offset=49),
                    lineno=115,
                    col_offset=12,
                    end_lineno=115,
                    end_col_offset=49),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=116,
                          col_offset=29,
                          end_lineno=116,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=116,
                        col_offset=29,
                        end_lineno=116,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=116,
                      col_offset=29,
                      end_lineno=116,
                      end_col_offset=66),
                    lineno=116,
                    col_offset=12,
                    end_lineno=116,
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
                              lineno=117,
                              col_offset=28,
                              end_lineno=117,
                              end_col_offset=32),
                            attr='prefix',
                            ctx=Load(),
                            lineno=117,
                            col_offset=28,
                            end_lineno=117,
                            end_col_offset=39),
                          conversion=-1,
                          lineno=117,
                          col_offset=25,
                          end_lineno=117,
                          end_col_offset=59),
                        Constant(
                          value='_',
                          lineno=117,
                          col_offset=25,
                          end_lineno=117,
                          end_col_offset=59),
                        FormattedValue(
                          value=Attribute(
                            value=Name(
                              id='block_node',
                              ctx=Load(),
                              lineno=117,
                              col_offset=42,
                              end_lineno=117,
                              end_col_offset=52),
                            attr='name',
                            ctx=Load(),
                            lineno=117,
                            col_offset=42,
                            end_lineno=117,
                            end_col_offset=57),
                          conversion=-1,
                          lineno=117,
                          col_offset=25,
                          end_lineno=117,
                          end_col_offset=59)],
                      lineno=117,
                      col_offset=25,
                      end_lineno=117,
                      end_col_offset=59),
                    lineno=117,
                    col_offset=12,
                    end_lineno=117,
                    end_col_offset=59)],
                lineno=113,
                col_offset=24,
                end_lineno=118,
                end_col_offset=9),
              lineno=113,
              col_offset=8,
              end_lineno=118,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=120,
                      col_offset=8,
                      end_lineno=120,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=120,
                    col_offset=8,
                    end_lineno=120,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=120,
                  col_offset=8,
                  end_lineno=120,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=120,
                    col_offset=29,
                    end_lineno=120,
                    end_col_offset=42)],
                keywords=[],
                lineno=120,
                col_offset=8,
                end_lineno=120,
                end_col_offset=43),
              lineno=120,
              col_offset=8,
              end_lineno=120,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=106,
            col_offset=60,
            end_lineno=106,
            end_col_offset=63),
          lineno=106,
          col_offset=4,
          end_lineno=120,
          end_col_offset=43),
        FunctionDef(
          name='visit_ClassDef',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=122,
                col_offset=23,
                end_lineno=122,
                end_col_offset=27),
              arg(
                arg='block_node',
                annotation=Name(
                  id='ClassDef',
                  ctx=Load(),
                  lineno=122,
                  col_offset=41,
                  end_lineno=122,
                  end_col_offset=49),
                lineno=122,
                col_offset=29,
                end_lineno=122,
                end_col_offset=49)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='This is a block, we want a subgraph, so parse content',
                lineno=123,
                col_offset=8,
                end_lineno=123,
                end_col_offset=67),
              lineno=123,
              col_offset=8,
              end_lineno=123,
              end_col_offset=67),
            Assign(
              targets=[
                Name(
                  id='mermaid_safe_name',
                  ctx=Store(),
                  lineno=124,
                  col_offset=8,
                  end_lineno=124,
                  end_col_offset=25)],
              value=JoinedStr(
                values=[
                  FormattedValue(
                    value=Attribute(
                      value=Name(
                        id='self',
                        ctx=Load(),
                        lineno=124,
                        col_offset=31,
                        end_lineno=124,
                        end_col_offset=35),
                      attr='prefix',
                      ctx=Load(),
                      lineno=124,
                      col_offset=31,
                      end_lineno=124,
                      end_col_offset=42),
                    conversion=-1,
                    lineno=124,
                    col_offset=28,
                    end_lineno=124,
                    end_col_offset=71),
                  Constant(
                    value='_c',
                    lineno=124,
                    col_offset=28,
                    end_lineno=124,
                    end_col_offset=71),
                  FormattedValue(
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='BlockGenerator',
                          ctx=Load(),
                          lineno=124,
                          col_offset=46,
                          end_lineno=124,
                          end_col_offset=60),
                        attr='_count',
                        ctx=Load(),
                        lineno=124,
                        col_offset=46,
                        end_lineno=124,
                        end_col_offset=67),
                      args=[],
                      keywords=[],
                      lineno=124,
                      col_offset=46,
                      end_lineno=124,
                      end_col_offset=69),
                    conversion=-1,
                    lineno=124,
                    col_offset=28,
                    end_lineno=124,
                    end_col_offset=71)],
                lineno=124,
                col_offset=28,
                end_lineno=124,
                end_col_offset=71),
              lineno=124,
              col_offset=8,
              end_lineno=124,
              end_col_offset=71),
            Assign(
              targets=[
                Name(
                  id='link_generator',
                  ctx=Store(),
                  lineno=125,
                  col_offset=8,
                  end_lineno=125,
                  end_col_offset=22)],
              value=Call(
                func=Name(
                  id='LinkGenerator',
                  ctx=Load(),
                  lineno=125,
                  col_offset=25,
                  end_lineno=125,
                  end_col_offset=38),
                args=[],
                keywords=[
                  keyword(
                    arg='prefix',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=125,
                      col_offset=46,
                      end_lineno=125,
                      end_col_offset=63),
                    lineno=125,
                    col_offset=39,
                    end_lineno=125,
                    end_col_offset=63)],
                lineno=125,
                col_offset=25,
                end_lineno=125,
                end_col_offset=64),
              lineno=125,
              col_offset=8,
              end_lineno=125,
              end_col_offset=64),
            For(
              target=Name(
                id='sub_element',
                ctx=Store(),
                lineno=126,
                col_offset=12,
                end_lineno=126,
                end_col_offset=23),
              iter=Attribute(
                value=Name(
                  id='block_node',
                  ctx=Load(),
                  lineno=126,
                  col_offset=27,
                  end_lineno=126,
                  end_col_offset=37),
                attr='body',
                ctx=Load(),
                lineno=126,
                col_offset=27,
                end_lineno=126,
                end_col_offset=42),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='link_generator',
                        ctx=Load(),
                        lineno=127,
                        col_offset=12,
                        end_lineno=127,
                        end_col_offset=26),
                      attr='visit',
                      ctx=Load(),
                      lineno=127,
                      col_offset=12,
                      end_lineno=127,
                      end_col_offset=32),
                    args=[],
                    keywords=[
                      keyword(
                        arg='node',
                        value=Name(
                          id='sub_element',
                          ctx=Load(),
                          lineno=127,
                          col_offset=38,
                          end_lineno=127,
                          end_col_offset=49),
                        lineno=127,
                        col_offset=33,
                        end_lineno=127,
                        end_col_offset=49)],
                    lineno=127,
                    col_offset=12,
                    end_lineno=127,
                    end_col_offset=50),
                  lineno=127,
                  col_offset=12,
                  end_lineno=127,
                  end_col_offset=50)],
              orelse=[],
              lineno=126,
              col_offset=8,
              end_lineno=127,
              end_col_offset=50),
            Assign(
              targets=[
                Name(
                  id='mermaid_block',
                  ctx=Store(),
                  lineno=129,
                  col_offset=8,
                  end_lineno=129,
                  end_col_offset=21)],
              value=Call(
                func=Name(
                  id='MermaidClass',
                  ctx=Load(),
                  lineno=129,
                  col_offset=24,
                  end_lineno=129,
                  end_col_offset=36),
                args=[],
                keywords=[
                  keyword(
                    arg='ast_node',
                    value=Name(
                      id='block_node',
                      ctx=Load(),
                      lineno=130,
                      col_offset=23,
                      end_lineno=130,
                      end_col_offset=33),
                    lineno=130,
                    col_offset=12,
                    end_lineno=130,
                    end_col_offset=33),
                  keyword(
                    arg='mermaid_safe_name',
                    value=Name(
                      id='mermaid_safe_name',
                      ctx=Load(),
                      lineno=131,
                      col_offset=32,
                      end_lineno=131,
                      end_col_offset=49),
                    lineno=131,
                    col_offset=12,
                    end_lineno=131,
                    end_col_offset=49),
                  keyword(
                    arg='block_contents',
                    value=Call(
                      func=Attribute(
                        value=Name(
                          id='link_generator',
                          ctx=Load(),
                          lineno=132,
                          col_offset=29,
                          end_lineno=132,
                          end_col_offset=43),
                        attr='get_list_of_elements',
                        ctx=Load(),
                        lineno=132,
                        col_offset=29,
                        end_lineno=132,
                        end_col_offset=64),
                      args=[],
                      keywords=[],
                      lineno=132,
                      col_offset=29,
                      end_lineno=132,
                      end_col_offset=66),
                    lineno=132,
                    col_offset=12,
                    end_lineno=132,
                    end_col_offset=66),
                  keyword(
                    arg='display_name',
                    value=Attribute(
                      value=Name(
                        id='block_node',
                        ctx=Load(),
                        lineno=133,
                        col_offset=25,
                        end_lineno=133,
                        end_col_offset=35),
                      attr='name',
                      ctx=Load(),
                      lineno=133,
                      col_offset=25,
                      end_lineno=133,
                      end_col_offset=40),
                    lineno=133,
                    col_offset=12,
                    end_lineno=133,
                    end_col_offset=40)],
                lineno=129,
                col_offset=24,
                end_lineno=134,
                end_col_offset=9),
              lineno=129,
              col_offset=8,
              end_lineno=134,
              end_col_offset=9),
            Expr(
              value=Call(
                func=Attribute(
                  value=Attribute(
                    value=Name(
                      id='self',
                      ctx=Load(),
                      lineno=136,
                      col_offset=8,
                      end_lineno=136,
                      end_col_offset=12),
                    attr='elements',
                    ctx=Load(),
                    lineno=136,
                    col_offset=8,
                    end_lineno=136,
                    end_col_offset=21),
                  attr='append',
                  ctx=Load(),
                  lineno=136,
                  col_offset=8,
                  end_lineno=136,
                  end_col_offset=28),
                args=[
                  Name(
                    id='mermaid_block',
                    ctx=Load(),
                    lineno=136,
                    col_offset=29,
                    end_lineno=136,
                    end_col_offset=42)],
                keywords=[],
                lineno=136,
                col_offset=8,
                end_lineno=136,
                end_col_offset=43),
              lineno=136,
              col_offset=8,
              end_lineno=136,
              end_col_offset=43)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=122,
            col_offset=54,
            end_lineno=122,
            end_col_offset=57),
          lineno=122,
          col_offset=4,
          end_lineno=136,
          end_col_offset=43),
        FunctionDef(
          name='generic_visit',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=138,
                col_offset=22,
                end_lineno=138,
                end_col_offset=26),
              arg(
                arg='_node',
                annotation=Name(
                  id='AST',
                  ctx=Load(),
                  lineno=138,
                  col_offset=35,
                  end_lineno=138,
                  end_col_offset=38),
                lineno=138,
                col_offset=28,
                end_lineno=138,
                end_col_offset=38)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]),
          body=[
            Expr(
              value=Constant(
                value='Non block nodes are not interesting here',
                lineno=139,
                col_offset=8,
                end_lineno=139,
                end_col_offset=54),
              lineno=139,
              col_offset=8,
              end_lineno=139,
              end_col_offset=54),
            Pass(
              lineno=140,
              col_offset=8,
              end_lineno=140,
              end_col_offset=12)],
          decorator_list=[],
          returns=Name(
            id='Any',
            ctx=Load(),
            lineno=138,
            col_offset=43,
            end_lineno=138,
            end_col_offset=46),
          lineno=138,
          col_offset=4,
          end_lineno=140,
          end_col_offset=12),
        FunctionDef(
          name='get_list_of_elements',
          args=arguments(
            posonlyargs=[],
            args=[
              arg(
                arg='self',
                lineno=142,
                col_offset=29,
                end_lineno=142,
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
                  lineno=143,
                  col_offset=15,
                  end_lineno=143,
                  end_col_offset=19),
                attr='elements',
                ctx=Load(),
                lineno=143,
                col_offset=15,
                end_lineno=143,
                end_col_offset=28),
              lineno=143,
              col_offset=8,
              end_lineno=143,
              end_col_offset=28)],
          decorator_list=[],
          returns=Subscript(
            value=Name(
              id='list',
              ctx=Load(),
              lineno=142,
              col_offset=38,
              end_lineno=142,
              end_col_offset=42),
            slice=Name(
              id='MermaidElement',
              ctx=Load(),
              lineno=142,
              col_offset=43,
              end_lineno=142,
              end_col_offset=57),
            ctx=Load(),
            lineno=142,
            col_offset=38,
            end_lineno=142,
            end_col_offset=58),
          lineno=142,
          col_offset=4,
          end_lineno=143,
          end_col_offset=28)],
      decorator_list=[],
      lineno=78,
      col_offset=0,
      end_lineno=143,
      end_col_offset=28)],
  type_ignores=[])
```
</details>

