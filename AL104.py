
class AL104:
	def __init__(self):
		self.__cd = {'a':'<->','b':'<|>','c':'<#>','d':'<h>','e':'<!>','f':'<X>','g':'<+>','h':'<&>','i':'<_>','j':'<@>','k':'<.>','l':'<*>','m':'<z>','n':'<^>','o':'<%>','p':'<~>','q':'<=>','r':'</>','s':'<?>','t':'<[>','u':'<]>','v':'<{>','w':'<}>','x':'<(>','y':'<)>','z':'<$>',' ':'###','1':'>5<','2':'>0<','3':'>7<','4':'>9<','5':'>6<','6':'>8<','7':'>3<','8':'>4<','9':'>1<','0':'>2<','!':'x-x','#':'k-k','@':'y>p','$':'4-A','%':'i~n','^':'ala','&':'kyu','*':'nin','(':'jaz',')':'y~~','-':'&ko','+':'&ka','{':'uwu','}':'owo','[':'Y.Y',']':'T.T','\\':')X(','/':'(x)','~':'exe','`':'det','.':'t%t',',':'bee','?':'que','<':'-l-','>':'-r-',"'":'~wu','"':'~~w','=':'*6*','_':';-;',':':'^*^',';':'@=@','A':'=->','B':'=|>','C':'=#>','D':'=H>','E':'=!>','F':'=X>','G':'=+>','H':'=&>','I':'=_>','J':'=@>','K':'=.>','L':'=*>','M':'=Z>','N':'=^>','O':'=%>','P':'=~>','Q':'==>','R':'=/>','S':'=?>','T':'=[>','U':'=]>','V':'={>','W':'=}>','X':'=(>','Y':'=)>','Z':'=$>'}
		self.__rev_cd = {v: k for k, v in self.__cd.items()}
		#'!':'x-x','#':'k-k','@':'y>p','$':'4-A','%':'i~n','^':'ala','&':'kyu','*':'nin','(':'jaz',')':'y~~','-':'&ko','+':'&ka','{':'uwu','}':'owo','[':'Y.Y',']':'T.T','\\':')X(','/':'(x)','~':'exe','`':'det','.':'t%t',',':'bee','?':'que','<':'-l-','>':'-r-',"'":'~wu','"':'~~w'

	def encode(self, ui)->exec:return ''.join([self.__cd.get(c, '<69>') for c in ui])

	def decode(self, x):
		try:
			return ''.join([self.__rev_cd[x[i:i+3]] for i in range(0, len(x), 3)])
		except KeyError:
			return "[decode-err]: Invalid cipher!"

	def __str__(self):
        return "AL104 cipher or AL1-04(Anikin Luke Cipher)"


def main():
	cipher = AL104()
	line = "☲"*30
	banner = f"\n{line}\n[1] == Encode\n[2] == Decode\n[0] == Exit\n{line}\nSelc-> "
	ui = input(banner)
	match(ui):
		case '1':
			print(f'\nResult: {cipher.encode(input("Enter msg to encode: "))}')
			return True
		case '2':
			print(f'\nResult: {cipher.decode(input("Enter cipher to decode: "))}')
			return True
		case '0':
			print("\nBye bye!")
			return False
		case _:
			print("\nInvalid option!")
			return True


if(__name__ == "__main__"):
	while main():
		pass

