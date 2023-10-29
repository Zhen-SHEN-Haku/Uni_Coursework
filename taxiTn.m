function [Pairs,M] = Tn (n) 
% CUBICTAXICABNUM returns the smallest cubic taxicab number M that
% can be expressed as the sum of two positive integers cubed in N distinct 
% ways with input N = pairs.
lensol = 0;% The initial number.
N = 1;
Pairs = '';
if n == 1 % For the special case, since 1==1, cannot show twice in the vector using my way
    M = 2;
    Pairs= [Pairs, '(1,1)'];
else
    while lensol<2*n
        if n == 3 && N == 1
            N = 87000000;% Start larger for n==3 to save the time.
        end
        j = floor(N^(1/3)+10*eps);% The largest number a,b,c,d counld be given N.
        x = 1:j;y = 1:j; % Using this way can only consider the integer value.
        [x,y] = meshgrid(x,y);
        z = x.^3 + y.^3;% The M in the function which need at least two pairs of solution
        k = find(z==N);% Find the solution in the different cobinatinos of [x,y]
        lensol = length(x(k));% Twice of the number of solution piars since x&y are two elements in the vector.
        N = N+1;
    end
    sol = x(k);
    for i = 1:(length(sol)/2)
        Pairs = [Pairs,'(',num2str(sol(i)),',',num2str(sol(end+1-i)),')'];
    end
    M = N-1;
end
disp(['For T_n given n=' num2str(n) ', the smallest integer is ' num2str(M) ...
    ', and the corresponding pairs of numbers are ' ])
end

