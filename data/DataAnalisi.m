clear all
close all

dim=12;
Dati=readcell("Erica_Test_Shapes_2022-08-01_17h39.48.619.csv");
[Dati,PosDatix,PosDatiy,ResponseTimes,Responses,Scores,Sizes,isDifficult]=leggi("Erica_Test_Shapes_2022-08-01_17h39.48.619.csv",dim);
Totptx=sum(Scores); %punti totali
FrameRate=Dati{2,62}; %frequenza dei fotogrammi
TimeOut=0;
TimeIn=0;
for i=1:dim
    TotalReactTime(i)= sum(ResponseTimes(i,:)); %tempo di risposta totale
end

TotScore=sum(Scores);
ScoreDiff=0;
ScoreEasy=0;
TimeAverageDiff=0;
TimeAverageEasy=0;
PCOutDiff=0;
PCOutEasy=0;
RoamDiff=0;
RoamEasy=0;
    d=0;
    e=0;
DomandeIncomprese=0;
for i=1:dim
    OutInitial(i)=0;
    TimeOut(i)=0;
    TimeIn(i)=0;



    if (((PosDatix(i,1)<-.72)||(PosDatix(i,1)>.42)) || ((PosDatiy(i,1)<-.36)||(PosDatiy(i,1)>.42))) %verifico se mouse partito fuori
        OutInitial(i)=1;
    end
    for j=1:(Sizes(i,2)) %vedo frame spesi dentro/fuori zona di interesse
        if (((PosDatix(i,j)<-.72)||(PosDatix(i,j)>.42)) || ((PosDatiy(i,j)<-.36)||(PosDatiy(i,j)>.42)))
            TimeOut(i)=TimeOut(i)+1;
        else
            TimeIn(i)=TimeIn(i)+1;
        end
    end
    TimeIn(i)=TimeIn(i)/Sizes(i,2)*ResponseTimes(i,1); %trasformo numero frame in tempo
    TimeOut(i)=TimeOut(i)/Sizes(i,2)*ResponseTimes(i,1);

    for j=1:(Sizes(i,2)-1) %ricavo delta movimento
        dx(i,j)=PosDatix(i,j+1)-PosDatix(i,j);
        dy(i,j)=PosDatiy(i,j+1)-PosDatiy(i,j);
        dx(i+12,j)=PosDatix(i+12,j+1)-PosDatix(i+12,j);
        dy(i+12,j)=PosDatiy(i+12,j+1)-PosDatiy(i+12,j);

    end
    if(isDifficult(i))  %discriminante per difficolta domande
        d=d+1;
        ScoreDiff=Scores(i)+ScoreDiff;
        TimeAverageDiff=TotalReactTime(i)+TimeAverageDiff;
        mediad(d)=TimeAverageDiff/d;
        PCOutDiff=TimeOut(i)+PCOutDiff;

    elseif(isDifficult(i)==0)
        e=e+1;
        ScoreEasy=Scores(i)+ScoreEasy;
        TimeAverageEasy=TotalReactTime(i)+TimeAverageEasy;
        PCOutEasy=TimeOut(i)+PCOutEasy;
        mediae(e)=TimeAverageDiff/e;
    end


end
if(mediad(3)>mediad(6)) %difficoltà domande facili/difficili
    progd=1;
elseif(mediad(3)<mediad(6))
    progd=0;
end
if(mediae(3)>mediae(6))
    proge=1;
elseif(mediae(3)<mediae(6))
    proge=0;
end
TimeAverage=mean(TotalReactTime);
RTTotDiff=TimeAverageDiff;

RTTotEasy=TimeAverageEasy;
PCOutDiff=PCOutDiff/RTTotDiff*100;
PCOutEasy=PCOutEasy/RTTotEasy*100;
PCOutTot=sum(TimeOut)/sum(ResponseTimes(1:dim,1))*100;
TimeAverageDiff=TimeAverageDiff/5;
TimeAverageEasy=TimeAverageEasy/5;


cambipre(i)=0;
cambipost(i)=0;

for i=1:dim
    cambipre(i)=0;
    cambipost(i)=0;
    for j=1:(Sizes(i,2)-2)
        if dy(i,j+1)*dy(i,j) < 0 || dx(i,j+1)*dx(i,j) < 0
            cambipre(i)=cambipre(i)+1;
        end
        if dy(12+i,j)*dy(12+i,j+1) < 0 || dx(12+i,j)*dx(12+i,j+1) < 0
            cambipost(i)=cambipost(i)+1;
        end
    end
    if(isDifficult(i))  %discriminante per difficolta domande

        RoamDiff=RoamDiff+cambipre(i);

    elseif(isDifficult(i)==0)

        RoamEasy=RoamEasy+cambipre(i);
    end
end
RoamTot=sum(cambipre);
for i=1:dim
    if Scores(i)==0 && cambipre(i)>2
        DomandeIncomprese=DomandeIncomprese+1;
    end 
end
%%per mouse in traiettoria favorevole
%definisco linea di traiettoria ideale con stessa frequenza di frame rate(linea da punto a a punto b)

for i=1:dim
        totalTracky=abs(dy(12+i,:));
        totalTrackx=abs(dx(12+i,:));
        %totalTrack=sqrt(sum(totalTracky(12+i,:))^2+sum(totalTrackx(12+i,:))^2);
        totalTracky=sum(totalTracky);
        totalTrackx=sum(totalTrackx);
        IdealTotalx=(PosDatix(i+12,1)-PosDatix(i+12,Sizes(i+12,2)));
        IdealTotaly=(PosDatiy(i+12,1)-PosDatiy(i+12,Sizes(i+12,2)));
        deltay=0;
        deltax=0;
    for j=1:(Sizes(i+12,2))
        deltax=deltax+abs(dx(i+12,j))/totalTrackx;
        deltay=deltay+abs(dy(i+12,j))/totalTracky;
        idealx(i,j)=IdealTotalx*deltax+PosDatix(i+12,1);
        idealy(i,j)=IdealTotaly*deltay+PosDatiy(i+12,1);
        diff(i,j)=sqrt((PosDatix(i+12,j)-idealx(i,j))^2+(PosDatiy(i+12,j)-(idealy(i,j)))^2);
    end
 
end

for i=1:dim
    TotalTrajectoryDistance(i)=sum(diff(i,:))/(Sizes(i+12,2)); %con data collection da vedere deviazione normale dalla retta
end
AverageDiff=mean(TotalTrajectoryDistance);
%% inserimento in tabella
Generali=readtable("DataTable.csv", VariableNamingRule="preserve");

addpath("C:\Users\irene.LAPTOP-IPO788K1\Desktop\Polimi\NECST\Progetto NL2\Test_Validazione\images");

M=[Dati{2,57},TotScore,ScoreDiff,ScoreEasy,TimeAverage,TimeAverageDiff,TimeAverageEasy,PCOutTot,PCOutDiff,PCOutEasy,RoamTot,RoamDiff,RoamEasy,AverageDiff,progd,proge,DomandeIncomprese];
dlmwrite("DataTable.csv",M,'delimiter',',','-append');

%% analisi dati statistica
%{
%MediaRT=mean(Generali(:,2));
PTXGen=table2array(Generali(:,2));
PTXGenMed=mean(PTXGen);
PTX25=prctile(PTXGen,25);
PTX50=prctile(PTXGen,50);
PTX75=prctile(PTXGen,75);
fprintf("\n Punteggio: ")
if TotScore<PTX25
    fprintf("Minore del 25 percento dei partecipanti");
elseif TotScore<PTX50
    fprintf("Tra il 25 e 50 percento dei partecipanti");
elseif TotScore<PTX75
    fprintf("Tra il 50 e 75 percento dei partecipanti");
elseif TotScore>PTX75
    fprintf("Maggiore del 75 percento dei partecipanti");
end

RTGen=table2array(Generali(:,5));
RTGenMed=mean(RTGen);
RT25=prctile(RTGen,25);
RT50=prctile(RTGen,50);
RT75=prctile(RTGen,75);
fprintf("\n Reaction Time: ")
if TimeAverage<RT25
    fprintf("Minore del 25 percento dei partecipanti");
elseif TimeAverage<RT50
    fprintf("Tra il 25 e 50 percento dei partecipanti");
elseif TimeAverage<RT75
    fprintf("Tra il 50 e 75 percento dei partecipanti");
elseif TimeAverage>RT75
    fprintf("Maggiore del 75 percento dei partecipanti");
end

MIGen=table2array(Generali(:,11));
MIGenMed=mean(MIGen);
MI25=prctile(MIGen,25);
MI50=prctile(MIGen,50);
MI75=prctile(MIGen,75);
fprintf("\n Roaming: ")
if RoamTot<MI25
    fprintf("Minore del 25 percento dei partecipanti");
elseif RoamTot<MI50
    fprintf("Tra il 25 e 50 percento dei partecipanti");
elseif RoamTot<MI75
    fprintf("Tra il 50 e 75 percento dei partecipanti");
elseif RoamTot>MI75
    fprintf("Maggiore del 75 percento dei partecipanti");
end

PCOutGen=table2array(Generali(:,8));
PCOutGenMed=mean(PCOutGen);
PCOutGen25=prctile(PCOutGen,25);
PCOutGen50=prctile(PCOutGen,50);
PCOutGen75=prctile(PCOutGen,75);
fprintf("\n Tempo fuori da area di interesse: ")
if PCOutTot<PCOutGen25
    fprintf("Minore del 25 percento dei partecipanti");
elseif PCOutTot<PCOutGen50
    fprintf("Tra il 25 e 50 percento dei partecipanti");
elseif PCOutTot<PCOutGen75
    fprintf("Tra il 50 e 75 percento dei partecipanti");
elseif PCOutTot>PCOutGen75
    fprintf("Maggiore del 75 percento dei partecipanti");
end

%grafico correlazione
i=1:(dim/2);
figure(1)
plot(i,mediae);
%}