f = open("timestat.txt",'r')
l=[a for a in f.readlines() if a!="\n"]
f.close()
x=[]
for s in l:
	x.append(s.replace("\n",""))

y=[]
i=0
while(i+3<=len(x)):
	l=[]
	for t in range(i,i+3):
		l.append(x[t])
	y.append(l)
	i=i+3
'''real list in y'''
user_min = []
user_sec=[]
real_min=[]
real_sec=[]
sys_min=[]
sys_sec = []

for s in y:
	user = s[1].split("    ")[1]
	real = s[0].split("    ")[1]
	sys=s[2].split(" ")[1]
	user_min.append(float(user.split("m")[0]))
	user_sec.append(float(user.split("m")[1].split("s")[0]))
	real_min.append(float(real.split("m")[0]))
	real_sec.append(float(real.split("m")[1].split("s")[0]))
	sys_min.append(float(sys.split("m")[0]))
	sys_sec.append(float(sys.split("m")[1].split("s")[0]))

l = (sum(user_min)*60+sum(user_sec))/len(user_sec)
x = (sum(real_min)*60+sum(real_sec))/len(user_sec)
y = (sum(sys_min)*60+sum(sys_sec))/len(user_sec)

print ("Average Time statistics")
print("real ",int(x/60),"m ",round(x%60,4),"s   user",int(l/60),"m ",round(l%60,4),"s   sys",int(y/60),"m ",round(y%60,4),"s")
print ("Standard deviation of Time statistics")
q=[]
i=0
for j in range(0,len(user_sec)):
	i += (x-(real_min[j]*60+real_sec[j]))**2

print ("real ",int(((i/len(user_sec))**0.5)/60),"m ",round(((i/len(user_sec))**0.5)%60,4),"s",end="   ")
q.append(round((i/len(user_sec))**0.5,4))
i=0
for j in range(0,len(user_sec)):
	i += (l-(user_min[j]*60+user_sec[j]))**2
print ("user ",int(((i/len(user_sec))**0.5)/60),"m ",round(((i/len(user_sec))**0.5)%60,4),"s",end="  ")
q.append(round((i/len(user_sec))**0.5,4))

i=0
for j in range(0,len(user_sec)):
	i += (y-(sys_min[j]*60+sys_sec[j]))**2
print ("sys ",int(((i/len(user_sec))**0.5)/60),"m ",round(((i/len(user_sec))**0.5)%60,4),"s")
q.append(round((i/len(user_sec))**0.5,4))
w=0
e=0
r=0
for i in range(len(user_sec)):
	if(real_min[i]*60+real_sec[i]<x+q[0] and real_min[i]*60+real_sec[i]>x-q[0]):
		w+=1
	if(user_min[i]*60+user_sec[i]<l+q[1] and user_min[i]*60+user_sec[i]>l-q[1]):
		e+=1
	if(sys_min[i]*60+sys_sec[i]<y+q[2] and sys_min[i]*60+sys_sec[i]>y-q[2]):
		r+=1
print ("Number of runs within average - standard deviation to average + standard deviation")
print ("real ",w,"  user ",e,"  sys ",r)
input()
