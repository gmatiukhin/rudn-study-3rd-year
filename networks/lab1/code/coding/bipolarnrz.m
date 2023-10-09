% Кодирование NRZ:
function wave=bipolarnrz(data)
  data(data==0)=-1;
  wave=maptowave(data);
