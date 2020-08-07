def goster(resim:list,can,res:int):
	print(resim[res])
	print("kalan canınız {} ".format(can))

def X(can:int,kelime):
	import time
	s = input("kelime olarak tahmin etmek ister misiniz?(K/H): ")
	while True:
		if s == "K":
			k = input("Kelimeyi giriniz. : ")
			if k == kelime:
				print("doğru bildiniz...")
				
				q=input("Tekrar oynamak ister misiniz?(E/H) : ")
			
				while True:
					if q=="E" or q=="e":
						print("öyleyse üst ok deyip enter a basınız")
						break
					elif q=="H" or q=="h":
						print("tekrar bekleriz...")
						time.sleep(3)
						quit()	
					else:
						print("lütfen e veya h giriniz!!!")
						quit()

			elif k!=kelime:
				print("yanlış bildiniz...")
				can-=1
			else:
				pass 

		elif s=="H":        
			return

		else:
			print("lütfen sadece K veya H giriniz")
			break