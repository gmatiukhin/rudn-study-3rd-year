% Функция построения спектра сигнала:
function spectre = calcspectre(wave)
  % Частота дискретизации (Гц):
  Fd = 512;
  Fd2 = Fd/2;
  Fd3 = Fd/2 + 1;
  X = fft(wave,Fd);
  spectre = X.*conj(X)/Fd;
  f = 1000*(0:Fd2)/Fd;
  plot(f,spectre(1:Fd3));
  xlabel('Frequency (Hz)');
