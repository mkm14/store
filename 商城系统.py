print("------------------------欢迎来到陈鑫涛水果商城--------------------------")
print("编号          名称          价格        数量          品质        出产地")
print("---------------------------------------------------------------------")
print("1             苹果          3.6         500           A+          烟台")
print("2             香蕉          5.0         200           B+          海南")
print("3             榴莲          120         60            A+          泰国")
print("4             大枣          0.2         800           C+          山东")
print("5             猕猴桃        2           600           A+          四川")
print("----------------------------------------------------------------------")
print("总金额为：￥", (3.6 * 500 + 5 * 200 + 120 * 60 + 0.2 * 800 + 2 * 600))

# 1. jason衣服商城（风衣、羽绒服、牛仔裤、鞋）
aa = "风衣"
zx = 5
num = 100
print("--------------------------")
print("aa", "\t", "zx")
print("--------------------------")
print("你的金额为￥", (zx * num))
date = "1号"
nam = "羽绒服"
price = 253.6
stock = 500
sale = 10
print("-------------------天地商场------------------------------")
print("日期         服装名称              价格       库存数量     销售量")
print("--------------------------------------------------------")
print(date,"          ",nam,"      ",price,"        ",stock,"   ",sale)
print("2号           牛仔裤              86.3         600        60")
print("3号           风衣               96.8         335        43")
print("4号           皮草                135.9        855         63")
print("5号           T血                 65.8         632        63")
print("6号           衬衫                49.3         562        120")
print("7号           牛仔裤               86.3        600        72")
print("8号           羽绒服               253.6	     500	    69")
print("9号           牛仔裤              86.3	         600	   35")
print("10号          羽绒服              253.6	      500	   140")
print("11号           牛仔裤             86.3	          600	   90")
print("12号           皮草                135.9	       855	   24")
print("13号           T血                  65.8	      632	    45")
print("14号           风衣               96.8	      335	   25")
print("15号           牛仔裤              86.3	      600	    60")
print("16号           T血                 65.8	      632	   129")
print("17号           羽绒服              253.6	      500	   10")
print("18号           风衣                96.8	      335	43")
print("19号           皮草                65.8	      632	63")
print("20号           牛仔裤              86.3	      600	60")
print("21号           皮草                135.9       855	63")
print("22号           风衣               96.8	     335	60")
print("23号           T血                65.8	     632	58")
print("24号           牛仔裤              86.3	     600	140")
print("25号           T血                65.8	     632	48")
print("26号           风衣                96.8	      335	43")
print("27号           皮草                135.9	     855	57")
print("28号           羽绒服               253.6       500	10")
print("29号           T血                65.8	     632	63")
print("30号           风衣                96.8	     335	78")
print("--------------------------------------------------------")
print("风衣12月总金额: ￥",((43+25+43+60+43+78)*96.8))
print("羽绒服12月总金额: ￥",((10+69+140+10+10)*253.6))
print("衬衫12月总金额: ￥",(120*49.3))
print("牛仔裤12月总金额: ￥",((60+72+35+90+60+60+140)*86.3))
print("T血12月总金额: ￥",((63+63+129+48+58+63+129+45)*65.8))
print("皮草12月总金额: ￥",((63+57+63+24)*135.9))
print("12月份销售总金额: ￥",(((43+25+43+60+43+78)*96.8)+((10+69+140+10+10)*253.6)+(120*49.3)+((60+72+35+90+60+60+140)*86.3)+((63+63+129+48+58+63+129+45)*65.8)+((63+57+63+24)*135.9)))
as1 = (43+25+43+60+43+78)
as2 = (10+69+140+10+10)
as3 = 120
as4 = (60+72+35+90+60+60+140)
as5 = (63+63+129+48+58+63+129+45)
as6 = (63+57+63+24)
as7 = (as1+as2+as3+as4+as5+as6)
zx = ((43+25+43+60+43+78)*96.8)+((10+69+140+10+10)*253.6)+(120*49.3)+((60+72+35+90+60+60+140)*86.3)+((63+63+129+48+58+63+129+45)*65.8)+((63+57+63+24)*135.9)
print("风衣12月销售额占比: ￥",(as1*96.8/ zx))
print("羽绒服12月销售额占比: ￥",(as2*253.6/zx))
print("衬衫12月销售额占比: ￥",(as3*120/zx))
print("牛仔裤12月销售额占比: ￥",(as4*86.3/zx))
print("T血12月销售额占比: ￥",(as5*65.8/zx))
print("皮草12月销售额占比: ￥",(as6*135.9/zx))
print("风衣12月销售额占比: ￥",(as1/as7))
print("羽绒服12月销售占比: ￥",(as2/as7))
print("衬衫12月销售占比: ￥",(as3/as7))
print("牛仔裤12月销售占比: ￥",(as4/as7))
print("T血12月销售占比: ￥",(as5/as7))
print("皮草12月销售占比: ￥",(as6/as7))

