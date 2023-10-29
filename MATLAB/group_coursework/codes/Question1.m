% Question 1
x=[-1:0.01:1];% values of x, use 0.01 as a step to make curve smooth 
plot(x,cos(x).^2,x,exp(x)-2*sin(2*x).^2)%draw both two curves on same axes
title('Question 1')%title the graph
ylabel('cos(x)^2 or exp(x)-2*sin(2*x)^2')%y axis
xlabel('x')%x axis