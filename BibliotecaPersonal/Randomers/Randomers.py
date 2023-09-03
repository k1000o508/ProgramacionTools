 def randomer_nomap(c):
        
        for i in range(c):
            apes  = ["lopez","martines" ,"abalos" , "ramos", "faustino"]
            nomes = ["Valentina","juan"  ,"Mariano" ,"Lucas" ,"Tadeo" ]
            
            ind_a= random.randint(1,len(apes)-1)
            ind_n= random.randint(1,len(nomes)-1)
            
            ap.append(apes[ind_a])
            nom.append(nomes[ind_n])

    def randomer(principal,a,b,c):
        
        for i in range(c):
            x = random.randint(a,b)
            principal.append(x)


    def randomer_bol(principal,c):

        for i in range(c):
            x = random.randint(1,2)
            
            if x == 1:
                principal.append("S")
            else:
                principal.append("N")