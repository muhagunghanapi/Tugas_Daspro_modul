def kalimat(teks):
	huruf_Besar = 0
	for kar in teks :
		if kar.isupper() : 
			huruf_Besar = huruf_Besar + 1
	print("Banyak Kemunculan HurufBesar =", huruf_Besar)