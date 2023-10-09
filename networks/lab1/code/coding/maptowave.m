function wave=maptowave(data)
data=upsample(data,100);
wave=filter(5*ones(1,100),1,data);
