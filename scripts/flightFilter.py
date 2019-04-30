import xlrd
import xlwt
import sys

# 因为没有在遍历的时候删除相同项，向后的相同项匹配会造成统计不全和重复统计的情况，
# 实际上遍历一边，归类，再做提取才是正确的情况。

def fun(filename, sheetNo=0):
    book=xlrd.open_workbook(filename)
    sh=book.sheet_by_index(sheetNo)
    cols = sh.ncols
    rows = sh.nrows
    print('cols=', cols)
    print('rows=', rows)

    dataSet = {

    }

    for r in range(1, rows): # cols and rows start from 0

        value = sh.cell_value(rowx=r,colx=0)
        if not dataSet.get(value):
            dataSet[value] = []

        dataSet[value].append([
            sh.cell_value(rowx=r,colx=0),
            sh.cell_value(rowx=r,colx=1),
            sh.cell_value(rowx=r,colx=2),
            sh.cell_value(rowx=r,colx=3),
            sh.cell_value(rowx=r,colx=4),
            sh.cell_value(rowx=r,colx=5),
            sh.cell_value(rowx=r,colx=6),
            sh.cell_value(rowx=r,colx=7),
            sh.cell_value(rowx=r,colx=8)
        ])

    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('筛选过的冻结订单')
    for c in range(cols):
        worksheet.write(0, c, label = sh.cell_value(rowx=0,colx=c))

    countrow = 1
    for i,j in dataSet.items():
        # 存在单数的情况可能就是冻结了未解冻
        if len(j) % 2 != 0:
            for k in j:
                if (k[4] == "冻结"):
                    for c in range(cols):
                        worksheet.write(countrow, c, label = k[c])
                    countrow += 1
                    break

    workbook.save('freezeFilter.xls')



    #     count = 1
    #     row_list = list()
    #     row_list.append(r)
    #     value = sh.cell_value(rowx=r,colx=0)
    #     # 遍历首列，订单号
    #     for l in range(r + 1, rows):
    #         if (sh.cell_value(rowx=l,colx=0) == value):
    #             count += 1
    #             row_list.append(l)
    #     
    #     if (count%2 == 1):
    #         # 单数情况，可能是多次冻结后未有解冻的情况
    #         print(count)
    #         for i in row_list:
    #             if (sh.cell_value(rowx=i,colx=4) == '冻结'):
    #                 dataSet[value] = [
    #                     sh.cell_value(rowx=i,colx=0),
    #                     sh.cell_value(rowx=i,colx=1),
    #                     sh.cell_value(rowx=i,colx=2),
    #                     sh.cell_value(rowx=i,colx=3),
    #                     sh.cell_value(rowx=i,colx=4),
    #                     sh.cell_value(rowx=i,colx=5),
    #                     sh.cell_value(rowx=i,colx=6),
    #                     sh.cell_value(rowx=i,colx=7),
    #                     sh.cell_value(rowx=i,colx=8)
    #                 ]
    #                 break
# 
# 
    # workbook = xlwt.Workbook(encoding = 'ascii')
    # worksheet = workbook.add_sheet('My Worksheet')
    # for c in range(cols):
    #     worksheet.write(0, c, label = sh.cell_value(rowx=0,colx=c))
# 
    # writerow=0
    # for key, data in dataSet.items():
    #     writerow+=1
    #     for c in range(cols):
    #         worksheet.write(writerow, c, label = data[c])
# 
    # workbook.save('Excel_Workbook.xls')

if __name__ == "__main__":
    path = sys.argv[1:]
    fun(path[0])