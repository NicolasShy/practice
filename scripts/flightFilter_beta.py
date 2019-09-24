import xlrd
import xlwt
import sys

# 因为没有在遍历的时候删除相同项，向后的相同项匹配会造成统计不全和重复统计的情况，
# 实际上遍历一边，归类，再做提取才是正确的情况。

def fun1(filename, sheetNo=0):
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
    worksheet = workbook.add_sheet('冻结的订单')
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


def fun2 (filename, sheetNo = 2):
    book=xlrd.open_workbook(filename)
    sh=book.sheet_by_index(sheetNo)
    cols = sh.ncols
    rows = sh.nrows
    print('cols=', cols)
    print('rows=', rows)
    
    dataSet = {}
    for r in range(1, rows):
        value = sh.cell_value(rowx=r,colx=1) # 流水号为key
        if not dataSet.get(value):
            dataSet[value] = []

        dataSet[value].append([
            sh.cell_value(rowx=r,colx=0),
            sh.cell_value(rowx=r,colx=1),
            sh.cell_value(rowx=r,colx=2),
            sh.cell_value(rowx=r,colx=3),
            sh.cell_value(rowx=r,colx=4),
            sh.cell_value(rowx=r,colx=5)
        ])

    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('冻结的流水')
    # add title
    for c in range(cols):
        worksheet.write(0, c, label = sh.cell_value(rowx=0,colx=c))

    countrow = 1
    for i,j in dataSet.items():
        # 算出总金额，如果是0就过滤，不平衡就把该流水号下所有数据填入workbook
        balance_sum = 0
        for k in j:
            balance_sum += k[4]

        if (balance_sum != 0):
            for k in j:
                for c in range(cols):
                    worksheet.write(countrow, c, label = k[c])
                countrow += 1
            

    workbook.save('freezeBalanceFilter.xls')

if __name__ == "__main__":
    path = sys.argv[1:]
    fun1(path[0])
    fun2(path[0])