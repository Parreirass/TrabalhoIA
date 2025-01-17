def arvore_decisao():
    equipe = input("Você gosta de trabalhar em equipe? (sim/não): ").strip().lower()
    
    if equipe == "sim":
        ar_livre = input("Prefere atividades ao ar livre? (sim/não): ").strip().lower()
        
        if ar_livre == "sim":
            print("Sugestão: Explore hobbies como esportes ou jardinagem.")
        else:
            comunicacao = input("Prefere atividades que envolvam comunicação? (sim/não): ").strip().lower()
            
            if comunicacao == "sim":
                print("Sugestão: Considere carreiras em Direito ou áreas relacionadas à comunicação.")
            else:
                tecnologia = input("Se sente confortável trabalhando com tecnologia? (sim/não): ").strip().lower()
                
                if tecnologia == "sim":
                    print("Sugestão: Considere carreiras em Tecnologia ou Programação como hobby.")
                else:
                    print("Sugestão: Experimente hobbies criativos como Música ou Fotografia.")
                    
    else:
        numeros = input("Gosta de lidar com números? (sim/não): ").strip().lower()
        
        if numeros == "sim":
            problemas = input("Gosta de resolver problemas complexos? (sim/não): ").strip().lower()
            
            if problemas == "sim":
                print("Sugestão: Áreas como Engenharia ou Tecnologia podem ser interessantes.")
            else:
                print("Sugestão: Carreiras em Direito ou Administração.")
                
        else:
            arte = input("Prefere usar habilidades artísticas? (sim/não): ").strip().lower()
            
            if arte == "sim":
                print("Sugestão: Explore carreiras em Artes ou hobbies como Fotografia ou Música.")
            else:
                cuidar_pessoas = input("Se interessa por cuidar de outras pessoas? (sim/não): ").strip().lower()
                
                if cuidar_pessoas == "sim":
                    print("Sugestão: Carreiras em Medicina ou áreas da saúde.")
                else:
                    desafios_fisicos = input("Gosta de desafios físicos? (sim/não): ").strip().lower()
                    
                    if desafios_fisicos == "sim":
                        print("Sugestão: Considere hobbies como Esportes.")
                    else:
                        organizacao = input("Prefere trabalhar em ambientes organizados? (sim/não): ").strip().lower()
                        
                        if organizacao == "sim":
                            print("Sugestão: Carreiras em Administração ou Direito.")
                        else:
                            print("Sugestão: Explore hobbies individuais como Jardinagem ou Fotografia.")

arvore_decisao()
