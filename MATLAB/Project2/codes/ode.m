function dzdt = ode(t,z,sr0,sf0,mur,muf)
%1.df 2.xf 3.yf 4.dr 5.xr 6.yr
dzdt=0*z;% make sure the shape of dzdt is same to the z
sight=1;% move towards rabbit
s=[-200 -400];
n=[-200 0];
dist=sqrt((z(5)-z(2))^2+(z(6)-z(3))^2); % |FR|
dist1=sqrt((s(1)-z(2))^2+(s(2)-z(3))^2);% |SF|
dzdt(1)=sf0*exp(-muf*z(1));% sf
dzdt(4)=sr0*exp(-mur*z(4));% sr
dzdt(5)=-dzdt(4)/sqrt(2);% vr x-axis
dzdt(6)=dzdt(4)/sqrt(2);% vr y-axis
if abs(z(2)-z(5))>eps% k ~= -1
    k=(-200-z(2))/(z(5)+200);
    yp=(k*z(6)+z(3))/(1+k);
    if yp>=s(2) && yp<=n(2)% fox's sight is blocked
        sight=0;
    end
end
if sight==0
    if z(3)<s(2) && z(2)<s(1)% towards s
        dzdt(2)=dzdt(1)*(s(1)-z(2))/dist1;% vf x-axis
        dzdt(3)=dzdt(1)*(s(2)-z(3))/dist1;% vf y-axis
    else% straight
        dzdt(2)=0;% vf x-axis
        dzdt(3)=dzdt(1);% vf y-axis
    end
else
    dzdt(2)=dzdt(1)*(z(5)-z(2))/dist;% vf x-axis
    dzdt(3)=dzdt(1)*(z(6)-z(3))/dist;% vf y-axis, towards rabbit
end
end
