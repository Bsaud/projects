def processtext(txt):
  dictionary = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a','A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A','1':'9','2':'8','3':'7','4':'6','6':'4','7':'3','8':'2','9':'1'}
  transTable = txt.maketrans(dictionary)
  txt = txt.translate(transTable)
  print(txt)
x=input("enter the text you want to hide: ")
processtext(x)