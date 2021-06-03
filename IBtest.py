Bank = {
    'แบงค์พัน' : 0,
    'แบงค์ห้าร้อย': 10, 
    'แบงค์ร้อย': 50, 
    'แบงค์ห้าสิบ': 50, 
    'แบงค์ยี่สิบ': 50
    }

Coin = {
    'เหรียญสิบบาท': 20,
    'เหรียญห้าบาท': 20,
    'เหรียญบาท': 100
}

price = int(input('input(ยอดต้องชำระ):'))
bill = int(input('input(แบงค์พัน):'))

t_back = Bank['แบงค์พัน']
new_t_bank = t_back + bill
Bank['แบงค์พัน'] = new_t_bank

Wallet = 13900
get = bill * 1000
change = get - price
new_Wallet = Wallet + price

def change_cal(change):
    print('1.เงินทอนคือ',change,'บาท')
    fivbill = change // 500
    change = change % 500 
    onebill = change // 100
    change = change % 100
    fifbill = change // 50
    change = change % 50
    twobill = change // 20
    change = change % 20
    tencoin = change //10
    change = change % 10
    fivcoin = change // 5
    change = change % 5
    onecoin = change // 1
    change = change % 1
  
    if fivbill != 0:
        print('- แบงค์ห้าร้อย',fivbill,'ใบ')
        back = Bank['แบงค์ห้าร้อย']
        new_bank = back - fivbill
        Bank['แบงค์ห้าร้อย'] = new_bank
    if onebill != 0:
        print('- แบงค์ร้อย',onebill,'ใบ')
        back = Bank['แบงค์ร้อย']
        new_bank = back - onebill
        Bank['แบงค์ร้อย'] = new_bank
    if fifbill != 0:
        print('- แบงค์ห้าสิบ',fifbill,'ใบ')
        back = Bank['แบงค์ห้าสิบ']
        new_bank = back - fifbill
        Bank['แบงค์ห้าสิบ'] = new_bank
    if twobill != 0:
        print('- แบงค์ยี่สิบ',twobill,'ใบ')
        back = Bank['แบงค์ยี่สิบ']
        new_bank = back - twobill
        Bank['แบงค์ยี่สิบ'] = new_bank
    if tencoin != 0:
        print('- เหรียญสิบบาท',tencoin,'เหรียญ')
        back = Coin['เหรียญสิบบาท']
        new_bank = back - tencoin
        Coin['เหรียญสิบบาท'] = new_bank
    if fivcoin != 0:
        print('- เหรียญห้าบาท',fivcoin,'เหรียญ')
        back = Coin['เหรียญห้าบาท']
        new_bank = back - fivcoin
        Coin['เหรียญห้าบาท'] = new_bank
    if onecoin != 0:
        print('- เหรียญบาท',onecoin,'เหรียญ')
        back = Coin['เหรียญบาท']
        new_bank = back - onecoin
        Coin['เหรียญบาท'] = new_bank

change_cal(change)

print('2.เงินคงเหลือคือ',new_Wallet,'บาท')
for key, value in Bank.items() :
    print ('-',key, value,'ใบ')
for key, value in Coin.items() :
    print ('-',key, value,'เหรียญ')