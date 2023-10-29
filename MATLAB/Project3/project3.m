format short
a=readtable('bananas.csv');a=sortrows(a,2);% full data
origin=unique(a.Origin); % answer for Q1 
units=unique(a.Units); % answer for Q1 
disp(['There are ' num2str(height(origin)) ' different origins, ' ...
    'with unit ' units{:} ', they are:'])
disp(cell2table(origin,'VariableNames',{'Origin'}))% answer for Q1
b=[];x=[];Q2=cell(height(origin),2);% initial variables
q3={'colombia','costa_rica','dominican_republic','honduras', ...
    'jamaica','windward_isles','mexico'};% need box plots
for c=1:height(origin)
    name=repmat(origin(c),height(a),1); % vector for find one by one
    inx=find(strcmp(a.Origin,name));b=a{inx,3};% the price for each country
    Q2{c,1}=cell2mat(origin(c));Q2{c,2}=mean(b);% storage the value in a cell
    if ismember(origin(c),q3) % table for Q3 to draw box plots
        x=[x;a(inx,3) a(inx,1)];
    end

end
Q2=cell2table(Q2,'VariableNames',{'Origin','Mean'});% add variable names
disp('The mean price for each origin is shown below:')
disp(Q2)% answer for Q2
figure
boxplot(table2array(x(:,1)),table2array(x(:,2)))% plot for Q3
title('Box plot for comparasion');
ylabel('price £/kg');

% Q4 Time Series
q4={'colombia'};q5={'costa_rica'};% same step as previous to extract data
name=repmat(q4,height(a),1);name2=repmat(q5,height(a),1);
inx=find(strcmp(a.Origin,name));COL=[];COL=[COL;a(inx,3) a(inx,2)];
inx2=find(strcmp(a.Origin,name2));COS=[];COS=[COS;a(inx2,3) a(inx2,2)];
IQR_COL=prctile(COL.Price,75)-prctile(COL.Price,25);% prepare for outliers
IQR_COS=prctile(COS.Price,75)-prctile(COS.Price,25);
% values greater than the upper bound or 
% less than the lower bound are outliers
inx_o_L=find(COL.Price>prctile(COL.Price,75)+1.5*IQR_COL ...
    |COL.Price<prctile(COL.Price,25)-1.5*IQR_COL);% index for outliers
COL(inx_o_L,:)=[];% remove the outliers
inx_o_S=find(COS.Price>prctile(COS.Price,75)+1.5*IQR_COS ...
    |COS.Price<prctile(COS.Price,25)-1.5*IQR_COS);
COS(inx_o_S,:)=[];% remove the outliers
xq = (COL.Date(1):days(7):COL.Date(end))';% resampling time series
V = interp1(COL.Date, COL.Price, xq, 'spline');% resampling
y = fft(V);
y(1) = [];% remove the sum of the data
n = length(y);
power = abs(y(1:ceil(n/2))).^2;  % power of first half of transform data
maxfreq = 1/2;                   % maximum frequency
freq = (1:n/2)/(n/2)*maxfreq;    % equally spaced frequency grid
period=1./freq;                  % convenient vision
index=find(power==max(power));
mainPeriodStr=num2str(period(index)); % find the strongest frequency
figure
plot(period,power) % if the x-axis is freq, then is PSD
xlim([0 70]); % zoom in on max power
xlabel('period (Weeks/Cycle)') 
ylabel('Power')
hold on
plot(period(index),power(index),'r.', 'MarkerSize',25)
title('power against period figure'); 
text(2,1200,'Period is the reciprocal of the frequency.','FontSize',15);
text(period(index)+2,power(index),['Period = ',mainPeriodStr]);
legend({'trend','the highest power point'},'Location','northwest');
mon=[];
for i=1:12
    inx=find(xq.Month==i);
    mon=[mon mean(V(inx))];
end
figure
plot(1:12,mon,'LineWidth',1.3)% trend over 20 years
hold on 
years=unique(year(COL.Date));
for i=1:length(years)
    y=[];
    inx=find(year(COL.Date)==years(i));
    y=[y;COL(inx,:)];
    mons=[];
    for j=1:12
        inx=find(y.Date.Month==j);
        mons=[mons mean(y{inx,1})];
    end
    plot(1:12,mons,'LineWidth',0.8,'Color',[0.8 0.8 0.8])% trend in one year
    hold on
end
ylim([0.65 0.8])
xlabel('Month')
ylabel('Price')
legend('mean price over 20 years','each year monthly price')
title('Monthly mean price')% answer for Q4 (2 pics)

% Q5
xq=(unique([COL.Date;COS.Date]))';
A=interp1(COL.Date,COL.Price,xq,'spline');
B=interp1(COS.Date,COS.Price,xq,'spline');
R=corrcoef(normalize(A),normalize(B));
disp(['The correlation coefficient between Colombia and Costa rica is ' ...
    num2str(R(2)) '.'])% answer for Q5


