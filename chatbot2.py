from tkinter import *
import pickle

customerDict = {}

def uploadData(customerDict):
    with open('database', 'wb') as DatabaseFile:
        pickle.dump(customerDict, DatabaseFile)

def loadData():
    global customerDict
    with open('database', 'rb') as DatabaseFile:
        customerDict = pickle.load(DatabaseFile)



class musteri():
    musteriNo = ""
    isimSoyisim = ""
    urun = ""
    arızaTarih = ""
    talep = ""
    
    def __init__(self, musteriNo):
        self.musteriNo = musteriNo

    def getInfo(self):
        return (f" Müşteri No; {self.musteriNo} \n İsim Soyisim; {self.isimSoyisim}  \n Ürün; {self.urun} \n Arıza Tarihi; {self.arızaTarih} \n Talep; {self.talep}")

loadData()

root = Tk()

isimSoyisimBool = False
urunBool = False
ArızaBool = False
talepBool = False
musteriNoBool = False
musteriNo = None

def send():
    global musteriNoBool
    global isimSoyisimBool
    global urunBool
    global ArızaBool
    global talepBool
    global customerDict
    global musteriNo
    
    validQuestion = False

    userInput = e.get()
    send = "You => " + e.get()
    txt.insert(END, "\n" + send)
    e.delete(0,END)

    if talepBool:
        talepBool = False
        customerDict[musteriNo].talep = userInput
        giveAnswer(txt, "Gerekli Bilgiler alınmıştır, müşteri temsilcimiz size geri dönüş yapacaktır. İyi günler!")
        #DATABASE'E VERİLER BURADA GİRİLECEKTİR !
        uploadData(customerDict)
        with open("musteriler.txt","a", encoding="UTF-8") as file:
            file.write("\n")
            file.write("Müşteri No; " + musteriNo + "\n")
            file.write("İsim Soyisim; " + customerDict[musteriNo].isimSoyisim + "\n")
            file.write("Ürün; " + customerDict[musteriNo].urun + "\n")
            file.write("Arıza Tarihi; " + customerDict[musteriNo].arızaTarih + "\n")
            file.write("Talep; " + customerDict[musteriNo].talep + "\n")
            file.write("----------------------------------------------------------------------")
        return

    if ArızaBool:
        ArızaBool = False
        customerDict[musteriNo].arızaTarih = userInput
        giveAnswer(txt, "Talebinizi öğrenebilir miyim ?")
        talepBool = True

    if urunBool:
        urunBool = False
        customerDict[musteriNo].urun = userInput
        giveAnswer(txt, "Ürününüzün marka ve modeli; " + userInput + " \n Arıza tarihini öğrenebilir miyim ?")
        ArızaBool = True

    if isimSoyisimBool:
        isimSoyisimBool = False

        customerDict[musteriNo].isimSoyisim = userInput
        giveAnswer(txt, "Sayın "+ userInput + ", Ürününüzün markasını ve modelini öğrenebilir miyim ?")
        urunBool = True


    if musteriNoBool:
        musteriNoBool = False

        if userInput in customerDict:
            giveAnswer(txt, "Sizin talebiniz zaten alındı !")
            return       

        customerDict[userInput] = musteri(userInput)
        customerDict[userInput].musteriNo = userInput
        musteriNo = userInput
        giveAnswer(txt, "İsminizi ve soyisminizi öğrenebilir miyim ? Örnek = \" Mehmet Demir \"")
        isimSoyisimBool = True

    if userInput.lower() in ["merhaba", "selam"]:
        giveAnswer(txt, "Merhaba hoşgeldiniz ! Ben bir arıza botuyum, eğer herhangi bir cihazınızla ilgili arıza yaşıyorsanız bu konuda size yardımcı olabilirim ! Arıza kaydı için lütfen \"Arıza kaydı\" yazınız.")
        validQuestion = True

    if userInput.lower() == "arıza kaydı":
        giveAnswer(txt, "Hemen sizinle ilgileniyorum ! Öncelikle müşteri numaranızı öğrenebilir miyim ? ")
        musteriNoBool = True
        validQuestion = True

    if userInput.lower() == "arıza kayıtları":
        for i in customerDict.values():
            info = i.getInfo()
            giveAnswer(txt, info)
        giveAnswer(txt, "-------------------------------------")
        validQuestion = True

    if (not validQuestion) and not (talepBool | ArızaBool | urunBool | isimSoyisimBool):
        giveAnswer(txt, "Geçersiz bir cevap verdiniz. Arıza kaydı için lütfen \" Arıza Kaydı \" yazınız")



def giveAnswer(txt,answer):
    txt.insert(END, "\n" + "Bot => " +answer)



txt = Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Arıza Kayıt Sistemi")
txt.configure(background='lightblue')
root.configure(background='black')
root.mainloop()