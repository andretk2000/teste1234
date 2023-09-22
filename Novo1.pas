Program Pzim ;
var
    horas, minutos, segundos, valor: integer;
begin
    ReadLn(valor);
    horas := (valor div 3600);

    minutos := (valor div 60) mod 60;

    segundos := (valor mod 60);

    WriteLn(horas, ':', minutos, ':', segundos);
    ReadLn();
end.