% Q1
mur=0;muf=0;
sr0=13;sf0=16;
s=[-200 -400];n=[-200 0];
z0=[0 -250 -550 0 0 0];
tspan=[0 100];
x=[-500,-200,-200,-500];
y=[-400,-400,0,0];% plot for a warehouse 
options = odeset('Events',@(t,z) stop(t,z),'MaxStep',0.002);
[t,z,te,ze,yi] = ode45(@(t,z)ode(t,z,sr0,sf0,mur,muf),tspan,z0,options);
plot(x,y,z(:,2),z(:,3),z(:,5),z(:,6),'LineWidth',2)
legend('warehouse','fox','rabbit')
hold on 
text(-200,0,'N')
text(-200,-400,'S')
if abs(ze(6)-600)<10^(-10)% adjust for float number
    a='the rabbit escapes.';
elseif sqrt((ze(5)-ze(2))^2+(ze(6)-ze(3))^2)<=0.1
    a='the rabbit is captured.';
end
disp(['At time T=' num2str(te) 's the fox travelled ' num2str(ze(1)) ...
    ' meters and located at(' num2str(ze(2)) ',' num2str(ze(3)) '), ' a ])