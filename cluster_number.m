queryline = 'MyNodesDump';
fID = fopen('log_ts31_mote_3102.log');
C = textscan(fID,'%s','delimiter','\n');
fclose(fID);
C = C{1};
[temp matchedLines] = regexp(C,['(?<date>^[0-9,-:T]*)Z.*' queryline ':(?<otherNum>[0-9]*)'] ,'tokens','match');
matchedLines = [matchedLines{:}]';
temp = [temp{:}];
temp = reshape([temp{:}],2,[])';
Time_1501  = datetime(temp(:,1),'InputFormat','yyyy-MM-dd''T''HH:mm:ss.SS');
[h,m,s]= hms(Time_1501);
time = {h; m; s};
time_in_hrs = [time{:}];
t = [time{1:3}];
 
Numnode_1501 = temp(:,2);
