function [Dati,PosDatix, PosDatiy, ResponseTimes, Responses,Scores,Sizes,isDifficult]= leggi(name,dim)
Dati=readcell(name); %legge file .csv
for i=1:dim 
    Sizes(i,:)=size(str2num(Dati{16+i-1,28})); %indentifica dimensione della fase test
    Sizes(i+12,:)=size(str2num(Dati{16+i-1,47})); %indentifica dimensione della fase test
end
PosDatix=zeros(2*dim,max(max(Sizes)));
PosDatiy=zeros(2*dim,max(max(Sizes)));
for i=1:dim
    if Dati{16-1+i,27}<6 %divisione domande facili e difficili
        isDifficult(i)=0;
    elseif Dati{16-1+i,27}>5
        isDifficult(i)=1;
    end
    Posx=(str2num(Dati{16+i-1,28})); %risposta 1 fase test
    Posy=(str2num(Dati{16+i-1,29}));
    Posx2=(str2num(Dati{16+i-1,47})); %risposta 2 fase test
    Posy2=(str2num(Dati{16+i-1,48}));
    ResponseTimez=str2num(Dati{16+i-1,52}); %tempo di risposta 2 fase test
    ResponseTimes(i,2)=ResponseTimez(end);
    ResponseTimez=str2num(Dati{16+i-1,33}); %tempo di risposta 1 fase test
    ResponseTimes(i,1)=ResponseTimez(end);
    Responses{i,1}=Dati{16+i-1,34}; %risposta 1 fase test
    Responses{i,2}=Dati{16+i-1,53}; %rispsota 2 fase test
    Scores(i)=Dati{16-1+i,46}; %punteggio fase test
    class(Dati{16+i-1,34});
    for j=1:Sizes(i,2)
        PosDatix(i,j)=Posx(j);
        PosDatiy(i,j)=Posy(j);

    end
    for j=1:Sizes(i+12,2)
        PosDatix(i+12,j)=Posx2(j);
        PosDatiy(i+12,j)=Posy2(j);
    end
end

end
