%Question4 (a)
S=sym('10725458');% Though this number is not that big, but for the further calculate, use 'sym'
p=nextprime(10*(S^4));
while isprime((p-1)/2)==0
      p=nextprime(p+1);% Because nextprime function find the smallest prime greater than or 'equal to', so we have to add 1 otherwise the number will keep unchange
end
p

q=prevprime(4*(S^5));
while isprime((q-1)/2)==0
      q=prevprime(q-1);% Similar to nextorime function, subtract 1
end
q

e=65537;
d=(powermod(e,-1,(p-1)*(q-1)))% Use powermod to deal with e, move it to the right as e^-1

%Question4 (b)
c1=sym('2444363766791208361109708477180523484580556774594169616110635595');
c2=sym('54165492371574924964670228300407737522306612118787636666325107864');
n=p*q;
m1=powermod(c1,d,n)
m2=powermod(c2,d,n)
%MATHEMATICS IS THE DOOR AND KEY TO THE SCIENCES ROGER BACON