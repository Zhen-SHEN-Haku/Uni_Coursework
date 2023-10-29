function [value,isterminal,direction] = stop(t,z)
dist=sqrt((z(5)-z(2))^2+(z(6)-z(3))^2);% |FR|
value(1)=(600-z(6))*(dist-0.1);% captured or escape
isterminal(1)=1;
direction(1)=0;
end
