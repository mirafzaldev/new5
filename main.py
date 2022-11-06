from pathlib import Path 

# 1 - funksiy bu funkisya orqali biz  1 - ta failni papkadan papkaga kochirishni korip chqamz
def new(fayl_nomi : str, eski_joy : str, yangi_joy : str ): # new dgan funksiya yaratamz va unga parametrlarni krtamz
    desktop = Path("/Users/HP/desktop") #Biz buyerda desktopga kirvolamiz
    old = desktop/eski_joy/fayl_nomi #bu yerda eski failni joini kratamza va failni nomini yozamiz 
    new = desktop/yangi_joy/fayl_nomi # bu yerda kochirmoxchi bogan joimizni krtamz va failni nomini yozamz
    old.replace(new) # replace() --> funsiyasi blan "old" da gi failni "new" ga kochiramz 
new("main.html","eski","yangi")

# 2 - funkiya bu funksiyada biz barcha failni kochirishni korip chqamz 
def bmw(eski_joy : str , yangi_joy : str):
    desktop = Path("Users/HP/desktop")
    eski = desktop/eski_joy
    for x in eski:
        yangi = desktop/yangi_joy/x
        eski.replace(yangi)
bmw("eski", "yangi")
     # Assalomlkum Otabek aka 2- chi funksiya xali oxirgacha qmadm Xudo Xohlasa bugun kechgach qb tashvoraman 