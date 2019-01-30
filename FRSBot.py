import requests
import subprocess as sp
from lxml import html
from threading import Thread
import json
from time import sleep

class FRSBot:

    def __init__(self, name, ErroPrev = False):
        self.__page = None
        self.__ErroPrev = ErroPrev
        self.name = name
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        self.__matkul = json.load(open('matkul.json'))[self.name]
        self.__user = json.load(open('user.json'))[self.name]
        self.__session = requests.session()
        self.__get('https://integra.its.ac.id/')
    
    def __post(self, url, dataDict):

        if(self.__ErroPrev):
            self.__page = self.__session.post(url, data=dataDict, headers=self.__headers)
        else:
            try:
                self.__page = self.__session.post(url, data=dataDict, headers=self.__headers)
            except:
                print(self.name + " : Error POST Data Methode to --> " + url)
    
    def __get(self, url):

        if(self.__ErroPrev):
            self.__page = self.__session.get(url, headers=self.__headers)
        else:
            try:
                self.__page = self.__session.get(url, headers=self.__headers)
            except:
                print(self.name + " : Error Get Methode to --> " + url)

    def __xpath(self, param):

        tree = html.fromstring(self.__page.content)

        if(self.__ErroPrev):
            Element = tree.xpath(param)
            return Element
        else:
            try:
                Element = tree.xpath(param)
                return Element
            except:
                print(self.name + ": Error Finding Element --> " + param)
                return []

    def __procLogin(self, publicKey):
        a = str(sp.check_output(["node","login.js", self.__user['nrp'],  self.__user['password'], publicKey]))
        return a[2:-3]

    def __login(self):
        self.__get('https://integra.its.ac.id/')
        data = str(self.__page.text)
        start = data.find("-----BEGIN PUBLIC KEY-----")
        end = data.rfind("-----END PUBLIC KEY-----") + 24
        publicKey = data[start:end]
        loginData = self.__procLogin(publicKey)
        self.__post('https://integra.its.ac.id/', dict(content=loginData, p='', n=''))
        self.__get('https://integra.its.ac.id/dashboard.php?sim=AKAD__10__')
        self.__get(self.__page.text[self.__page.text.find('URL=')+4:-2])
        self.__get('https://akademik.its.ac.id/sys_login.php')

    def __pilihMatkul(self, namaMatkul, kelas):
        datas = self.__xpath('//option[contains(text(),"' + namaMatkul +'")]')
        value = ''
        for data in datas:
            if(data.attrib['value'].find('|' + kelas + '|') != -1):
                value = data.attrib['value']
                break
        if(value != ''):
            oldNRP = self.__xpath('//input[@id="nrp"]')[0].attrib['value']
            self.__post('https://akademik.its.ac.id/list_frs.php', dict(semesterTerm='2', thnAjaran='2018', kelasjur=value, kelastpb='UG4905|—|2018|__TPB|0', nrp=oldNRP, act='ambil', key=value))
            print(self.name + " Memilih : " + value + " - " + namaMatkul)
        else:
            print(self.name + " : Error Memilih Matkul")

    def __isAllMatkulSelected(self):
        self.__get('https://akademik.its.ac.id/list_frs.php')
        while(self.__matkul):
            if(self.__xpath('//td[contains(text(),"' + self.__matkul[0]['nama'] + '")]') != []): self.__matkul.pop(0)
        
        if(not self.__matkul): return True
        else: return False
    
    def prevPage(self, print=False):
        f = open('FRSBot-Respose.html','w')
        f.write(self.__page.text)
        f.close()

        if(print): print(self.__page.text)

    def run(self):
        print("MASTERW6B is Starting FRS BOT for " + self.name + " !")
        print(self.name + " LOGIN !")
        self.__login()

        while(not self.__isAllMatkulSelected()):
            threadMatkul = []
            for data in self.__matkul:
                threadMatkul.append(Thread(target=self.__pilihMatkul,args=(data['nama'], data['kelas'],), daemon=True))
                    
            for t in threadMatkul: t.start()
            for t in threadMatkul: t.join()

            del threadMatkul
            sleep(5)
            
        if(not self.__matkul): print(self.name + ' : Semua Matkul Sudah Terpilih, yeeeyy :)')