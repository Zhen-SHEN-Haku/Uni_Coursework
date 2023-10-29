%Question 2 (a)
n=sym('94315998521786533270923681389978318509265315584058689828801');
s=n-1;
r=0;
while mod(s,2)==0 % make s divide by 2 to get the final odd integer 
      s=s/2;
      r=r+1; % The value of r
end
r% Output the value of r

i=s;
j=1;
while i~=2*(n-1)% calculate until the i=n-1
      a=powermod(7,i,n)% Output the sequence of remainders
      data(j)=a;% storage the remainders in a vector
      j=j+1;
      i=2*i;
end

%Question 2 (b)
k=1;
while k<=7 
      m=gcd(data(k)+1,n);% add 1 to remainders and calculate the greatest common divisor of each of the resulting numbers with n
      p=gcd(data(k)-1,n);% subtract 1 from the remainders and calculate the greatest common divisor of each of the resulting numbers with n
      data2(k)=m;% storage the value of gcds in a vector(+1)
      data3(k)=p;% storage the value of gcds in a vector(-1)
      k=k+1;
end

data4=[data2,data3];% combine the vector "data2" and "data3"(the gcds)
for o=1:14
    if isprime(data4(o))==0% judge if the elements in data4 is prime or not
       data4(o)=1;% make the non-prime number elements equal to 1
    end
end
data4=unique(data4);% delete repeat elements, this is the vector which containing the the prime factorisation of n
data4(data4==1)=[] % delete 1 which is not a prime number
