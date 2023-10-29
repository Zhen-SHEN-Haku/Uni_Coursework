%Question 1 (a)
p=sym('636449999');
a=sym('557229101');
v=sym('340924010');
g=0;% The start of circulation
while isPrimitiveRoot(g,p)~=1 % To judge if g is a primitive root modulo p
      g=g+1;% Then we can get the smallest positive primitive root modulo p
end
g % Output the answer (11)

%Question 1 (b)
u=powermod(g,a,p)% Calculate the value of u and output it (18122020)
k=powermod(v,a,p)% Calculate the value of k and output it (20201218)

