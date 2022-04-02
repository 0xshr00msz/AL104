dds = {'<->':'a','<|>':'b','<#>':'c','<h>':'d','e':'<!>','f':'<X>','g':'<+>','h':'<&>','i':'<_>','j':'<@>','k':'<.>','l':'<*>','m':'<z>','n':'<^>','o':'<%>','p':'<~>','q':'<=>','r':'</>','s':'<?>','t':'<[>','u':'<]>','v':'<{>','w':'<}>','x':'<(>','y':'<)>','z':'<$>',' ':' ','1':'0','2':'9','3':'8','4':'7','5':'6','6':'5','7':'4','8':'3','9':'2','0':'1'}

def decode(ui):
	msg_all = ''
	for charz in ui:
		try:
			if charz == charz.upper():
				x = dds.get(charz.lower())
				msg_all+=x.upper()
			else:
				x = dds.get(charz)
				msg_all+=x
		except:
			msg_all+=''
	return msg_all

#x='aaabbbcccdddeee'
x='<-><-><-><|><|><|><#><#><#><h><h><h><!><!><!>'
msg_all=''
code=[]
s_code=''
count=3
x+=' '
for charz in x:
	if count<1:
		count=3
		code.append(s_code)
		s_code=''
	count-=1
	s_code+=charz

for sym in code:
	decoded = dds.get(sym)
	msg_all+=str(decoded)

print(msg_all)
