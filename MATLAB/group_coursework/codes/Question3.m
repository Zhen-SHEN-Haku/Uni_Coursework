% Question 3(a)
x=1;
y=exp(x)-2.*sin(2*x)^2;%f(x)
for h=[0.1,0.01,0.001,0.0001];%the values of h we need to calculate
    h %one value of h with one value of gradient
    z1=exp(x-h)-2.*sin(2*(x-h))^2;%f(x-h)
    z2=exp(x+h)-2.*sin(2*(x+h))^2;%f(x+h)
    gradient=(z2-z1)/(2*h)%the gradient using central difference method
end
format long % Question 3(b)
x=1;
gradient=exp(x)-8*sin(2*x)*cos(2*x);%gradient before accurating(formula is the differentiate calculated by hand)
gradient=roundn(gradient,-7)%value after accurating
