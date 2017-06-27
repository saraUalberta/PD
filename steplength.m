SL = load('patientwalk_17.txt');
%SL = load('sarawalk3.txt');

%Comienza desde patientwalk_3

siz = size(SL);
clc;
val = 0;
count = 0;
val2 = 0;
steps = 0;


%columnas 4 y 55


for i = 1:(siz(1)-5)

slc = SL(i,58);
slc3 = SL(i+5,58);

dif = abs (slc3 - slc);

if (dif >= 0.1)
    
    if (val == 0 && count == 0)
        start = slc;
    end
    
    val = 1;
    val2 = val2 + 1;
    
else
    
    if (val == 1 && val2 >= 5)       
        val = 0;
        finish = slc3;
        count = count + 1;
        steps(count) = abs(finish - start);
        start = finish;
        val2 = 0;
    end
    
end



end

size2 = 0;
sizesteps = size(steps);

for j = 1:sizesteps(2)
   
    size2 = size2 + steps(j);
    
end

size2 = size2 / sizesteps(2);

disp(['Average Step Length: ', num2str(size2), ' meters']);