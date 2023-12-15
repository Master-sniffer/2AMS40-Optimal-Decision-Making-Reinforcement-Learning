import ast
import numpy as np
import math

def pointer(s):
    return s[0] * 11 + s[1]
I = [i for i in range(41)]
A = [i for i in range(11)]
S = [(i, a) for i in I for a in A]
P = np.array(ast.literal_eval(open('Probability.txt', 'r').read()))
R = np.array(ast.literal_eval(open('R.txt', 'r').read()))
gamma = 0.9

max_iter = 5
delta = 1e-400
V = [0 for _ in range(len(S))]
pi = [0 for _ in range(len(S))]
count = 0

for i in range(max_iter):
    max_diff = 0
    V_new = [0 for _ in range(len(S))]
    for s in S:
        max_val = 0
        for a in A:
            val = R[a][pointer(s)]
            for i in I:
                val += P[pointer(s)][pointer((i, a))] * (gamma * V[pointer((i, a))])
            max_val = max(val, max_val)
            if V[pointer(s)] < val:
                pi[pointer(s)] = a
        V_new[pointer(s)] = max_val
        max_diff = max(max_diff, abs(V[pointer(s)] - V_new[pointer(s)]))
    V = V_new
    count += 1
    print('Count: ' + str(count))
    if max_diff < delta:
        print('Break')
        break
print(V)
print(pi)
print(count)

# V = [108496.44208422315, 110146.44208422315, 111796.44208422315, 113446.44208422315, 115096.44208422315, 116746.44208422315, 118396.44208422315, 120046.44208422315, 121696.44208422315, 123346.44208422315, 124996.44208422315, 110496.44208422315, 112146.44208422315, 113796.44208422315, 115446.44208422315, 117096.44208422315, 118746.44208422315, 120396.44208422315, 122046.44208422315, 123696.44208422315, 125346.44208422315, 126996.44208422315, 112496.44208422315, 114146.44208422315, 115796.44208422315, 117446.44208422315, 119096.44208422315, 120746.44208422315, 122396.44208422315, 124046.44208422315, 125696.44208422315, 127346.44208422315, 128996.44208422315, 114496.44208422315, 116146.44208422315, 117796.44208422315, 119446.44208422315, 121096.44208422315, 122746.44208422315, 124396.44208422315, 126046.44208422315, 127696.44208422315, 129346.44208422315, 130996.44208422315, 116496.44208422315, 118146.44208422315, 119796.44208422315, 121446.44208422315, 123096.44208422315, 124746.44208422315, 126396.44208422315, 128046.44208422315, 129696.44208422315, 131346.44208422315, 132996.44208422315, 118496.44208422315, 120146.44208422315, 121796.44208422315, 123446.44208422315, 125096.44208422315, 126746.44208422315, 128396.44208422315, 130046.44208422315, 131696.44208422315, 133346.44208422315, 134996.44208422315, 120496.44208422315, 122146.44208422315, 123796.44208422315, 125446.44208422315, 127096.44208422315, 128746.44208422315, 130396.44208422315, 132046.44208422315, 133696.44208422315, 135346.44208422315, 136996.44208422315, 122496.44208422315, 124146.44208422315, 125796.44208422315, 127446.44208422315, 129096.44208422315, 130746.44208422315, 132396.44208422315, 134046.44208422315, 135696.44208422315, 137346.44208422315, 138996.44208422315, 124496.44208422315, 126146.44208422315, 127796.44208422315, 129446.44208422315, 131096.44208422315, 132746.44208422315, 134396.44208422315, 136046.44208422315, 137696.44208422315, 139346.44208422315, 140996.44208422315, 126496.44208422315, 128146.44208422315, 129796.44208422315, 131446.44208422315, 133096.44208422315, 134746.44208422315, 136396.44208422315, 138046.44208422315, 139696.44208422315, 141346.44208422315, 142996.44208422315, 128496.44208422315, 130146.44208422315, 131796.44208422315, 133446.44208422315, 135096.44208422315, 136746.44208422315, 138396.44208422315, 140046.44208422315, 141696.44208422315, 143346.44208422315, 144996.44208422315, 130496.44208422315, 132146.44208422315, 133785.94208422315, 135446.44208422315, 137096.44208422315, 138746.44208422315, 140396.44208422315, 142046.44208422315, 143696.44208422315, 145346.44208422315, 146996.44208422315, 132496.44208422315, 134146.44208422315, 135796.44208422315, 137446.44208422315, 139096.44208422315, 140746.44208422315, 142396.44208422315, 144046.44208422315, 145696.44208422315, 147346.44208422315, 148996.44208422315, 134496.44208422315, 136146.44208422315, 137796.44208422315, 139446.44208422315, 141096.44208422315, 142746.44208422315, 144396.44208422315, 146046.44208422315, 147696.44208422315, 149342.94208422315, 150996.44208422315, 136496.44208422315, 138146.44208422315, 139796.44208422315, 141446.44208422315, 143096.44208422315, 144746.44208422315, 146392.94208422315, 148046.44208422315, 149696.44208422315, 151346.44208422315, 152982.44208422315, 138496.44208422315, 140132.44208422315, 141778.94208422315, 143442.94208422315, 145092.94208422315, 146746.44208422315, 148396.44208422315, 150042.94208422315, 151696.44208422315, 153346.44208422315, 154992.94208422315, 140482.44208422315, 142125.44208422312, 143796.44208422315, 145421.94208422315, 147089.44208422315, 148725.44208422315, 150385.94208422315, 152042.94208422315, 153689.44208422315, 155335.94208422315, 156982.44208422312, 142485.94208422315, 144128.94208422312, 145768.44208422318, 147421.94208422312, 149068.44208422315, 150725.44208422312, 152375.44208422315, 154035.94208422315, 155657.94208422315, 157318.44208422315, 158978.81608422313, 144457.94208422315, 146111.44208422318, 147778.94208422315, 149432.44208422315, 151061.44208422318, 152711.44208422312, 154364.94208422315, 155997.44208422315, 157668.44208422315, 159304.44208422315, 160936.81608422313, 146394.94208422318, 148097.44208422315, 149757.94208422318, 151404.44208422318, 153047.44208422315, 154707.94208422315, 156354.44208422315, 157972.94208422312, 159654.44208422315, 161258.91058422314, 162950.69008422314, 148412.44208422315, 150065.94208422315, 151740.44208422312, 153404.44208422315, 155033.44208422315, 156721.94208422312, 158277.44208422318, 159983.44208422315, 161654.44208422315, 163269.44208422315, 164929.94208422318, 150352.94208422318, 151988.94208422318, 153680.94208422315, 155194.44208422315, 156956.44208422315, 158623.94208422315, 160277.31608422316, 161902.94208422312, 163475.78458422312, 165093.74908422315, 166837.4289502231, 152356.44208422318, 153953.94208422315, 155673.94208422318, 157316.94208422312, 158791.81608422316, 160504.94208422315, 162189.94208422318, 163794.44208422315, 165478.77831622315, 167086.33845022315, 168781.74281622312, 154111.44208422318, 155852.44208422312, 157474.44208422315, 159152.31608422313, 160826.94208422312, 162441.81608422313, 164077.56408422318, 165671.78458422315, 167338.90545022316, 168914.74168222307, 170636.90619801715, 156174.44208422315, 157677.44208422315, 159243.44208422315, 161054.44208422315, 162648.44208422312, 164238.94208422315, 166021.56408422318, 167464.62195022314, 169173.10941422312, 170857.41754822308, 172556.06083201716, 158041.44208422315, 159533.94208422318, 161047.44208422315, 162781.31608422313, 164385.91058422314, 166091.9105842231, 167702.3361822231, 169436.68381622314, 171131.71358422312, 172784.73881622317, 174402.50978022316, 159600.19008422317, 161201.41058422317, 163008.94208422315, 164651.94208422315, 166490.94208422318, 167923.40658422312, 169650.78458422312, 171190.9581822231, 172899.29041422316, 174349.30327309927, 176111.85706007513, 161295.94208422315, 163145.41058422314, 164732.44208422312, 166417.0640842231, 168119.81608422313, 169594.53258422317, 171337.1065482231, 173025.54014622315, 174889.64431622313, 176140.3743580171, 178049.5357045541, 163064.94208422312, 164826.65858422322, 166613.44208422315, 168294.91058422317, 169723.62308422316, 171555.55895022315, 173025.26231622312, 174798.85298681117, 176492.80736627142, 178144.91400386917, 179599.01528003544, 165176.91058422314, 166675.93808422313, 168252.56408422315, 170027.99708422314, 171442.42041422313, 173120.58018222314, 174731.09185281108, 176094.68914239915, 178217.09613304125, 179814.86290078115, 181255.15433473012, 166634.25308422314, 168329.37508422314, 169972.53258422317, 171596.73995022313, 173456.95818222317, 174743.75682324724, 176496.84216201716, 178128.9115240751, 179815.94437397076, 181346.29128082943, 183015.23033030092, 168497.4380842231, 170235.00108422316, 171863.46445022314, 173194.62457981115, 175021.21093001714, 176581.15489401718, 178232.51700027141, 179550.04869921142, 181707.85870235943, 182879.78307565118, 182943.98386755094, 169684.80581622315, 171611.3069502231, 173207.45131622313, 174942.14101222315, 176673.20801222316, 177976.7888469474, 179783.62119241824, 181477.89369638887, 183133.24420745403, 182889.53456320942, 182368.80146780907, 171588.25718222314, 173447.86838881113, 175290.31504822313, 176634.76759674726, 178217.29320381113, 179632.98745217753, 181835.70217656382, 183350.4261453053, 182644.57914986266, 182485.78019462634, 181941.03138650424, 173301.60368222315, 174926.34087822313, 176539.96846264214, 178307.4234053991, 180250.5169042231, 181570.31620602956, 183338.51124963624, 182785.39986171134, 182394.5964591133, 182277.21528008083, 181507.83385917172, 174645.68051222316, 176664.66111022315, 178627.30078022307, 179999.25322460514, 181440.1672352114, 183290.99452496995, 182457.44462925894, 182606.28756272912, 182087.2844555487, 181929.75416516032, 181367.1768449152, 176519.07033027138, 178229.1454010413, 179769.0767090896, 181512.01489721728, 183413.79807490192, 182779.7439736528, 182705.89333547172, 182025.69656879955, 181426.1622408075, 181197.70076911696, 180607.6620227236, 178464.26718281116, 179976.60393118142, 181646.72920081974, 183223.68967491432, 182528.45116874695, 182468.21203939102, 182046.4289496379, 181611.79657099975, 181561.93475747237, 181075.31746251482, 180433.81000691955, 180104.36254507513, 181736.83537604514, 183130.15709686637, 182744.59548560728, 182457.61679278803, 182341.19195137886, 181559.36668103337, 181261.82459610124, 180681.72820074516, 180481.4031052028, 180008.6771648689, 181592.31977290765, 183289.40463642863, 182750.58971082416, 182335.30557344964, 181898.7585117631, 181771.83119815297, 181249.14259194068, 180768.7704269938, 179771.59372318847, 179455.59564506347, 178894.34000561872, 183217.36089883544, 182957.5839194996, 182412.84843659872, 182036.3825278219, 181547.09046655157, 181429.7291255159, 180999.3958890379, 180154.76026265047, 179547.5699903571, 179565.3763965654, 178650.83145186782]
# pi = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]