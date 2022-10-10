clear all
close all
%prctile(dato,percetile voluto)

%lettura tabella
Generali=readtable("TotalData.csv", VariableNamingRule="preserve");
Eta=table2array(Generali(:,1));
PTGen=table2array(Generali(:,2));
PTDiff=table2array(Generali(:,3));
PTFac=table2array(Generali(:,4));
RTGen=table2array(Generali(:,5));
RTDiff=table2array(Generali(:,6));
RTFac=table2array(Generali(:,7));
PCOutGen=table2array(Generali(:,8));
PCOutDiff=table2array(Generali(:,9));
PCOutFac=table2array(Generali(:,10));
RoamGen=table2array(Generali(:,11));
RoamDiff=table2array(Generali(:,12));
RoamFac=table2array(Generali(:,13));
Dev=table2array(Generali(:,14));
ProgDiff=table2array(Generali(:,15));
ProgFac=table2array(Generali(:,16));
DomInc=table2array(Generali(:,17));

%alcuni dati medi
PTGenMed=mean(PTGen);
PTDiffMed=mean(PTDiff);
PTFacMed=mean(PTFac);
RTGenMed=mean(RTGen);
PCOutGenMed=mean(PCOutGen);
RoamGenMed=mean(RoamGen);
fprintf("\n Punteggio medio: %.1f", PTGenMed);
fprintf("\n Punteggio difficile medio: %.1f", PTDiffMed);
fprintf("\n Punteggio facile medio: %.1f", PTFacMed);
fprintf("\n Tempo di reazione medio: %.3f sec", RTGenMed);
fprintf("\n Tempo fuori dall'area d'interesse: %.3f sec", PCOutGenMed);
fprintf("\n Movimento del mouse: %.3f", RoamGenMed);

%boxplot
%{
la variabile deve essere continua
boxplot([PTGen, PTDiff, PTFac], 'Labels', {'Totale','Difficile', 'Facile'});
title("Punteggio");
ylabel("Domande corrette");
%}
figure(1)
boxplot([RTGen, RTDiff, RTFac], 'Labels', {'Totale','Difficile', 'Facile'});
title("Tempo di risposta");
ylabel("Tempo in secondi");

figure(2)
subplot(3,1,1)
boxplot([PCOutGen, PCOutDiff, PCOutFac], 'Labels', {'Totale','Difficile', 'Facile'});
title("Tempo fuori dall'area d'interesse");
ylabel("Tempo in secondi");
subplot(3,1,2)
boxplot([RoamGen, RoamDiff, RoamFac], 'Labels', {'Totale','Difficile', 'Facile'});
title("Movimento del mouse");
ylabel("Quantità");
subplot(3,1,3)
boxplot(Dev);
ylabel("Spostamento");
title("Deviazionedalla traiettoria ideale");




%{
grafico correlazione
dim=12;
i=1:(dim/2);
figure(1)
plot(i,mediae);
%}