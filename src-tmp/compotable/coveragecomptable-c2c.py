from relations import srel

def findkey(mapp, value):
    return mapp.keys()[mapp.values().index(value)]

# R32 composition table
#"inconsistent" = 0
#"!" = 1 << 0 = 1
#"<" = 1 << 1 = 2
#"=" = 1 << 2 = 4
#">" = 1 << 3 = 8
#"o" = 1 << 4 = 16

l = []
l.append(["<<<<", ""])
l.append(["<<<>", ""])
l.append(["<<<=", ""])
l.append(["<<<!", ""])
l.append(["<<<o", ""])
l.append(["<<><", ""])
l.append(["<<>>", ""])
l.append(["<<>=", ""])
l.append(["<<>!", ""])
l.append(["<<>o", ""])
l.append(["<<=<", ""])
l.append(["<<=>", ""])
l.append(["<<==", ""])
l.append(["<<=!", ""])
l.append(["<<=o", ""])
l.append(["<<!<", ""])
l.append(["<<!>", ""])
l.append(["<<!=", ""])
l.append(["<<!!", ""])
l.append(["<<!o", ""])
l.append(["<<o<", ""])
l.append(["<<o>", ""])
l.append(["<<o=", ""])
l.append(["<<o!", ""])
l.append(["<<oo", ""])
l.append(["<><<", ""])
l.append(["<><>", ""])
l.append(["<><=", ""])
l.append(["<><!", ""])
l.append(["<><o", ""])
l.append(["<>><", ""])
l.append(["<>>>", ""])
l.append(["<>>=", ""])
l.append(["<>>!", ""])
l.append(["<>>o", ""])
l.append(["<>=<", ""])
l.append(["<>=>", ""])
l.append(["<>==", ""])
l.append(["<>=!", ""])
l.append(["<>=o", ""])
l.append(["<>!<", ""])
l.append(["<>!>", ""])
l.append(["<>!=", ""])
l.append(["<>!!", ""])
l.append(["<>!o", ""])
l.append(["<>o<", ""])
l.append(["<>o>", ""])
l.append(["<>o=", ""])
l.append(["<>o!", ""])
l.append(["<>oo", ""])
l.append(["<=<<", ""])
l.append(["<=<>", ""])
l.append(["<=<=", ""])
l.append(["<=<!", ""])
l.append(["<=<o", ""])
l.append(["<=><", ""])
l.append(["<=>>", ""])
l.append(["<=>=", ""])
l.append(["<=>!", ""])
l.append(["<=>o", ""])
l.append(["<==<", ""])
l.append(["<==>", ""])
l.append(["<===", ""])
l.append(["<==!", ""])
l.append(["<==o", ""])
l.append(["<=!<", ""])
l.append(["<=!>", ""])
l.append(["<=!=", ""])
l.append(["<=!!", ""])
l.append(["<=!o", ""])
l.append(["<=o<", ""])
l.append(["<=o>", ""])
l.append(["<=o=", ""])
l.append(["<=o!", ""])
l.append(["<=oo", ""])
l.append(["<!<<", ""])
l.append(["<!<>", ""])
l.append(["<!<=", ""])
l.append(["<!<!", "<"])
l.append(["<!<o", ""])
l.append(["<!><", ""])
l.append(["<!>>", ""])
l.append(["<!>=", ""])
l.append(["<!>!", ""])
l.append(["<!>o", ""])
l.append(["<!=<", ""])
l.append(["<!=>", ""])
l.append(["<!==", ""])
l.append(["<!=!", ""])
l.append(["<!=o", ""])
l.append(["<!!<", "<"])
l.append(["<!!>", "o"])
l.append(["<!!=", "<"])
l.append(["<!!!", "o"])
l.append(["<!!o", "o"])
l.append(["<!o<", ""])
l.append(["<!o>", "<>=o"])
l.append(["<!o=", ""])
l.append(["<!o!", "o"])
l.append(["<!oo", "<o"])
l.append(["<o<<", ""])
l.append(["<o<>", ""])
l.append(["<o<=", ""])
l.append(["<o<!", ""])
l.append(["<o<o", ""])
l.append(["<o><", ""])
l.append(["<o>>", ""])
l.append(["<o>=", ""])
l.append(["<o>!", ""])
l.append(["<o>o", ""])
l.append(["<o=<", ""])
l.append(["<o=>", ""])
l.append(["<o==", ""])
l.append(["<o=!", ""])
l.append(["<o=o", ""])
l.append(["<o!<", ""])
l.append(["<o!>", ""])
l.append(["<o!=", ""])
l.append(["<o!!", ""])
l.append(["<o!o", ""])
l.append(["<oo<", ""])
l.append(["<oo>", ""])
l.append(["<oo=", ""])
l.append(["<oo!", ""])
l.append(["<ooo", ""])
l.append(["><<<", ""])
l.append(["><<>", ""])
l.append(["><<=", ""])
l.append(["><<!", ""])
l.append(["><<o", ""])
l.append(["><><", ""])
l.append(["><>>", ""])
l.append(["><>=", ""])
l.append(["><>!", ""])
l.append(["><>o", ""])
l.append(["><=<", ""])
l.append(["><=>", ""])
l.append(["><==", ""])
l.append(["><=!", ""])
l.append(["><=o", ""])
l.append(["><!<", ""])
l.append(["><!>", ""])
l.append(["><!=", ""])
l.append(["><!!", ""])
l.append(["><!o", ""])
l.append(["><o<", ""])
l.append(["><o>", ""])
l.append(["><o=", ""])
l.append(["><o!", ""])
l.append(["><oo", ""])
l.append([">><<", ""])
l.append([">><>", ""])
l.append([">><=", ""])
l.append([">><!", ""])
l.append([">><o", ""])
l.append([">>><", ""])
l.append([">>>>", ""])
l.append([">>>=", ""])
l.append([">>>!", ""])
l.append([">>>o", ""])
l.append([">>=<", ""])
l.append([">>=>", ""])
l.append([">>==", ""])
l.append([">>=!", ""])
l.append([">>=o", ""])
l.append([">>!<", ""])
l.append([">>!>", ""])
l.append([">>!=", ""])
l.append([">>!!", ">"])
l.append([">>!o", ""])
l.append([">>o<", ""])
l.append([">>o>", ""])
l.append([">>o=", ""])
l.append([">>o!", ""])
l.append([">>oo", ""])
l.append([">=<<", ""])
l.append([">=<>", ""])
l.append([">=<=", ""])
l.append([">=<!", ""])
l.append([">=<o", ""])
l.append([">=><", ""])
l.append([">=>>", ""])
l.append([">=>=", ""])
l.append([">=>!", ""])
l.append([">=>o", ""])
l.append([">==<", ""])
l.append([">==>", ""])
l.append([">===", ""])
l.append([">==!", ""])
l.append([">==o", ""])
l.append([">=!<", ""])
l.append([">=!>", ""])
l.append([">=!=", ""])
l.append([">=!!", ""])
l.append([">=!o", ""])
l.append([">=o<", ""])
l.append([">=o>", ""])
l.append([">=o=", ""])
l.append([">=o!", ""])
l.append([">=oo", ""])
l.append([">!<<", ""])
l.append([">!<>", ""])
l.append([">!<=", ""])
l.append([">!<!", ""])
l.append([">!<o", ""])
l.append([">!><", ""])
l.append([">!>>", ""])
l.append([">!>=", ""])
l.append([">!>!", ""])
l.append([">!>o", ""])
l.append([">!=<", ""])
l.append([">!=>", ""])
l.append([">!==", ""])
l.append([">!=!", ""])
l.append([">!=o", ""])
l.append([">!!<", "o"])
l.append([">!!>", ">"])
l.append([">!!=", ">"])
l.append([">!!!", "o"])
l.append([">!!o", "o"])
l.append([">!o<", ""])
l.append([">!o>", ""])
l.append([">!o=", ""])
l.append([">!o!", ""])
l.append([">!oo", ""])
l.append([">o<<", ""])
l.append([">o<>", ""])
l.append([">o<=", ""])
l.append([">o<!", ""])
l.append([">o<o", ""])
l.append([">o><", ""])
l.append([">o>>", ""])
l.append([">o>=", ""])
l.append([">o>!", ""])
l.append([">o>o", ""])
l.append([">o=<", ""])
l.append([">o=>", ""])
l.append([">o==", ""])
l.append([">o=!", ""])
l.append([">o=o", ""])
l.append([">o!<", "<>=o"])
l.append([">o!>", ""])
l.append([">o!=", ""])
l.append([">o!!", "o"])
l.append([">o!o", ">o"])
l.append([">oo<", ""])
l.append([">oo>", ""])
l.append([">oo=", ""])
l.append([">oo!", ""])
l.append([">ooo", ""])
l.append(["=<<<", ""])
l.append(["=<<>", ""])
l.append(["=<<=", ""])
l.append(["=<<!", ""])
l.append(["=<<o", ""])
l.append(["=<><", ""])
l.append(["=<>>", ""])
l.append(["=<>=", ""])
l.append(["=<>!", ""])
l.append(["=<>o", ""])
l.append(["=<=<", ""])
l.append(["=<=>", ""])
l.append(["=<==", ""])
l.append(["=<=!", ""])
l.append(["=<=o", ""])
l.append(["=<!<", ""])
l.append(["=<!>", ""])
l.append(["=<!=", ""])
l.append(["=<!!", ""])
l.append(["=<!o", ""])
l.append(["=<o<", ""])
l.append(["=<o>", ""])
l.append(["=<o=", ""])
l.append(["=<o!", ""])
l.append(["=<oo", ""])
l.append(["=><<", ""])
l.append(["=><>", ""])
l.append(["=><=", ""])
l.append(["=><!", ""])
l.append(["=><o", ""])
l.append(["=>><", ""])
l.append(["=>>>", ""])
l.append(["=>>=", ""])
l.append(["=>>!", ""])
l.append(["=>>o", ""])
l.append(["=>=<", ""])
l.append(["=>=>", ""])
l.append(["=>==", ""])
l.append(["=>=!", ""])
l.append(["=>=o", ""])
l.append(["=>!<", ""])
l.append(["=>!>", ""])
l.append(["=>!=", ""])
l.append(["=>!!", ""])
l.append(["=>!o", ""])
l.append(["=>o<", ""])
l.append(["=>o>", ""])
l.append(["=>o=", ""])
l.append(["=>o!", ""])
l.append(["=>oo", ""])
l.append(["==<<", ""])
l.append(["==<>", ""])
l.append(["==<=", ""])
l.append(["==<!", ""])
l.append(["==<o", ""])
l.append(["==><", ""])
l.append(["==>>", ""])
l.append(["==>=", ""])
l.append(["==>!", ""])
l.append(["==>o", ""])
l.append(["===<", ""])
l.append(["===>", ""])
l.append(["====", ""])
l.append(["===!", ""])
l.append(["===o", ""])
l.append(["==!<", ""])
l.append(["==!>", ""])
l.append(["==!=", ""])
l.append(["==!!", ""])
l.append(["==!o", ""])
l.append(["==o<", ""])
l.append(["==o>", ""])
l.append(["==o=", ""])
l.append(["==o!", ""])
l.append(["==oo", ""])
l.append(["=!<<", ""])
l.append(["=!<>", ""])
l.append(["=!<=", ""])
l.append(["=!<!", ""])
l.append(["=!<o", ""])
l.append(["=!><", ""])
l.append(["=!>>", ""])
l.append(["=!>=", ""])
l.append(["=!>!", ""])
l.append(["=!>o", ""])
l.append(["=!=<", ""])
l.append(["=!=>", ""])
l.append(["=!==", ""])
l.append(["=!=!", ""])
l.append(["=!=o", ""])
l.append(["=!!<", "<"])
l.append(["=!!>", ">"])
l.append(["=!!=", "="])
l.append(["=!!!", "o"])
l.append(["=!!o", "o"])
l.append(["=!o<", ""])
l.append(["=!o>", ""])
l.append(["=!o=", ""])
l.append(["=!o!", ""])
l.append(["=!oo", ""])
l.append(["=o<<", ""])
l.append(["=o<>", ""])
l.append(["=o<=", ""])
l.append(["=o<!", ""])
l.append(["=o<o", ""])
l.append(["=o><", ""])
l.append(["=o>>", ""])
l.append(["=o>=", ""])
l.append(["=o>!", ""])
l.append(["=o>o", ""])
l.append(["=o=<", ""])
l.append(["=o=>", ""])
l.append(["=o==", ""])
l.append(["=o=!", ""])
l.append(["=o=o", ""])
l.append(["=o!<", ""])
l.append(["=o!>", ""])
l.append(["=o!=", ""])
l.append(["=o!!", ""])
l.append(["=o!o", ""])
l.append(["=oo<", ""])
l.append(["=oo>", ""])
l.append(["=oo=", ""])
l.append(["=oo!", ""])
l.append(["=ooo", ""])
l.append(["!<<<", ""])
l.append(["!<<>", ""])
l.append(["!<<=", ""])
l.append(["!<<!", "<"])
l.append(["!<<o", ""])
l.append(["!<><", ""])
l.append(["!<>>", ""])
l.append(["!<>=", ""])
l.append(["!<>!", "o"])
l.append(["!<>o", "<>=o"])
l.append(["!<=<", ""])
l.append(["!<=>", ""])
l.append(["!<==", ""])
l.append(["!<=!", "<"])
l.append(["!<=o", ""])
l.append(["!<!<", "<"])
l.append(["!<!>", ""])
l.append(["!<!=", ""])
l.append(["!<!!", "o"])
l.append(["!<!o", "o"])
l.append(["!<o<", ""])
l.append(["!<o>", ""])
l.append(["!<o=", ""])
l.append(["!<o!", "o"])
l.append(["!<oo", "<o"])
l.append(["!><<", ""])
l.append(["!><>", ""])
l.append(["!><=", ""])
l.append(["!><!", "o"])
l.append(["!><o", ""])
l.append(["!>><", ""])
l.append(["!>>>", ""])
l.append(["!>>=", ""])
l.append(["!>>!", ">"])
l.append(["!>>o", ""])
l.append(["!>=<", ""])
l.append(["!>=>", ""])
l.append(["!>==", ""])
l.append(["!>=!", ">"])
l.append(["!>=o", ""])
l.append(["!>!<", ""])
l.append(["!>!>", ""])
l.append(["!>!=", ""])
l.append(["!>!!", "o"])
l.append(["!>!o", ""])
l.append(["!>o<", ""])
l.append(["!>o>", ""])
l.append(["!>o=", ""])
l.append(["!>o!", "o"])
l.append(["!>oo", ""])
l.append(["!=<<", ""])
l.append(["!=<>", ""])
l.append(["!=<=", ""])
l.append(["!=<!", "<"])
l.append(["!=<o", ""])
l.append(["!=><", ""])
l.append(["!=>>", ""])
l.append(["!=>=", ""])
l.append(["!=>!", ">"])
l.append(["!=>o", ""])
l.append(["!==<", ""])
l.append(["!==>", ""])
l.append(["!===", ""])
l.append(["!==!", "="])
l.append(["!==o", ""])
l.append(["!=!<", ""])
l.append(["!=!>", ""])
l.append(["!=!=", ""])
l.append(["!=!!", "o"])
l.append(["!=!o", ""])
l.append(["!=o<", ""])
l.append(["!=o>", ""])
l.append(["!=o=", ""])
l.append(["!=o!", "o"])
l.append(["!=oo", ""])
l.append(["!!<<", ""])
l.append(["!!<>", ""])
l.append(["!!<=", ""])
l.append(["!!<!", "o"])
l.append(["!!<o", ""])
l.append(["!!><", ""])
l.append(["!!>>", ">"])
l.append(["!!>=", ""])
l.append(["!!>!", "o"])
l.append(["!!>o", "o"])
l.append(["!!=<", ""])
l.append(["!!=>", ""])
l.append(["!!==", ""])
l.append(["!!=!", "o"])
l.append(["!!=o", ""])
l.append(["!!!<", "o"])
l.append(["!!!>", "o"])
l.append(["!!!=", "o"])
l.append(["!!!!", "!"])
l.append(["!!!o", "o"])
l.append(["!!o<", ""])
l.append(["!!o>", "o"])
l.append(["!!o=", ""])
l.append(["!!o!", "o"])
l.append(["!!oo", "o"])
l.append(["!o<<", ""])
l.append(["!o<>", ""])
l.append(["!o<=", ""])
l.append(["!o<!", "o"])
l.append(["!o<o", ""])
l.append(["!o><", ""])
l.append(["!o>>", ""])
l.append(["!o>=", ""])
l.append(["!o>!", "o"])
l.append(["!o>o", ">o"])
l.append(["!o=<", ""])
l.append(["!o=>", ""])
l.append(["!o==", ""])
l.append(["!o=!", "o"])
l.append(["!o=o", ""])
l.append(["!o!<", "o"])
l.append(["!o!>", ""])
l.append(["!o!=", ""])
l.append(["!o!!", "o"])
l.append(["!o!o", "o"])
l.append(["!oo<", ""])
l.append(["!oo>", ""])
l.append(["!oo=", ""])
l.append(["!oo!", "o"])
l.append(["!ooo", "o"])
l.append(["o<<<", ""])
l.append(["o<<>", ""])
l.append(["o<<=", ""])
l.append(["o<<!", ""])
l.append(["o<<o", ""])
l.append(["o<><", ""])
l.append(["o<>>", ""])
l.append(["o<>=", ""])
l.append(["o<>!", ""])
l.append(["o<>o", ""])
l.append(["o<=<", ""])
l.append(["o<=>", ""])
l.append(["o<==", ""])
l.append(["o<=!", ""])
l.append(["o<=o", ""])
l.append(["o<!<", ""])
l.append(["o<!>", ""])
l.append(["o<!=", ""])
l.append(["o<!!", ""])
l.append(["o<!o", ""])
l.append(["o<o<", ""])
l.append(["o<o>", ""])
l.append(["o<o=", ""])
l.append(["o<o!", ""])
l.append(["o<oo", ""])
l.append(["o><<", ""])
l.append(["o><>", ""])
l.append(["o><=", ""])
l.append(["o><!", "<>=o"])
l.append(["o><o", ""])
l.append(["o>><", ""])
l.append(["o>>>", ""])
l.append(["o>>=", ""])
l.append(["o>>!", ""])
l.append(["o>>o", ""])
l.append(["o>=<", ""])
l.append(["o>=>", ""])
l.append(["o>==", ""])
l.append(["o>=!", ""])
l.append(["o>=o", ""])
l.append(["o>!<", ""])
l.append(["o>!>", ""])
l.append(["o>!=", ""])
l.append(["o>!!", "o"])
l.append(["o>!o", ""])
l.append(["o>o<", ""])
l.append(["o>o>", ""])
l.append(["o>o=", ""])
l.append(["o>o!", ">o"])
l.append(["o>oo", ""])
l.append(["o=<<", ""])
l.append(["o=<>", ""])
l.append(["o=<=", ""])
l.append(["o=<!", ""])
l.append(["o=<o", ""])
l.append(["o=><", ""])
l.append(["o=>>", ""])
l.append(["o=>=", ""])
l.append(["o=>!", ""])
l.append(["o=>o", ""])
l.append(["o==<", ""])
l.append(["o==>", ""])
l.append(["o===", ""])
l.append(["o==!", ""])
l.append(["o==o", ""])
l.append(["o=!<", ""])
l.append(["o=!>", ""])
l.append(["o=!=", ""])
l.append(["o=!!", ""])
l.append(["o=!o", ""])
l.append(["o=o<", ""])
l.append(["o=o>", ""])
l.append(["o=o=", ""])
l.append(["o=o!", ""])
l.append(["o=oo", ""])
l.append(["o!<<", ""])
l.append(["o!<>", ""])
l.append(["o!<=", ""])
l.append(["o!<!", "o"])
l.append(["o!<o", ""])
l.append(["o!><", ""])
l.append(["o!>>", ""])
l.append(["o!>=", ""])
l.append(["o!>!", ""])
l.append(["o!>o", ""])
l.append(["o!=<", ""])
l.append(["o!=>", ""])
l.append(["o!==", ""])
l.append(["o!=!", ""])
l.append(["o!=o", ""])
l.append(["o!!<", "o"])
l.append(["o!!>", "o"])
l.append(["o!!=", "o"])
l.append(["o!!!", "o"])
l.append(["o!!o", "o"])
l.append(["o!o<", ""])
l.append(["o!o>", ">o"])
l.append(["o!o=", ""])
l.append(["o!o!", "o"])
l.append(["o!oo", "o"])
l.append(["oo<<", ""])
l.append(["oo<>", ""])
l.append(["oo<=", ""])
l.append(["oo<!", "<o"])
l.append(["oo<o", ""])
l.append(["oo><", ""])
l.append(["oo>>", ""])
l.append(["oo>=", ""])
l.append(["oo>!", ""])
l.append(["oo>o", ""])
l.append(["oo=<", ""])
l.append(["oo=>", ""])
l.append(["oo==", ""])
l.append(["oo=!", ""])
l.append(["oo=o", ""])
l.append(["oo!<", "<o"])
l.append(["oo!>", ""])
l.append(["oo!=", ""])
l.append(["oo!!", "o"])
l.append(["oo!o", "o"])
l.append(["ooo<", ""])
l.append(["ooo>", ""])
l.append(["ooo=", ""])
l.append(["ooo!", "o"])
l.append(["oooo", "<>=o"])


# create B5 table
base = [[[[None for i in range(32)] for j in range(32)] for k in range(32)] for m in range(32)]
for pair in l:
    rel1 = srel[pair[0][0]]
    rel2 = srel[pair[0][1]]
    rel3 = srel[pair[0][2]]
    rel4 = srel[pair[0][3]]
    resultStr = pair[1]
    
    num = 0
    if resultStr != "":
        for ch in resultStr:
            num = num | srel[ch]
    
    base[rel1][rel2][rel3][rel4] = num

# create R32 table
covtab = [[[[None for i in range(32)] for j in range(32)] for k in range(32)] for m in range(32)]
for i in range(32):
    for j in range(32):
        for k in range(32):
            for m in range(32):
                if base[i][j][k][m]:
                    covtab[i][j][k][m] = base[i][j][k][m]
                else:
                    rel1s = findkey(srel, i).replace("{","").replace("}","").split(", ")
                    rel2s = findkey(srel, j).replace("{","").replace("}","").split(", ")
                    rel3s = findkey(srel, k).replace("{","").replace("}","").split(", ")
                    rel4s = findkey(srel, m).replace("{","").replace("}","").split(", ")
                    R = 0
                    for rel1 in rel1s:
                        for rel2 in rel2s:
                            for rel3 in rel3s:
                                for rel4 in rel4s:
                                    tmpR = base[srel[rel1]][srel[rel2]][srel[rel3]][srel[rel4]]
                                    if tmpR:
                                        R = R | tmpR
                                    else:
                                        R = R | 0
                    if R == 0:
                        covtab[i][j][k][m] = None
                    else:
                        covtab[i][j][k][m] = R


for i in range(32):
    for j in range(32):
        for k in range(32):
            for m in range(32):
                print "i=",i, "j=",j, "k=",k, "m=",m, "covtab=",covtab[i][j][k][m] 

