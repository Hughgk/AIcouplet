import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
lossfilename = 'loss.txt'
evaluatefilename = 'score'

step = []
loss = []

evaluate_step , evaluate_score , evaluate_loss = [] , [] , []

def readloss() :

    with open(lossfilename , 'r' , encoding='utf-8') as f :
        lines = f.readlines()

        for line in lines :
            data = []
            try :
                temp = line.split('. ')
                temp1 = temp[1].split(', ')
                for i in temp1:
                    tt = i.split(': ')
                    data.append(float(tt[1]))
            except :
                continue

            step.append(data[0])
            loss.append(data[1])


def readevaluate():
    with open(evaluatefilename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            data = []
            try:
                temp = line.split('. ')
                temp1 = temp[1].split(', ')
                for i in temp1:
                    tt = i.split(': ')
                    data.append(float(tt[1]))
            except:
                continue

            evaluate_step.append(data[0])
            evaluate_score.append(data[1])
            evaluate_loss.append(data[2])

        print(evaluate_step)

def drawloss() :

    fig = plt.figure(figsize=(10, 10))  # 创建绘图窗口，并设置窗口大小
    # 画第一张图
    ax1 = fig.add_subplot(211)  # 将画面分割为2行1列选第一个
    ax1.plot(step, loss, 'red', label='loss')  # 画dis-loss的值，颜色红
    ax1.legend(loc='upper right')  # 绘制图例，plot()中的label值
    ax1.set_xlabel('step')  # 设置X轴名称
    ax1.set_ylabel('loss')  # 设置Y轴名称

    # 画第二张图
    ax2 = fig.add_subplot(212)  # 将画面分割为2行1列选第二个
    ax2.plot(evaluate_step, evaluate_score, 'blue', label='score')  # 画gan-loss的值，颜色蓝
    ax2.legend(loc='upper right')  # loc为图例位置，设置在右上方，（右下方为lower right）
    ax2.set_xlabel('step')
    ax2.set_ylabel('Evaluate-score')
    plt.show()  # 显示绘制的图



if __name__ == '__main__' :
    readloss()
    readevaluate()
    drawloss()