################################
# FUNCIÓN QUE PERMITE REALIZAR
# LA PRUEBA DE HIPÓTESIS PARA 
# UNA VARIANZA POBLACIONAL
################################

# n: tamaño de la muestra
# s2: varianza muestral
# v0: valor de la varianza en H0
# H1: c("distinto","menor","mayor")
# NS: nivel de significación

prueba.var=function(n,s2,v0,H1="distinto",NS)
{
  E0=(n-1)*s2/v0
  if(H1=="distinto")
  {
    cat("H1 es:","varianza","distinta a",v0,"\n")
    c1=qchisq(NS/2,n-1)
    c2=qchisq(1-NS/2,n-1)
    if(E0<c1 || E0>c2) D="Rechazo H0"
    else D="No Rechazo H0"
  }
  if(H1=="mayor")
  {
    cat("H1 es:","varianza","mayor a",v0,"\n")
    c2=qchisq(1-NS,n-1)
    if(E0>c2) D="Rechazo H0"
    else D="No Rechazo H0"
  }
  if(H1=="menor")
  {
    cat("H1 es:","varianza","menor a",v0,"\n")
    c1=qchisq(NS,n-1)
    if(E0<c1) D="Rechazo H0"
    else D="No Rechazo H0"
  }
  cat("La decisión es:",D,"\n")
}