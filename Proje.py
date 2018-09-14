
# coding: utf-8

# In[ ]:





# In[2]:


from tkinter import *

frame=Tk()

#Framelerin yerleştirilmesi
frame.geometry("500x400")
frame.title("PassaParola")
ck1=Frame(bg="red")
ck1.pack()

ck2=Frame(ck1,bg="white")
ck2.grid(row=0, column=0)

#Labelların oluşturulması
first_contestant={"score":0,"state":True}
second_contestant={"score":0,"state":False}
letter_text=Label(frame,text="",fg="red",bd="2px",)
result=Label(frame,text="Passaparola",fg="red",bd="2px") 
first=Label(frame,text="Birinci Oyuncu",fg="black",bd="2px",font="Helvetica 10 bold")
second=Label(frame,text="İkinci Oyuncu",fg="black",bd="2px",font="Helvetica 10 bold")
first_score=Label(frame,text="0",fg="black",bd="2px")
second_score=Label(frame,text="0",fg="black",bd="2px")
turn=Label(frame,text="State",fg="black",bd="2px")
turn_description=Label(frame,text="Oyun Sırası: ",fg="black",bd="2px",font="Helvetica 13 bold")
answer=Entry(frame)

#Oyuncunun ilk durumu
first_contestant['state']==True
buttons = []

#tüm harflerin olduğu butonların oluşturulması
alfabe=["a", "b", "c","ç", "d", "e", "f", "g", "h","ı", "i", "j", "k", "l", "m", "n", "o","ö", "p", "r", "s","ş", "t", "u","ü", "v", "y", "z"]
for i in range(len(alfabe)):
    x=Button(ck2, text=alfabe[i].upper(), command=(lambda i=i: changecolor(i)), width=4, height=2)
    x.grid(column=i%10, row=i//10)
    #button_index=changecolor(i)
    buttons.append(x)
    
#Soruların oluşturulması   
global questions
questions={"AKLA VE GERÇEĞE AYKIRI":"abes","DOKÜMAN":"belge",
"KAHVE PİŞİRMEK İÇİN KULLANILAN SİLİNDİR BİÇİMLİ VE SAPLI KAP":"cezve","ÇÖZÜM YOLU BULAMAYAN":"çaresiz",
 "BALIK AVLAMAK İÇİN KIYILARA YAKIN YERLERDE DENİZ İÇİNE KURULAN YAPI":"dalyan",
"GENELLİKLE İPLİK DURUMUNA GETİRİLEBİLECEK LİFLİ MADDELER":"elyaf","İNSANLARIN BAŞKA İNSANLARLA İLETİŞİM KURMASINI \n VE BİLGİ ALIŞVERİŞİ YAPMASINI AMAÇLAYAN BİR SOSYAL PAYLAŞIM SİTESİ":"facebook",
"ALBAYLIKTAN SONRA GELEN YÜKSEK RÜTBELİ SUBAYLARA VERİLEN GENEL AD":"general",
"İÇİNE MÜREKKEP KONULAN KÜÇÜK KAP":"hokka",
"BÜYÜK AKARSULARA VERİLEN GENEL İSİM":"ırmak","TİKSİNTİ VEREN":"iğrenç",
"KEDİGİLLER FAMİLYASINDAN BİR YENİ DÜNYA MEMELİSİ":"jaguar","PAPAYI SEÇEN VE BAŞDANIŞMANLIĞINI YAPAN BAŞPAPAZ":"kardinal",
 "ADINI TAVUĞUN BİR KEMİĞİNDEN ALAN, HAFIZAYA DAYALI OYUN":"lades",
 "İSKAMBİLDE BİR KAĞIT DİZİSİ":"maça","TURUNÇGİLLER":"naranciye","FOTOĞRAF MAKİNESİNDE CİSİMLERDEN GELEN IŞINLARI\n EKRAN ÜZERİNE YANSITAN MERCEK":"objektif",
"LATİNCE: EUKARYOTA, HÜCRELERİNDE BİR ÇEKİRDEK \nVE BAŞKA ORGANELLER İÇEREN BİR CANLILAR GRUBU":"ökaryotlar",
"YUNAN MİTOLOJİSİNDE ADI GEÇEN KANATLI AT":"pegasus","BİR MÜZİK TOPLULUĞUNUN VEYA SANATÇININ HAZIRLAMIŞ OLDUĞU PARÇALAR":"repertuar",
 "BİR SAYFA ÜZERİNDE ALT ALTA VE YAN YANA GELEN KELİMELERDEN OLUŞAN DİZİ":"satır",
"ÜLKE ÇAPINDA YAYGINLAŞTIRILMIŞ ULAŞIM VE İLETİŞİM ÖRGÜSÜ":"şebeke",
 "GAZETE VE KİTAPLARDA BASKI SAYISI":"tiraj","GÜNEŞ SİSTEMİNİN GÜNEŞ'TEN YAKINLIK SIRASINA GÖRE 7. GEZEGENİ":"uranüs",
"ASLINDA OLMAYAN, TASARLANMIŞ İDEAL TOPLUM":"ütopya","OSMANLI İMPARATORLUĞU DÖNEMİNDE,\n ZAMANIN OLAYLARINI SAPTAYIP TARİHE GEÇİRMEKLE GÖREVLİ DEVLET TARİHÇİSİ": "vakanüvis",
"HİNDİSTANIN BAŞKENTİ":"yeni delhi","BURÇLAR KUŞAĞI":"zodyak"}

turn["text"]="Birinci Oyuncu"
sayi=0
#Butonlara tıklandığında sorularıgetirecek metodun çalıştırır ve Butonu tıklanmış gösterir.
def changecolor(i):
    buttons[i]["state"]=DISABLED
    global sayi
    sayi=sayi+1
    letter_text["text"]=buttons[i]["text"]
    play()
    
#Ekrana gelen soru ceplanarak puanlama yapılır
def cevapla():
    a= answer.get()
    global first_contestant
    harf= letter_text["text"]
    i=alfabe.index(harf.lower())
    print(i)
    print(list(questions.values())[i])
    if(a.lower()== list(questions.values())[i]):
        buttons[i]["bg"]="green"
        #yarışmacıların puanını arttırmak
        if(first_contestant["state"]==True):
            first_contestant['score']+=100 
        else:second_contestant['score']+=100
    else:
        if(first_contestant['state']==True):
            first_contestant['state']=False 
            second_contestant['state']=True 
            turn["text"]="İkinci Oyuncu"
        else:
            first_contestant['state']=True
            second_contestant['state']=False
            turn["text"]="Birinci Oyuncu"
        buttons[i]["bg"]="red"
    first_score["text"]=(first_contestant["score"])
    second_score["text"]=second_contestant["score"]
    
   #Oyunun sonunda Kazananın belirlenmesi
    if sayi==28:
        if int(first_score["text"])>int(second_score["text"]):
            turn["text"]="Kazanan: Birinci Oyuncu"
            turn["fg"]="Green"
            turn["font"]="Helvetica 15 bold"
        elif int(first_score["text"])<int(second_score["text"]):
            turn["text"]="Kazanan: İkinci Oyuncu"
            turn["fg"]="Green"
            turn["font"]="Helvetica 15 bold"
        else:
            turn["text"]="Oyun Berabere"
            turn["fg"]="Green"
            turn["font"]="Helvetica 15 bold"

#Pas tuşuna absıldığında oyun hakkı diğer oyuncuya geçer 
def pas():
    if(first_contestant["state"]==True):
            first_contestant['state']=False 
            second_contestant['state']=True 
            turn["text"]="İkinci Oyuncu"
    else:
        first_contestant['state']=True
        second_contestant['state']=False
        turn["text"]="Birinci Oyuncu"

#Cevapla ve Pas butonunun oluşturulması
reply = Button(frame, text ="CEVAPLA", command = cevapla,width=15)
pas = Button(frame, text ="PAS", command = pas,width=15)

#Butona tıklandığında o harf ile başlayan cevabın sorusu ekrana gelir.
def play():
    for i in range(len(questions.keys())):
        if(letter_text["text"].lower()==list(questions.values())[i][0]):
            #butona tıklanan soruyu labela yazdırır
            result["text"]=list(questions.keys())[i]
    first_score["text"]=first_contestant["score"]
    second_score["text"]=second_contestant["score"]
    
#Tüm design nesnelerinin frame içine yerleştirilmesi
letter_text.pack()
result.pack()
answer.pack()
reply.pack()
pas.pack(side=TOP)
turn_description.pack(side=TOP)
turn.pack(side=TOP)
first.pack(side=LEFT)
first_score.pack(side=LEFT)
second_score.pack(side=RIGHT)
second.pack(side=RIGHT)

frame.mainloop()

