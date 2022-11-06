# 1. Githubda new repo oching va unga main.py  kiritishingiz kerak.
# 2. main.py faylingiz ichida ikkita funksiya bo’lsin ya’ni 
# 3. 1-funksiya faqat bitta kiritilgan faylni shu fayldan boshqa faylga ko’chirsin.
# 3. 2-funksiya esa barcha fayllarni bir fayldan ikkinchisiga ko’chirsin
# Hint:
# 1-funksiya 3ta parametr olsin: 
# (fayl_nomi : str, eski_joy : str, yangi_joy : str) -> Bool
# 2-funksiya 2ta parametr olsin:
# (eski_joy : str, yangi_joy : str)
# Funksiyangizga doc-string yozishingiz ham mumkin agar xohish bo'lsa yoki men bergandanda boshqacharoq mukammalroq funksiya qiladigan bo'lsangiz.

# commitni ma’noli qilib yozing iltimos shunchaki added emas nima vazifa bajarishini to’liqroq qilib yozing.

# P.S: reop degani bu — repository so’zini qisqartmasi
from pathlib import Path 

# # 1 - funksiy bu funkisya orqali biz  1 - ta failni papkadan papkaga kochirishni korip chqamz
# def new(fayl_nomi : str, eski_joy : str, yangi_joy : str ): # new dgan funksiya yaratamz va unga parametrlarni krtamz
#     desktop = Path("/Users/HP/desktop") #Biz buyerda desktopga kirvolamiz
#     old = desktop/eski_joy/fayl_nomi #bu yerda eski failni joini kratamza va failni nomini yozamiz 
#     new = desktop/yangi_joy/fayl_nomi # bu yerda kochirmoxchi bogan joimizni krtamz va failni nomini yozamz
#     old.replace(new) # replace() --> funsiyasi blan "old" da gi failni "new" ga kochiramz 
# new("main.html","eski","yangi")

# 2 - funkiya bu funksiyada biz barcha failni kochirishni korip chqamz 
def bmw(eski_joy : str , yangi_joy : str):
    desktop = Path("Users/HP/desktop")
    eski = desktop/eski_joy
    for x in eski:
        yangi = desktop/yangi_joy/x
        eski.replace(yangi)
bmw("eski", "yangi")
    