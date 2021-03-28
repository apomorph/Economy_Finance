import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from brokenaxes import brokenaxes               #pip install brokenaxes 

plt.rcParams['font.sans-serif']=['SimHei']      #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      #用来正常显示负号

x = [100,200,300,400,500]
yd = [950,900,850,800,750]
ys = [750,800,850,900,950]

plt.figure(figsize=(12,8))
#打断y轴
bax = brokenaxes(ylims=((0, 10), (730, 1000)),hspace=0.05,diag_color='r')

bax.plot(x,yd,marker='o',markersize=5,markerfacecolor='k')
bax.plot(x,ys,marker='o',markersize=5,markerfacecolor='k')

bax.annotate('A',xy=(x[0],yd[0]),xytext=(x[0]-5,yd[0]-10))
bax.annotate('B',xy=(x[1],yd[1]),xytext=(x[1]-5,yd[1]-10))
bax.annotate('C',xy=(x[2],yd[2]),xytext=(x[2],yd[2]+5))
bax.annotate('D',xy=(x[3],yd[3]),xytext=(x[3]-5,yd[3]-10))
bax.annotate('E',xy=(x[4],yd[4]),xytext=(x[4]-5,yd[4]-10))

bax.annotate('F',xy=(x[0],ys[0]),xytext=(x[0]+5,ys[0]-10))
bax.annotate('G',xy=(x[1],ys[1]),xytext=(x[1]+5,ys[1]-10))
bax.annotate('H',xy=(x[3],ys[3]),xytext=(x[3]+5,ys[3]-10))
bax.annotate('I',xy=(x[4],ys[4]),xytext=(x[4]+5,ys[4]-10))

bax.text(520, 750, r'$B^{d}$',fontsize=12,color='blue')
bax.text(520, 950, r'$B^{s}$',fontsize=12,color='orange')

bax.plot([500, 0], [750, 750], color ='green', linewidth=0.5, linestyle="--")
bax.plot([500, 0], [950, 950], color ='green', linewidth=0.5, linestyle="--")
bax.plot([300, 300], [850, 0], color ='red', linewidth=0.5, linestyle="--")
bax.plot([300, 0], [850, 850], color ='red', linewidth=0.5, linestyle="--")

# bax.axs[0].set_yticks([750, 800, 850, 900, 950, 1000], 
#         ['r$750\\(i=33.0%)$','r$800\\(i=25.0%)$','r$P^{*}=850\\(i^{*}=17.6%)$','r$900\\(i=11.1%)$','r$950\\(i=5.3%)$','r$1000\\(i=0%)$']) 
#set_ticks() 从Matplotlib 3.2之后就废弃了 然而装回3.1版本也没有生效... 是brokenaxes的问题吗？
#只能当普通文本写了（按缩放figure会导致位置不准确）：
bax.text(-40, 740, '(i=33.0%)')
bax.text(-40, 790, '(i=25.0%)')
bax.text(-45, 847, '$P^{*}=$')  
bax.text(-54, 840, '$(i^{*}=17.6\\%)$')  
bax.text(-40, 890, '(i=11.1%)')
bax.text(-35, 940, '(i=5.3%)')
bax.text(-26, 990, '(i=0%)')

# plt.xlim(0, 600)  
bax.set_xlim(0, 600)

#设置刻度间隔 （使用了brokenaxes后不需要设置了...）
# x_major_locator=MultipleLocator(100)
# y_major_locator=MultipleLocator(50)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# ax.yaxis.set_major_locator(y_major_locator)

bax.set_title("债券的供需曲线", fontsize = 15)
bax.set_xlabel("债券数量，B(十亿美元)")
bax.set_ylabel("债券价格，P(美元)", loc = "top", rotation = 0, fontsize = 9)

# plt.subplots_adjust(left=0.25, wspace=0.5, hspace=0.8, bottom=0.15, top=0.9)

bax.annotate('', 
                xy=(50, 850), 
                xytext=(50, 950), 
                arrowprops=dict(facecolor='grey', shrink=0.1, headwidth=8, width=2)
            )
bax.annotate('', 
                xy=(50, 850), 
                xytext=(50, 750), 
                arrowprops=dict(facecolor='grey', shrink=0.1, headwidth=8, width=2)
            )


bax.text(180, 950, 
        '存在超额供给时,\n债券价格下跌到$P^{*}$', 
        fontsize=13,
        bbox=dict(facecolor='red', alpha=0.5))
bax.text(150, 750, 
        '存在超额需求时,\n债券价格上升到$P^{*}$', 
        fontsize=13,
        bbox=dict(facecolor='red', alpha=0.5))

plt.show()
