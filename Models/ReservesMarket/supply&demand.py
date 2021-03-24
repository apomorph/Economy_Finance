import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']      #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号

#变量
NBR = 10000
i_d = 1.0
i_or = 0.35
i_ff = 0.6
i_ff_1 = 0.475
i_ff_2 = 0.725


plt.plot([NBR,NBR,1.75*NBR],[0,i_d,i_d])
plt.plot([0.5*NBR,NBR,1.25*NBR,1.75*NBR],[1.1,i_ff,i_or,i_or])

plt.text(1.8*NBR, i_or, r'$R^{d}$')
plt.text(1.8*NBR, i_d, r'$R^{s}$')

plt.plot([NBR, 0], [i_ff, i_ff], color ='red', linewidth=0.5, linestyle="--")
plt.plot([1.125*NBR, 0],[i_ff_1, i_ff_1],color ='green', linewidth=0.5, linestyle="--")
plt.plot([0.875*NBR, 0],[i_ff_2, i_ff_2],color ='green', linewidth=0.5, linestyle="--")

plt.annotate('', 
                xy=(0.5*NBR, i_ff), 
                xytext=(0.5*NBR, i_ff_1), 
                arrowprops=dict(facecolor='black', shrink=0.05, headwidth=8, width=1)
            )
plt.annotate('', 
                xy=(0.5*NBR, i_ff), 
                xytext=(0.5*NBR, i_ff_2), 
                arrowprops=dict(facecolor='black', headwidth=8, width=1)
            )
plt.annotate("在$i_{ff}^{1}$处，准备金出现超额需求，\n联邦基金利率上升到$i_{ff}^{*}$", 
                xy=(0.53*NBR,(i_ff_1+i_ff)/2), 
                xytext=(0.6*NBR, 0.4*i_ff), 
                arrowprops=dict(facecolor='grey', headwidth=0.001, width=0.001),                #todo 这块不适合用箭头注释
                bbox=dict(boxstyle='round,pad=0.5', fc='grey', ec='k',lw=1 ,alpha=0.5)
            )
plt.annotate("在$i_{ff}^{2}$处，准备金出现超额供给，\n联邦基金利率下跌到$i_{ff}^{*}$", 
                xy=(0.53*NBR,(i_ff_2+i_ff)/2), 
                xytext=(0.7*NBR, 1.7*i_ff), 
                arrowprops=dict(facecolor='grey', headwidth=0.001, width=0.001),
                bbox=dict(boxstyle='round,pad=0.5', fc='grey', ec='k', lw=1, alpha=0.5)
            )
plt.text(NBR, i_ff_1, '{', alpha=0.7, fontsize=29, fontweight="light", rotation="90", verticalalignment="center")               #todo 转晕了 这个花括号怎么调...
plt.text(0.875*NBR, i_ff_2, '}', alpha=0.7, fontsize=29, fontweight="light", rotation="vertical", verticalalignment="bottom")

plt.plot([(0.875*NBR+NBR)/2,(0.7*NBR+NBR)/2],[1.05*i_ff_2,1.63*i_ff],color="black",linewidth=1)
plt.plot([(NBR+1.125*NBR)/2,(0.6*NBR+NBR)/2],[0.95*i_ff_1,0.65*i_ff],color="black",linewidth=1)

#设置轴线的范围
plt.axis([4000, 20000, 0, 1.2])

#设置轴线的点位置及提示
plt.xticks([NBR], [r'NBR']) 
plt.yticks([i_d, i_ff, i_or, i_ff_1, i_ff_2], [r'$i_{d}$', r'$i_{ff}^{*}$', r'$i_{or}$', r'$i_{ff}^{1}$', r'$i_{ff}^{2}$']) 

#将右边和上边的边框（脊）的颜色去掉
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.title("准备金市场的供需曲线")
plt.xlabel("准备金数量，R", loc = "right")
plt.ylabel("联邦基金利率", loc = "top", rotation = 0, fontsize = 9)

plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25, bottom=0.13, top=0.91)

plt.show()