%Question 3
H=sym('3424781706');
r=sym('8859445681');
s=sym('15992960169');
p=sym('30167674936870980426367');
q=sym('17456345243');
g=sym('18008617784390347685963');
y=sym('6172647251731232412543');% Input the value of numbers
w=powermod(s,-1,q);% Intermediate step to helo find u1 and u2
u1=mod(H*w,q)% Find and output u1
u2=mod(r*w,q)% Find and output u2
a=powermod(g,u1,p);
b=powermod(y,u2,p);
c=mod(mod(a*b,p),q);
if isequal(c,r)==0% Judge is the remainder equal to r. 
   disp('Invalid')
else disp('Valid')
end