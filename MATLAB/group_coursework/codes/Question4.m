%Question 4
y=0;%the start of y befor circulation
for x=[0.01:0.02:0.29];% the x value of mid ponits
    y=exp(x)-2.*sin(2*x).^2+y;% use f(x)+y to achieve the sum which we need
    area=0.02*y;%calculate the area
end
area%output the value of area
    