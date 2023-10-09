% Кодирование RZ:
function wave=bipolarrz(data)
  data(data==0)=-1;
  data=upsample(data,2);
  wave=maptowave(data);
