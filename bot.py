import requests
from time import sleep
from os import system

#çerezlerin değerlerini giriniz
reqs = { 
    "ct0":"",
    "auth_token":""
    }


def follow(userid):
    cookie =  {
        "ct0":reqs["ct0"],
        "auth_token":reqs["auth_token"]
        }
    
    data = {
        "include_profile_interstitial_type": "1",
        "include_blocking": "1",
        "include_blocked_by": "1",
        "include_followed_by": "1",
        "include_want_retweets": "1",
        "include_mute_edge": "1",
        "include_can_dm": "1",
        "include_can_media_tag": "1",
        "include_ext_has_nft_avatar": "1",
        "skip_status": "1",
        "id": userid
        }
    
    header = {
        "X-Csrf-Token": reqs["ct0"],
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        }
    
    istek = requests.post("https://twitter.com/i/api/1.1/friendships/create.json",  cookies=cookie, data=data, headers=header)
    
    try:
        istek.json()
        return(userid+" --> Takip edildi!")
    except:
        return(userid+" --> Hata!")

def unfollow(userid):
    cookie =  {
        "ct0":reqs["ct0"],
        "auth_token":reqs["auth_token"]
        }
    
    data = {
        "include_profile_interstitial_type": "1",
        "include_blocking": "1",
        "include_blocked_by": "1",
        "include_followed_by": "1",
        "include_want_retweets": "1",
        "include_mute_edge": "1",
        "include_can_dm": "1",
        "include_can_media_tag": "1",
        "include_ext_has_nft_avatar": "1",
        "skip_status": "1",
        "id": userid
        }
    
    header = {
        "X-Csrf-Token": reqs["ct0"],
        "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        }
    
    istek = requests.post("https://twitter.com/i/api/1.1/friendships/destroy.json",  cookies=cookie, data=data, headers=header)
    
    try:
        istek.json()
        return(userid+" --> Takipten çıkıldı!")
    except:
        return(userid+" --> Hata!")

def userId(username):
    header = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    }
    twitter = requests.get("https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D", headers=header)
    try:
        return twitter.json()["data"]["user"]["rest_id"]
    except:
        return(username+" --> Hata!")


while 1:
    system("cls||clear")
    try:
        menu = int(input("@_tingirifistik\n\n1- Takip et\n2- Takipten çık\n3- UserId bul\n4- Çıkış\n\nSeçiminiz: "))
    except ValueError:
        system("cls||clear")
        print("Lütfen sayı giriniz.")
        sleep(2)
        system("cls||clear")
        continue
    if menu == 1:    
        while 1:
            system("cls||clear")
            try:
                menu = int(input("1- Takip et\n2- Birden fazla kişiyi takip et\n3- Ana menüye git\n\nSeçiminiz: "))
            except ValueError:
                system("cls||clear")
                print("Lütfen sayı giriniz.")
                sleep(2)
                system("cls||clear")
                continue
            if menu == 1:
                system("cls||clear")   
                username = input("Kullanıcı adı giriniz: ")
                system("cls||clear")
                print(follow(userId(username)))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 2:
                system("cls||clear")
                file_path = input("Kullanıcı adlarının bulunduğu dosyanın yolunu giriniz: ")
                system("cls||clear")
                with open(file_path, "r", encoding="utf-8") as f:
                    for i in f.read().split("\n"):
                        print(follow(userId(i)))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 3:
                break
            else:
                system("cls||clear")
                print("Lütfen 1-3 arasında bir rakam giriniz.")
                sleep(3)
                system("cls||clear")
    elif menu == 2:
        while 1:
            system("cls||clear")
            try:
                menu = int(input("1- Takipten çık\n2- Birden fazla kişiyi takipten çık\n3- Ana menüye git\n\nSeçiminiz: "))
            except ValueError:
                system("cls||clear")
                print("Lütfen sayı giriniz.")
                sleep(2)
                system("cls||clear")
                continue
            if menu == 1:
                system("cls||clear")   
                username = input("Kullanıcı adı giriniz: ")
                system("cls||clear")
                print(unfollow(userId(username)))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 2:
                system("cls||clear")
                file_path = input("Kullanıcı adlarının bulunduğu dosyanın yolunu giriniz: ")
                system("cls||clear")
                with open(file_path, "r", encoding="utf-8") as f:
                    for i in f.read().split("\n"):
                        print(unfollow(userId(i)))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 3:
                break
            else:
                system("cls||clear")
                print("Lütfen 1-3 arasında bir rakam giriniz.")
                sleep(3)
                system("cls||clear")
    elif menu == 3:
        while 1:
            system("cls||clear")
            try:
                menu = int(input("1- UserId bul\n2- Birden fazla UserId bul\n3- Ana menüye git\n\nSeçiminiz: "))
            except ValueError:
                system("cls||clear")
                print("Lütfen sayı giriniz.")
                sleep(2)
                system("cls||clear")
                continue
            if menu == 1:
                system("cls||clear")
                username = input("Kullanıcı adı giriniz: ")
                system("cls||clear")
                print(username+" --> "+userId(username))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 2:
                system("cls||clear")
                file_path = input("Kullanıcı adlarının bulunduğu dosyanın yolunu giriniz: ")
                system("cls||clear")
                with open(file_path, "r", encoding="utf-8") as f:
                    for i in f.read().split("\n"):
                        print(i+" --> "+userId(i))
                input("\n\nDevam etmek 'Enter' tuşuna basınız...")
            elif menu == 3:
                break
            else:
                system("cls||clear")
                print("Lütfen 1-3 arasında bir rakam giriniz.")
                sleep(3)
                system("cls||clear")
    elif menu == 4:
        break
    else:
        system("cls||clear")
        print("Lütfen 1-4 arasında bir rakam giriniz.")
        sleep(3)
        system("cls||clear")
