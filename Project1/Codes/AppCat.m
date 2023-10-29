function [p,q] = AppCat(N)
% APPCat Approximates the catalan constant by p/q
% among all pairs of positive integers (p,q) such that p + q <= N
catconst =0.915965594177219;% Catalan constant
min = NaN;P = NaN;Q = NaN;% Set the initial values to NaN
for p = 1:N
    for q = 1:(N-p)
        value = abs(p/q-catconst);% Aim to find the smallest one
        if isnan(min) || value < min
            min = value;
            P = p; Q = q;% Update the output
        elseif value == min
            if p+q < P+Q % Select the one with smaller sum
                P=p;Q=q;
            end
        end
    end
end
p = P;q = Q;
disp(['The best approximates to the Catalan constant ' ...
    'satisfies p+q<=' num2str(N) ' is p=' num2str(p) ' and q=' ...
    num2str(q) ' with difference ' num2str(min) '.'])
end

