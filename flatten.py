### flatten function
### @ app.patika.dev/moduller/python-temel/proje

# Author: Fatih Yalçın
# 18th August, 2021
# linkedin.com/in/fatih-yalcin-/

def flatten(ls):
    def main(ls, _new_ls = []): # <, _new_ls = []> kısmı yeni listeyi hafızasında tutması için
        if ls == []: # boş listeyi de eleman sayıyor, özellikle böyle yaptım ama olmasa da olur
            _new_ls.append([])
            
        for i in ls: # verilen listenin içindekileri sırayla tarıyor
            
            if type(i) == list: # eğer bir eleman zaten listeyse 
                main(i, _new_ls) # onun içindekileri en başından sırayla tarıyor
                
            else: # eğer bir liste değilse
                _new_ls.append(i) # elemanı sonuç listesine ekliyor
    
        return _new_ls
    
    return main(ls)
    #print(main(ls))


# program başka yerde kullanılacağı zaman gereksiz yere benim
# örneklerimin çalışmaması için bu şekilde bir kontrol ifadesi koydum.
if __name__ == "__main__":
    print(flatten([[1,'a',['cat'],2],[[[[]]]],[[[3]],'dog'],4,5]))

    # burada birkaç test yaptım
    print(flatten([1, [[[['a']]], 2123,12984, [],[123]], 'cat', 2, [], 3, 'dog', 4, 5]))
    print(flatten([[[[[]]]]]))
    print(flatten([]))
    ls1 = [[1], "benim", ["guzel", "listem", []]]
    print(flatten(ls1))

