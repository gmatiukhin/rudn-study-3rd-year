% Манчестерское кодирование:
function wave=manchester(data)
  data(data==0)=-1;
  data=upsample(data,2);
  data=filter([-1 1],1,data);
  wave=maptowave(data);
