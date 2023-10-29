function [a,b,c,d,M] = CubicTaxicabNum ( N ) 
% CUBICTAXICABNUM returns the smallest cubic taxicab number M 
% M=a^3+b^3=c^3+d^3 greater than or equal to N
t = N; % storage of the initial N for disp
lensol = 0;% set the initial number for the loop
while lensol<4
    n = floor(N^(1/3)+10*eps);% the upper bound for a,b,c,d
    x = 1:n;y = 1:n;
    [x,y] = meshgrid(x,y);
    z = x.^3 + y.^3;
    k = find(z==N);
    lensol = length(x(k));
    N = N+1;
end
sol = x(k); % the solution set
a = sol(1);b = sol(end);c = sol(2);d = sol(end-1);
M = N-1; % there is an extra 1 in the last loop
disp(['The smallest cubic taxicab number greater than ' ...
    num2str(t) ' is ' num2str(M) ' and is equal to ' ...
    num2str(a) '^3+' num2str(b) '^3=' num2str(c) '^3+' ...
    num2str(d) '^3.'])
end

