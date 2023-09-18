def recortar(num, lim_inf, lim_sup):
    return max(min(num, lim_sup), lim_inf)

num=25
lim_sup=10
lim_inf=0

resultado=recortar (num, lim_inf, lim_sup)

print (resultado)
