%Question2
format long %in order to show more decimal places
x=1
a=cos(x)^2-exp(x)+2*sin(2*x)^2;
b=-2*sin(x)*cos(x)-exp(x)+8*cos(2*x)*sin(2*x);
x=x-a/b; %first iteration
z=x; %make z=x, in order to achieve a comparation for the further code
x=fix(z);% and x equal to the integer part of z
while roundn(x,-5)~=roundn(z,-5) %if their decimal part are not equal, implement the code,and code can stop iterating at the correct time
    x=z
    a=cos(x)^2-exp(x)+2*sin(2*x)^2;%f(x)
    b=-2*sin(x)*cos(x)-exp(x)+8*cos(2*x)*sin(2*x);%diff(f(x),x)
    z=x-a/b;% the code about Newton-Raphson method
    z;
end
x=roundn(x,-5);%correct to 5 decimal places
x %output the value of x